import requests
from bs4 import BeautifulSoup
import re

# Ana sayfa URL'si
main_url = "https://kpfu.ru/main_page?p_sub=7860&p_id=11650&p_order=1"

# Ana sayfanın içeriğini çek
try:
    response = requests.get(main_url, timeout=20)  # Timeout ekledik
    response.raise_for_status()  # HTTP hatalarını yakala
except requests.exceptions.RequestException as e:
    print(f"Hata: {e}")
    exit()

# HTML içeriğini işle
soup = BeautifulSoup(response.text, "html.parser")

# Sadece target="_blank" olan <a> etiketlerini bul
target_blank_links = soup.find_all("a", target="_blank", href=True)

# Mailto bağlantılarını bulmak için regex deseni
mailto_pattern = re.compile(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

# Bulunan mailto bağlantılarını saklayacağımız liste
mailto_links = []

# Her bir bağlantıya girip mailto bağlantılarını alalım
for link in target_blank_links:
    href = link["href"]
    if href.startswith("https://kpfu.ru/"):
        print(f"\n🔗 Profil sayfası: {href}")

        # Profil sayfasının HTML içeriğini al
        try:
            profile_response = requests.get(href, timeout=15)  # Timeout ekledik
            profile_response.raise_for_status()  # Sayfa yüklenemezse hata verir
        except requests.exceptions.RequestException as e:
            print(f"Hata: {e}")
            continue

        # Profil sayfasını işle
        profile_soup = BeautifulSoup(profile_response.text, "html.parser")

        # Mailto bağlantılarını arıyoruz
        found_mailtos = re.findall(mailto_pattern, profile_soup.prettify())

        # Filtreleme: public.mail@kpfu.ru adresini ekleme
        filtered_mailtos = [mail for mail in found_mailtos if mail.lower() != "public.mail@kpfu.ru"]

        # Filtrelenmiş e-posta adreslerini listeye ekle
        mailto_links.extend(filtered_mailtos)

# Mailto bağlantılarını terminale yazdırıyoruz
if mailto_links:
    print("\n💌 Bulunan mail adresleri:")
    for mail in mailto_links:
        print(mail)
else:
    print("\n💌 Hiç mail adresi bulunamadı.")
