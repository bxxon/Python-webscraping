from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def log_ip():
    # Kullanıcının IP adresini al
    ip = request.remote_addr

    # IP adresini log dosyasına yaz
    with open('ip_log.txt', 'a') as f:
        f.write(ip + '\n')

    return "IP adresiniz loglandı."

if __name__ == '__main__':
    app.run(host='192.168.180.100', port=5000)
