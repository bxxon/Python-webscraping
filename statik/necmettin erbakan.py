import requests
from bs4 import BeautifulSoup

# Örnek URL
url = "https://erbakan.edu.tr/tr/birim/egitim-fakultesi/akademik-personeller#abd_list82"

# Sayfanın HTML içeriğini çek
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# "mail_tel mb-5" classına sahip divleri bul
mail_containers = soup.find_all("div", class_="mail_tel mb-5")

# Bulunan öğe sayısını yazdır
print(f"Toplam {len(mail_containers)} 'mail_tel mb-5' öğesi bulundu.")

# Her bir öğe içinde "fa-regular fa-envelope" class'ına sahip i etiketlerini bul ve içeriğini yazdır
for container in mail_containers:
    envelope_icon = container.find("i", class_="fa-regular fa-envelope")
    if envelope_icon:
        # Icon varsa, bu öğenin metnini al ve yazdır
        print(f"Mail içeriği: {container.text.strip()}")
