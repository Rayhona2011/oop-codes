# name = "python"
# son  = 10

# ismi = "Ali"
# yoshi = 40
# mutaxasisligi = "Bolalar shifokori"

# print(f"Shifokor ismi {ismi}\nShifokor yoshi:{yoshi}\nShifokor mutaxasissligi: {mutaxasisligi}")

# ism2 = "Xasan"
# yoshi2 = 38
# mutaxasisligi2 = "Jarroh"

# print(f"Shifokor ismi {ism2}\nShifokor yoshi:{yoshi2}\nShifokor mutaxasissligi: {mutaxasisligi2}")

# Opject oriented programming(OOP)
# class va obyekt



# class Shifokor: #bu shablon
#     def __init__(self ,ismi , yoshi , mutaxassisligi):
#         self.name = ismi
#         self.age = yoshi
#         self.mutaxassisligi = mutaxassisligi
        
#     def malumot_ber(self):    
#         return f"Shifokor ismi {self.name}\nShifokor yoshi:{self.age}\nShifokor mutaxasissligi: {self.mutaxassisligi}"



# doktor1 = Shifokor("Ali",40,"Bolalar shifokori") # bu esa shu shablon yaratilgan obyekt
# doktor2 = Shifokor("Xasan" , 38,"Jarroh")
# print(doktor1.malumot_ber(),doktor2.malumot_ber())


# 1
# class Student:
#     def __init__(self , ismi , yoshi , bahosi):
#         self.name = ismi
#         self.age = yoshi
#         self.baho = bahosi

#     def malumot_ber(self):
#         return f"Student ismi : {self.name}\nStudent yoshi : {self.age}\nStudent olgan bahosi : {self.baho}\n"
    
# student = Student("Ali" , 19 , 5)
# student2 = Student("Vali" , 20 , 4)
# student3 = Student("Xasan" , 19 , 3)
# student4 = Student("Xusan" , 20 , 5)
# print(student.malumot_ber(), student2.malumot_ber(),student3.malumot_ber(),student4.malumot_ber())

# 2
# class Avto:
#     def __init__(self , model , yil , rang):
#         self.modeli = model
#         self.yili = yil
#         self.rangi = rang

#     def malumot_ber(self):
#         return f"Modeli: {self.modeli}\n Yili: {self.yili}\n Rangi: {self.rangi}\n"
    
# telefon =Avto("samsung" , 2026 , "kulrang")
# print(telefon.malumot_ber())

# 3
# class Bank:
#     def __init__(self , balans , pul_qoshish , pul_yechish):
#         self.balansi = balans
#         self.qoshish = pul_qoshish
#         self.yechish = pul_yechish

#     def malumot_ber(self):
#         return f"Hisobingizda {self.balansi} so'm pul bor\nSiz {self.qoshish} so'm qoshdingiz\nSiz {self.yechish} so'm yechib oldingiz"
    
# pul = Bank(200000 , 150000 , 90000)
# print(pul.malumot_ber())

# # 4
# class Dokon:
#     def __init__(self , mahsulot):
#         self.mahsulotlar = mahsulot
#         self.royhat = []

#     def add_meva(self , mahsulot_nomi):
#         self.royhat.append(mahsulot_nomi)

#     def show_meva(self):
#         return f"{self.mahsulotlar}   do'kondagi mahsulotlar ro'yxati"
    
# dokon = Dokon("Oziq - ovat do'koni")
# dokon.add_meva("Apelsin")
# print(dokon.show_meva())


# 5
# class Kompaniya:
#     def __init__(self , kompaniya_nomi):
#         self.name = kompaniya_nomi
#         self.ishchilar = []

#     def add_hodim(self , hodim_ismi):
#         self.ishchilar.append(hodim_ismi)

#     def del_hodim(self , hodim_ismi):
#         self.ishchilar.remove(hodim_ismi)

#     def show_hodim(self):
#         return f"{self.name} kompaniyasidagi ishchilar ro'yhati {self.ishchilar}"
    
# kompaniya = Kompaniya("Artel")
# kompaniya.add_hodim("Rayhona")
# kompaniya.del_hodim("Sevinchoy")
# kompaniya.add_hodim("Dilnura")
# print(kompaniya.show_hodim())
    
