import csv
from datetime import datetime
import time
import pandas as pd
import os
import pymysql.cursors
import random

#Mysql bağlantı kodlarımız 
db = pymysql.connect(host='localhost',
                        user='******',
                        password='*********', # Bilgisayarında Mysql olanlar için user ve password alanları kendi mysqllerine göre yazılmalıdır.
                        db='projeglobalaıhub',
                        cursorclass=pymysql.cursors.DictCursor)
connection = db.cursor()

# Her yerde erişmek istediğimiz değişkenleri tanımladık.
global sosPrice,total_price,count,i,sosListe,pizza_name,userid_list,sizes
global kckBoy,kckBoy_Price,ortBoy,ortBoy_Price,bykBoy,bykBoy_Price
global ayran,ayran_price,cola,cola_price,gazoz,gazoz_price,fanta,fanta_price,icetea1,icetea1_price,icetea2,icetea2_price,soguk_icecekler

soguk_icecekler = []
sizes = []
userid_list = []
sosPrice = 0
sosListe = []
count = 0
i = 0

# Üst Pizza sınıfımızı tanımladık.
class Pizza():

  def __init__(self, description, cost):
    self.__description = description,
    self.__cost = cost

  #Encapsulation ile cost ve description tanımladık
  def get_description(self):
    return self.__description

  def set_description(self,description_):
    self.__description = description_    

  def get_cost(self):
    return self.__cost
  
  def set_cost(self,cost_):
    self.__cost = cost_

# Alt sınıflarımız Pizza üst sınıfından kalıtım almasını sağladık.
class Classic(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)

class Margherita(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)

class TurkPizza(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)

class Dominos(Pizza):
  def __init__(self,description, cost):
    super().__init__(description, cost)  


# Nesnelerimizi oluşturarak pizzalar için sabit değerlerini tanımladık. 
pizCls = Classic("Klasik Pizza",100)
# Fiyatın cost methoduna açıklamanın ise description methoduna atanmasının doğruluğunu kontrol etmek için yazdırdık.
# print("Pizza İsmi:{acıklama} \nPizza Fiyatı:{fiyat} ".format(acıklama = pizCls.get_description(),fiyat = pizCls.get_cost()))

pizMar = Margherita("Margeritha Pizza", 135)
# print("Pizza İsmi:{acıklama} \nPizza Fiyatı:{fiyat} ".format(acıklama = pizMar.get_description(),fiyat = pizMar.get_cost()))

pizTurk = TurkPizza("Türk Pizza", 120)
# print("Pizza İsmi:{acıklama} \nPizza Fiyatı:{fiyat} ".format(acıklama = pizTurk.get_description(),fiyat = pizTurk.get_cost()))

pizDo = Dominos("Dominos Pizza", 150)
# print("Pizza İsmi:{acıklama} \nPizza Fiyatı:{fiyat} ".format(acıklama = pizDo.get_description(),fiyat = pizDo.get_cost()))

print("\n")

 #Soslar için süper sınıf olan decorator'ın Pizza üst sınıfından kalıtım almasını saülıyoruz
class Decorator(Pizza):
  # Cost ve description  özelliklerimizi tanımlıyoruz
  def __init__(self, description, cost):
    self._description = description,
    self._cost = cost

  #Encapsulation ile cost ve description tanımlanması
  def get_description(self):
    return self._description

  def set_description(self,description_):
    self._description = description_    

  def get_cost(self):
    return self._cost
  
  def set_cost(self,cost_):
    self._cost = cost_
  

# Zeytin, Mantar, Keçi Peyniri, Et, Soğan ve Mısır atl sınıflarımızın decorator sınıfından kalıtım almasını sağladık. 
class Zeytin(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost) 

class Mantar(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)   

class KeciPeyniri(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)   

class Et(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)   

class Sogan(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)   

class Misir(Decorator):
  def __init__(self,description, cost):
    super().__init__(description, cost)

# Sos nesnelerini tanımladık.
sosZeytin = Zeytin("Siyah Zeytin",5)
# Fiyatın cost methoduna açıklamanın ise description methoduna atanmasının doğruluğunu kontrol etmek için yazdırdık.
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosZeytin.get_description(),fiyat = sosZeytin.get_cost()))
sosMantar = Mantar("Kültür Mantarı",12)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosmantar.get_description(),fiyat = sosmantar.get_cost()))

sosKeciPeyniri = KeciPeyniri("Keçi Peyniri 50gr",25)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosKeciPeyniri.get_description(),fiyat = sosKeciPeyniri.get_cost()))

