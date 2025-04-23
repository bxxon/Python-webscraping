<?php
// Kullanıcının IP adresini al
$ip = $_SERVER['REMOTE_ADDR'];

// Log dosyasının yolu
$file = 'ip_log.txt';

// IP adresini dosyaya yaz
file_put_contents($file, $ip . "\n", FILE_APPEND);

// Kullanıcıya bir yanıt verin (isteğe bağlı)
echo "IP adresiniz loglandı.";
?>
