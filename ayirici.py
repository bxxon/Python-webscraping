import os
import shutil

# Dinamik ve Statik kütüphaneler
dynamic_libraries = ['selenium', 'webdriver_manager', 'beautifulsoup4', 'flask', 'pandas', 'numpy']
static_libraries = ['requests', 're', 'beautifulsoup4']

# Çalışma dizinindeki dosyaları kontrol et
current_dir = os.getcwd()

statik_files = []
dinamik_files = []

# Dosyaların içeriğini kontrol et
for file_name in os.listdir(current_dir):
    if file_name.endswith(".py") and file_name != "ayirici.py":  # .py uzantılı dosyaları kontrol et
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

        # Dinamik kütüphaneleri içeriyorsa dinamik olarak sınıflandır
        if any(lib in content for lib in dynamic_libraries):
            dinamik_files.append(file_name)
        # Statik kütüphaneleri içeriyorsa statik olarak sınıflandır
        elif any(lib in content for lib in static_libraries):
            statik_files.append(file_name)

# Statik ve Dinamik klasörlerini oluştur
statik_dir = os.path.join(current_dir, 'statik')
dinamik_dir = os.path.join(current_dir, 'dinamik')

# Eğer klasörler yoksa oluştur
if not os.path.exists(statik_dir):
    os.mkdir(statik_dir)

if not os.path.exists(dinamik_dir):
    os.mkdir(dinamik_dir)

# Dosyaları klasörlere taşı
for file in statik_files:
    shutil.move(file, os.path.join(statik_dir, file))

for file in dinamik_files:
    shutil.move(file, os.path.join(dinamik_dir, file))

# Çıktı
print("Statik dosyalar:")
if statik_files:
    for file in statik_files:
        print(f"- {file}")
else:
    print("Hiç statik dosya bulunamadı.")

print("\nDinamik dosyalar:")
if dinamik_files:
    for file in dinamik_files:
        print(f"- {file}")
else:
    print("Hiç dinamik dosya bulunamadı.")
