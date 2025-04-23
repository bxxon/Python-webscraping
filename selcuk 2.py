import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Selçuk Üniversitesi Ana Sayfası URL'si
main_url = "https://www.selcuk.edu.tr/Birim/fakulteler/edebiyat/1818/Person/Akademik"

# Selenium WebDriver Ayarları
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-software-rasterizer")
# options.add_argument("--headless")  # Tarayıcıyı görsel olarak çalıştırmak için bu satırı kaldırabilirsiniz
driver = webdriver.Chrome(service=service, options=options)

# Sayfaya git ve yüklenmesini bekle (timeout süresini 120 saniyeye çıkardık)
try:
    driver.get(main_url)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.TAG_NAME, "html")))  # Sayfanın yüklenmesini bekleyin
    print("Sayfa yüklendi!")
except Exception as e:
    print(f"Sayfa yüklenirken hata oluştu: {e}")
    driver.quit()

# Ana sayfanın HTML içeriğini al ve işle
html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")

# 1️⃣ Yeni 'col-xl-4 col-sm-6 mb-5' class'ını bul
profile_links = []

for container in soup.find_all("div", class_="col-xl-4 col-sm-6 mb-5"):
    a_tag = container.find("a", href=True)
    if a_tag:
        href = a_tag["href"]
        if href.startswith("http"):
            profile_links.append(href)
        else:
            full_url = f"https://www.selcuk.edu.tr{href}"
            profile_links.append(full_url)

print(f"🔍 {len(profile_links)} profil bağlantısı bulundu!")

# 2️⃣ Profilleri tek tek ziyaret et ve e-posta adresini al
emails = []
for profile_url in profile_links:
    try:
        driver.get(profile_url)
        
        # Sayfa tamamen yüklenene kadar bekle (maks 10 saniye)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "staff-name")))

        profile_html = driver.page_source
        profile_soup = BeautifulSoup(profile_html, "html.parser")

        # 3️⃣ E-posta adresini bul
        email_element = profile_soup.find("a", class_="mailTo")
        if email_element:
            email = email_element.get_text(strip=True)
            emails.append(email)
            print(f"✅ {profile_url} adresinden e-posta bulundu: {email}")
        else:
            print(f"⚠ '{profile_url}' sayfasında e-posta bulunamadı!")

    except Exception as e:
        print(f"⛔ '{profile_url}' sayfasında hata oluştu: {e}")

# Sonuçları ekrana yazdır
driver.quit()

if emails:
    print("\n📧 OLUŞTURULAN E-POSTALAR:")
    for email in emails:
        print(email)
else:
    print("\n❌ Hiç e-posta bulunamadı!")
