import requests
from bs4 import BeautifulSoup
import time
import urllib3

# SSL uyarılarını kapat (Opsiyonel)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Örnek URL
url = "https://ayu.edu.kz/birimler/tr/0-ahmet-yesevi-universitesi/yonetim-kurulu-uyeleri"

# Sayfanın HTML içeriğini çek (SSL doğrulama kapalı)
response = requests.get(url, verify=False)  # SSL hatasını önlemek için verify=False kullanıldı

# Eğer sayfa başarıyla çekildiyse devam et
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # "team-hover-wrap" class'ına sahip divleri bul
    team_containers = soup.find_all("div", class_="team-hover-wrap")
    print(f"Toplam {len(team_containers)} 'team-hover-wrap' öğesi bulundu.")

    # Mailleri saklamak için liste oluştur
    emails = []

    # Her "team-hover-wrap" içinde "th-social" div'ini ara
    for container in team_containers:
        social_div = container.find("div", class_="th-social")
        if social_div:
            mail_links = social_div.find_all("a", href=True)  # Tüm a etiketlerini al
            for link in mail_links:
                href = link["href"]
                if href.startswith("mailto:"):
                    email = href.replace("mailto:", "").strip()
                    emails.append(email)

    print(f"Toplam {len(emails)} mail adresi bulundu.")

    for email in emails:
        print(email)

else:
    print(f"Hata! HTTP Yanıt Kodu: {response.status_code}")

#time.sleep(10)
