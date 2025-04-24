import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Tarayıcıyı başlatmak için gerekli seçenekler
options = Options()
options.add_argument("--headless")  # Arka planda çalıştırma

# WebDriver'ı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Hedef URL'yi belirle
url = "https://edebiyat.istanbul.edu.tr/tr/akademikkadro"  # Burada hedef URL'yi kullanabilirsiniz

# Sayfayı aç
driver.get(url)
time.sleep(5)  # Sayfanın yüklenmesini bekle

# Sayfa içeriğini al
elements = driver.find_elements(By.CSS_SELECTOR, 'a[ng-href^="//profil.istanbul.edu.tr"]')  # ng-href içeren öğeleri bul

# Bağlantıları yazdır
emails = []
for element in elements:
    href = element.get_attribute("ng-href")
    # URL'nin başına "https:" ekle
    full_url = f"https:{href}" if href.startswith("//") else href
    # Sonuna @istanbul.edu.tr ekle
    email = f"{href.split('/')[-1]}@istanbul.edu.tr"  # /tr/p/barisozener -> barisozener@istanbul.edu.tr
    emails.append(email)

# Bulunan e-posta adreslerini yazdır
if emails:
    print("Bulunan E-posta adresleri:")
    for email in emails:
        print(email)
else:
    print("Hiçbir bağlantı bulunamadı.")

# Tarayıcıyı kapat
driver.quit()
