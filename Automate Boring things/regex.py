import re


def regex_search():
    in_text = 'My Phone Number is 415-555-4242.'
    PhoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = PhoneNumRegex.search(in_text)
    print (f'Mobile Number Found: {mo.group()}.')

    PhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = PhoneNumRegex.search(in_text)

    print (mo.group())
    print (mo.groups())
    print (mo.group(1))
    print (mo.group(2))

    area_code, main_number = mo.groups()
    print (area_code, main_number)

    print ('hi .........')

    heroRegex = re.compile(r'Batman|Tina Fey')
    mo1 = heroRegex.search('Batman and Tina Fey.')
    print (mo1.group())
    mo2 = heroRegex.search('Tina Fey and Batman.')
    print (mo2.group())

    print ('# match one of several patterns as part of your regex.')
    heroRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo1 = heroRegex.search('Batmobile lost a wheel')
    print (mo1.group())
    print (mo1.group(1))

    print ('# optional group')
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search('The Adventures of Batman')
    mo2 = batRegex.search('The Adventures of Batwoman')
    print (mo1.group())
    print (mo2.group())

    

regex_search()