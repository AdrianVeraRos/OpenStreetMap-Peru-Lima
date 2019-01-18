
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def audit_phone_type(phone_types, phone_name):
    phone_types.add(phone_name)

#Created a set to iterate over and modify the digits in the numbers. Dict elements didn't work

def audit_phone(filename):
    osm_file = open(filename, "r", encoding="utf8")
    phones_types = set()
    for _, elem in ET.iterparse(filename, events=("start",)):
        if elem.tag == "tag" and elem.attrib['k'] == 'phone':
            for tag in elem.iter("tag"):
                    audit_phone_type(phones_types, tag.attrib['v'])
    osm_file.close()
    return phones_types


def update_phones(phonenumber):
    #Eliminates double numbers and keeps the first one
    sep = ";"
    phonenumber = phonenumber.split(sep, 1)[0]

    #Keep first num
    phonenumber = ''.join(ele for ele in phonenumber if ele.isdigit())

    #Standarization of numbers (both land and mobile)
    if phonenumber.startswith('5101'):
        phonenumber = phonenumber[4:]
    elif phonenumber.startswith('051'):
        phonenumber = phonenumber[3:]
    elif phonenumber.startswith('511'):
        phonenumber = phonenumber[3:]
    elif phonenumber.startswith('51'):
        phonenumber = phonenumber[2:]
    elif phonenumber.startswith('01'):
        phonenumber = phonenumber[2:]
    elif phonenumber.startswith('1'):
        phonenumber = phonenumber[1:]
    elif phonenumber.startswith('9'):
        phonenumber = phonenumber[0:9]
    else:
        phonenumber = phonenumber[0:7]
    return phonenumber