# HTTP Server Projesi Raporu

## 1. Projenin Amacı
Bu projede, Python ile bir HTTP sunucusu geliştirerek HTTP protokolü üzerinden GET ve POST isteklerinin işlenmesi ve dosya yükleme gibi temel işlevlerin uygulanması hedeflenirken aynı zamanda da çok iş parçacıklı bir yapıya sahip olması da hedeflenmektedir.

## 2. Projenin Tanımı
HTTP sunucusu, istemcilerden gelen GET ve POST isteklerini karşılamaktadır. GET isteğinde dinamik olarak veri sunulurken, POST isteğinde istemciden gelen dosya sunucuya kaydedilir ve gerekli yanıt istemciye döndürülür.

## 3. Kullanılan Teknolojiler
- **Programlama Dili**: Python
- **Kütüphaneler**:
  - socket (TCP/IP bağlantısı için)
  - concurrent.futures.ThreadPoolExecutor (çoklu istemci desteği için)
  - os (dosya işlemleri için)
- **Test Araçları**: Postman
- **Yardımcı Modüller**:
  - core.middleware.exceptionMiddleware (hata yönetimi)
  - core.utils.binaryParser (dosya kaydetme)
  - core.utils.receiveFullRequest (tam HTTP isteği alımı)
  - core.utils.slugParser (istek ayrıştırma)
  - view.dataView (dinamik veri oluşturma)

## 4. Mimari
- **Sunucu Mimarisi**:
  - **Socket Bağlantısı**: TCP/IP protokolü kullanılarak istemci-sunucu bağlantısı sağlanır.
  - **Thread Pool**: Aynı anda birden fazla istemci bağlantısını yönetmek için ThreadPoolExecutor kullanılmaktadır.
  - **Middleware Yapısı**: Hataları yakalamak ve işlemleri kolaylaştırmak için ara yazılımlar kullanılmıştır.

- **Uygulama Adımları**:
  - **Socket Sunucusunun Oluşturulması**
  - **Dosya Kayıt Dizinini Oluşturma**
  - **HTTP İsteklerinin Karşılanması**:
    - **GET isteği için**: slugParser ile istek ayrıştırılır ve DataView modülü kullanılarak uygun yanıt döndürülür.
    - **POST isteği için**: Gelen veriler save_file_from_bytes yardımıyla dosya olarak kaydedilir ve GET isteğine benzer bir yanıt döndürülür.
  - **Hata Yönetimi**: Tüm işlevler exceptionMiddleware ile sarılarak hata durumlarında sunucunun yanıt verebilmesi sağlanır.

## 5. Test Senaryoları
- Sunucunun başlatılması ve port dinleme kontrolü
- GET isteğinde dinamik verinin doğru dönmesi
- POST isteğinde dosyanın başarıyla kaydedilmesi
- Yanlış formatta gelen HTTP isteklerine "405 Method Not Allowed" yanıtı verilmesi
- Hata durumunda "500 Internal Server Error" mesajı dönmesi

## 6. Karşılaşılan Sorunlar ve Çözümler
- **Sorun**: POST isteğinde dosyanın eksik kaydedilmesi.
- **Çözüm**: receive_full_request ile tam HTTP isteği alınmıştır.

## 7. Sonuç ve Değerlendirme
Bu proje ile basit bir HTTP sunucusu geliştirilmiştir. GET-POST istekleri ve dosya yükleme gibi temel HTTP işlevleri, temel istemci-sunucu iletişimi başarıyla uygulanmıştır.

## 8. Projede Emeği Geçen Yazılımcılar
- **Ahmet Özseven**
  - **Yaptığı Çalışmalar**:
    - GET İstekleri: Ahmet, web sunucusunun GET isteklerini işleyen kısmını geliştirdi.
    - Dosya Yükleme (Upload) Özelliği: Ahmet, kullanıcıların dosya yükleme imkanını sunan modülü tasarladı ve implementasyonunu gerçekleştirdi.
    - Proje Temeli ve Yapılandırma: Projenin genel yapı taşlarını oluşturdu ve geliştirme ortamının kurulumunda öncü oldu.

- **Berkay Emikönel**
  - **Yaptığı Çalışmalar**:
    - POST İstekleri: Berkay, web sunucusunun POST isteklerini işleyen kısmını geliştirdi.
    - Proje Yapılandırma: Ahmet Özseven ile birlikte, projenin başlangıç aşamalarında yardımcı oldu.

- **Ahmet Hakan Özkurt**
  - **Yaptığı Çalışmalar**:
    - Multi-Threading Desteği: Ahmet Hakan, web sunucusuna multi-threading desteği kazandırdı.
    - HTML ve CSS Tasarımı: Ahmet Hakan, web sunucusunun arayüzünü tasarladı.

- **Yiğit Kadayifçi & Hüseyin Berke Ok**
  - **Yaptıkları Çalışmalar**:
    - Dosya İndirme Modülü: Yiğit ve Hüseyin, dosya indirme modülünü geliştirdiler.

- **Kerem Batı**
  - **Yaptığı Çalışmalar**:
    - Home Page Düzenlemeleri: Kerem, HTML sayfasının ana sayfasına eklemeler yaptı.

## Sonuç ve Değerlendirme
Grup olarak, her birimiz projeye katkı sağlayarak, farklı alanlarda görev aldık ve bu projeyi başarıyla tamamladık. Ahmet Özseven ve Berkay Emikönel, temel işlevleri ve altyapıyı oluşturduktan sonra, Ahmet Hakan Özkurt, sunucunun performansını iyileştirdi ve estetik anlamda sayfanın tasarımını yaptı. Yiğit Kadayifçi ve Hüseyin Berke Ok, dosya indirme modülünü geliştirerek kullanıcıların veri almasını sağladı. Kerem Batı ise ana sayfa üzerinde önemli düzenlemeler yaparak, kullanıcıların sunucu ile daha etkileşimli hale gelmesini sağladı.
