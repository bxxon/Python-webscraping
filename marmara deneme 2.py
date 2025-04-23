import requests
from bs4 import BeautifulSoup

def scrape_emails(url):
    # URL'yi iste
    response = requests.get(url)
    
    # İstek başarılı ise işlem yap
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tüm e-posta adreslerini saklamak için liste
        emails = []

        # 'ng-binding' class'ı içeren her 'p' etiketini bul
        email_parts = soup.find_all('p', class_='ng-binding')

        # Her e-posta parçasını işle
        for email_part in email_parts:
            # Kullanıcı adı ve domain kısmını al
            name = email_part.contents[0] if len(email_part.contents) > 0 else ''
            domain = email_part.contents[2] if len(email_part.contents) > 2 else ''

            if name and domain:
                # E-posta adresini oluştur
                email = f"{name}@{domain}"
                emails.append(email)

        return emails
    else:
        return f"Error: {response.status_code}"

# Kullanıcıdan URL al
url = input("Lütfen scraping yapmak istediğiniz URL'yi girin: ")

# E-posta adreslerini al ve yazdır
emails = scrape_emails(url)
if isinstance(emails, list):
    print("Bulunan e-posta adresleri:")
    for email in emails:
        print(email)
else:
    print(emails)
