import requests
from bs4 import BeautifulSoup
#from save_to_excel import save_list_to_excel
from DBHandle import save_list
#import csv


def save_url(urls, file_name):
    f = open(file_name, 'w+', encoding='utf-8')
    for url in urls:
        print ('saving requests ....', url)
        r = requests.get(url)
        if r is None:
            break
        f.write(r.text)
    f.close()


def encode_site(urls, html_file_name, rec_list):
    try:
        f = open(html_file_name, 'r', encoding='utf-8')
    except FileNotFoundError:  # not found, create it
        print ('create html file ', html_file_name)
        save_url(urls, html_file_name)
        f = open(html_file_name, 'r', encoding='utf-8')

    r_html = f.read()
    f.close()

    parse_site_file(r_html, rec_list)
    #print ('encode_site_list:', rec_list)


def parse_site_file(r_html, rec_list):
    print ('parsing file, beautifulSoup ....')
    soup = BeautifulSoup(r_html, 'html.parser')
    print ('After BeautifulSoup ....')
    drs = soup.find_all(class_='card-info')
    print ('soup.find_all ...')
    i = 1
    for d in drs:
        print ('parsing file ..., dr # ', i)
        dr_name = d.find(class_='doctor-prefix')
        if dr_name is None:
            dr_name = "no title ...."
        else:
            dr_name = dr_name ['title']
        print(f'{i} - name: ', dr_name)
        i +=1
        short_desc = d.find(class_='font-size-15').text
        #print('short desc:', short_desc.text)
        address = d.find(class_='mb-0').text
        #print('address:', address.text)
        fees = d.find(class_="gray80 nomargin ellipsis").find("span").find_next().text.strip().split(' ')[0]
        #print ('fees (EGP):', fees.text.strip().split(' ')[0])

        image_link = d.find(class_="mobmargin text-center pull-left search-doctor-card--image-container")
        if image_link is not None:
            try:
                image_link = image_link.find('img')['alter-img-src']
            except:
                print ('image source error: ', image_link)
                image_link = ''
        """
            <span class="waiting-time-blue">
                <span>Waiting Time :</span> 42 Minutes
            </span>
        """
        waiting_time= d.find(class_="waiting-time-blue")
        #print ('waiting time (min): ', waiting_time)
        if waiting_time is not None:
            waiting_time = waiting_time.text.split(' ')[3]
        elif d.find(class_="waiting-time-green") is not None:
            waiting_time = d.find(class_="waiting-time-green")
            waiting_time = waiting_time.text.split(' ')[3]
        else:
            waiting_time = '0'

        #-----------------
        #  Rating
        # ----------------
        """
        <div class="search-card-rating">
            <div class="star-rating disp-inline rating-xs rating-active">
                <span>
                    <span content="5"></span>
                    <span class="disp-none">782 </span>
                    <input type="number" data-show-caption="false" data-show-clear="false" disabled="disabled" data-size="xs" step="1" max="5" min="0" value="5" class="rating form-control displaynone" dir="ltr">
                </span>
            </div>
                <div class="number-of-reviews padding-left-2 disp-inline rating-custom-text" style=''>
                        <span><span class="strong">Overall Rating</span> From 782 Visitors</span>
                </div>
        </div>
        """
        rating = d.find(class_="star-rating").find('span').find()['content']
        #print('rating: ', rating)
        #visitors = d.find(class_="search-card-rating").\
        try:
            visitors=  d.find(class_='number-of-reviews').find('span').text.split(' ')[3]
        except:
            print ('visitors exception: ', d.find(class_='number-of-reviews').find('span').text)
            visitors = '0'
        #print ('visitors: ', visitors)
        #print('-------------------------------------')

        rec_list.append([
            dr_name,
            address,
            short_desc,
            int(fees),
            image_link,
            float(rating),
            int(visitors),
            int(waiting_time)
        ])

#        break

# -------------------------------
#   Execution
# -------------------------------
urls = ['https://www.vezeeta.com/en/doctor']
#https://www.vezeeta.com/en/doctor?page=2
for i in range (2,1637):
     urls.append (f'https://www.vezeeta.com/en/doctor?page={i}')
file_name = 'vezeeta.html'
#excel_file_name = file_name.split('.')[0] + ".xlsx"
drs_list = []
encode_site(urls, file_name, drs_list)
#print ('drs_list: ', drs_list)
print ('saving list to DB')
save_list(drs_list)
