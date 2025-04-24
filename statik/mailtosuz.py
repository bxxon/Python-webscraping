import requests
from bs4 import BeautifulSoup
import re

# Ana sayfa URL'si
base_url = 'http://www.phil.bilkent.edu.tr/index.php/faculty-members/'  # Değiştirmeniz gereken URL

# Sayfayı çekme
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Mail adreslerini tanımak için regex deseni
email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

# Sayfa içindeki metni tarıyoruz
page_text = soup.get_text()

# Regex ile mail adreslerini buluyoruz
emails = re.findall(email_pattern, page_text)

# Bulunan mail adreslerini yazdırıyoruz
for email in emails:
    print(email)
