import os
import pytesseract
from tkinter import messagebox
from DB import open_db, insert_row_list, close_db, exec_query, exec_db_cmd, exec_db_cmd_conn

from PIL import Image

def pdf2db(page_no):
    
    page = f".\\data\\books\\ABH\\pages\\ABH-{format(page_no, '03')}.png"
    
    words= str(((pytesseract.image_to_string(Image.open(page), lang='ara'))))

    # get last record number in dict
    conn, cursor = open_db()
    rows = exec_query (cursor, "select count(*) FROM pdf_dict")
    if len(rows) == 0:
         st_dict_no = 1
    else:
        st_dict_no = rows[0][0]+1

    for w in words.split():
        insert_row_list(conn, cursor, 'pdf_dict', [w,w,page_no], ignoreUnique=True)    
    conn.commit()
    close_db(cursor)

    words = words.replace("'", "*") # replace single quote
    words = words.replace('"', "*") # replace double quote
    cmd = f"""INSERT INTO page_text VALUES ({page_no}, '{words}', '', {st_dict_no})"""
    exec_db_cmd(cmd)

    
def test():


    page = r"C:\Yahia\Home\Yahia-Dev\Python\training\pdf\data\ABH pages\ABH-025.png"
    
    outfile = f".\\out\\{os.path.split(page)[1].split('.')[0]}.txt"
    f = open(outfile, "w", encoding='utf-8')
    # filename = "page_"+str(i)+".jpg"
    filename = f'.\\data\\ABH pages\\{page}'
    # text = str(((pytesseract.image_to_string(Image.open(filename), lang='ara'))))
    words= str(((pytesseract.image_to_string(Image.open(page), lang='ara'))))
    # print(words)
    f.write(words)
    f.write ('----------------------------\n')
    for w in words.split():
        f.write(w + "\n")
    f.close()
    conn, cursor = open_db()
    # print(words)
    for w in words.split():
        # print (w)
        insert_row_list(conn, cursor, 'pdf_dict', [w,w], ignoreUnique=True)
    
    conn.commit()
    close_db(cursor)

def rebuild_page_text(page_no):

    conn, cursor = open_db()
    rows = exec_query (cursor, f"SELECT page_raw FROM page_text WHERE page_no = {page_no}")

    if len(rows) == 0:
        tk.messagebox ('Page not found')
        close_db(cursor)
        return
    else:
        edited_page = edit_page_text_details(rows[0][0], cursor, page_no)

    cmd = f"UPDATE page_text SET page_edited_txt = '{edited_page}' WHERE page_no = {page_no}"
    r= exec_db_cmd_conn (cmd, cursor)
    if r == 0:   #success
        update_dict(page_no, conn, cursor)
        conn.commit()

    close_db(cursor)
    return edited_page

def edit_page_text_details(org_txt, cursor, page_no):
    # fp = open ('.\\out\\tt.txt', 'a', encoding = 'utf-8')
    edited_text = ''
    for l in org_txt.split('\n'):
        edited_line = ''
        for i,w in enumerate(l.split()):
            cmd = f"SELECT dict_word FROM pdf_book WHERE pdf_word = '{w}' and page_no = {page_no}"
            rows = exec_query (cursor, cmd)
            if len(rows) == 0 or len (rows[0]) == 0:
                # fp.writelines (cmd)
                w_db = '****'
            else:
                w_db = rows[0][0]
            if i > 0 and w_db == '،':
                edited_line += w_db     # ommit space before comma
            else:
                edited_line += ' ' + w_db
        edited_text += edited_line + '\n'
    # fp.close()
    return edited_text


def get_db_page(page_no):
    conn, cursor = open_db()
    rows = exec_query (cursor, f"SELECT * FROM page_text WHERE page_no = {page_no}")
    close_db(cursor)
    # print (page_no, len (rows[0]))
    if len(rows) == 0:        
        return None
    else:
        return rows[0][1], rows[0][2]

def get_page_dict(page_no):
    conn, cursor = open_db()
    rows = exec_query (cursor, f"SELECT * FROM pdf_book WHERE page_no = {page_no}")
    close_db(cursor)
    # print (page_no, len (rows[0]))
    if len(rows) == 0:        
        return None
    else:
        return rows

def update_book_word(pdf_word, dict_word, page_no, word_type):
  
    cmd = f"""
UPDATE pdf_book SET type  = '{word_type}', dict_word = '{dict_word}' WHERE pdf_word = '{pdf_word}' AND page_no  = {page_no}"""
    # print (cmd)
    exec_db_cmd (cmd)



def load_book():

    page_path = r"C:\Yahia\Home\Yahia-Dev\Python\training\pdf\data\books\ABH\pages"
    conn, cursor = open_db()
    for page_no in range (3,75):
        page = os.path.join(page_path, f"ABH-{format(page_no, '03')}.png")
        print (page_no)
        words= str(((pytesseract.image_to_string(Image.open(page), lang='ara'))))
        for w in words.split():
            insert_row_list(conn, cursor, 'pdf_book', [w,w, page_no,None])
    
    conn.commit()
    close_db(cursor)

# ----------------------------------------------------------  
# update pdf_dict from book table:
# add/replace book's rows of type 'Dict'
# ----------------------------------------------------------
def update_dict(page_no, conn, cursor):
    rows = exec_query (cursor, f"SELECT * FROM pdf_book WHERE page_no = {page_no} and type = 'Dict'")
    for row in rows:
        insert_row_list(conn, cursor, 'pdf_dict', [row[0],row[1],row[2]], ignoreUnique=True)
    
def update_book():
    cmd = """
UPDATE pdf_book 
SET dict_word =  dict.dict_word, 
	type = 'Dict'
FROM
(SELECT pdf_word, dict_word FROM pdf_dict) dict 
WHERE pdf_book.pdf_word = dict.pdf_word AND type is NULL"""
    r = exec_db_cmd (cmd)
    messagebox.showinfo ("Success", f"{r.rowcount} rows updated" )
    