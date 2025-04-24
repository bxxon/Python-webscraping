import requests
from bs4 import BeautifulSoup

# URL'yi belirle
url = "http://www.fen.bilkent.edu.tr/~cvmath/tr/faculty-tr.html"

# URL'den HTML içeriğini al
response = requests.get(url)
html_content = response.text

# BeautifulSoup ile HTML içeriğini işle
soup = BeautifulSoup(html_content, 'html.parser')

# -at- yazısını içeren elementleri bul ve yazılarını al
elements_with_at = soup.find_all(text=lambda text: '[-at-]' in str(text))

# Bulunan elementleri yazdır
for element in elements_with_at:
    print(element.strip())
