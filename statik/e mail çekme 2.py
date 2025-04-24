# import requests
# from bs4 import BeautifulSoup

# # Web sitesinin URL'si
# url = "https://birimler.atauni.edu.tr/matematik/akademik-personel/"

# # Web sitesinden veri çekme
# response = requests.get(url)

# # HTML içeriğini işleme
# soup = BeautifulSoup(response.text, "html.parser")

# # E-posta adreslerini saklamak için bir liste oluşturma
# emails = []

# # Her bir öğretim görevlisinin bilgilerini içeren HTML elementlerini bulma
# academic_staff = soup.find_all("div", class_="personel-kutu")

# # Her bir öğretim görevlisinin bilgilerini kontrol etme
# for personel in academic_staff:
#     # E-posta adresini içeren HTML elementini bulma
#     email_element = personel.find("a", class_="email")

#     # E-posta adresi varsa, bu adresi alıp emails listesine ekleyin
#     if email_element:
#         email = email_element.text.strip()
#         emails.append(email)

# # E-posta adreslerini yazdırma
# for email in emails:
#     print(email)

import time
import requests
from bs4 import BeautifulSoup
import re

def unique_strings(string_list):
    unique_list = []
    for string in string_list:
        if string not in unique_list:
            unique_list.append(string)
    return unique_list


# URL'yi belirleyin
url = "https://research.monash.edu/en/organisations/school-of-mathematics/persons/?page=1"
# URL'den kaynak kodunu alın
response = requests.get(url)
html_content = response.text.replace("<span class=\"email-ta\"></span><script>encryptedA();</script>","@").replace("<span class=\"email-tod\"></span><script>encryptedDot();</script>",".")
#print(html_content)

# print(response.text)
# BeautifulSoup kullanarak HTML'i parse edin
soup = BeautifulSoup(html_content, "html.parser")

# # Regex deseni tanımlayın
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Tüm e-postaları bulun
emails = unique_strings(re.findall(email_pattern, html_content))
#print(len(emails))
# print(soup)

# Bulunan e-postaları yazdırın
for email in emails:
    
    print(email)
    

