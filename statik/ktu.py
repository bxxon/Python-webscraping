import requests
from bs4 import BeautifulSoup


# URL'yi belirleyin
url = "https://math.gatech.edu/people?field_job_type_tid=11"

# URL'den kaynak kodunu alın
response = requests.get(url)
html_content = response.text

# BeautifulSoup kullanarak HTML'i parse edin
soup = BeautifulSoup(html_content, "html.parser")

target_src = "views-field views-field-field-email"
img_tags = soup.find_all('img', src=target_src)

# Her bir img etiketinin parent'ının içindeki metni alma
for img_tag in img_tags:
    parent_tag = img_tag.parent
    if parent_tag:
        text_inside_parent = parent_tag.get_text(strip=True)
        print( text_inside_parent + "@ktu.edu.tr")
