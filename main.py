# 1. GİRDİLERİN ALINMASI VE TEMİZLENMESİ
musteri_adi = input("Müşteri Adı: ").strip().title()
urun_adi = input("Ürün Adı: ").strip().capitalize()
adet = int(input("Adet: "))
birim_fiyat = float(input("Birim Fiyat (TL): "))
kulup_uye = input("Sadakat Kulübü Üyesi mi? (E/H): ").strip().lower() == "e"
saat = int(input("Sipariş Saati (0-23): "))

# 2. HESAPLAMA VE KARAR YAPILARI (İNDİRİM MANITIĞI)
ham_tutar = adet * birim_fiyat

# Mutlu Saatler (Happy Hour: 14:00 - 17:00 arası %15 indirim)
happy_hour = 14 <= saat <= 17

indirim_orani = 0.0
if kulup_uye and happy_hour:
    indirim_orani = 0.25  # Hem üye hem Happy Hour ise %25 indirim
elif kulup_uye:
    indirim_orani = 0.10  # Sadece üye ise %10 indirim
elif happy_hour:
    indirim_orani = 0.15  # Sadece Happy Hour ise %15 indirim

indirim_tutari = ham_tutar * indirim_orani
odenecek_tutar = ham_tutar - indirim_tutari

# 3. HİZALANMIŞ FİŞ ÇIKTISI (F-STRING & STR METOTLARI)
print("\n" + " KAFE FİŞİ ".center(30, "*"))
print(f"Müşteri  : {musteri_adi}")
print(f"Saat     : {saat:02d}:00")
print("-" * 30)
print(f"{'Ürün':<12}{'Adet':^6}{'Tutar':>12}")
print("-" * 30)
print(f"{urun_adi:<12}{adet:^6}{ham_tutar:>12.2f} TL")

if indirim_tutari > 0:
    print(f"{'İndirim':<18}{-indirim_tutari:>12.2f} TL")

print("=" * 30)
print(f"{'TOPLAM TUTAR':<18}{odenecek_tutar:>12.2f} TL")
print("=" * 30)
print(f"{'Bizi Tercih Ettiğiniz İçin Teşekkürler!':^30}")