sosEt = Et("Dana Eti 100gr",32)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosEt.get_description(),fiyat = sosEt.get_cost()))

sosSogan = Sogan("Soğan",7)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosSogan.get_description(),fiyat = sosSogan.get_cost()))

sosMisir= Misir("Süt Mısır 35gr",9)
# print("Sos İsmi:{acıklama} \nSos Fiyatı:{fiyat} ".format(acıklama = sosMisir.get_description(),fiyat = sosMisir.get_cost()))

# Ödeme işlemi her pizza ayrı description'a sahip olduğundan bu şekilde tanımladık. Koşullarımız description'dan gelen isim'e göre yönlendirilmektedir.

def SuccesMessage():
  print('Sosunuz başarıyla siparişinize eklendi.')

  # Her pizzanın uygulamadaki seçimlerine göre şekillenen ödeme ekranları bulunmakta burdan itibaren Klasik pizza ile başlamaktadır.
def payment_Process():
  os.system('cls')
  if pizza_name == "Klasik Pizza":
    name = pizza_name
    liste = convertList(sosListe)
    size_name = sizes[0]
    icecek_ismi = convertList(soguk_icecekler)
    if icecek_ismi in soguk_icecekler:
      icecek_ismi = convertList(soguk_icecekler)
      print('Total prices for Pizza: {pizza} + Sauces: {sos} + Sizes: {size} + İcecek:{icecek} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price,size =size_name,icecek= icecek_ismi))
      credit_card_username = input('Name on credit card: ')
      userid = input("Enter identification number: ")
      userid_list.append(userid)
      userid = str(userid)
      order_description = name +' '+ liste +' '+ size_name +' '+ icecek_ismi
      order_time = datetime.now()
      credit_card_number = input('Enter credit card number: ')
      credit_card_last_time = input('Enter credit card last time (Exp:02/24): ')
      cvv = input("Enter CVV: ")
      credit_card_password = input("Enter credit card password: ")
      connection.execute('INSERT INTO ordersystem VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv, credit_card_password))
      db.commit()
      print("Ödeme işlemi başarılı.\nSipariş başarıyla alındı.\nBizi tercih ettiğiniz için teşekkürler\nYine bekleriz....")
      exit()
    else:
      print('Total prices for Pizza: {pizza} + Sauces: {sos} + Sizes: {size}= {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price,size =size_name))
      credit_card_username = input('Name on credit card: ')
      userid = input("Enter identification number: ")
      userid_list.append(userid)
      userid = str(userid)
      order_description = name +' '+ liste +' '+ size_name
      order_time = datetime.now()
      credit_card_number = input('Enter credit card number: ')
      credit_card_last_time = input('Enter credit card last time (Exp:02/24): ')
      cvv = input("Enter CVV: ")
      credit_card_password = input("Enter credit card password: ")
      connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv, credit_card_password))
      db.commit()
      print("Ödeme işlemi başarılı.\nSipariş başarıyla alındı.\nBizi tercih ettiğiniz için teşekkürler\nYine bekleriz....")
      exit()

  if pizza_name == "Margeritha Pizza":
    name = pizza_name
    size_name = sizes[0]
    liste = convertList(sosListe)
    icecek_ismi = convertList(soguk_icecekler)
    if icecek_ismi in soguk_icecekler: 
      icecek_ismi = convertList(soguk_icecekler)
      print('Total prices for Pizza: {pizza} + Sauces: {sos} + Sizes: {size} + İcecek:{icecek} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price,size =size_name,icecek= icecek_ismi))
      credit_card_username = input('Name on credit card: ')
      userid = input("Enter identification number: ")
      userid = str(userid)
      order_description = name +' '+ liste +' '+ size_name +' '+ icecek_ismi
      order_time = datetime.now()
      credit_card_number = input('Enter credit card number: ')
      credit_card_last_time = input('Enter credit card last time: ')
      cvv = input("Enter CVV: ")
      credit_card_password = input("Enter credit card password: ")
      connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv,   credit_card_password))
      db.commit()
      print("Ödeme işlemi başarılı.\nSipariş başarıyla alındı.\nBizi tercih ettiğiniz için teşekkürler\nYine bekleriz....")
      exit()
    else:
      name = pizza_name
      size_name = sizes[0]
      liste = convertList(sosListe)
      print('Total prices for Pizza: {pizza} + Sauces: {sos} + Sizes: {size} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price,size =size_name))
      credit_card_username = input('Name on credit card: ')
      userid = input("Enter identification number: ")
      userid = str(userid)
      order_description = name +' '+ liste +' '+ size_name
      order_time = datetime.now()
      credit_card_number = input('Enter credit card number: ')
      credit_card_last_time = input('Enter credit card last time: ')
      cvv = input("Enter CVV: ")
      credit_card_password = input("Enter credit card password: ")
      connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv,   credit_card_password))
      db.commit()
      print("Ödeme işlemi başarılı.\nSipariş başarıyla alındı.\nBizi tercih ettiğiniz için teşekkürler\nYine bekleriz....")
      exit()

  if pizza_name == "Türk Pizza":
    name = pizza_name
    size_name = sizes[0]
    liste = convertList(sosListe)
    icecek_ismi = convertList(soguk_icecekler)
    if icecek_ismi in soguk_icecekler:
      icecek_ismi = convertList(soguk_icecekler)
      print('Total prices for Pizza: {pizza} + Sauces: {sos} + Sizes: {size} + İcecek:{icecek} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price,size =size_name,icecek= icecek_ismi))
      credit_card_username = input('Name on credit card: ')
      userid = input("Enter identification number: ")
      userid = str(userid)
      order_description = name +' '+ liste +' '+ size_name +' '+ icecek_ismi
      order_time = datetime.now()
      credit_card_number = input('Enter credit card number: ')
      credit_card_last_time = input('Enter credit card last time: ')
      cvv = input("Enter CVV: ")
      credit_card_password = input("Enter credit card password: ")
      connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv,   credit_card_password))
      db.commit()
      print("Ödeme işlemi başarılı.\nSipariş başarıyla alındı.\nBizi tercih ettiğiniz için teşekkürler\nYine bekleriz....")
      exit()
    else:
      name = pizza_name
      size_name = sizes[0]
      liste = convertList(sosListe)
      print('Total prices for Pizza: {pizza} + Sauces: {sos} + Sizes: {size} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price,size =size_name))
      credit_card_username = input('Name on credit card: ')
      userid = input("Enter identification number: ")
      userid = str(userid)
      order_description = name +' '+ liste +' '+ size_name
      order_time = datetime.now()
      credit_card_number = input('Enter credit card number: ')
      credit_card_last_time = input('Enter credit card last time: ')
      cvv = input("Enter CVV: ")
      credit_card_password = input("Enter credit card password: ")
      connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv,   credit_card_password))
      db.commit()
      print("Ödeme işlemi başarılı.\nSipariş başarıyla alındı.\nBizi tercih ettiğiniz için teşekkürler\nYine bekleriz....")
      exit()


  if pizza_name == "Dominos Pizza":
    name = pizza_name
    size_name = sizes[0]
    liste = convertList(sosListe)
    icecek_ismi = convertList(soguk_icecekler)
    if icecek_ismi in soguk_icecekler:
      icecek_ismi = convertList(soguk_icecekler)
      print('Total prices for Pizza: {pizza} + Sauces: {sos} + Sizes: {size} + İcecek:{icecek} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price,size =size_name,icecek= icecek_ismi))
      credit_card_username = input('Name on credit card: ')
      userid = input("Enter identification number: ")
      userid = str(userid)
      order_description = name +' '+ liste +' '+ size_name +' '+ icecek_ismi
      order_time = datetime.now()
      credit_card_number = input('Enter credit card number: ')
      credit_card_last_time = input('Enter credit card last time: ')
      cvv = input("Enter CVV: ")
      credit_card_password = input("Enter credit card password: ")
      connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv,credit_card_password))
      db.commit()
      print("Ödeme işlemi başarılı.\nSipariş başarıyla alındı.\nBizi tercih ettiğiniz için teşekkürler\nYine bekleriz....")
      exit()
    else:
      name = pizza_name
      size_name = sizes[0]
      liste = convertList(sosListe)
      print('Total prices for Pizza: {pizza} + Sauces: {sos} + Sizes: {size} = {totalPrice}'.format(pizza = name,sos = liste, totalPrice = total_price,size =size_name))
      credit_card_username = input('Name on credit card: ')
      userid = input("Enter identification number: ")
      userid = str(userid)
      order_description = name +' '+ liste +' '+ size_name
      order_time = datetime.now()
      credit_card_number = input('Enter credit card number: ')
      credit_card_last_time = input('Enter credit card last time: ')
      cvv = input("Enter CVV: ")
      credit_card_password = input("Enter credit card password: ")
      connection.execute('INSERT INTO ordersystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(None,credit_card_username,userid,order_description,order_time,credit_card_number,credit_card_last_time,cvv,   credit_card_password))
      db.commit()
      print("Ödeme işlemi başarılı.\nSipariş başarıyla alındı.\nBizi tercih ettiğiniz için teşekkürler\nYine bekleriz....")
      exit()


def convertTuple(tup):
  pizza_name = ''.join(tup)
  return pizza_name

def convertList(lis):
  sosListe = ' '.join(lis)
  return sosListe

# Main fonksiyonumuz
if __name__ == "__main__":
  df = pd.read_csv("Menu.txt") 
  print(df.head(4))
  selection = input("Pizza Seçiminiz: ")

# Pizzalar için dictionary tanımladık.
  casesPizza={
    1:pizCls,
    2:pizMar,
    3:pizTurk,
    4:pizDo
  }

  # Soslar için dictionary tanımladık.
  casesSos ={
        1:sosZeytin,
        2:sosMantar,
        3:sosKeciPeyniri,
        4:sosEt,
        5:sosSogan,
        6:sosMisir
      }

  kckBoy = "Küçük Boy"
  kckBoy_Price = 10
  ortBoy = "Orta Boy"
  ortBoy_Price = 20
  bykBoy = "Büyük Boy"
  bykBoy_Price = 30

  ayran = "Ayran"
  ayran_price = 5
  cola = "Coca-Cola"
  cola_price = 12
  gazoz = "Gazoz"
  gazoz_price = 12
  fanta = "Fanta"
  fanta_price = 12
  icetea1 = "Ice-Tea (Şeftali)"
  icetea1_price = 15
  icetea2 = "Ice-Tea (Limon)"
  icetea2_price = 15

# Pizza seçimlerinin sağlandığı koşul bloğumuz
if selection == "1":
  os.system('cls')
  classic_pizza_price = pizCls.get_cost()
  print(convertTuple(pizCls.get_description()) , ' seçtiniz')
  time.sleep(3)

  df3 = pd.read_csv("PİzzaBoyutları.txt")
  print(df3.head(5))
  select_size = input("Pizza boyutunuzu seçiniz: ")

  if select_size == "1":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = kckBoy))
    sizes.append(kckBoy)

  if select_size == "2":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = ortBoy))
    sizes.append(ortBoy)

  if select_size == "3":
    os.system('cls')    
    print('Boyutunuz: {boy}'.format(boy = ortBoy))
    sizes.append(bykBoy)

  do_you_want_sos = input("Sos ister misiniz(e/h): ") 
  if do_you_want_sos == "e":

    os.system('cls')
    print("Bilgilendirme: Sos seçimi için 3 hakkınız var\n")

    count = 3
    while count > i:
      df2 = pd.read_csv("Menu2.txt") #Sosların bulunduğu dosyayı okuyoruz.
      print(df2.head(6))

      sos = str(input("Hangi sosu istersiniz: "))

      if sos == "1":
        sos_name = convertTuple(sosZeytin.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = convertTuple(sosZeytin.get_description()),fiyat = sosZeytin.get_cost()))
          print("-------------------------------")

          sosZeytin_price = sosZeytin.get_cost()
          sosPrice = sosPrice + sosZeytin_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "2":
        sos_name = convertTuple(sosMantar.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMantar.get_cost()))
          print("-------------------------------")

          sosMantar_price = sosMantar.get_cost()
          sosPrice = sosPrice + sosMantar_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "3":
        sos_name = convertTuple(sosKeciPeyniri.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')

        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosKeciPeyniri.get_cost()))
          print("-------------------------------")

          sosKeciPeyniri_price = sosKeciPeyniri.get_cost()
          sosPrice = sosPrice + sosKeciPeyniri_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "4":
        sos_name = convertTuple(sosEt.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosEt.get_cost()))
          print("-------------------------------")

          sosEt_price = sosEt.get_cost()
          sosPrice = sosPrice + sosEt_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "5":
        sos_name = convertTuple(sosSogan.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosSogan.get_cost()))
          print("-------------------------------")

          sosSogan_price = sosSogan.get_cost()
          sosPrice = sosPrice + sosSogan_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "6":
        sos_name = convertTuple(sosMisir.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMisir.get_cost()))
          print("-------------------------------")

          sosMisir_price = sosMisir.get_cost()
          sosPrice = sosPrice + sosMisir_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')
  else:
    if kckBoy in sizes:
      size_name = sizes[0]
      add_Price = kckBoy_Price 
      total_price = classic_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizCls.get_description())

    if ortBoy in sizes:
      size_name = sizes[0]
      add_Price = ortBoy_Price
      total_price = classic_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizCls.get_description())
    
    if bykBoy in sizes:
      size_name = sizes[0]
      add_Price = bykBoy_Price
      total_price = classic_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizCls.get_description())

  icecek_ister_mi = input("İçecek ister misiniz(e/h): ")
  if icecek_ister_mi == "e":
    df4 = pd.read_csv("İcecekler.txt")
    print(df4.head(7))
    icecek_secim = input("\nİçceceğinizi seçiniz: \n")

    if icecek_secim == "1":
      icecek_ismi = ayran
      ayran_price = ayran_price
      soguk_icecekler.append(ayran)
      total_price = classic_pizza_price + sosPrice + ayran_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizCls.get_description())
      payment_Process()

    if icecek_secim == "2":
      icecek_ismi = cola
      print(type(icecek_ismi))
      soguk_icecekler.append(cola)
      total_price = classic_pizza_price + sosPrice + cola_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizCls.get_description())
      payment_Process()

    if icecek_secim == "3":
      icecek_ismi = gazoz
      soguk_icecekler.append(gazoz)
      total_price = classic_pizza_price + sosPrice + gazoz_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizCls.get_description())
      payment_Process()

    if icecek_secim == "4":
      icecek_ismi = fanta
      soguk_icecekler.append(fanta)
      total_price = classic_pizza_price + sosPrice + fanta_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizCls.get_description())
      payment_Process()

    if icecek_secim == "5":
      icecek_ismi = icetea1
      soguk_icecekler.append(icetea1)
      total_price = classic_pizza_price + sosPrice + icetea1_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizCls.get_description())
      payment_Process()

    if icecek_secim == "6":
      icecek_ismi = icetea2
      soguk_icecekler.append(icetea2)
      total_price = classic_pizza_price + sosPrice + icetea2_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizCls.get_description())
      payment_Process()

  else:
    if sizes[0] == kckBoy:
      boyut = kckBoy_Price
    if sizes[0] == ortBoy:
      boyut = ortBoy_Price
    if sizes[0] == bykBoy:
      boyut = bykBoy_Price
      
    total_price = classic_pizza_price + sosPrice+ boyut
    print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
    time.sleep(3)
    pizza_name = convertTuple(pizCls.get_description())
    payment_Process()
   
  
