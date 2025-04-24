from bs4 import BeautifulSoup
import requests

url = "https://www.math.nus.edu.sg/people/regular-faculty/"

# URL'den kaynak kodunu alın
response = requests.get(url)
html_content = response.text

# HTML içeriğini parse edelim
soup = BeautifulSoup(html_content, 'html.parser')

# "email:" içeren tüm metinleri bulalım ve işleyelim
for elem in soup.find_all(string=lambda text: 'e-mail:' in text):
    new = elem.strip().replace("e-mail:","")
    if(new != ""):
        print((new + "@marmara.edu.tr").strip())

    
    


