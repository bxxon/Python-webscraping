# Web Scraping Projesi

Bu proje, farklı web sayfalarından veri çekmek için kullanılan bir web scraping aracıdır. Kullanıcılar, URL girerek ve belirli bir sınıf adı girerek web sayfasından verileri çekebilirler. Kodlar, statik ve dinamik web sayfaları için farklı yöntemler kullanarak veri çekme işlemlerini gerçekleştirir.

## Proje Özellikleri

- **Statik Sayfalar**: HTML içeriğini doğrudan analiz eden ve verileri çeken yöntemler.
- **Dinamik Sayfalar**: Selenium ve WebDriver kullanarak dinamik olarak yüklenen içeriklerden veri çeker.
- **Arayüz**: Kullanıcı, URL ve class bilgisi girerek verilerini kolayca çekebilir.

## Etik Kurallar

Bu projeye katkı sağlarken lütfen aşağıdaki etik kurallara uyduğunuzdan emin olun:

- **Dürüstlük**: Kodunuzu ve katkılarınızı dürüst bir şekilde yazın. Başkalarının çalışmalarını alıp kendi yazılımınız olarak sunmayın.
- **Saygı**: Diğer geliştiricilere saygılı ve adil davranın. Katkılarınızda olumlu ve yapıcı bir tutum sergileyin.
- **Erişilebilirlik**: Kodunuzu mümkün olduğunca erişilebilir hale getirin, açıklamalar ekleyin ve belgeleri güncel tutun.
- **İzinler ve Lisanslar**: Kullanmakta olduğunuz üçüncü parti yazılımlarının lisanslarına ve haklarına saygı gösterin. Bu projede kullanılan kütüphanelerin lisanslarına göz atın ve uygun şekilde kullanın.
- **Yasal Uyumluluk**: Yazılımın yasalarla uyumlu olduğundan emin olun. Özellikle kişisel verilerin korunmasına yönelik yasalar (örneğin GDPR) hakkında bilgi sahibi olun. Web scraping işlemleri yaparken, sitelerin kullanım şartlarına uymaya özen gösterin ve herhangi bir veriyi toplarken sitenin robots.txt dosyasına dikkat edin.
- **Adil Kullanım**: Web sayfalarından veri çekerken adil kullanım ilkesine sadık kalın. Web sitelerinin yükünü artıracak şekilde aşırı trafik gönderiminden kaçının.

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki kütüphanelerin kurulu olması gerekmektedir:

- **requests**: Web sayfalarına HTTP istekleri yapmak için kullanılır.
- **beautifulsoup4**: HTML ve XML verilerini analiz etmek için kullanılır.
- **selenium**: Dinamik web sayfalarından veri çekmek için kullanılır.
- **webdriver_manager**: WebDriver'ın doğru sürümünü otomatik olarak indirir.
- **re**: Regex kullanarak metin işleme.

### Kütüphaneleri Yüklemek İçin:

```bash
pip install requests beautifulsoup4 selenium webdriver_manager
## kullanım
python scraping.py
