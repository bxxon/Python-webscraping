from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_emails_from_url(url):
    # Sayfayı çek
    response = requests.get(url, verify=False)  # SSL hatasını önlemek için
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    emails = []
    for a_tag in soup.find_all('a', href=True):  # href özelliği olan tüm <a> etiketlerini bul
        href = a_tag['href']
        if href.startswith("mailto:"):  # mailto bağlantısını kontrol et
            email = href.replace("mailto:", "")
            emails.append(email)
            print(f"Bulunan e-posta: {email}")

    return emails

url = "https://turkdiliveedebiyati.ege.edu.tr/tr-5854/akademik_kadro.html"

emails = get_emails_from_url(url)

print("\nTüm bulunan benzersiz e-posta adresleri:")
unique_emails = list(set(emails))
for email in unique_emails:
    print(email)
