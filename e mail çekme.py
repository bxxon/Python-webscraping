import requests
from bs4 import BeautifulSoup

url = 'https://www.math.nus.edu.sg/people/regular-faculty/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

emails = []

for link in soup.find_all('mathematics department'):
    href = link.get('href')
    if href and 'mailto:' in href:
        emails.append(href.replace('mailto:', ''))


print(emails)