if selection == "2":
  os.system('cls')
  mar_pizza_price = pizMar.get_cost()
  print(convertTuple(pizMar.get_description()) , ' seçtiniz ')
  time.sleep(3)

  df = pd.read_csv("PİzzaBoyutları.txt")
  print(df.head())

  select_size = input("Pizza boyutunuzu seçiniz: ")

  if select_size == "1":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = kckBoy))
    sizes.append(kckBoy)

  if select_size == "2":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = ortBoy))
    sizes.append(ortBoy)

  if select_size == "3":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = ortBoy))
    sizes.append(bykBoy)

  do_you_want_sos = input("Sos ister misiniz(e/h): ") 
  if do_you_want_sos == "e":

    os.system('cls')
    print("Bilgilendirme: Sos seçimi için 3 hakkınız var\n")

    count = 3
    while count > i:
      df2 = pd.read_csv("Menu2.txt") #Sosların bulunduğu dosyayı okuyoruz.
      print(df2.head(6))

      sos = str(input("Hangi sosu istersiniz: "))

      if sos == "1":
        sos_name = convertTuple(sosZeytin.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = convertTuple(sosZeytin.get_description()),fiyat = sosZeytin.get_cost()))
          print("-------------------------------")

          sosZeytin_price = sosZeytin.get_cost()
          sosPrice = sosPrice + sosZeytin_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "2":
        sos_name = convertTuple(sosMantar.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMantar.get_cost()))
          print("-------------------------------")

          sosMantar_price = sosMantar.get_cost()
          sosPrice = sosPrice + sosMantar_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "3":
        sos_name = convertTuple(sosKeciPeyniri.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')

        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosKeciPeyniri.get_cost()))
          print("-------------------------------")

          sosKeciPeyniri_price = sosKeciPeyniri.get_cost()
          sosPrice = sosPrice + sosKeciPeyniri_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "4":
        sos_name = convertTuple(sosEt.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosEt.get_cost()))
          print("-------------------------------")

          sosEt_price = sosEt.get_cost()
          sosPrice = sosPrice + sosEt_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "5":
        sos_name = convertTuple(sosSogan.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosSogan.get_cost()))
          print("-------------------------------")

          sosSogan_price = sosSogan.get_cost()
          sosPrice = sosPrice + sosSogan_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "6":
        sos_name = convertTuple(sosMisir.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMisir.get_cost()))
          print("-------------------------------")

          sosMisir_price = sosMisir.get_cost()
          sosPrice = sosPrice + sosMisir_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

  else:
    if kckBoy in sizes:
      size_name = sizes[0]
      add_Price = kckBoy_Price 
      total_price = mar_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizMar.get_description())

    if ortBoy in sizes:
      size_name = sizes[0]
      add_Price = ortBoy_Price
      total_price = mar_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizMar.get_description())
    
    if bykBoy in sizes:
      size_name = sizes[0]
      add_Price = bykBoy_Price
      total_price = mar_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizMar.get_description())

  icecek_ister_mi = input("İçecek ister misiniz(e/h): ")
  if icecek_ister_mi == "e":
    df4 = pd.read_csv("İcecekler.txt")
    print(df4.head(7))
    icecek_secim = input("\nİçceceğinizi seçiniz: \n")

    if icecek_secim == "1":
      icecek_ismi = ayran
      ayran_price = ayran_price
      soguk_icecekler.append(ayran)
      total_price = mar_pizza_price + sosPrice + ayran_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizMar.get_description())
      payment_Process()

    if icecek_secim == "2":
      icecek_ismi = cola
      print(type(icecek_ismi))
      soguk_icecekler.append(cola)
      total_price = mar_pizza_price + sosPrice + cola_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizMar.get_description())
      payment_Process()

    if icecek_secim == "3":
      icecek_ismi = gazoz
      soguk_icecekler.append(gazoz)
      total_price = mar_pizza_price + sosPrice + gazoz_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizMar.get_description())
      payment_Process()

    if icecek_secim == "4":
      icecek_ismi = fanta
      soguk_icecekler.append(fanta)
      total_price = mar_pizza_price + sosPrice + fanta_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizMar.get_description())
      payment_Process()

    if icecek_secim == "5":
      icecek_ismi = icetea1
      soguk_icecekler.append(icetea1)
      total_price = mar_pizza_price + sosPrice + icetea1_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizMar.get_description())
      payment_Process()

    if icecek_secim == "6":
      icecek_ismi = icetea2
      soguk_icecekler.append(icetea2)
      total_price = mar_pizza_price + sosPrice + icetea2_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizMar.get_description())
      payment_Process()

  else:
    if sizes[0] == kckBoy:
      boyut = kckBoy_Price
    if sizes[0] == ortBoy:
      boyut = ortBoy_Price
    if sizes[0] == bykBoy:
      boyut = bykBoy_Price

    total_price = mar_pizza_price + sosPrice+ boyut
    print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
    time.sleep(3)
    pizza_name = convertTuple(pizMar.get_description())
    payment_Process()

  
