import time
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Kullanacağımız sayfanın URL'si
url = "https://www.yyu.edu.tr/Birimler/25/akademik-kadro"

# Selenium WebDriver'ı başlat (webdriver-manager ile otomatik kurulum)
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştır
driver = webdriver.Chrome(service=service, options=options)

# Sayfayı aç
driver.get(url)
time.sleep(5)  # Sayfanın yüklenmesini bekle

# Sayfanın HTML içeriğini al
html_content = driver.page_source
driver.quit()  # Tarayıcıyı kapat

# BeautifulSoup ile HTML'yi işle
soup = BeautifulSoup(html_content, "html.parser")

# E-posta listesini saklamak için bir dizi
emails = []

# 1️⃣ **"mailto" içeren e-posta adreslerini bul**
for link in soup.find_all("a", href=True):
    if "mailto:" in link["href"]:
        email = link["href"].replace("mailto:", "").strip()
        emails.append(email)

# 2️⃣ **Sayfadaki tüm metinden e-posta çek (JavaScript ile gizlenenleri yakalamak için)**
text_content = soup.get_text()
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails.extend(re.findall(email_pattern, text_content))

# **Tekrar eden e-postaları temizle**
emails = list(set(emails))

# **E-postaları terminale yazdır**
if emails:
    print("\n🔍 BULUNAN E-POSTALAR:")
    for email in emails:
        print(email)
else:
    print("\n❌ Hiç e-posta bulunamadı!")
