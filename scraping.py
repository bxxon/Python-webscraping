import tkinter as tk
from tkinter import messagebox
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Statik ve dinamik kütüphaneler
dynamic_libraries = ['selenium', 'webdriver_manager', 'beautifulsoup4', 'flask', 'pandas', 'numpy']
static_libraries = ['requests', 're', 'beautifulsoup4']

def check_url(url):
    """URL'nin statik mi dinamik mi olduğunu kontrol et"""
    try:
        # URL'nin içeriğini alalım
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # URL içeriği içinde dinamik kütüphaneler var mı kontrol et
        if any(lib in response.text for lib in dynamic_libraries):
            return "dinamik"
        elif any(lib in response.text for lib in static_libraries):
            return "statik"
        else:
            return "bilinmiyor"
    except Exception as e:
        messagebox.showerror("Hata", f"URL kontrol edilirken bir hata oluştu: {e}")
        return None

def extract_emails_statik(url, class_name):
    """Statik sayfada mail adreslerini çıkar"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        mailto_pattern = re.compile(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
        mailto_links = []
        
        elements_with_class = soup.find_all(class_=class_name)
        for element in elements_with_class:
            found_mailtos = re.findall(mailto_pattern, str(element))
            mailto_links.extend(found_mailtos)
        
        if mailto_links:
            return "\n".join(mailto_links)
        else:
            return "Hiç mail adresi bulunamadı."
    except Exception as e:
        return f"Hata: {e}"

def extract_emails_dinamik(url, class_name):
    """Dinamik sayfada mail adreslerini çıkar (selenium kullanarak)"""
    try:
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-software-rasterizer")
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
        
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        
        mailto_pattern = re.compile(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
        mailto_links = []
        
        elements_with_class = soup.find_all(class_=class_name)
        for element in elements_with_class:
            found_mailtos = re.findall(mailto_pattern, str(element))
            mailto_links.extend(found_mailtos)
        
        driver.quit()
        
        if mailto_links:
            return "\n".join(mailto_links)
        else:
            return "Hiç mail adresi bulunamadı."
    except Exception as e:
        return f"Hata: {e}"

def on_submit():
    """Formu gönderme işlevi"""
    url = url_entry.get()
    class_name = class_entry.get()

    # URL'nin türünü kontrol et
    url_type = check_url(url)
    
    if url_type == "bilinmiyor":
        messagebox.showwarning("Uyarı", "Bu URL'nin türü bilinmiyor.")
        return
    
    result_text.delete(1.0, tk.END)
    
    # Kullanıcıya hangi türde işlem yapacağına göre işlemi başlat
    if url_type == "statik":
        result = extract_emails_statik(url, class_name)
    elif url_type == "dinamik":
        result = extract_emails_dinamik(url, class_name)
    
    # Sonuçları göster
    result_text.insert(tk.END, f"URL Türü: {url_type.capitalize()}\n\n{result}")

# Tkinter penceresini oluşturma
window = tk.Tk()
window.title("Web Scraping Arayüzü")
window.geometry("600x400")

# URL girişi
url_label = tk.Label(window, text="URL girin:")
url_label.pack(pady=10)
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

# Class adı girişi
class_label = tk.Label(window, text="Class adı girin:")
class_label.pack(pady=10)
class_entry = tk.Entry(window, width=50)
class_entry.pack(pady=5)

# Sonuçları gösterecek metin alanı
result_text = tk.Text(window, width=70, height=10)
result_text.pack(pady=20)

# Gönder butonu
submit_button = tk.Button(window, text="Kontrol Et ve Çek", command=on_submit)
submit_button.pack(pady=10)

# Pencereyi başlat
window.mainloop()
