import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Ana sayfa URL'si
base_url = 'https://antropoloji.hacettepe.edu.tr/tr/menu/ogretim_uye_ve_gorevlileri-33'  # Gerçek URL'nizi buraya ekleyin

# Ana sayfayı çekme
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Profil bağlantıları için belirli bir class'ı bulma
profile_links = []

# Profil URL'lerinin bulunduğu class'ı bulma
for a_tag in soup.find_all('<p>', href=True, class_='icerik'):  # 'your_class_here' yerine doğru class adını girin
    profile_links.append(a_tag['href'])  # Profil URL'lerini listeye ekliyoruz

# mailto bağlantılarını bulma regex deseni
mailto_pattern = re.compile(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

# Profil sayfalarındaki mailto bağlantılarını toplama
mailto_links = []

# Her profil URL'sini kontrol etme ve mailto bağlantısını alma
for link in profile_links:
    # Profil URL'sinin tam halini almak için urljoin kullanıyoruz
    profile_url = urljoin(base_url, link)  # URL'yi birleştiriyoruz
    profile_response = requests.get(profile_url)
    
    # Profil sayfasının HTML içeriğini alıyoruz
    profile_html = profile_response.text
    
    # mailto bağlantılarını arıyoruz
    found_mailtos = re.findall(mailto_pattern, profile_html)
    
    # Bulunan mail adreslerini listeye ekliyoruz
    mailto_links.extend(found_mailtos)

# mailto bağlantılarını terminale yazdırıyoruz
for mail in mailto_links:
    print(mail)