#-------------------------------------------------------------------------------------------------
if selection == "3":
  os.system('cls')
  tr_pizza_price = pizTurk.get_cost()
  print(convertTuple(pizTurk.get_description()) , ' seçtiniz ')
  time.sleep(3)

  df = pd.read_csv("PİzzaBoyutları.txt")
  print(df.head())

  select_size = input("Pizza boyutunuzu seçiniz: ")

  if select_size == "1":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = kckBoy))
    sizes.append(kckBoy)

  if select_size == "2":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = ortBoy))
    sizes.append(ortBoy)

  if select_size == "3":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = ortBoy))
    sizes.append(bykBoy)
  do_you_want_sos = input("Sos ister misiniz(e/h): ") 
  if do_you_want_sos == "e":

    os.system('cls')
    print("Bilgilendirme: Sos seçimi için 3 hakkınız var\n")

    count = 3
    while count > i:
      df2 = pd.read_csv("Menu2.txt") #Sosların bulunduğu dosyayı okuyoruz.
      print(df2.head(6))

      sos = str(input("Hangi sosu istersiniz: "))

      if sos == "1":
        sos_name = convertTuple(sosZeytin.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = convertTuple(sosZeytin.get_description()),fiyat = sosZeytin.get_cost()))
          print("-------------------------------")

          sosZeytin_price = sosZeytin.get_cost()
          sosPrice = sosPrice + sosZeytin_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')
        
      if sos == "2":
        sos_name = convertTuple(sosMantar.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMantar.get_cost()))
          print("-------------------------------")

          sosMantar_price = sosMantar.get_cost()
          sosPrice = sosPrice + sosMantar_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "3":
        sos_name = convertTuple(sosKeciPeyniri.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')

        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosKeciPeyniri.get_cost()))
          print("-------------------------------")

          sosKeciPeyniri_price = sosKeciPeyniri.get_cost()
          sosPrice = sosPrice + sosKeciPeyniri_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "4":
        sos_name = convertTuple(sosEt.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosEt.get_cost()))
          print("-------------------------------")

          sosEt_price = sosEt.get_cost()
          sosPrice = sosPrice + sosEt_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')
   
      if sos == "5":
        sos_name = convertTuple(sosSogan.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosSogan.get_cost()))
          print("-------------------------------")

          sosSogan_price = sosSogan.get_cost()
          sosPrice = sosPrice + sosSogan_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "6":
        sos_name = convertTuple(sosMisir.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMisir.get_cost()))
          print("-------------------------------")

          sosMisir_price = sosMisir.get_cost()
          sosPrice = sosPrice + sosMisir_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')
  else:
    if kckBoy in sizes:
      size_name = sizes[0]
      add_Price = kckBoy_Price 
      total_price = tr_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizTurk.get_description())

    if ortBoy in sizes:
      size_name = sizes[0]
      add_Price = ortBoy_Price
      total_price = tr_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizTurk.get_description())
    
    if bykBoy in sizes:
      size_name = sizes[0]
      add_Price = bykBoy_Price
      total_price = tr_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizTurk.get_description())
      
  icecek_ister_mi = input("İçecek ister misiniz(e/h): ")
  if icecek_ister_mi == "e":
    df4 = pd.read_csv("İcecekler.txt")
    print(df4.head(7))
    icecek_secim = input("\nİçceceğinizi seçiniz: \n")

    if icecek_secim == "1":
      icecek_ismi = ayran
      ayran_price = ayran_price
      soguk_icecekler.append(ayran)
      total_price = tr_pizza_price + sosPrice + ayran_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizTurk.get_description())
      payment_Process()

    if icecek_secim == "2":
      icecek_ismi = cola
      print(type(icecek_ismi))
      soguk_icecekler.append(cola)
      total_price = tr_pizza_price + sosPrice + cola_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizTurk.get_description())
      payment_Process()

    if icecek_secim == "3":
      icecek_ismi = gazoz
      soguk_icecekler.append(gazoz)
      total_price = tr_pizza_price + sosPrice + gazoz_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizTurk.get_description())
      payment_Process()

    if icecek_secim == "4":
      icecek_ismi = fanta
      soguk_icecekler.append(fanta)
      total_price = tr_pizza_price + sosPrice + fanta_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizTurk.get_description())
      payment_Process()

    if icecek_secim == "5":
      icecek_ismi = icetea1
      soguk_icecekler.append(icetea1)
      total_price = tr_pizza_price + sosPrice + icetea1_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizTurk.get_description())
      payment_Process()

    if icecek_secim == "6":
      icecek_ismi = icetea2
      soguk_icecekler.append(icetea2)
      total_price = tr_pizza_price + sosPrice + icetea2_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizTurk.get_description())
      payment_Process()

  else:
    if sizes[0] == kckBoy:
      boyut = kckBoy_Price
    if sizes[0] == ortBoy:
      boyut = ortBoy_Price
    if sizes[0] == bykBoy:
      boyut = bykBoy_Price
      
    total_price = tr_pizza_price + sosPrice + boyut
    print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
    time.sleep(3)
    pizza_name = convertTuple(pizTurk.get_description())
    payment_Process()

  
