import requests
from bs4 import BeautifulSoup
import re

# Ana sayfa URL'si
base_url = 'https://history.hacettepe.edu.tr/tr/menu/ogretim_uyeleri-59'  # Değiştirmeniz gereken URL

# Sayfayı çekme
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tabloları bulma
tables = soup.find_all('table')  # Tablo etiketini buluyoruz

# Mail adresi regex deseni
email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

# 5. sütundaki mail adreslerini toplama
mailto_links = []

# Her tabloyu kontrol et
for table in tables:
    rows = table.find_all('tr')  # Satırları alıyoruz
    
    for row in rows:
        cols = row.find_all('td')  # Sütunları alıyoruz
        
        # Eğer 5. sütun varsa
        if len(cols) >= 5:
            email_column = cols[2]  # 5. sütun (index 4)
            email_text = email_column.get_text().strip()  # Metni alıyoruz
            
            # Mail adreslerini regex ile çekiyoruz
            found_emails = re.findall(email_pattern, email_text)
            if found_emails:
                mailto_links.extend(found_emails)

# mailto bağlantılarını terminale yazdırma
for mail in mailto_links:
    print(mail)
