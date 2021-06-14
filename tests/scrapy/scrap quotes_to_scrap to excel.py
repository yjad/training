import requests
from bs4 import BeautifulSoup
from tests.save_to_excel import save_list_to_excel


def save_url(urls, file_name):
    f = open(file_name, 'w+', encoding='utf-8')
    for url in urls:
        r = requests.get(url)
        f.write(r.text)
    f.close()


def encode_site(urls, html_file_name, excel_file_name):
    try:
        f = open(html_file_name, 'r', encoding='utf-8')
    except:     # not found, create it
        save_url(urls, html_file_name)
        f = open(html_file_name, 'r', encoding='utf-8')

    r_html = f.read()
    f.close()

    parse_site_file(r_html, excel_file_name)
    # print (r_html)


def parse_site_file(r_html, excel_file_name):
    soup = BeautifulSoup(r_html, 'html.parser')

    quotes= soup.find_all(class_='quote')

    quote_details = []
    quote_list = []

    # write header
    sheet_header = ['Quote', 'author', 'tag-1', 'tag-2','tag-3','tag-4','tag-5']
    for q in quotes:
        quote_body = q.find('span')
        author = q.find(class_='author')
        quote_tags = q.find(class_='keywords') ['content']
        tags_list=quote_tags.split(',')

        quote_details.clear()
        quote_details.append(quote_body.text)
        quote_details.append(author.text)
        for t in tags_list:
            quote_details.append(t)
        quote_list.append(quote_details.copy())

    save_list_to_excel(sheet_header, quote_list, excel_file_name)


# -------------------------------
#   Execution
# -------------------------------
urls =[]
urls.append ('http://quotes.toscrape.com/')
for i in range (2,11):
    urls.append (f'http://quotes.toscrape.com/page/{i}/')
file_name = 'quotes_toscrape_com.html'
excel_file_name = file_name.split('.')[0]+".xlsx"


encode_site(urls, file_name, excel_file_name)