if selection == "4":
  os.system('cls')
  do_pizza_price = pizDo.get_cost()
  print(convertTuple(pizDo.get_description()) , ' seçtiniz ')
  time.sleep(3)

  df = pd.read_csv("PİzzaBoyutları.txt")
  print(df.head())

  select_size = input("Pizza boyutunuzu seçiniz: ")

  if select_size == "1":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = kckBoy))
    sizes.append(kckBoy)

  if select_size == "2":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = ortBoy))
    sizes.append(ortBoy)

  if select_size == "3":
    os.system('cls')
    print('Boyutunuz: {boy}'.format(boy = ortBoy))
    sizes.append(bykBoy)

  do_you_want_sos = input("Sos ister misiniz(e/h): ") 
  if do_you_want_sos == "e":

    os.system('cls')
    print("Bilgilendirme: Sos seçimi için 3 hakkınız var\n")

    count = 3
    while count > i:
      df2 = pd.read_csv("Menu2.txt") #Sosların bulunduğu dosyayı okuyoruz.
      print(df2.head(6))

      sos = str(input("Hangi sosu istersiniz: "))

      if sos == "1":
        sos_name = convertTuple(sosZeytin.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = convertTuple(sosZeytin.get_description()),fiyat = sosZeytin.get_cost()))
          print("-------------------------------")

          sosZeytin_price = sosZeytin.get_cost()
          sosPrice = sosPrice + sosZeytin_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')
        
      if sos == "2":
        sos_name = convertTuple(sosMantar.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMantar.get_cost()))
          print("-------------------------------")

          sosMantar_price = sosMantar.get_cost()
          sosPrice = sosPrice + sosMantar_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "3":
        sos_name = convertTuple(sosKeciPeyniri.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')

        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosKeciPeyniri.get_cost()))
          print("-------------------------------")

          sosKeciPeyniri_price = sosKeciPeyniri.get_cost()
          sosPrice = sosPrice + sosKeciPeyniri_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "4":
        sos_name = convertTuple(sosEt.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosEt.get_cost()))
          print("-------------------------------")

          sosEt_price = sosEt.get_cost()
          sosPrice = sosPrice + sosEt_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "5":
        sos_name = convertTuple(sosSogan.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosSogan.get_cost()))
          print("-------------------------------")

          sosSogan_price = sosSogan.get_cost()
          sosPrice = sosPrice + sosSogan_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

      if sos == "6":
        sos_name = convertTuple(sosMisir.get_description())

        if sos_name in sosListe:
          print('Her sostan sadece bir adet seçilebilir.')
          
        else:
          sosListe.append(sos_name)
          i+=1
          print("Sos : {acıklama}\nSos Fiyatı: {fiyat}".format(acıklama = sos_name,fiyat = sosMisir.get_cost()))
          print("-------------------------------")

          sosMisir_price = sosMisir.get_cost()
          sosPrice = sosPrice + sosMisir_price
          SuccesMessage()
          time.sleep(1)
          os.system('cls')

  else:
    if kckBoy in sizes:
      size_name = sizes[0]
      add_Price = kckBoy_Price 
      total_price = do_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizDo.get_description())

    if ortBoy in sizes:
      size_name = sizes[0]
      add_Price = ortBoy_Price
      total_price = do_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizDo.get_description())
    
    if bykBoy in sizes:
      size_name = sizes[0]
      add_Price = bykBoy_Price
      total_price = do_pizza_price + sosPrice + add_Price
      pizza_name = convertTuple(pizDo.get_description())

  icecek_ister_mi = input("İçecek ister misiniz(e/h): ")
  if icecek_ister_mi == "e":
    df4 = pd.read_csv("İcecekler.txt")
    print(df4.head(7))
    icecek_secim = input("\nİçceceğinizi seçiniz: \n")

    if icecek_secim == "1":
      icecek_ismi = ayran
      ayran_price = ayran_price
      soguk_icecekler.append(ayran)
      total_price = do_pizza_price + sosPrice + ayran_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizDo.get_description())
      payment_Process()

    if icecek_secim == "2":
      icecek_ismi = cola
      print(type(icecek_ismi))
      soguk_icecekler.append(cola)
      total_price = do_pizza_price + sosPrice + cola_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizDo.get_description())
      payment_Process()

    if icecek_secim == "3":
      icecek_ismi = gazoz
      soguk_icecekler.append(gazoz)
      total_price = do_pizza_price + sosPrice + gazoz_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizDo.get_description())
      payment_Process()

    if icecek_secim == "4":
      icecek_ismi = fanta
      soguk_icecekler.append(fanta)
      total_price = do_pizza_price + sosPrice + fanta_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizDo.get_description())
      payment_Process()

    if icecek_secim == "5":
      icecek_ismi = icetea1
      soguk_icecekler.append(icetea1)
      total_price = do_pizza_price + sosPrice + icetea1_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizDo.get_description())
      payment_Process()

    if icecek_secim == "6":
      icecek_ismi = icetea2
      soguk_icecekler.append(icetea2)
      total_price = do_pizza_price + sosPrice + icetea2_price
      print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
      pizza_name = convertTuple(pizDo.get_description())
      payment_Process()

  else:
    if sizes[0] == kckBoy:
      boyut = kckBoy_Price
    if sizes[0] == ortBoy:
      boyut = ortBoy_Price
    if sizes[0] == bykBoy:
      boyut = bykBoy_Price
      
    total_price = do_pizza_price + sosPrice + boyut
    print('\n Ödeme işlemi için yönlendiriliyorsunuz...')
    time.sleep(3)
    pizza_name = convertTuple(pizDo.get_description())
    payment_Process()

    
