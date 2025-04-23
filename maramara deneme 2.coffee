from bs4 import BeautifulSoup

# Örnek HTML kodu
html_content = """
<li ng-if="abd" class="ng-scope">
    <p ng-bind-html="ds_profile.Personel.Eposta | email" class="ng-binding">
        barisozener<span><i class="fa fa-at"></i></span>istanbul.edu.tr
    </p>
</li>
"""

# BeautifulSoup ile HTML'yi parse et
soup = BeautifulSoup(html_content, 'html.parser')

# E-posta kısmını bul
email_part = soup.find('p', class_='ng-binding')

# 'ng-binding' içindeki metni al
name = email_part.contents[0]  # 'barisozener'
domain = email_part.contents[2]  # 'istanbul.edu.tr'

# '@' işaretini ekle
email = f"{name}@{domain}"

print(email)
