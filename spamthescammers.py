import random
import re
import requests
import time

addresses = open('addresses.txt').read().splitlines()
first_names = open('first-names.txt').read().splitlines()
last_names = open('surnames.txt').read().splitlines()

def generate():
    while True:
        try:
            first = random.choice(first_names)
            last = random.choice(last_names).title()
            address = re.split('[A-Z]{2} \d{5}', random.choice(addresses))
            check = address[1]
            street, city = address[0].split(',')
            city = city.strip()
            state = re.findall('[A-Z]{2}', random.choice(addresses))[0]
            zip_code = re.findall('\d{5}', random.choice(addresses))[0]
            print(f'{first} {last}\n {street} {city}, {state} {zip_code}')
            # Enter URL here. 
            url = ''
            payload = {'first':first,
                       'last':last,
                       'street':street,
                       'city':city,
                       'state':state,
                       'zip':zip_code
                        }
            try:
                requests.post(url, data = payload)
            except Exception as e:
                print(e)
            
            time.sleep(0.5)
            break
        except:
            continue

for _ in range(20):
    generate()
