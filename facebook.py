import requests
from bs4 import BeautifulSoup
from secrets import username, password

payload = {
    'email' : username,
    'pass' : password
}

POST_LOGIN_URL = 'http://www.facebook.com/login'

with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    page = requests.get('https://mbasic.facebook.com/CareersAtDarazBangladesh')

    print(page)
