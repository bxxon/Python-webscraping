import requests
from bs4 import BeautifulSoup

# Hedef site URL'si
url = "https://www.selcuk.edu.tr/Birim/fakulteler/edebiyat/1818/Person/Akademik"

# Sayfa içeriğini çek
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# "td style="width:270.344px;height:59px;" içerenleri bu
links = [a['href'] for a in soup.find_all('div', target="class="row staff text-center"", href=True)]

# Bulunan href linklerini saklamak için liste
href_links = []

# Her <td> içindeki <a> etiketlerinin href değerlerini al
for td in td_elements:
    links = td.find_all("a", href=True)
    for link in links:
        href_links.append(link["href"])

# Bulunan href sayısını yazdır
print(f"Toplam {len(href_links)} href bulundu.")

# Mail adreslerini saklamak için liste
emails = []

# Bulunan her href'e bağlan ve içeriğini kontrol et
for href in href_links:
    try:
        # Sayfa içeriğini çek
        response = requests.get(href)
        sub_soup = BeautifulSoup(response.text, "html.parser")
        
        # Sayfada "mail :" ifadesini ara
        mail_texts = sub_soup.find_all(string=lambda text: text and "mail :" in text)
        
        # Bulunan "mail :" sayısını yazdır
        print(f"{href} sayfasında {len(mail_texts)} 'mail :' bulundu.")

        # Her "mail :" içeriğini al ve listeye ekle
        for mail_text in mail_texts:
            email = mail_text.split("mail :")[-1].strip()
            emails.append(email)

    except Exception as e:
        print(f"{href} sayfasına bağlanırken hata oluştu: {e}")

# Sonuçları yazdır
print("\nBulunan E-posta Adresleri:")
for email in emails:
    print(email)
