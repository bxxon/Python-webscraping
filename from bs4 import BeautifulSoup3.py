from bs4 import BeautifulSoup
import requests
import re
import urllib3

# SSL sertifikası doğrulama uyarılarını devre dışı bırak
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def unique_strings(string_list):
    return list(set(string_list))  # Daha kısa ve performanslı

emails = []

url = "https://ayu.edu.kz/birimler/tr/135-felsefe-bolumu/akademik-personel"

# Sayfayı çek
response = requests.get(url, verify=False)  # SSL hatasını önlemek için
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# Belirli class'a sahip tüm elementleri bul
elements_with_class = soup.find_all(lambda tag: tag.has_attr("class") and "th-social" in tag.get("class", []))
print(f"Bulunan öğe sayısı: {len(elements_with_class)}")

# Her bir elementteki e-posta içeren <a> etiketlerini bul ve yazdır
for element in elements_with_class:
    first_a_tag = element.find("a")
    if first_a_tag and first_a_tag.get("href"):
        href = first_a_tag.get("href")

        # URL tam mı, değil mi kontrol et
        full_url = href if href.startswith("http") else "https://history.bilkent.edu.tr/faculty/" + href

        # Bağlantının içeriğini çek
        target_response = requests.get(full_url, verify=False)
        target_html_content = target_response.text
        target_soup = BeautifulSoup(target_html_content, 'html.parser')

        # E-posta regex pattern
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        # Sayfadan e-postaları bul
        found_emails = re.findall(email_pattern, target_html_content)
        emails.extend(found_emails)

        # Bulunan öğeyi ve URL'yi yazdır
        print(f"URL: {full_url}")
        print(f"Bulunan e-postalar: {found_emails}")

# Tekrarlayan e-postaları filtrele
emails = unique_strings(emails)

# Sonuçları yazdır
print("\nTüm bulunan benzersiz e-postalar:")
for email in emails:
    print(email)
