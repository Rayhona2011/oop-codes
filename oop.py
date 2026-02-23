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

