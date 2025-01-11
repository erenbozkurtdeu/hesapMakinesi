Hesap Makinesi Test Senaryoları
===============================

Pozitif Senaryo
---------------
Tags: Yatırım Hesaplamaları
* Login olunur
* 100 değeri yazılır
* "showNumber" elementi "100" değerini içeriyor mu kontrol et
* Elementine tıkla "multipleButton"
* 1,05 değeri yazılır
* "showNumber" elementi "100 * 1,05" değerini içeriyor mu kontrol et
* Elementine tıkla "equalButton"
* "showNumber" elementi "100 * 1,05 = 105" değerini içeriyor mu kontrol et
* "1" saniye bekle

Negatif Senaryo
---------------
Tags: Yatırım Hesaplamaları
* Login olunur
* 100 değeri yazılır
* "showNumber" elementi "100" değerini içeriyor mu kontrol et
* Elementine tıkla "multipleButton"
* Elementine tıkla "oneButton"
* Elementine tıkla "equalButton"
* "showNumber" elementi "100 * 1 = 100" değerini içeriyor mu kontrol et
* "1" saniye bekle

Sıfır Senaryosu
---------------
Tags: Yatırım Hesaplamaları
* Login olunur
* 100 değeri yazılır
* "showNumber" elementi "100" değerini içeriyor mu kontrol et
* Elementine tıkla "multipleButton"
* Elementine tıkla "zeroButton"
* Elementine tıkla "equalButton"
* "showNumber" elementi "100 * 0 = 0" değerini içeriyor mu kontrol et
* "1" saniye bekle

Karar Tablosu İlk Değer Senaryosu
---------------------------------
Tags: Aylık Bütçe Hesaplaması
* Login olunur
* 1000 değeri yazılır
* Elementine tıkla "subtractButton"
* 800 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1000 - 800 = 200" değerini içeriyor mu kontrol et
* "1" saniye bekle

Karar Tablosu İkinci Değer Senaryosu
---------------------------------
Tags: Aylık Bütçe Hesaplaması
* Login olunur
* 1000 değeri yazılır
* Elementine tıkla "subtractButton"
* 1000 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1000 - 1000 = 0" değerini içeriyor mu kontrol et
* "1" saniye bekle

Karar Tablosu Üçüncü Değer Senaryosu
---------------------------------
Tags: Aylık Bütçe Hesaplaması
* Login olunur
* 1000 değeri yazılır
* Elementine tıkla "subtractButton"
* 1200 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1000 - 1200 = -200" değerini içeriyor mu kontrol et
* "1" saniye bekle

Karar Tablosu Dördüncü Değer Senaryosu
---------------------------------
Tags: Aylık Bütçe Hesaplaması
* Login olunur
* 2000 değeri yazılır
* Elementine tıkla "subtractButton"
* 1000 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "2000 - 1000 = 1000" değerini içeriyor mu kontrol et
* "1" saniye bekle

Karar Tablosu Beşinci Değer Senaryosu
---------------------------------
Tags: Aylık Bütçe Hesaplaması
* Login olunur
* 1500 değeri yazılır
* Elementine tıkla "subtractButton"
* 500 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1500 - 500 = 1000" değerini içeriyor mu kontrol et
* "1" saniye bekle

Karar Tablosu Altıncı Değer Senaryosu
---------------------------------
Tags: Aylık Bütçe Hesaplaması
* Login olunur
* 500 değeri yazılır
* Elementine tıkla "subtractButton"
* 500 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "500 - 500 = 0" değerini içeriyor mu kontrol et
* "1" saniye bekle

Kredi Karşılaştırma
-------------------
Tags: Kredi Karşılaştırması
* Login olunur
* Elementine tıkla "oneButton"
* Elementine tıkla "addButton"
* 0,01 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1 + 0,01 = 1,01" değerini içeriyor mu kontrol et
* "1" saniye bekle
* Elementine tıkla "multipleButton"
* 1,01 değeri yazılır
* Elementine tıkla "equalButton"
* 10 kere 1,01 ile çarpılır
* "1" saniye bekle
* Elementine tıkla "subtractButton"
* Elementine tıkla "oneButton"
* Elementine tıkla "equalButton"
* Elementine tıkla "acButton"
* 1000 değeri yazılır
* Elementine tıkla "multipleButton"
* 0,01 değeri yazılır
* Elementine tıkla "equalButton"
* Elementine tıkla "acButton"
* 10 değeri yazılır
* Elementine tıkla "multipleButton"
* 1,126825 değeri yazılır
* Elementine tıkla "equalButton"
* Elementine tıkla "divideButton"
* 0,126825 değeri yazılır
* Elementine tıkla "equalButton"

Yatırım Hesaplaması
-------------------
Tags: Kısa Vadeli Yatırım Hesaplaması
* Login olunur
* 0,03 değeri yazılır
* Elementine tıkla "multipleButton"
* 0,5 değeri yazılır
* Elementine tıkla "equalButton"
* Elementine tıkla "addButton"
* Elementine tıkla "oneButton"
* Elementine tıkla "equalButton"
* Elementine tıkla "multipleButton"
* 500 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1,015 * 500 = 507,5" değerine eşit mi kontrol et

Gider Takibi
------------
Tags: Günlük Gider Takibi
* Login olunur
* 20 değeri yazılır
* Elementine tıkla "addButton"
* 10 değeri yazılır
* Elementine tıkla "equalButton"
* Elementine tıkla "addButton"
* Elementine tıkla "fiveButton"
* Elementine tıkla "equalButton"
* "showNumber" elementi "30 + 5 = 35" değerine eşit mi kontrol et

Yıllık Yatırım Hesaplaması
--------------------------
Tags: Yıllık Yatırım Hesaplaması
* Login olunur
* Elementine tıkla "oneButton"
* Elementine tıkla "addButton"
* 0,04 değeri yazılır
* Elementine tıkla "equalButton"
* Elementine tıkla "multipleButton"
* 200 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1,04 * 200 = 208" değerine eşit mi kontrol et

Tl Usd Çevirme
--------------
Tags: Döviz Dönüşümü
* Login olunur
* 36000 değeri yazılır
* Elementine tıkla "divideButton"
* 33,1 değeri yazılır
* Elementine tıkla "equalButton"
* Elementine tıkla "acButton"
* Elementine tıkla "oneButton"
* Elementine tıkla "subtractButton"
* 0,002 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1 - 0,002 = 0,998" değerine eşit mi kontrol et
* Elementine tıkla "acButton"
* 1087,61 değeri yazılır
* Elementine tıkla "multipleButton"
* 0,998 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "1087,61 * 0,998 = 1085,43" değerine eşit mi kontrol et

Tl Euro Çevirme
---------------
Tags: Döviz Dönüşümü
* Login olunur
* 36000 değeri yazılır
* Elementine tıkla "divideButton"
* 36,5 değeri yazılır
* Elementine tıkla "equalButton"
* Elementine tıkla "acButton"
* Elementine tıkla "oneButton"
* Elementine tıkla "subtractButton"
* 0,002 değeri yazılır
* Elementine tıkla "equalButton"
* "1" saniye bekle
* Elementine tıkla "multipleButton"
* 986,3 değeri yazılır
* Elementine tıkla "equalButton"
* "showNumber" elementi "0,998 * 986,3 = 984,33" değerine eşit mi kontrol et