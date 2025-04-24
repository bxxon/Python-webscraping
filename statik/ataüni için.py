import requests
import re
from bs4 import BeautifulSoup

# Hedef URL
url = "https://birimler.atauni.edu.tr/edebiyat-fakultesi/akademik-personel/"

# E-posta adresi yakalamak için regex
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

try:
    # Sayfanın HTML içeriğini indir
    response = requests.get(url, timeout=30)
    response.raise_for_status()  # Hata kontrolü
    soup = BeautifulSoup(response.text, "html.parser")

    # <div class="accordion" id="personel-kart"> içeren bölümleri bul
    personel_kartlar = soup.find_all("div", class_="accordion", id="personel-kart")

    found_emails = set()  # Tekrar eden e-postaları engellemek için set kullanıyoruz

    for kart in personel_kartlar:
        # İçinde class="bilgiler" olan kısmı bul
        bilgiler_div = kart.find(class_="bilgiler")
        if bilgiler_div:
            # Div içindeki tüm metni al
            bilgiler_text = bilgiler_div.get_text(separator="\n")

            # Regex ile e-posta adreslerini ara
            emails = email_pattern.findall(bilgiler_text)
            found_emails.update(emails)  # Set içine ekleyerek tekrarları önlüyoruz

    # Bulunan e-posta sayısını yazdır
    email_count = len(found_emails)
    print(f"Toplam bulunan e-posta sayısı: {email_count}")

    # E-postaları yazdır
    if email_count > 0:
        print("Bulunan E-posta Adresleri:")
        for email in found_emails:
            print(email)
    else:
        print("Hiç e-posta adresi bulunamadı.")

except requests.exceptions.RequestException as e:
    print(f"Hata: {e}")
