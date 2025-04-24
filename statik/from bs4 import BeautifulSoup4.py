from bs4 import BeautifulSoup
import requests
import re
import urllib3

# SSL sertifikası doğrulama uyarılarını devre dışı bırak
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def unique_strings(string_list):
    return list(set(string_list))  # Daha kısa ve performanslı

emails = []

url = "https://gefcografya.gazi.edu.tr/akademik-personel"

# Sayfayı çek
response = requests.get(url, verify=False)  # SSL hatasını önlemek için
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# Belirli class'a sahip tüm elementleri bul
elements_with_class = soup.find_all(lambda tag: tag.has_attr("class") and "th-social" in tag.get("class", []))
print(f"Bulunan öğe sayısı: {len(elements_with_class)}")

# Her bir elementteki mailto bağlantılarını bul ve yazdır
for element in elements_with_class:
    first_a_tag = element.find("a")
    if first_a_tag and first_a_tag.get("href"):
        href = first_a_tag.get("href")

        # Eğer href "mailto:" içeriyorsa, bu bir e-posta adresidir
        if href.startswith("mailto:"):
            email = href.replace("mailto:", "")
            emails.append(email)
            print(f"Bulunan e-posta: {email}")

# Tekrarlayan e-postaları filtrele
emails = unique_strings(emails)

# Sonuçları yazdır
print(emails)
for email in emails:
    print(email)
