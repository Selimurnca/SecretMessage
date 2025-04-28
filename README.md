Secret Message Project
Proje Açıklaması:
Bu proje, kullanıcıların metin mesajlarını belirli bir anahtar (key) kullanarak şifrelemelerini ve şifreli mesajları dosyaya kaydetmelerini sağlar. Ayrıca, aynı anahtar ile şifrelenmiş mesajları çözebilmek için bir çözme (decrypt) fonksiyonu da içerir. Proje, Python'un Tkinter kütüphanesini kullanarak bir grafiksel kullanıcı arayüzü (GUI) sağlar.

Kullanılan Teknolojiler:
Python 3.x

Tkinter (Grafiksel kullanıcı arayüzü için)

Pillow (Görüntü işleme için)

ASCII Değerleri (Şifreleme ve şifre çözme için)

Özellikler:
Metin yazma ve şifreleme: Kullanıcı, metin kutusuna bir mesaj yazar ve verilen anahtar ile bu mesaj şifrelenir. Şifreli mesaj bir dosyaya kaydedilir.

Şifreli mesajı çözme: Kullanıcı, aynı anahtar ile şifreli mesajı çözebilir ve orijinal mesajı tekrar görebilir.

Görseller: Proje, görsel öğelerle (örn. matrix görselleri) şık bir arayüz sağlar.

Kurulum ve Kullanım:
Gerekli Kütüphanelerin Yüklenmesi: Projeyi çalıştırmadan önce gerekli Python kütüphanelerini yükleyin:

bash
Kopyala
Düzenle
pip install pillow
Proje Dosyalarını Alın:

Proje dosyasını [GitHub Repo Linki] veya başka bir kaynak üzerinden indirin.

Proje içinde matrix.png ve matrix2.png gibi görsellerin bulunduğundan emin olun.

Projenin Çalıştırılması: Python betiğini çalıştırarak projeyi başlatın:

bash
Kopyala
Düzenle
python secret_message.py
Kullanım:

Mesaj Başlığı kısmına bir başlık yazın.

Secret Message kısmına şifrelemek istediğiniz mesajı yazın.

Key Words kısmına şifreleme ve şifre çözme işlemleri için kullanılacak anahtar (key) değerini girin.

Save & Encrypt butonuna tıklayarak mesajınızı şifreleyin ve SecretMassage.txt dosyasına kaydedin.

Decrypt butonuna tıklayarak şifreli mesajı çözebilirsiniz. Şifreli mesajı key ile çözülmüş haliyle görebilirsiniz.

Örnek Kullanım:
Kullanıcı "HELLO" mesajını yazıp, key olarak "abc" girer.

"Save & Encrypt" butonuna tıklandığında, "HELLO" mesajı "©§¯­±" gibi şifreli bir hale gelir.

Aynı key ile "Decrypt" butonuna tıklayarak, şifrelenmiş mesaj tekrar orijinal haline