# 6
# class Mashina:
#     def __init__(self , model):
#         self.name = model
#         self.tezlik = [] 

#     def add_tez(self , mashina_tezligi):
#         self.tezlik.append(mashina_tezligi)

#     def show_tez(self):
#         return f"{self.name} mashinasi tezligi {self.tezlik}"
    
# mashina = Mashina("BMW")
# mashina.add_tez("1500km/h")
# print(mashina.show_tez)

# 7
# class Telefon:
#     def __init__(self , nom , brend , batareya):
#         self.name = nom
#         self.brendi = brend 
#         self.quvvati = batareya

#     def add_quvvat(self ):
#         return f"Telefonizda {self.quvvati}% zaryad bor 100% bo'lguncha {100-self.quvvati}% ga to'ldirish kerak"


# samsunga36 = Telefon("Samsung A36" , "Samsung" , 25)

# print(samsunga36.add_quvvat())

# 8
# class Oqituvchi:
#     def __init__(self , ism , fan , tajriba):
#         self.name = ism
#         self.fani = fan
#         self.tajribasi = tajriba

#     def info(self):
#         return f"O'qituvchi ismi:{self.name}\nO'qituvchi fani:{self.fani}\nO'qituvhi tajribasi{self.tajribasi}\n\n"
    
# ustoz1 =Oqituvchi("Sevinchoy" , "Ingliz tili" , "O'rtacha")    
# ustoz2=Oqituvchi("Dilnura" , "Huquq" , "Boshlang'ich")
# print(ustoz1.info() , ustoz2.info())
 
# 9
# class Noutbook:
#     def __init__(self , name , ram , hdd , cpu):
#         self.name = name
#         self.ram = ram
#         self.hdd =hdd
#         self.cpu = cpu

#     def info(self):
#         return f"kompyuter nomi :{self.name}\nRAM:{self.ram}\nHdd{self.hdd}\nCPU:{self.cpu}"
        
# kompyuter = Noutbook("HP", "16Gb" , "1TB" , "Intel Core i5-10400F")
# print(kompyuter.info())

# class Ustoz:
#     def __init__(self ,  maktab_raqami , ism , yosh , tajriba):
#         self.name = maktab_raqami
#         self.ismi = ism
#         self.yoshi = yosh
#         self.tajribasi = tajriba
#         self.royhat = []

#     def malumot_ber(self):
#         return f"O'qituvchi ismi{self.ismi}\nO'qituvchi yoshi{self.yoshi}\nTajribasi{self.tajribasi}"
    
#     def add_ustozlar(self , ustozlar_ismi):
#           self.royhat.append(ustozlar_ismi)

#     def del_ustozlar(self , ustozlar_ismi):
#           self.royhat.remove(ustozlar_ismi)

#     def show_ustozlar(self):
#          return f"{self.name}-son maktabdagi ustozlar royhati {self.royhat}"
    
# maktab = Ustoz(6 ,"Sevinchoy , Dilnura" , 15 , "O'rtacha")
# maktab.add_ustozlar("Sevinchoy")
# maktab.add_ustozlar("Dilnura")
# maktab.del_ustozlar("Rayhona")
# print(maktab.show_ustozlar())

# 10
# class Oquvchi:
#     def __init__(self , maktb_raqami):
#         self.name = maktb_raqami
#         self.oquvchilar = []

#     def add_oquvchi(self , oquvchi_ismi):
#         self.oquvchilar.append(oquvchi_ismi)

#     def del_oquvchi(self , oquvchi_ismi):
#         self.oquvchilar.remove(oquvchi_ismi)

#     def show_oquvchi(self):
#         return f"{self.name}-son maktabdagi o'quvchilar royhati {self.oquvchilar}"


# maktab = Oquvchi(6)
# maktab.add_oquvchi("Ali")
# maktab.add_oquvchi("Vali")
# maktab.add_oquvchi("Xusan")
# maktab.add_oquvchi("Xasan")
# maktab.del_oquvchi("Xasan")
# print(maktab.show_oquvchi())

# 11
# class Shaxs:
#     def __init__(self , ism , yosh):
#         self.name = ism
#         self.age = yosh
    
#     def malumot_ber(self):
#         return f"Shaxs ismi :{self.name}\nShaxs yoshi :{self.age}"
    
# shaxs1 = Shaxs("Ali" , 19)
# print(shaxs1.malumot_ber())

