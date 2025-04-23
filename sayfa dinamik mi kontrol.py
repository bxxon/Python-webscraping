import requests

url = "https://edebiyat.istanbul.edu.tr/tr/akademikkadro"
response = requests.get(url)

# Sayfanın HTML kaynağını kaydet
with open("source.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML kaynağı 'source.html' olarak kaydedildi. İçeriği elle kontrol edin.")
