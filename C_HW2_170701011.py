-1-
#include<stdio.h>
  
int main() {
  
   int sayi,sayi1,sayi2;
  
   printf("\n 1.tamsayıyı giriniz: ");
   scanf("%d", &sayi);
  
   printf("\n 2.tamsayıyı giriniz: ");
   scanf("%d", &sayi1);
   
   printf("\n 3.tamsayıyı giriniz: ");
   scanf("%d", &sayi2);
   
 
   printf("\nGirdiğiniz sayılar şunlardır: %d %d %d ", sayi,sayi1,sayi2);
  
   return (0);
}
-2-
-a-
#include<stdio.h>
  
int main() {
    
    int n;
   
  
   printf("\n Lütfen bir değer giriniz: ");
   scanf("%d", &n);
   printf("\nN'nin değeri %d. ",n);
   return (0);
}



-b-
#include<stdio.h>
  
int main() {
    
    double kenar_uzunlugu,alan;
   
  
   printf("\nKarenin cm cinsinden uzunlugunu yazınız: ");
   scanf("%lf", &kenar_uzunlugu);
  
   alan = kenar_uzunlugu*kenar_uzunlugu;
   printf("\nkenar uzunluğu  %lf cm olan karenin alanı %lf kare cm'dir.  ", kenar_uzunlugu,alan);
   return (0);
}





-3-

#include<stdio.h>
  
int main() {
  
   int yaricap;
   float PI = 3.14, alan, cevre;
  
   printf("\nDairenin yarıçapını giriniz: ");
   scanf("%d", &yaricap);
  
   alan = PI * yaricap * yaricap;
   printf("\nDairenin alanı: %f ", alan);
  
   return (0);
}

-4-

1-Bazı bilgisayar kullanıcıları, gönderen kişiyi tanımadıkları sürece bir
e-posta mesajı açmazlar. Birisi neden bu politikayı benimseyebilir?
İnternet üzerinden tacizi engellemeye yönelik yasalar olduğunu biliyoruz ve Kişisel bilgilerin istendiği
şüpheli bir e-posta görürseniz bu e-postayı kimlik avı olarak bildirebiliriz. Bu sebeplerden dolayı
tanımadığımız kişilerden gelen mailleri açmamalıyız.

2-Okulunuzdaki intihal cezası var mı? Nedir?
İntihal cezası vardır. Ödevlerde intihal yakalanıyorsa bu ödevlerin notsuz bırakılması yani 0 girilmesidir.
Sınav kağıtlarında ise %80 oranındabenzerlik varsa sınav iptalidir ve final sınavına da girilmesi yasaktır.
Çok ileri düzeyde ise burs kesimi de olabilir.

3-E-posta eklerini açarken neden seçici olmak iyi bir politika?
E-postalarımıza dosya veya fotoğraf gibi ekleri ekleyebiliriz.En çok 25 MB boyutunda ek
gönderebiliriz.Hem boyut büyüklüğüne göre yer kaplamaması için
hem de ilgi duyduğumuz konular hakkında e-posta eklerini görüntüleyebiliriz.Böylece
fazlalık yapılmadan gerekli ekler dışında kalanları çöpe atmış oluruz.

-4- Virüs ve solucan terimlerini tanımlayın.
VİRÜSLER :
    Bilgisayar kullanıcıları tarafından farkında olmadan gönderilirler.Bu kötü amaçlı yazılımlar
çoğunlukla başka bir yazılımın yanında ek olarak ya da progrmların kaynak kodlarına
kendilerini gizleyebilirler.
Dosya sistemi virüsleri: Farklı dosya sistemleri içerisinde yer alan virüs çeşididir.

Önyükleme bölümü (boot sector) virüsleri: İşletim sisteminin önyükleme dosyaları arasına sızarak bilgisayarın açılmasıyla birlikte çalışmaya başlayan virüslerdir.

Makro yazılım virüsleri: MS Office gibi makro yazılımların içerisinde gizlenen virüslerdir.

Komut dosyası (script host) virüsleri: İnternet sayfalarının kaynak kodu dosyaları içerisinde gizlenen virüslerdir.

SOLUCANLAR:
    Genellikle e-posta ile gönderilen ekler, çeşitli web siteleri ve ağ üzerinde paylaşılan dosyaları kullanarak yayılırlar.
Solucanlar, bir sistemi ele geçirdiklerinde, kullanıcının başka bir eylemine ihtiyaç duymadan, kullanıcının veri kaynaklarını kullanarak
(e-posta adres listesi gibi) kendi kaynak dosyalarını hızlı bir şekilde diğer kullanıcılara da ulaştırmayı denerler ve bu yolla kendilerini
çok fazla sayıda çoğaltabilirler. Solucanlar bunu yaparken kullanıcıların bant genişliklerini ve ağ kaynaklarını kullandıklarından ağların
kilitlenmesine, e-posta sunucularının aşırı yüklenmesine veya Web kaynaklarına erişim hızının düşmesine sebep olabilmektedirler.




-5-
/*
* Calculate and display the difference of two
input values
*/
#include <stdio.h>
int main(void) {
int X;                              /*int tipinde değişkenlerimizi düşünüdük ve yazdık*/
 /* first input value*/  

int x;
/*second input value */
int sum; 
/* sum of inputs */

printf("\n 1.tamsayıyı giriniz: ");            /*toplama işlemine değer atamamız için 2 değer almalıyız ama void de tek başına değer almadan programı çalıştırabilir ben yinede değer aldım*/
scanf("%d", &X);
  
printf("\n 2.tamsayıyı giriniz: ");
scanf("%d", &x);

sum=X + x ;
printf("%d + %d = %d\n", X ,x, sum);                /* toplama işlemini üst satırda tanımladık alt satırda ise değerlerini yerleştirip işlem yaptırdık*/
scanf("%d%d",&X,&x); 

return (0);
    
}

---çıktı---
                                                                                                                                                                                    
 1.tamsayıyı giriniz: 2                                                                                                                                                             
                                                                                                                                                                                    
 2.tamsayıyı giriniz: 3                                                                                                                                                             
2 + 3 = 5                                                                                                                                                                           
           