# 12
# class Maktab:
#     def __init__(self , maktab_raqami):
#         self.name = maktab_raqami
    
# 13
# class Kitob:
#     def __init__(self , nomi , muallifi , sahifasi):
#         self.name = nomi
#         self.muallifi = muallifi
#         self.sahifasi = sahifasi

#     def info(self):
#         return f"Kitob nomi : {self.name}\nKitob muallifi : {self.muallifi}\nKitob sahifasi : {self.sahifasi}"

# kitob = Kitob("Odam bo'lish qiyin" , "O'lmas Umarbekov" , 200)
# print(kitob.info())

# 14
# class Kutubxona:
#     def __init__(self , kitob_nomi , kitob_muallifi):
#         self.name = kitob_nomi
#         self.muallifi = kitob_muallifi
#         self.royhat = []

#     def add_kitob(self , kitob_nomi):
#         self.royhat.append(kitob_nomi)

#     def del_kitob(self , kitob_nomi):
#         self.royhat.remove(kitob_nomi)
    
#     def show_kitob(self):
#         return f"{self.name} kutubxonasidagi kitoblar ro'yhati {self.royhat}"
    
# kutubxona = Kutubxona("Maktab kutubxonasi" , "O'lmas Umarbekov")
# kutubxona.add_kitob("Odam bo'lish qiyin")
# kutubxona.add_kitob("Odam bo'lish qiyin 2")
# kutubxona.del_kitob("Odam bo'lish qiyin 2")
# print(kutubxona.show_kitob())




# class Firma:
#     def __init__(self , nomi):
#         self.name = nomi
#         self.shartnomalar = []

#     def add_shartnoma(self , shartnoma_nomi):
#         self.shartnomalar.append(shartnoma_nomi)
    
#     def del_shartnoma(self , shartnoma_nomi):
#         self.shartnomalar.remove(shartnoma_nomi)

#     def show_shartnoma(self):
#         return f"{self.name} firmasidagi shartnomalar ro'yhati: {self.shartnomalar}"


# firma =Firma("ARTEL") 
# firma.add_shartnoma("Shartnoma 1")
# firma.add_shartnoma("Shartnoma 2")
# firma.del_shartnoma("Shartnoma 2")
# print(firma.show_shartnoma())

# 16
# class Hayvon:
#     def __init__(self , hayvon_nomi , hayvon_turi , hayvon_ovozi):
#         self.name = hayvon_nomi
#         self.turi = hayvon_turi
#         self.ovozi = hayvon_ovozi   

#     def info(self):
#         return f"Hayvon nomi : {self.name}\nHayvon turi : {self.turi}\nHayvon ovozi : {self.ovozi}"
    
# hayvon = Hayvon("Mushuk" , "Uy hayvoni" , "Miyav")
# print(hayvon.info())

# 17
# class Uy:
#     def __init__(self , uy_manzili , xonalari_soni):
#         self.manzil = uy_manzili
#         self.xonalar = xonalari_soni

#     def info(self):
#         return f"Uy manzili : {self.manzil}\nUydagi xonalari soni : {self.xonalar}"
    
# uy = Uy("Xorazm Viloyati , Tuproqqal'a tumani" , 5)
# print(uy.info())

# 18
# class Oila:
#     def __init__(self , ism , yosh , kasb):
#         self.name = ism
#         self.age = yosh
#         self.kasbi = kasb

#     def info(self):
#         return f"Oila a'zosi ismi : {self.name}\nOila a'zosi yoshi : {self.age}\nOila a'zosi kasbi : {self.kasbi}"
    
    
# oila = Oila("Ali" , 19 , "Talaba")
# print(oila.info())

# 19
# class Sportchi:
#     def __init__(self, ism , sport_turi , natija):
#         self.name=ism
#         self.sport_turi = sport_turi
#         self.natija = natija

#     def info(self):
#         return f"Sportchi ismi : {self.name}\nSport turi : {self.sport_turi}\nSportchi natijasi : {self.natija}"
    
# sportchi = Sportchi("G'olibjon" , "kurash" , "0-o'rin")
# print(sportchi.info())

# 20
# class Sportchi:
#     def __init__(self , ism , yosh , sport_turi):
#         self.name = ism
#         self.age = yosh
#         self.sport_turi = sport_turi

