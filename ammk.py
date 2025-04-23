import requests
import re
from bs4 import BeautifulSoup

# Ana sayfa URL'si
base_url = 'https://birimler.atauni.edu.tr/edebiyat-fakultesi/akademik-personel/'

# Ana sayfayı çekiyoruz
response = requests.get(base_url)
response.raise_for_status()  # Sayfa yüklenemezse hata verir
soup = BeautifulSoup(response.text, 'html.parser')

# style="height" özelliğine sahip öğeleri buluyoruz
elements_with_height = soup.find_all(style=re.compile(r'height:\s*(\d+)\s*px;'))

# mailto bağlantılarını bulmak için regex deseni
mailto_pattern = re.compile(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

# mailto adreslerini depolamak için liste
mailto_links = []

# 18 ile 26 arasında olan height değerlerine sahip öğeleri filtreliyoruz
for element in elements_with_height:
    # height değerini alıyoruz
    style = element['style']
    match = re.search(r'height:\s*(\d+)\s*px', style)
    
    if match:
        height_value = int(match.group(1))
        
        # height değeri 18 ile 26 arasında ise, bu öğeye giriyoruz
        if 18 <= height_value <= 26:
            # İçindeki <a> etiketlerini buluyoruz
            for a_tag in element.find_all('a', href=True):
                profile_url = a_tag['href']
                
                # Eğer href bir profil bağlantısı ise, mailto'yu kontrol ediyoruz
                profile_response = requests.get(profile_url)
                profile_response.raise_for_status()  # Sayfa yüklenemezse hata verir

                # Profil sayfasının HTML içeriğini alıyoruz
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
