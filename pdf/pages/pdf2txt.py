import streamlit as st
from PIL import Image
import pytesseract
import sys
# from pdf2image import convert_from_path
import os
  
# Path of the pdf
PDF_file = r"C:\Yahia\Home\Yahia-Dev\Python\training\pdf\ABH.pdf"

def all():
    '''
    Part #1 : Converting PDF to images
    '''
      
    # Store all the pages of the PDF in a variable
    pages = convert_from_path(PDF_file, 10)
      
    # Counter to store images of each page of PDF to image
    image_counter = 1
      
    # Iterate through all the pages stored above
    for page in pages:
      
        # Declaring filename for each page of PDF as JPG
        # For each page, filename will be:
        # PDF page 1 -> page_1.jpg
        # PDF page 2 -> page_2.jpg
        # PDF page 3 -> page_3.jpg
        # ....
        # PDF page n -> page_n.jpg
        filename = "page_"+str(image_counter)+".jpg"
          
        # Save the image of the page in system
        page.save(filename, 'JPEG')
      
        # Increment the counter to update filename
        image_counter = image_counter + 1
     
    exit()
    '''
    Part #2 - Recognizing text from the images using OCR
    '''
    # Variable to get count of total number of pages
    filelimit = image_counter-1
      
    # Creating a text file to write the output
    outfile = "out_text.txt"
      
    # Open the file in append mode so that 
    # All contents of all images are added to the same file
    f = open(outfile, "a")
      
    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1):
      
        # Set filename to recognize text from
        # Again, these files will be:
        # page_1.jpg
        # page_2.jpg
        # ....
        # page_n.jpg
        filename = "page_"+str(i)+".jpg"
              
        # Recognize the text as string in image using pytesserct
        text = str(((pytesseract.image_to_string(Image.open(filename)))))
      
        # The recognized text is stored in variable text
        # Any string processing may be applied on text
        # Here, basic formatting has been done:
        # In many PDFs, at line ending, if a word can't
        # be written fully, a 'hyphen' is added.
        # The rest of the word is written in the next line
        # Eg: This is a sample text this word here GeeksF-
        # orGeeks is half on first line, remaining on next.
        # To remove this, we replace every '-\n' to ''.
        text = text.replace('-\n', '')    
      
        # Finally, write the processed text to the file.
        f.write(text)
      
    # Close the file after writing all the text.
    f.close()
    
def img2text ():
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:

    # text_path = r".\data\books\{book_folder}\text"
    # page = r"C:\Yahia\Python\training\pdf\data\books\ABH\pages\ABH-025.png"
    # page = r"C:\Users\yahia\Downloads\page1.png"
    # for p in range(frrom_page,to_page+1):
    #     outfile = os.path.join(text_path, f".\\out\\{os.path.split(page)[1].split('.')[0]}.txt"

    # f = open(outfile, "w", encoding='utf-8')
    # filename = "page_"+str(i)+".jpg"
    # filename = f'.\\data\\ABH pages\\{page}'
    # text = str(((pytesseract.image_to_string(Image.open(filename), lang='ara'))))
        words= str(((pytesseract.image_to_string(Image.open(uploaded_file), lang='ara'))))
        col1, col2 = st.columns(2)
        img = Image.open(uploaded_file) 
        col1.image(img, clamp=True, channels="RGB")

        # col1.image(Image.open(page))
    # col2.write(words)
        col2.text_area("Text", value = words, height=800)
    # f.write(words)
    # st.write ('----------------------------')
    # st.dataframe(words.split())
    # for w in words.split():
    #     f.write(w + "\n")
    # f.close()
    # conn, cursor = open_db()
    # # print(words)
    # for w in words.split():
    #     # print (w)
    #     insert_row_list(conn, cursor, 'pdf_dict', [w,w], ignoreUnique=True)
    
    # conn.commit()
    # close_db(cursor)
     
img2text()