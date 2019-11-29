import requests
from bs4 import BeautifulSoup


def save_url(url, file_name):
    # url = 'https://www.hdb-reservation.com'
    # url = 'http://github.com'
    r = requests.get(url)
    f = open(file_name, 'w+', encoding='utf-8')
    f.write(r.text)
    f.close()


def encode_url(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    r_html = f.read()
    f.close()
    # print (r_html)
    soup = BeautifulSoup(r_html, 'html.parser')
    # title = soup.find('span', 'articletitle').string
    #
    # title = soup.find('span')
    #     #('span', 'articletitle').string
    # print (title)
    print('soup.title: ', soup.title)
    print('soup.title.name: ', soup.title.name)
    print('soup.title.string: ', soup.title.string)
    print('soup.title.parent.name: ', soup.title.parent.name)
    print('link : ', soup.link)
    print('link href: ', soup.link['href'])
    print('soup.meta : ', soup.meta)
    print('soup.link["href"] : ', soup.link['href'])
    # print ('soup.meta["property"] : ', soup.meta['property'])
    print(soup.find(content="GitHub"))

    # print (soup.get_text())


def encode_reservation(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    r_html = f.read()
    f.close()
    # print (r_html)
    soup = BeautifulSoup(r_html, 'html.parser')

    project_desc = soup.find_all(class_='col-md-5')

    proj_detail = []
    proj_list = []
    for p in project_desc:
        proj_name = p.find('a')
        proj_desc = proj_name.find_next()
        open_date = (p.find('span')).find_next()
        close_date = (((p.find('span')).find_next('span')).find_next('span')).find_next()
        proj_long_desc = p.find(class_='mt-30').find_next('p')
        # print ('------------------------', proj_long_desc.text)
        proj_detail.clear()
        proj_detail.append(proj_name.text)
        proj_detail.append(proj_desc.text)
        proj_detail.append(open_date.text)
        proj_detail.append(close_date.text)
        proj_detail.append(proj_long_desc.text)
        proj_list.append(proj_detail.copy())

    for proj in proj_list:
        print(f'name: {proj[0]}, desc: {proj[1]}, long desc: {proj[4]}, open_date:'
              ' {proj[2]}, close_date: {proj[3]}')


# url = 'https://www.hdb-reservation.com'
url = 'https://bravo.harery.com'
# url = 'http://github.com'
# r = requests.get(url)
# r_html = r.text
file_name = 'bravo_harery_site.html'
# file_name = "html.txt"
# save_url(url, file_name)

encode_reservation(file_name)
