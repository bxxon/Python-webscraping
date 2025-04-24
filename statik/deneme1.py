import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Ana sayfa URL'si
base_url = 'https://kpfu.ru/main_page?p_sub=7860&p_id=9414&p_order=1'

# Ana sayfayı çekiyoruz
response = requests.get(base_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

# Profil bağlantılarının bulunduğu alan (target=_blank içeren href'ler)
profile_links = []

# target="_blank" içeren <a> tag'larını buluyoruz
for a_tag in soup.find_all('a', href=True, target="_blank"):
    link = a_tag['href']
    profile_links.append(link)

# Mailto bağlantılarını bulmak için regex deseni
mailto_pattern = re.compile(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

# Profil sayfalarındaki mailto bağlantılarını toplama
mailto_links = []

# Her profil sayfasına gidip mailto bağlantılarını alma
for link in profile_links:
    profile_url = urljoin(base_url, link)  

    print(f"Profil sayfası: {profile_url}")

    profile_response = requests.get(profile_url)
    profile_response.raise_for_status()

    profile_html = profile_response.text

    # mailto bağlantılarını arıyoruz
    found_mailtos = re.findall(mailto_pattern, profile_html)

    # Bulunan mail adreslerini listeye ekliyoruz
    mailto_links.extend(found_mailtos)

# mailto bağlantılarını terminale yazdırıyoruz
if mailto_links:
    print("\nBulunan mail adresleri:")
    for mail in mailto_links:
        print(mail)
else:
    print("Hiç mail adresi bulunamadı.")