#     def info(self):
#         return f"Sportchi ismi : {self.name}\nSportchi yoshi : {self.age}\nSport turi : {self.sport_turi}"
    
# sportchi = Sportchi("G'olibjon" , 15 , "kurash")
# print(sportchi.info())

# 21
# class Kompaniya:
#     def __init__(self , kompaniya_nomi):
#         self.name = kompaniya_nomi
#         self.ishchilar = []


#     def info(self):
#         return f"Kompaniya nomi : {self.name}"

# kompaniya = Kompaniya("Artel")          

# class Ishchi(Kompaniya):
#     def __init__(self, kompaniya_nomi , ishchilar):
#         add_ishchi = input("Ishchi ismini kiriting : ")
#         self.ishchilar.append(ishchilar)
#     def show_ishchi(self):
#         return f"{kompaniya.name} kompaniyasidagi ishchilar ro'yhati {self.ishchilar}"
    
# kompaniya = Ishchi("Artel" , "Rayhona")    
# print(kompaniya.show_ishchi())

# 22
# class Kino:
#     def __init__(self , nomi , janr , davomilylik):
#         self.name = nomi
#         self.janr = janr
#         self.davomiylik = davomilylik

#     def info(self):
#         return f"Kino nomi : {self.name}\nKino janri : {self.janr}\nKino davomiyligi : {self.davomiylik}"
    
# kino = Kino("Biz hammamiz o'likmiz" , "Qorqinchli" , "1 soat ")  
# print(kino.info())  

# 23
# class Kinoteatr:
#     def __init__(self , nomi , janr , davomilylik):
#         self.name = nomi
#         self.janr = janr
#         self.davomiylik = davomilylik

#     def info(self):
#         return f"Kino nomi : {self.name}\nKino janri : {self.janr}\nKino davomiyligi : {self.davomiylik}"
    
# kino = Kino("Biz hammamiz o'likmiz" , "Qorqinchli" , "1 soat ")  
# print(kino.info())  

# 24
# class Oquvchi:
#     def __init__(self , ism , yosh , qiziqqan_fan):
#         self.name = ism
#         self.age = yosh
#         self.qiziqqan_fan = qiziqqan_fan

#     def info(self):
#         return f"O'quvchi ismi : {self.name}\nO'quvchi yoshi : {self.age}\nO'quvchi qiziqqan fani : {self.qiziqqan_fan}"
    
# oquvchi = Oquvchi("Vali" , 16 , "Ingliz tili")     
# print(oquvchi.info())

# 25
# class Universitet:
#     def __init__(self , nomi , fakultetlar_soni ):
#         self.name = nomi
#         self.fakultetlar_soni = fakultetlar_soni

#     def info(self):
#         return f"Universitet nomi : {self.name}\nUniversitet fakultetlar soni : {self.fakultetlar_soni}"
    

# universitet =Universitet("URDU" , 5)
# print(universitet.info())

# 26
# class Avtosalon:
#     def __init__(self , nomi , manzili):
#         self.name = nomi
#         self.manzili = manzili

#     def info(self):
#         return f"Avtosalon nomi : {self.name}\nAvtosalon manzili : {self.manzili}"
    
# avtosalon = Avtosalon("Sammoy" , "Xorazm viloyati")
# print(avtosalon.info())

# 27
# class Kasalxona:
#     def __init__(self , shifokor_ismi , shifokor_yoshi , shifokor_tajriasi):
#         self.name = shifokor_ismi
#         self.age =shifokor_yoshi
#         self.tajriba = shifokor_tajriasi

#     def malumot_ber(self):
#         return f"Shifokor ismi:{self.name}\nShifokor yoshi{self.age}\nShifokor tajribasi:{self.tajriba}"
    
# shifokor = Kasalxona("Qobiljon" , 25 , "Boshlang'ich")
# print(shifokor.malumot_ber())
     
# 28
# class Oyinchi:
#     def __init__(self , ism , level , ball):
#         self.name =ism
#         self.level  = level
#         self.ball =ball

#     def malumot_ber(self):
#         return f"O'yinchi ismi{self.name}\nLevel:{self.level}\nO'yinchi to'plagan ball:{self.ball}"
    
# a = Oyinchi("Sevinchoy" , "3-level" , 300)
# print(a.malumot_ber())

