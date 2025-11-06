isim = input("Adınızı girin: ")
problem = input("Probleminizi girin: ")

print("Merhaba", isim + ",", problem, "ile ilgileniyorum.")

while True:
    cevap = input("Probleminiz çözüldü mü? (evet/hayır): ").lower()
    
    if cevap == "evet":
        print("Harika! Memnuniyet anketine yönlendiriliyorsunuz...\n")
        
      
        puan = int(input("1 ile 5 arasında hizmetimizi nasıl değerlendirirsiniz? "))
        yorum = input("Eklemek istediğiniz bir yorum var mı?: ")
        
        print("\nTeşekkürler,", isim + "!")
        print("Değerlendirmeniz:", puan)
        print("Yorumunuz:", yorum)
        break  
    elif cevap == "hayır":
        print("Tamam, tekrar deniyorum... Lütfen biraz bekleyin.\n")
    else:
        print("Lütfen sadece 'evet' veya 'hayır' yazın.\n")
