import requests
import re
from bs4 import BeautifulSoup

# Ana sayfa URL'si
base_url = "https://kpfu.ru/main_page?p_sub=7860&p_id=9414&p_order=1"

# Mailto regex deseni
mailto_pattern = re.compile(r"mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})")

# E-posta adreslerini saklamak için bir küme (tekrarları önlemek için)
emails = set()

# Ziyaret edilecek URL'ler listesi
to_visit = {base_url}  # Başlangıçta ana sayfa eklenir
visited = set()  # Ziyaret edilenleri kaydeder

# Web tarayıcısı (web crawler) işlemi başlat
while to_visit:
    url = to_visit.pop()  # Bir URL al
    if url in visited:  
        continue  # Daha önce ziyaret ettiysek atla
    
    visited.add(url)  # Ziyaret edildi olarak işaretle
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            continue  # Sayfa düzgün yüklenmediyse atla
        
        soup = BeautifulSoup(response.text, "html.parser")

        # 1. Önce body içindeki mailto linklerini bul ve ekle
        found_mails = re.findall(mailto_pattern, response.text)
        emails.update(found_mails)  # Yeni e-posta adreslerini ekle

        # 2. Sayfadaki tüm href bağlantılarını toplayıp, ziyaret edilecek listeye ekle
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            
            # Eğer bağlantı tam URL değilse, ana URL ile birleştir
            if not href.startswith("http"):
                href = base_url + href

            # Daha önce ziyaret edilmemişse listeye ekle
            if href not in visited:
                to_visit.add(href)

    except requests.RequestException:
        continue  # Hata oluşursa geç

# Sonuçları terminale yazdır
print("\nBulunan E-Postalar:")
for email in emails:
    print(email)