# 29
# class  Oyinchi:
#     def __init__(self , ism , level , ball):
#         self.name =ism
#         self.level  = level
#         self.ball =ball

#     def malumot_ber(self):
#         return f"O'yinchi ismi{self.name}\nLevel:{self.level}\nO'yinchi to'plagan ball:{self.ball}"
    
# a = Oyinchi("Sevinchoy" , "3-level" , 300)
# print(a.malumot_ber()) 

# 30 
# class Restaran:
#     def __init__(self , taom):
#         self.taom = taom

#     def malumot_ber(self):
#         return f"Restorandagi taomlar ro'yxati:{self.taom}"
    
# taom =Restaran("Manti , Chuchvara , Honim , Somsa , Norin")
# print(taom.malumot_ber())

# 31
# class Taom:
#     def __init__(self , nom , narx , kaloriya):
#         self.nomi = nom
#         self.narxi = narx
#         self.kaloriya = kaloriya

#     def malumot_ber(self):
#         return f"Taom nomi:{self.nomi}\nTaom narxi:{self.narxi}\nTaom kaloriyasi:{self.kaloriya}"
    
# taom = Taom("Somsa" , "10 ming so'm" , "Noma'lum")
# print(taom.malumot_ber())

# 32
# class Restoran:
#     def __init__(self , nomi , narxi):
#         self.name = nomi
#         self.narxi = narxi

#     def malumot_ber(self):
#         return f"Restorandagi taomlar menyusi\nTaom nomi:{self.name}\nTaom narxi:{self.narxi}"
    
# taom = Restoran("Somsa" , "10 ming so'm")
# taom2 = Restoran("Manti" , "15 ming so'm")
# print(taom.malumot_ber() , taom2.malumot_ber())

# 33
# class Kompyuter:
#     def __init__(self , dastur_nomi):
#         self.name = dastur_nomi
#         self.royxat = []

#     def add_dastur(self , dastur_nomi):
#         self.royxat.append(dastur_nomi)

#     def del_dastur(self , dastur_nomi):
#         self.royxat.remove(dastur_nomi)
    
#     def show_dastur(self):
#         return f"{self.name} kompyuteriga o'rnatilgan dasturlar ro'yhati {self.royxat}"

# kompyuter = Kompyuter("HP")
# kompyuter.add_dastur(" Word")
# kompyuter.add_dastur(" Excel")
# kompyuter.del_dastur(" Excel")
# print(kompyuter.show_dastur())    

# 34
# class Dastur:
#     def __init__(self , nom , versiya , ishlab_chiquvchi):
#         self.name = nom
#         self.versiyasi = versiya
#         self.ishlab_chiquvchi = ishlab_chiquvchi

#     def malumot_ber(self):
#         return f"Dastur nomi : {self.name}\nDastur versiyasi : {self.versiyasi}\nDastur ishlab chiquvchisi : {self.ishlab_chiquvchi}"
    
# dastur = Dastur("word" , "2026" , "Microsoft")
# print(dastur.malumot_ber())

# 35
# class Bank:
#     def __init__(self , mijoz_ismi):
#         self.name = mijoz_ismi
#         self.royxat = []

#     def add_mijoz(self , mijoz_ismi):
#         self.royxat.append(mijoz_ismi)

#     def del_mijoz(self , mijoz_ismi):
#         self.royxat.remove(mijoz_ismi)
    
#     def show_mijoz(self):
#         return f"{self.name} bankining mijozlari ro'yhati {self.royxat}"
    
# bank = Bank("Agrobank")
# bank.add_mijoz("Ali")
# bank.add_mijoz("Vali")
# bank.del_mijoz("Vali")
# print(bank.show_mijoz())

# 36
# class Mijoz:
#     def __init__(self , ism , balans):
#         self.name = ism
#         self.balans = balans

#     def malumot_ber(self):
#         return f"Mijoz ismi : {self.name}\nMijoz balansi : {self.balans}"


# mijoz = Mijoz("Ali" , 200000)
# print(mijoz.malumot_ber())

# 37
# class Sinf:
#     def __init__(self , fanlar):
#         self.fanlar = fanlar
#         self.royxat = []

#     def add_fan(self , fan_nomi):
#         self.royxat.append(fan_nomi)

