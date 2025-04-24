import requests
import re
from bs4 import BeautifulSoup

# Ana sayfa URL'si
base_url = 'https://history.hacettepe.edu.tr/tr/menu/ogretim_uyeleri-59'

# Ana sayfayı çekme
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Profil sayfalarına giden bağlantıları bulma
profile_links = []

# Profil bağlantıları için belirli bir class'ı bulma
for a_tag in soup.find_all('a', href=True, class_='your_class_herefio'):  # Class'ı buraya ekle
    profile_links.append(a_tag['href'])

# mailto bağlantılarını bulma regex deseni
mailto_pattern = re.compile(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

# Profil sayfalarındaki mailto bağlantılarını toplama
mailto_links = []

for link in profile_links:
    profile_url = 'https://www.yyu.edu.tr' + link  # Profil sayfasının tam URL'si
    profile_response = requests.get(profile_url)
    
    # Profil sayfasının içeriğini regex ile tarama
    profile_html = profile_response.text
    found_mailtos = re.findall(mailto_pattern, profile_html)
    
    # Bulunan mail adreslerini listeye ekleme
    mailto_links.extend(found_mailtos)

# mailto bağlantılarını terminale yazdırma
for mail in mailto_links:
    print(mail)
