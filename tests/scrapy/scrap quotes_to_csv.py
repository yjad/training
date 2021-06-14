import requests
from bs4 import BeautifulSoup
import csv


def save_url(urls, file_name):
    f = open(file_name, 'w+', encoding='utf-8')
    for url in urls:
        r = requests.get(url)
        f.write(r.text)
    f.close()


def encode_site(urls, html_file_name, csv_file_name):
    try:
        f = open(html_file_name, 'r', encoding='utf-8')
    except:     # not found, create it
        save_url(urls, html_file_name)
        f = open(html_file_name, 'r', encoding='utf-8')

    r_html = f.read()
    f.close()

    parse_site_file(r_html, csv_file_name)
    # print (r_html)


def parse_site_file(r_html, csv_file_name):
    soup = BeautifulSoup(r_html, 'html.parser')

    quotes= soup.find_all(class_='quote')

    quote_details = []
    quote_list = []

    csv_file = open(csv_file_name, mode='w+', newline="\n", encoding='utf-8')
    csv_writer = csv.writer(csv_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # write header
    csv_writer.writerow(['Quote', 'author', 'tag-1', 'tag-2','tag-3','tag-4','tag-5'])
    for q in quotes:
        quote_body = q.find('span')
        #print (f'quote_body: {quote_body.text}')
        author = q.find(class_='author')
        #print (f'author: {author.text}')
        quote_tags = q.find(class_ = 'keywords') ['content']
        #print (quote_tags)
        tags_list=quote_tags.split(',')

        quote_details.clear()
        quote_details.append(quote_body.text)
        quote_details.append(author.text)
        for t in tags_list:
            quote_details.append(t)

        csv_writer.writerow(quote_details)
    csv_file.close()


# -------------------------------
#   Execution
# -------------------------------
urls =[]
urls.append ('http://quotes.toscrape.com/')
for i in range (2,11):
    urls.append (f'http://quotes.toscrape.com/page/{i}/')
file_name = 'quotes_toscrape_com.html'
csv_file_name = file_name.split('.')[0]+".csv"


encode_site(urls, file_name, csv_file_name)
