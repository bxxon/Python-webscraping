<?php
ob_start();
?>
<style>
    .bg-color {
        box-sizing: border-box;
        background-color: green;
        color: #000;
        width: 100%;
        font-weight: 600;
        text-align: center;
        font-size: 1.6rem;
        padding: 1rem;
    }

    .disable {
        display: none;
    }
</style>
<?php


require '/phpmailer/src/Exception.php';
require '/phpmailer/src/PHPMailer.php';
require '/phpmailer/src/SMTP.php';
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
use PHPMailer\PHPMailer\SMTP;

header('Content-Type: text/html; charset=utf-8');

//veritabanına veri eklemek için veri tabanı bağlantısını yapıyoruz.
$vt_sunucu = "localhost";
$vt_kullanici = "kullanıcıadı";
$vt_sifre = "sifre";
$vt_adi = "tablo adı";


// Bağlantıyı oluştur
$baglan = mysqli_connect($vt_sunucu, $vt_kullanici, $vt_sifre, $vt_adi);
$baglan->set_charset("utf8");

if (!$baglan) {
    die("Veri Tabanı Bağlantısı Başarısız: " . mysqli_connect_error());
}

//Post metodu ile gönderilen verilerimizi alıyoruz.
$firmaadi = isset($_POST["companyname"]) ? $_POST["companyname"] : NAN;
$firmatel = isset($_POST["companyphone"]) ? $_POST["companyphone"] : NAN;
$firmamail = isset($_POST["companymail"]) ? $_POST["companymail"] : NAN;
$firmatext = isset($_POST["companymessage"]) ? $_POST["companymessage"] : NAN;
$urunadi = isset($_POST["urunadi"]) ? $_POST["urunadi"] : NAN;
$urunrenk = isset($_POST["urunrenk"]) ? $_POST["urunrenk"] : NAN;
$urunadet = isset($_POST["urunadet"]) ? $_POST["urunadet"] : NAN;
$date = date("d-m-Y");
$urunid = isset($_POST["urunid"]) ? $_POST["urunid"] : NAN;

$urunler = new stdClass();
$arr = [];
$arr2 = [];
$firmabilgi = [];

function correct($str)
{
    $str = str_replace("ı", "i", $str);
    $str = str_replace("ö", "o", $str);
    $str = str_replace("ç", "c", $str);
    $str = str_replace("İ", "i", $str);
    $str = str_replace("ş", "s", $str);
    $str = str_replace("ğ", "g", $str);
    $str = str_replace("ü", "u", $str);
    return $str;
}



for ($i = 0; $i < count($urunadi); $i++) {

    $arr[] = [
        "name" => $urunadi[$i],
        "renk" => $urunrenk[$i],
        "adet" => $urunadet[$i],
        "firmaadi" => $firmaadi,
        "firmatel" => $firmatel,
        "firmamail" => $firmamail,
        "firmatext" => $firmatext,
        "date" => $date,
        'id' => $urunid[$i],
    ];
    $arr2[] = [
        "urun" => correct($urunadi[$i]),
        "renk" => correct($urunrenk[$i]),
        "adet" => $urunadet[$i],
        'urunid' => $urunid[$i],
    ];
    $firmabilgi = [
        "firmaadi" => $firmaadi,
        "firmatel" => $firmatel,
        "firmamail" => $firmamail,
        "firmamesaj" => $firmatext,
    ];
}

$xd = (object) $arr;

$ekle = $baglan->prepare("INSERT INTO teklifler (urun_adi,urun_renk,urun_adet,firma_adi,firma_tel,firma_mail,firma_text,_date,urun_id)  VALUES (?,?,?,?,?,?,?,?,?)");


foreach ($xd as $k => $v) {

    $ekle->bind_param("ssisssssi", $v['name'], $v['renk'], $v['adet'], $v['firmaadi'], $v['firmatel'], $v['firmamail'], $v['firmatext'], $v['date'], $v['id']);
    $ekle->execute();

}


$mail = new PHPMailer(true);

try {
    //Server settings
    // $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      //Enable verbose debug output
    $mail->isSMTP();                                            //Send using SMTP
    $mail->Host = 'smtp host adresi';                     //Set the SMTP server to send through
    $mail->SMTPAuth = true;                                   //Enable SMTP authentication
    $mail->Username = 'smtp mail adresi';                     //SMTP username
    $mail->Password = 'smtp şifresi';                               //SMTP password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;            //Enable implicit TLS encryption
    $mail->Port = 465;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`

    //Recipients
    $mail->setFrom('smtp mail adresi', "Mail gönderenin adı");
    $mail->addAddress('mail gönderilecek kişi');     //Add a recipient
    $mail->addAddress('mail gönderilecek 2. kişi');     //Add a recipient
    // $mail->addAddress('ellen@example.com');               //Name is optional
    // $mail->addReplyTo('info@example.com', 'Information');
    // $mail->addCC('cc@example.com');
    // $mail->addBCC('bcc@example.com');

    // //Attachments
    // $mail->addAttachment('/var/tmp/file.tar.gz');         //Add attachments
    // $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    //Optional name

    //Content
    $mail->isHTML(true);                                  //Set email format to HTML
    $mail->Subject = "Mail Başlığı";
    $mail->Body = "Gönderilen Mailin İçeriği";

    $mail->AltBody = "None";

    $mail->send();
    echo "Mail Gönderildi!";


    exit();
} catch (Exception $e) {
    echo "Mail Gönderilemedi Hata kodu: {$mail->ErrorInfo}";
}

ob_end_flush();
?>