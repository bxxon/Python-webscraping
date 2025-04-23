import requests
from bs4 import BeautifulSoup

# Hedef URL
url = "https://fef.marmara.edu.tr/akademik/akademik-kadro"

# Sayfa içeriğini çek
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 'td' etiketleri içinde class='xl66' olanları bul
td_elements = soup.find_all("td", class_="xl66")

# Mailleri saklamak için liste
emails = []

# İçerikleri alıp @marmara.edu.tr ekleyerek listeye kaydet
for td in td_elements:
    text = td.get_text(strip=True)  # td içindeki metni al
    if text and "GZFA" not in text:  # 'GZFA' içermeyenleri ekle
        emails.append(f"{text}@marmara.edu.tr")

# Sonuçları yazdır
print("Bulunan E-posta Adresleri:")
for email in emails:
    print(email)
