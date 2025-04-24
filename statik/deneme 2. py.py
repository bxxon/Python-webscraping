import requests
from bs4 import BeautifulSoup
import time

# Ana sayfa URL'si
main_url = "https://kpfu.ru/main_page?p_sub=7860&p_id=9414&p_order=1"

# Ana sayfanın içeriğini çek
try:
    response = requests.get(main_url, timeout=15)  # Timeout ekledik
    response.raise_for_status()  # HTTP hatalarını yakala
except requests.exceptions.RequestException as e:
    print(f"Hata: {e}")
    exit()

# HTML içeriğini işle
soup = BeautifulSoup(response.text, "html.parser")

# Tüm <a> etiketlerini bul (target="_blank" olanları dahil)
links = soup.find_all("a", href=True)

# Sadece "http://kpfu.ru/" ile başlayan linkleri al
kpfu_links = []
for link in links:
    href = link["href"].strip()  # Başındaki ve sonundaki boşlukları kaldır
    if href.startswith("http://kpfu.ru/"):  # Burada doğru koşul sağlanıyor
        kpfu_links.append(href)

# Bulunan linkleri yazdır
print("\n🔗 KPFU Linkleri (target='_blank'):")
for link in kpfu_links:
    print(link)

# Mail adreslerini saklayacak liste
emails = []

# KPFU sayfalarındaki mailto linklerini çek
for profile_url in kpfu_links:
    try:
        print(f"\n⏳ İşleniyor: {profile_url}")
        profile_response = requests.get(profile_url, timeout=15)
        profile_response.raise_for_status()
        
        profile_soup = BeautifulSoup(profile_response.text, "html.parser")
        mailto_links = profile_soup.find_all("a", href=True)

        for mail_link in mailto_links:
            href = mail_link["href"].strip()  # Fazladan boşlukları temizle
            if href.startswith("mailto:"):
                email = href.replace("mailto:", "").strip()
                if email not in emails:
                    emails.append(email)

    except requests.exceptions.RequestException as e:
        print(f"⚠️ {profile_url} adresine erişilemedi: {e}")
    
    # Çok hızlı istek atmayı önlemek için bekleme ekledik
    time.sleep(1)

# Bulunan e-postaları yazdır
print("\n📧 Bulunan E-postalar:")
for email in emails:
    print(email)