#     def del_fan(self , fan_nomi):
#         self.royxat.remove(fan_nomi)

#     def show_fan(self):
#         return f"Sinfdagi fanlar ro'yhati {self.royxat}"
    
# sinf = Sinf("8-sinf")
# sinf.add_fan("Matematika")
# sinf.add_fan("Ingliz tili")
# sinf.del_fan("Matematika")
# print(sinf.show_fan())

# 38
# class Fan:
#     def __init__(self , nomi , oqituvchi):
#         self.name = nomi
#         self.oqituvchi = oqituvchi

#     def malumot_ber(self):
#         return f"Fan nomi : {self.name}\nFan oqituvchisi : {self.oqituvchi}"
    
# fan = Fan("Ingliz tili" , "Sevinchoy")
# print(fan.malumot_ber())

# 39
# class Universitet:
#     def __init__(self , talabalar , oqituvchilar):
#         self.talabalar = talabalar
#         self.oqituvchilar = oqituvchilar

#     def add_talaba(self , talaba_ismi):
#         self.talabalar.append(talaba_ismi)

#     def del_talaba(self , talaba_ismi):
#         self.talabalar.remove(talaba_ismi)

#     def add_oqituvchi(self , oqituvchi_ismi):
#         self.oqituvchilar.append(oqituvchi_ismi)

#     def del_oqituvchi(self , oqituvchi_ismi):
#         self.oqituvchilar.remove(oqituvchi_ismi)

#     def show_universitet(self):
#         return f"Universitetdagi talabalar ro'yhati {self.talabalar}\nUniversitetdagi oqituvchilar ro'yhati {self.oqituvchilar}"
    
# universitet = Universitet("URDU" , "Sevinchoy")
# universitet.add_talaba("Ali")
# universitet.add_talaba("Rayhona")
# universitet.add_talaba("Vali")
# universitet.del_talaba("Ali")
# universitet.add_oqituvchi("Dilnura")
# universitet.add_oqituvchi("Sevinchoy")
# universitet.del_oqituvchi("Sevinchoy")
# print(universitet.show_universitet())

# 40
# class Market:
#     def __init__(self , nomi):          
#         self.name = nomi
#         self.mijozlar = []
#         self.mahsulotlar = []

#     def add_mijoz(self , mijoz_ismi):
#         self.mijozlar.append(mijoz_ismi)

#     def del_mijoz(self , mijoz_ismi):
#         self.mijozlar.remove(mijoz_ismi)

#     def add_mahsulot(self , mahsulot_nomi):
#         self.mahsulotlar.append(mahsulot_nomi)
    
#     def del_mahsulot(self , mahsulot_nomi):
#         self.mahsulotlar.remove(mahsulot_nomi)

#     def show_market(self):
#         return f"{self.name} marketidagi mijozlar ro'yhati {self.mijozlar}\n{self.name} marketidagi mahsulotlar ro'yhati {self.mahsulotlar}"
    
# market = Market("Magnit")
# market.add_mijoz("Ali")
# market.add_mijoz("Vali")
# market.del_mijoz("Vali")
# market.add_mahsulot("Sut")
# market.add_mahsulot("Non")
# market.del_mahsulot("Sut")
# print(market.show_market())

# 41
# class Teatr:
#     def __init__(self , teatr_nomi):
#         self.name = teatr_nomi
#         self.royxat = []

#     def add_spektakl(self , spektakl_nomi):
#         self.royxat.append(spektakl_nomi)

#     def del_spektakl(self , spektakl_nomi):
#         self.royxat.remove(spektakl_nomi)

#     def show_spektakl(self):
#         return f"{self.name} teatridagi spektakllar ro'yhati {self.royxat}"
    
# teatr = Teatr("Teatr")
# teatr.add_spektakl("Kelinlar qo'zg'oloni") 
# teatr.add_spektakl("O'tgan kunlar")
# teatr.del_spektakl("O'tgan kunlar")
# print(teatr.show_spektakl())

# 42
# class Spektakl:
#     def __init__(self , nom , muallif , vaqt):
#         self.name = nom
#         self.muallif = muallif
#         self.time = vaqt

#     def malumot_ber(self):
#         return f"Spektakl nomi:{self.name}\nMuallif:{self.muallif}\nSpektakl davomiyligi:{self.time}\n"
    
