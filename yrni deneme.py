from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# WebDriver'ı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Sayfayı aç
driver.get("https://tde.humanity.ankara.edu.tr/eski-turk-edebiyati-anabilim-dali/")  # Hedef URL'yi buraya girin
time.sleep(3)  # Sayfanın yüklenmesi için biraz bekleyin

# Sayfanın HTML içeriğini al
html_content = driver.page_source

# mailto: bağlantılarını bulmak için regex kullan ve mailto: kısmını atla
emails = re.findall(r'mailto:([\w\.-]+@[\w\.-]+)', html_content)

# Bulunan e-posta adreslerini yazdır
for email in emails:
    print(email)

# WebDriver'ı kapat
driver.quit()
