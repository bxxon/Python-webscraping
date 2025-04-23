from bs4 import BeautifulSoup
import requests

main_url = "https://www.selcuk.edu.tr/Birim/fakulteler/edebiyat/1818/Person/Akademik"  # Buraya ana sayfanın URL'sini yaz

# Ana sayfayı al
response = requests.get(main_url)
soup = BeautifulSoup(response.text, "html.parser")

# Profil sayfasına giden linkleri çek
profile_links = [a['href'] for a in soup.select('div.row.staff.text-center a[href]')]

emails = []  # E-posta adreslerini saklamak için liste

for link in profile_links:
    full_link = link if link.startswith("http") else main_url + link  # Link tam değilse tamamla
    
    try:
        profile_response = requests.get(full_link, timeout=30)  # 10 saniye bekle
        profile_response = requests.get(full_link)
        profile_soup = BeautifulSoup(profile_response.text, "html.parser")
        
        # Sayfada mailto içeren linkleri bul
        mail_links = profile_soup.select('a[href^=mailto]')
        
        for mail in mail_links:
            email = mail['href'].replace("mailto:", "")
            emails.append(email)
            print(email)  # Bulunan e-postayı ekrana yazdır

    except requests.exceptions.RequestException as e:
        print(f"Hata: {e} - {full_link}")

# Tüm e-postaları yazdır
print("\nToplanan e-posta adresleri:")
print("\n".join(emails))