# spektakl = Spektakl("Kelinlar qo'zg'aloni" , "O'tkir Hoshimov" , "2 soat")
# print(spektakl.malumot_ber())

# 43
# class Qishloq:
#     def __init__(self , uy_manzili , uy_nomeri):
#         self.manzil = uy_manzili
#         self.nomer = uy_nomeri

#     def malumot_ber(self):
#         return f"Uy manzili:{self.manzil}\nUy nomeri:{self.nomer}\n"
    
# uy = Qishloq("Obod mahallasi" , 2)
# print(uy.malumot_ber())



# import psycopg2
# ulanish = psycopg2.connect(
#     host="localhost",
#     database="vorislar",
#     user = "postgres",
#     password = "vorislar2026"
# )

# ulanish.autocommit = True
# ulash = ulanish.cursor()

# ulash.execute("CREATE DATABASE vorislar")
# print("Database yaratildi")

# ulash.execute(
#     """
#     CREATE TABLE foydalanuvchilar(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         age INTEGER,
#         email VARCHAR(100)
#     )
#     """
# )
# print("Jadval yaratildi")

# ulash.execute(
#     "INSERT INTO foydalanuvchilar(name,age,email) VALUES ('Rayhona',15,'rahmanovarayhon@gmail.com')"
# )
# print("malumot qo'shildi")

# ulash.execute(
#     "SELECT * FROM foydalanuvchilar"
# )
# ustunlar = ulash.fetchall()
# for ustun in ustunlar:
#     print(ustun)

# ulash.execute(
#     "UPDATE foydalanuvchilar SET name = 'Rayxona' where id='1' "
# )
# print("malumot muvaffaqiyatli yangilandi")

# ulash.execute(
#     "DELETE FROM foydalanuvchilar where id='1' "
# )
# print("malumot muvaffaqiyatli o'chirildi")





# from db import db_connect

# ulash = db_connect()
# ishlatish = ulash.cursor()
# ulash.autocommit = True
# ishlatish.execute(
#     "SELECT * FROM foydalanuvchilar"
# )
# ustunlar = ishlatish.fetchall()
# for ustun in ustunlar:
#     print(ustun)

# ishlatish.execute(
#     "INSERT INTO foydalanuvchilar(name , age , email) VALUES('Rayhona' , 15 , 'rayxona@gmail.com')"
# )




# import psycopg2
# ulanish = psycopg2.connect(
#     host="localhost",
#     database="rayhona",
#     user = "postgres",
#     password = "vorislar2026"
# )

# ulanish.autocommit = True
# ulash = ulanish.cursor()

# ulash.execute(
#     "CREATE DATABASE rayhona"
# )
# ulash.execute(
#     """
#     CREATE TABLE qarindoshlar(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         age INTEGER,
#         email VARCHAR(100)
#     )
#     """
# )
# print("Jadval yaratildi")


# ulash.execute(
#     "SELECT * FROM qarindoshlar"
# )
# ustunlar = ulash.fetchall()
# for ustun in ustunlar:
#     print(ustun)

# print("Jadval muvaffaqiyatli yaratiladi")




# import psycopg2
# ulanish = psycopg2.connect(
#     host="localhost",
#     database="school",
#     user = "postgres",
#     password = "vorislar2026"
# )


# ulanish.autocommit = True
# ulash = ulanish.cursor()


# ulash.execute(
#     "CREATE DATABASE school"
# )

# ulash.execute(
#     """
#     CREATE TABLE talabalar(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         familiya VARCHAR(100),
#         age INTEGER,
#         kurs VARCHAR(100),
#         fan VARCHAR(100),
#         guruh raqami INTEGER,
#         ball INTEGER
#     )
#     """
# )
# print("Jadval yaratildi")

# ulash.execute(
#     "INSERT INTO talabalar(name , familiya , age , kurs , fan , guruh raqami , ball) VALUES ('Rayhona' , 'Rahmanova' , 15 , 'IT' , 'matematika' , 100)"
# )
# print("malumot qo'shildi")









# from db import db_connect
# conn = db_connect()
# cur = conn.cursor()
# conn.autocommit = True

# cur.execute(
#     """CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )"""
# )
# print("Jadval yaratildi")


# cur.execute(
#     """CREATE TABLE subjects(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
#     )"""
# )
# print("Jadval yaratildi")



