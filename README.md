Bugün hataları gidermek için uğraştım klasörler yapı olarak daha anlaşılır oldu kodlarda anlaşılmayan isimleri daha anlaşılır yaptım ve artık hata da almıyoruz  birde loglama makenizması kurdum /logs altına şimdi yaptığım değişiklikleri anlatayım:

öncelikle main.py dosyası için:
<li>0:20 socket açılır ve tarayıcıdan request istek verisi alınır</li>
<li>exceptionMiddleware var o heryere try except yazmak yerine @exceptionMiddleware bu dekoratörü ekleyerek hata ayıklamamızı sağlar</li>
<li>slug parser var url'i parçalar </li>
<li> view var view hangi url için hangi cevabı döneceğimizi belirleyen katmandır </li>
<li>kullanıcıya dönülen html kodları view/templateFiles altındadır (@mainComponent adında bir dekoratör var bu dekoratör bizim her html nesnesi için aynı template'i dönmemizi sağlıyor yani sadece body değişiyor)</li>
<li>exceptionlar artık direkt olarak kullanıcıya dönülüyor</li>