# cur.execute(
#     """CREATE TABLE enrollments(
#     students_id INTEGER,
#     subject_id INTEGER
#     )"""
# )
# print("Jadval yaratildi")



# cur.execute(
#     "INSERT INTO students(name) VALUES('Sevinchoy')"
# )
# print("Malumot qo'shildi")

# cur.execute(
#     "INSERT INTO subjects(title) VALUES ('Ingliz tili')"
# )
# print("malumot qoshildi")


# cur.execute(
#     'SELECT * FROM students'
# )
# rows = cur.fetchall()   
# for row in rows:
    # print(row)


# cur.execute(
#     "INSERT INTO enrollments(students_id , subject_id) VALUES(2 , 2)"
# )
# print("Malumot qo'shildi")  

# cur.execute(
#     "SELECT students.name , subjects.title FROM enrollments JOIN students ON students.id = enrollments.students_id JOIN subjects ON subjects.id = enrollments.subject_id"
# )

# rows = cur.fetchall()

# for row in rows:
#     print(row)

# print("malumot qoshildi")






# from db import db_connect
# conn = db_connect()
# cur = conn.cursor()
# conn.autocommit = True


# cur.execute(
#     """CREATE TABLE readers(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )"""
# )
# print("Jadval yaratildi")


# cur.execute(
#     """CREATE TABLE books(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
#     )"""
# )
# print("Jadval yaratildi")


# cur.execute(
#     """CREATE TABLE rentors(
#     readers_id INTEGER,
#     books_id INTEGER
#     )"""
# )
# print("Jadval yaratildi")


# cur.execute(
#     "INSERT INTO readers(name) VALUES('Fotima')"
# )   
# print("Malumot qo'shildi")


# cur.execute(
#     "INSERT INTO books(title) VALUES('Chinor')"
# )
# print("Malumot qo'shildi")


# cur.execute(
#     'SELECT * FROM readers'
# )
# rows = cur.fetchall()   
# for row in rows:
#     print(row)
# print("Ma'lumot qoshildi")


# cur.execute(
#     "INSERT INTO rentors(readers_id ,  books_id) VALUES(3 , 3)"
# )
# print("Ma'lumot qo'shildi")


# cur.execute(
#     "SELECT readers.name , books.title FROM rentors JOIN readers ON readers.id = rentors.readers_id JOIN books ON books.id = rentors.books_id"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# print("Ma'lumot qoshildi")







# from db import db_connect
# conn = db_connect()

# cur = conn.cursor()
# conn.autocommit = True


# cur.execute(
#     "CREATE DATABASE library"
# )
# print("Database yaratildi")

# cur.execute(
#     """CREATE TABLE authors(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )"""
# )
# print("Jadval yaratildi")

# cur.execute(
#     """CREATE TABLE books(
#     id SERIAL PRIMARY KEY,
#     book_name VARCHAR(100)
#     )"""
# )
# print("Jadval yaratildi")

# cur.execute(
#     "INSERT INTO books(book_name) VALUES ('Sariq devni minib')"
# )
# print("Ma'lumot qo'shildi")

# cur.execute(
#     "SELECT authors.name , books.book_name FROM authors LEFT JOIN books ON authors.id = books.id "
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)





from db import db_connect
conn = db_connect()

cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     """CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )"""
# )

# cur.execute(
#     """CREATE TABLE course(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
#     )"""
# )
# print("Jadval yratildi")

# cur.execute(
#     """CREATE TABLE enrollments(
#     students_id INTEGER,
#     course_id INTEGER
#     )"""
# )
# print("Jadval yaratildi")

# cur.execute(
#     "INSERT INTO students(name) VALUES('Fotima')"
# )
# print("Ma'lumot qo'shildi")

# cur.execute(
#     "INSERT INTO course(title) VALUES ('Turk tili')"
# )
# print("Ma'lumot qo'shildi")

# cur.execute(
#     "INSERT INTO enrollments(students_id , course_id) VALUES (3,2)"
# )
# print("Ma'lumot qo'shildi")

# cur.execute(
#     "SELECT students.name , course.title FROM enrollments JOIN students ON students.id = enrollments.students_id JOIN course ON course.id = enrollments.course_id"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# print("Ma'lumot qo'shildi")    