
                              # Parlayan Yıldızlar Grubu Pizza Order System Project Kodluyorlar
import webbrowser
import tkinter as tk
from tkinter import *
import csv
import time 
import datetime
import pymysql.cursors
from tkinter import messagebox
#Mysql bağlantı kodlarımız 
db = pymysql.connect(host='localhost',
                        user='******',
                        password='******', # Bilgisayarında Mysql olanlar için user ve password alanları kendi mysqllerine göre yazılmalıdır.
                        db='projeglobalaıhub',
                        cursorclass=pymysql.cursors.DictCursor)
connection = db.cursor()

global sosListe, pizza_name, pizza_fiyat, boyut, boyutlar, pizzas, radio_sos_control, icecekListe, sosPrice, total_price, boyutlarPrice
global classic_pizza_acıklama, margherita_pizza_acıklama, turk_pizza_acıklama, dominos_pizza_acıklama, screens_name

classic_pizza_acıklama    = "İçindekiler:\nSucuk\nDomates\nMozarella\nFesleğen"
margherita_pizza_acıklama = "İçindekiler:\nSucuk\nBiber\nDomates\nFesleğen"
turk_pizza_acıklama       = "İçindekiler:\nSucuk\nMozarella Peyniri\nKüp Sucuk\nSalam"
dominos_pizza_acıklama    = "İçindekiler:\nSalam\nJambon\nSucuk\nKüp Patates"

pizzas      = ['Klasik Pizza','Margherita Pizza','Türk Pizza','Dominos Pizza']
sosListe    = []
boyutlar    = []
icecekListe = []
sosPrice    = []
icecekPrice = []
boyutlarPrice=[]
screens_name =[]
class Pizza():

  def __init__(self, description, cost):
    self.__description = description,
    self.__cost = cost

  def get_description(self):
    return self.__description

  def set_description(self,description_):
    self.__description = description_    

  def get_cost(self):
    return self.__cost
  
  def set_cost(self,cost_):
    self.__cost = cost_


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
pizMar = Margherita("Margherita Pizza", 135)
pizTurk = TurkPizza("Türk Pizza", 120)
pizDo = Dominos("Dominos Pizza", 150)
print("\n")

class Decorator(Pizza):

  def __init__(self, description, cost):
    self._description = description,
    self._cost = cost

  def get_description(self):
    return self._description

  def set_description(self,description_):
    self._description = description_    

  def get_cost(self):
    return self._cost
  
  def set_cost(self,cost_):
    self._cost = cost_
  

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

sosZeytin = Zeytin("Siyah Zeytin",5)
sosMantar = Mantar("Kültür Mantarı",12)
sosKeciPeyniri = KeciPeyniri("Keçi Peyniri 50gr",25)
sosEt = Et("Dana Eti 100gr",32)
sosSogan = Sogan("Soğan",7)
sosMisir= Misir("Süt Mısır 35gr",9)

kckBoy = "Küçük Boy"
kckBoy_Price = 10

ortBoy = "Orta Boy"
ortBoy_Price = 20

bykBoy = "Büyük Boy"
bykBoy_Price = 30

ayran = "Ayran"
ayran_price = 7

cola = "Coca-Cola"
cola_price = 15

gazoz = "Gazoz"
gazoz_price = 15

fanta = "Fanta"
fanta_price = 15

icetea1 = "Ice-Tea (Şeftali)"
icetea1_price = 12

icetea2 = "Ice-Tea (Limon)"
icetea2_price = 12

#Tuple tipinden string'e dönüştürme için fonksyion
def convertTupleName(tup):
  pizza_name = ''.join(tup)
  return pizza_name

#List yapısından string'e dönüştürme için fonskiyon
def convertList(lis):
  sosListe = ' '.join(lis)
  return sosListe

#Başarılı işlem mesajı
def Succes_Message():
     print('İşlem başarılı!!!')

# Hata Mesajı
def Error_Message():
     print('Bir hata oluştu tekrar deneyin!!!')

# # Kullanıcının kayıt olmas kısmındaki sorguların olduğu kısım
def register_user():

     # Globalde tanımladığımız değişkenlerimizin getirilmesi ve keywordlerde kafa karışıklığı yaratmaması için yeni değişkenlere atanması.
     name_surname_info = name_surname.get()
     email_info = email.get()
     phone_info = phone.get()
     password_info = password.get()

     # Kullanıcıdan alınan bilgilerin herhangi bir tanesinin boş olması durumunda hata mesajının yazdırılması

     if name_surname_info == " ":
          Error_Message()
     elif email_info == " ":
          Error_Message()
     elif phone_info == " ":
          Error_Message()
     elif password_info == " ":
          Error_Message()
     else:
          # Sql sorgumuzun olduğu kısım buarada alınan bilgiler database'e işlenir.
          connection.execute("INSERT INTO dbregister VALUES (%s,%s,%s,%s,%s)",(None,name_surname_info,email_info,phone_info,password_info)) 
          db.commit()
          time.sleep(1)
          Succes_Message() # işlemin başarılı olduğunu belirtmek için kullanılan olumlu mesaj 
          root.destroy()
          Login()


def Register():
     login_screen.destroy() # Eğer Login ekranından gelmiş ise bu  kod çalışır çünkü ilk login ekranımız çalışmaktadır.
     global root
     root = Tk()
     root.title("Pizza Order System Register Panel")
     root.geometry("550x425")
     
     #Gerekli değişkenlerin diğer fonksiyonlarda kullanılabilmesi için global şekilde tanımlandığı kısım
     global name_surname
     global email
     global phone
     global password

     Label(root, width=18, height=3, text="Name And Surname :", font="Times 10 bold").grid(row=1,column=0)
     Label(root, width=18, height=3, text="E-Mail :", font="Times 10 bold").grid(row=2,column=0)
     Label(root, width=18, height=3, text="Phone Number :", font="Times 10 bold").grid(row=3,column=0)
     Label(root, width=18, height=3, text="Password :", font="Times 10 bold").grid(row=4,column=0) 

     # Değişkenlerimize doğrudan erişim ve oluşturmak için kullanılan StringVar() tanımlama kısmı.
     name_surname = StringVar()
     email = StringVar()
     phone = StringVar()
     password = StringVar()

     Entry(root, textvariable=name_surname, width= 30).grid(row=1,column=1) 
     Entry(root, textvariable=email,width= 30).grid(row=2,column=1)
     Entry(root, textvariable=phone,width= 30).grid(row=3,column=1) 
     Entry(root,textvariable=password,width=30).grid(row=4,column=1) 

     Button(root,width=11,text='Kayıt Ol',command=register_user).grid(row=5,column=0)
     Button(root,width=11,text='Giriş Yap',command=login).grid(row=5,column=1)

     root.mainloop()

def login():
  root.destroy()
  Login()

# Login işleminin kontrolünün sağlandığı fonksiyon
def login_verify():
     Email_verify = email_verify.get() 
     Password_verify = password_verify.get()
     sql = "SELECT * FROM dbregister where email = %s and sifre = %s" 
     connection.execute(sql,[(Email_verify),(Password_verify)])
     result = connection.fetchall() # Buarada result değişkenine dbregister tablosundaki gerekli bilgiler atanır. 
     if result:
          for i in result:
               logged_message()
               login_screen.destroy() # Eğer giriş işlemi başarılı olursa buaradaki kodlar çalışır ve menü kullanıcıya sunulur gerekli hesaplamaların ardından 
               Home_Page()                            # ödenmesi gereken tutar hesaplanır ve kullanıcıya gösterilir.
               # total() # Hesaplamaların ve sosların seçimlerinin yapıldığı fonksiyondur.
     else:
          not_logged_message()

# Giriş işleminin kontrolünden sonra ekrana göstereceğimiz olumsuz mesaj
def not_logged_message():
     tk.messagebox.showinfo("Hata","Giriş bilgileri hatalı")

# Giriş işleminin kontrolünden sonra ekranda göstereceğimiz olumlu mesaj
def logged_message():
     tk.messagebox.showinfo("Doğru","Giriş İşlemi Başarılı")

# Login ekranı ---> Kullanıcı giriş ekranı e-mail ve şifrelerin girildiği kısımdır.
def Login():
     global login_screen
     login_screen = tk.Tk()
     login_screen.title("Pizza Order System Login Panel")
     login_screen.geometry("350x225")
     
     global email_verify
     global password_verify

     Label(login_screen, width=18, height=3, text="E-Mail:", font="Times 10 bold").grid(row=1,column=0)
     Label(login_screen, width=18, height=3, text="Password:", font="Times 10 bold").grid(row=2,column=0)

     email_verify = StringVar()
     password_verify = StringVar()

     Entry(login_screen, textvariable=email_verify,width= 30).grid(row=1,column=1)
     Entry(login_screen,textvariable=password_verify ,width= 30).grid(row=2,column=1)

     Button(login_screen,text='Giriş Yap',command=login_verify).grid(row=3,column=1)
     Label(login_screen,text="Hesabın yok ise: ").grid(row=4,column=0)
     Button(login_screen,text='Kayıt Ol',command=Register).grid(row=4,column=1)

     login_screen.mainloop()

def Odeme_ekranı_classic():
        classic_pizza_screen.destroy()
        global odeme_screen
        odeme_screen = tk.Tk()
        odeme_screen.geometry("500x300+840+200")
        odeme_screen.title(" Pizza Order System Ödeme Ekranı ")
        print(screens_name)

        global userid,credit_card_name_surname,credit_card_number,credit_card_last_time,credit_card_cvv,credit_card_password

        Label(odeme_screen,text=" ").grid(row=1,column=0)
        Label(odeme_screen,text=" ").grid(row=2,column=0)
        
        Label(odeme_screen,text="Kart Sahibi TC: ",font="verdana 11 bold").grid(row=3,column=0)
        userid = StringVar()
        Entry(odeme_screen,textvariable=userid).grid(row=3,column=1)
        
        Label(odeme_screen,text="Kart Sahibi Adı Soyadı: ",font="verdana 11 bold").grid(row=4,column=0)
        credit_card_name_surname = StringVar()
        Entry(odeme_screen,textvariable=credit_card_name_surname).grid(row=4,column=1)

        Label(odeme_screen,text="Kart Numrası: ",font="verdana 11 bold").grid(row=5,column=0)
        credit_card_number = StringVar()
        Entry(odeme_screen,textvariable=credit_card_number).grid(row=5,column=1)

        Label(odeme_screen,text="Kart Son K. Tarihi: ",font="verdana 11 bold").grid(row=6,column=0)
        credit_card_last_time = StringVar()
        Entry(odeme_screen,textvariable=credit_card_last_time).grid(row=6,column=1)

        Label(odeme_screen,text="Cvv: ",font="verdana 11 bold").grid(row=7,column=0)
        credit_card_cvv = StringVar()
        Entry(odeme_screen,textvariable=credit_card_cvv).grid(row=7,column=1)

        Label(odeme_screen,text="Şifre: ",font="verdana 11 bold").grid(row=8,column=0)
        credit_card_password= StringVar()
        Entry(odeme_screen,textvariable=credit_card_password).grid(row=8,column=1)

        
        Button(odeme_screen,text="<",command=goback,bg="red", fg="black", font="verdana 11 bold").place(x=5,y=5,width=30,height=30)

        def information_verify_classic():
          pizza_name = convertTupleName(pizCls.get_description())
          order_time = datetime.datetime.now()
          icecek_name= convertList(icecekListe)
          sos_name   = convertList(sosListe)
          boyut      = convertList(boyutlar)
          TotalHesaplamaClassic()
          order_description ="Pizza: " + pizza_name + " Boyut: " + boyut +  " İçecek: " + icecek_name + " Soslar: " + sos_name + " Fiyat: " + total
          userid_info = userid.get()
          credit_card_name_surname_info = credit_card_name_surname.get()
          credit_card_number_info = credit_card_number.get()
          credit_card_last_time_info = credit_card_last_time.get() 
          credit_card_cvv_info = credit_card_cvv.get()
          credit_card_password_info = credit_card_password.get()
          
          sql = ('INSERT INTO ordersystemtk VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)')
          data = (None,userid_info,credit_card_name_surname_info,order_description,order_time,credit_card_number_info,credit_card_last_time_info,credit_card_cvv_info,credit_card_password_info)
          connection.execute(sql,data)
          db.commit()
          messagebox.showinfo("Tebrikler!", "Ödemeniz Başarılı Bir Şekilde Yapıldı")
          odeme_screen.destroy()
        Button(odeme_screen,text="Ödeme",command=information_verify_classic, width=20,font="bold").grid(row=9,column=1)
        odeme_screen.mainloop()

#---------------------------------------------------*---------------------------------------------------------------*-----------------------------------------------------------------------*--------------------------
def Odeme_Ekranı_margherita():
        margherita_pizza_screen.destroy()
        global odeme_screen
        odeme_screen = tk.Tk()
        odeme_screen.geometry("500x300+840+200")
        odeme_screen.title(" Pizza Order System Ödeme Ekranı ")
        print(screens_name)

        global userid,credit_card_name_surname,credit_card_number,credit_card_last_time,credit_card_cvv,credit_card_password

        Label(odeme_screen,text=" ").grid(row=1,column=0)
        Label(odeme_screen,text=" ").grid(row=2,column=0)
        
        Label(odeme_screen,text="Kart Sahibi TC: ",font="verdana 11 bold").grid(row=3,column=0)
        userid = StringVar()
        Entry(odeme_screen,textvariable=userid).grid(row=3,column=1)
        
        Label(odeme_screen,text="Kart Sahibi Adı Soyadı: ",font="verdana 11 bold").grid(row=4,column=0)
        credit_card_name_surname = StringVar()
        Entry(odeme_screen,textvariable=credit_card_name_surname).grid(row=4,column=1)

        Label(odeme_screen,text="Kart Numrası: ",font="verdana 11 bold").grid(row=5,column=0)
        credit_card_number = StringVar()
        Entry(odeme_screen,textvariable=credit_card_number).grid(row=5,column=1)

        Label(odeme_screen,text="Kart Son K. Tarihi: ",font="verdana 11 bold").grid(row=6,column=0)
        credit_card_last_time = StringVar()
        Entry(odeme_screen,textvariable=credit_card_last_time).grid(row=6,column=1)

        Label(odeme_screen,text="Cvv: ",font="verdana 11 bold").grid(row=7,column=0)
        credit_card_cvv = StringVar()
        Entry(odeme_screen,textvariable=credit_card_cvv).grid(row=7,column=1)

        Label(odeme_screen,text="Şifre: ",font="verdana 11 bold").grid(row=8,column=0)
        credit_card_password= StringVar()
        Entry(odeme_screen,textvariable=credit_card_password).grid(row=8,column=1)

        
        Button(odeme_screen,text="<",command=goback,bg="red", fg="black", font="verdana 11 bold").place(x=5,y=5,width=30,height=30)

        def information_verify_margherita():
          pizza_name = convertTupleName(pizMar.get_description())
          order_time = datetime.datetime.now()
          icecek_name= convertList(icecekListe)
          sos_name   = convertList(sosListe)
          boyut      = convertList(boyutlar)
          TotalHesaplamaMargherita()
          order_description ="Pizza: " + pizza_name + " Boyut: " + boyut +  " İçecek: " + icecek_name + " Soslar: " + sos_name + " Fiyat: " + total
          userid_info = userid.get()
          credit_card_name_surname_info = credit_card_name_surname.get()
          credit_card_number_info = credit_card_number.get()
          credit_card_last_time_info = credit_card_last_time.get() 
          credit_card_cvv_info = credit_card_cvv.get()
          credit_card_password_info = credit_card_password.get()
          
          sql = ('INSERT INTO ordersystemtk VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)')
          data = (None,userid_info,credit_card_name_surname_info,order_description,order_time,credit_card_number_info,credit_card_last_time_info,credit_card_cvv_info,credit_card_password_info)
          connection.execute(sql,data)
          db.commit()
          messagebox.showinfo("Tebrikler!", "Ödemeniz Başarılı Bir Şekilde Yapıldı")
          odeme_screen.destroy()
        Button(odeme_screen,text="Ödeme",command=information_verify_margherita, width=20,font="bold").grid(row=9,column=1)
        odeme_screen.mainloop()

          
#*--------------------------------------------------------------*--------------------------------------------------------------------------*------------------------------------------------

def Odeme_Ekranı_Turk():
        turk_pizza_screen.destroy()
        global odeme_screen
        odeme_screen = tk.Tk()
        odeme_screen.geometry("500x300+840+200")
        odeme_screen.title(" Pizza Order System Ödeme Ekranı ")
        print(screens_name)

        global userid,credit_card_name_surname,credit_card_number,credit_card_last_time,credit_card_cvv,credit_card_password

        Label(odeme_screen,text=" ").grid(row=1,column=0)
        Label(odeme_screen,text=" ").grid(row=2,column=0)
        
        Label(odeme_screen,text="Kart Sahibi TC: ",font="verdana 11 bold").grid(row=3,column=0)
        userid = StringVar()
        Entry(odeme_screen,textvariable=userid).grid(row=3,column=1)
        
        Label(odeme_screen,text="Kart Sahibi Adı Soyadı: ",font="verdana 11 bold").grid(row=4,column=0)
        credit_card_name_surname = StringVar()
        Entry(odeme_screen,textvariable=credit_card_name_surname).grid(row=4,column=1)

        Label(odeme_screen,text="Kart Numrası: ",font="verdana 11 bold").grid(row=5,column=0)
        credit_card_number = StringVar()
        Entry(odeme_screen,textvariable=credit_card_number).grid(row=5,column=1)

        Label(odeme_screen,text="Kart Son K. Tarihi: ",font="verdana 11 bold").grid(row=6,column=0)
        credit_card_last_time = StringVar()
        Entry(odeme_screen,textvariable=credit_card_last_time).grid(row=6,column=1)

        Label(odeme_screen,text="Cvv: ",font="verdana 11 bold").grid(row=7,column=0)
        credit_card_cvv = StringVar()
        Entry(odeme_screen,textvariable=credit_card_cvv).grid(row=7,column=1)

        Label(odeme_screen,text="Şifre: ",font="verdana 11 bold").grid(row=8,column=0)
        credit_card_password= StringVar()
        Entry(odeme_screen,textvariable=credit_card_password).grid(row=8,column=1)

        
        Button(odeme_screen,text="<",command=goback,bg="red", fg="black", font="verdana 11 bold").place(x=5,y=5,width=30,height=30)

        def information_verify_turk():
          pizza_name = convertTupleName(pizTurk.get_description())
          order_time = datetime.datetime.now()
          icecek_name= convertList(icecekListe)
          sos_name   = convertList(sosListe)
          boyut      = convertList(boyutlar)
          TotalHesaplamaTurk()
          order_description ="Pizza: " + pizza_name + " Boyut: " + boyut +  " İçecek: " + icecek_name + " Soslar: " + sos_name + " Fiyat: " + total
          userid_info = userid.get()
          credit_card_name_surname_info = credit_card_name_surname.get()
          credit_card_number_info = credit_card_number.get()
          credit_card_last_time_info = credit_card_last_time.get() 
          credit_card_cvv_info = credit_card_cvv.get()
          credit_card_password_info = credit_card_password.get()
          
          sql = ('INSERT INTO ordersystemtk VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)')
          data = (None,userid_info,credit_card_name_surname_info,order_description,order_time,credit_card_number_info,credit_card_last_time_info,credit_card_cvv_info,credit_card_password_info)
          connection.execute(sql,data)
          db.commit()
          messagebox.showinfo("Tebrikler!", "Ödemeniz Başarılı Bir Şekilde Yapıldı")
          odeme_screen.destroy()
        Button(odeme_screen,text="Ödeme",command=information_verify_turk, width=20,font="bold").grid(row=9,column=1)
        odeme_screen.mainloop()

#*--------------------------------------------------------------*--------------------------------------------------------------------------*------------------------------------------------
def Odeme_Ekranı_Dominos():
        dominos_pizza_screen.destroy()
        global odeme_screen
        odeme_screen = tk.Tk()
        odeme_screen.geometry("500x300+840+200")
        odeme_screen.title(" Pizza Order System Ödeme Ekranı ")
        print(screens_name)

        global userid,credit_card_name_surname,credit_card_number,credit_card_last_time,credit_card_cvv,credit_card_password


        Label(odeme_screen,text=" ").grid(row=1,column=0)
        Label(odeme_screen,text=" ").grid(row=2,column=0)
        
        Label(odeme_screen,text="Kart Sahibi TC: ",font="verdana 11 bold").grid(row=3,column=0)
        userid = StringVar()
        Entry(odeme_screen,textvariable=userid).grid(row=3,column=1)
        
        Label(odeme_screen,text="Kart Sahibi Adı Soyadı: ",font="verdana 11 bold").grid(row=4,column=0)
        credit_card_name_surname = StringVar()
        Entry(odeme_screen,textvariable=credit_card_name_surname).grid(row=4,column=1)

        Label(odeme_screen,text="Kart Numrası: ",font="verdana 11 bold").grid(row=5,column=0)
        credit_card_number = StringVar()
        Entry(odeme_screen,textvariable=credit_card_number).grid(row=5,column=1)

        Label(odeme_screen,text="Kart Son K. Tarihi: ",font="verdana 11 bold").grid(row=6,column=0)
        credit_card_last_time = StringVar()
        Entry(odeme_screen,textvariable=credit_card_last_time).grid(row=6,column=1)

        Label(odeme_screen,text="Cvv: ",font="verdana 11 bold").grid(row=7,column=0)
        credit_card_cvv = StringVar()
        Entry(odeme_screen,textvariable=credit_card_cvv).grid(row=7,column=1)

        Label(odeme_screen,text="Şifre: ",font="verdana 11 bold").grid(row=8,column=0)
        credit_card_password= StringVar()
        Entry(odeme_screen,textvariable=credit_card_password).grid(row=8,column=1)

        
        Button(odeme_screen,text="<",command=goback,bg="red", fg="black", font="verdana 11 bold").place(x=5,y=5,width=30,height=30)

        def information_verify_dominos():
          pizza_name = convertTupleName(pizDo.get_description())
          order_time = datetime.datetime.now()
          icecek_name= convertList(icecekListe)
          sos_name   = convertList(sosListe)
          boyut      = convertList(boyutlar)
          TotalHesaplamaDominos()
          order_description ="Pizza: " + pizza_name + " Boyut: " + boyut +  " İçecek: " + icecek_name + " Soslar: " + sos_name + " Fiyat: " + total
          userid_info = userid.get()
          credit_card_name_surname_info = credit_card_name_surname.get()
          credit_card_number_info = credit_card_number.get()
          credit_card_last_time_info = credit_card_last_time.get() 
          credit_card_cvv_info = credit_card_cvv.get()
          credit_card_password_info = credit_card_password.get()
          
          sql = ('INSERT INTO ordersystemtk VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)')
          data = (None,userid_info,credit_card_name_surname_info,order_description,order_time,credit_card_number_info,credit_card_last_time_info,credit_card_cvv_info,credit_card_password_info)
          connection.execute(sql,data)
          db.commit()
          messagebox.showinfo("Tebrikler!", "Ödemeniz Başarılı Bir Şekilde Yapıldı")
          odeme_screen.destroy()
        Button(odeme_screen,text="Ödeme",command=information_verify_dominos, width=20,font="bold").grid(row=9,column=1)
        odeme_screen.mainloop()
        
def TotalHesaplamaDominos():
        boyut_Price   = sum(boyutlarPrice)
        totalİcecek   = sum(icecekPrice)
        dominos_price = pizDo.get_cost()
        global total
        total = int(dominos_price + boyut_Price + sum(sosPrice) + totalİcecek)
        total = str(total)

def TotalHesaplamaTurk():
        boyut_Price   = sum(boyutlarPrice)
        totalİcecek   = sum(icecekPrice)
        turk_price = pizTurk.get_cost()
        global total
        total = int(turk_price + boyut_Price + sum(sosPrice) + totalİcecek)
        total = str(total)

def TotalHesaplamaMargherita():
        boyut_Price   = sum(boyutlarPrice)
        totalİcecek   = sum(icecekPrice)
        margherita_price = pizMar.get_cost()
        global total
        total = int(margherita_price + boyut_Price + sum(sosPrice) + totalİcecek)
        total = str(total)

def TotalHesaplamaClassic():
        boyut_Price   = sum(boyutlarPrice)
        totalİcecek   = sum(icecekPrice)
        classic_price = pizCls.get_cost()
        global total
        total = int(classic_price + boyut_Price + sum(sosPrice) + totalİcecek)
        total = str(total)

def goback():
    odeme_screen.destroy()


def Home_Page():
    global home_screen
    home_screen = Tk()
    home_screen.geometry("1900x1900")
    home_screen.title('Menu Screen')
    home_screen.configure(background="light grey")

    Label(home_screen,text="Pizza Sipariş Uygulamasına Hoşgeldiniz....",fg="black", font="verdana 14 bold").place(x=750,y=10)

    # Klasik Pizza Kısmı---
    pizza_name =convertTupleName(pizCls.get_description())
    pizza_name = "Pizza Adı: {ad}".format(ad = pizza_name)
    pizza_fiyat = pizCls.get_cost()
    pizza_fiyat = "Fiyat: {fiyat}".format(fiyat=pizza_fiyat)
    #----------------------
    Button(home_screen,text='Klasik Pizza',command=classic_pizza,bg="red", fg="black", font="verdana 11 bold").place(x=200,y=100,width=320,height=80)
    Label( home_screen,text=pizza_name,bg="Gray",fg="black",font="verdana 11 bold").place(x=200,y=180,width=320,height=45)
    Label( home_screen,text=pizza_fiyat,bg="Gray",fg="black",font="verdana 11 bold").place(x=200,y=220,width=320,height=45)
    Label( home_screen,text=classic_pizza_acıklama,bg="Gray",fg="black",font="verdana 11 bold").place(x=200,y=250,width=320,height=110)


    #Margherita Pizza Kısmı----
    pizza_name = convertTupleName(pizMar.get_description())
    pizza_name = "Pizza Adı: {ad}".format(ad = pizza_name)
    pizza_fiyat = pizMar.get_cost()
    pizza_fiyat = "Fiyat: {fiyat}".format(fiyat=pizza_fiyat)
    #--------------------------
    Button(home_screen,text='Margherita Pizza',command=margherita_pizza,bg="red", fg="black", font="verdana 11 bold").place(x=600,y=100,width=320,height=80)
    Label( home_screen,text=pizza_name,bg="Gray",fg="black",font="verdana 11 bold").place(x=600,y=180,width=320,height=45)
    Label( home_screen,text=pizza_fiyat,bg="Gray",fg="black",font="verdana 11 bold").place(x=600,y=220,width=320,height=45)
    Label( home_screen,text=margherita_pizza_acıklama,bg="Gray",fg="black",font="verdana 11 bold").place(x=600,y=250,width=320,height=110)

    # Türk Pizza Kısmı --------
    pizza_name = pizTurk.get_description()
    pizza_name = convertTupleName(pizza_name)
    pizza_name = "Pizza Adı: {ad}".format(ad = pizza_name)
    pizza_fiyat = pizTurk.get_cost()
    pizza_fiyat = "Fiyat: {fiyat}".format(fiyat=pizza_fiyat)
    #--------------------------
    Button(home_screen,text='Türk Pizza',command=turk_pizza,bg="red", fg="black", font="verdana 11 bold").place(x=1000,y=100,width=320,height=80)
    Label( home_screen,text=pizza_name,bg="Gray",fg="black",font="verdana 11 bold").place(x=1000,y=180,width=320,height=45)
    Label( home_screen,text=pizza_fiyat,bg="Gray",fg="black",font="verdana 11 bold").place(x=1000,y=220,width=320,height=45)
    Label( home_screen,text=turk_pizza_acıklama,bg="Gray",fg="black",font="verdana 11 bold").place(x=1000,y=250,width=320,height=110)

    # Dominos Pizza Kısmı ------
    pizza_name = pizDo.get_description()
    pizza_name = convertTupleName(pizza_name)
    pizza_name = "Pizza Adı: {ad}".format(ad = pizza_name)
    pizza_fiyat = pizDo.get_cost()
    pizza_fiyat = "Fiyat: {fiyat}".format(fiyat=pizza_fiyat)
    #---------------------------
    Button(home_screen,text='Dominos Pizza',command=dominos_pizza,bg="red", fg="black", font="verdana 11 bold").place(x=1380,y=100,width=320,height=80)
    Label( home_screen,text=pizza_name,bg="Gray",fg="black",font="verdana 11 bold").place(x=1380,y=180,width=320,height=45)
    Label( home_screen,text=pizza_fiyat,bg="Gray",fg="black",font="verdana 11 bold").place(x=1380,y=220,width=320,height=45)
    Label( home_screen,text=dominos_pizza_acıklama,bg="Gray",fg="black",font="verdana 11 bold").place(x=1380,y=250,width=320,height=110)
    
    home_screen.mainloop()

def gohome():
  convertList(pizzas)
  if "Klasik Pizza" in pizzas:
     classic_pizza_screen.destroy()
     Home_Page()

def gohome1():
  convertList(pizzas)
  if "Margherita Pizza" in pizzas:
     margherita_pizza_screen.destroy()
     Home_Page()

def gohome2():
  convertList(pizzas)
  if "Türk Pizza" in pizzas:
     turk_pizza_screen.destroy()
     Home_Page()

def gohome3():
  convertList(pizzas)
  if "Dominos Pizza" in pizzas:
     dominos_pizza_screen.destroy()
     Home_Page()


# Klasik Pizza
def classic_pizza():
    home_screen.destroy()
    global classic_pizza_screen
    classic_screen_name = "Klasik"
    screens_name.append(classic_screen_name)
    pizza_name =convertTupleName(pizCls.get_description())
    
    if pizza_name == "Klasik Pizza":
      classic_pizza_screen = Tk()
      classic_pizza_screen.title('Klasik Pizza ')
      classic_pizza_screen.geometry('840x710+100+0')
      Button(classic_pizza_screen,text="<",command=gohome,bg="red", fg="black", font="verdana 11 bold").place(x=5,y=5,width=30,height=30)
      global radio 
      radio = IntVar()
      Label(text="Pizza Boyutunuzu Seçiniz", font=('Aerial 11')).pack()
      r1 = Radiobutton(classic_pizza_screen, text="Küçük Boy", variable=radio, value=1, command=selection_size_classic)
      r1.pack(anchor=N)
      r2 = Radiobutton(classic_pizza_screen, text="Orta Boy", variable=radio, value=2, command=selection_size_classic)

      r2.pack(anchor=N)
      r3 = Radiobutton(classic_pizza_screen, text="Büyük Boy", variable=radio, value=3, command=selection_size_classic)

      r3.pack(anchor=N)
      global label
      label = Label(classic_pizza_screen)
      label.pack()
      Label(classic_pizza_screen, text = " ").pack()
      yazı = "-----------------------------------------------------------------------------------------------------------------"
      Label(classic_pizza_screen,text=yazı,font="verdana 11 bold").place(x=20,y=120)
      Label(classic_pizza_screen, text = " ").pack()
      Label(classic_pizza_screen, text = " ").pack()
      Label(classic_pizza_screen, text = "Pizza Sosunuzu Seçiniz 3 Adet Seçebilirsiniz.", bg ='gray', font=(' verdana 11 ')).place(x=280,y=150)
      Label(classic_pizza_screen, text = " ").pack()
      Label(classic_pizza_screen, text = "Bilgilendirme: Yeni sos eklemek için sosunuzu seçtikten sonra aynı sosu tekrar seçerek boş hale getirmelisiniz.", bg ='gray', font=('verdana 11')).place(x=10,y=170)
      Label(classic_pizza_screen, text = " ").pack()
      
      l = tk.Label(classic_pizza_screen, bg='white', width=50, text=' ')
      l.pack()

      def selection1():
         if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_zeytin = convertTupleName( sosZeytin.get_description() )

            if sos_name_zeytin not in sosListe:
                
              if len(sosListe) < 3:
                sosListe.append(sos_name_zeytin)
                l.config(text=sos_name_zeytin)
                zeytin_price = 5
                sosPrice.append(zeytin_price)
                print(sosListe)
                  
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_mantar = convertTupleName(sosMantar.get_description())
            
            if sos_name_mantar not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_mantar)
                l.config(text=sos_name_mantar)
                mantar_price = 12
                sosPrice.append(mantar_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_peynir = convertTupleName(sosKeciPeyniri.get_description())
           
            if sos_name_peynir not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_peynir)
                l.config(text=sos_name_peynir)
                peynir_price = 25
                sosPrice.append(peynir_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_dana = convertTupleName(sosEt.get_description())
            
            if sos_name_dana not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_dana)
                l.config(text=sos_name_dana)
                dana_price = 32
                sosPrice.append(dana_price)
                print(sosListe)
               
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 1) & (var6.get() == 0):
            sos_name_sogan = convertTupleName(sosSogan.get_description())
           
            if sos_name_sogan not in sosListe:
             
              if len(sosListe) < 3:
                sosListe.append(sos_name_sogan)
                l.config(text=sos_name_sogan)
                sogan_price = 7
                sosPrice.append(sogan_price)
                print(sosListe)
               
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 1):
            sos_name_misir = convertTupleName(sosMisir.get_description())
            
            if sos_name_misir not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_misir)
                l.config(text=sos_name_misir)
                misir_price = 9
                sosPrice.append(misir_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")
         
         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
              l.config(text=" ")
         if len(sosListe) == 3:
            Total()
         if len(sosListe) == 2:
            Total()
         if len(sosListe) == 1:
            Total()

      var1 = tk.IntVar()
      var2 = tk.IntVar()
      var3 = tk.IntVar()
      var4 = tk.IntVar()
      var5 = tk.IntVar()
      var6 = tk.IntVar()

      sos1 = tk.Checkbutton(classic_pizza_screen, text='Siyah Zeytin: 5TL',      variable=var1, onvalue=1, offvalue=0, command=selection1)
      sos1.pack()
      sos2 = tk.Checkbutton(classic_pizza_screen, text='Kültür Mantarı: 12TL',   variable=var2, onvalue=1, offvalue=0, command=selection1)
      sos2.pack()
      sos3 = tk.Checkbutton(classic_pizza_screen, text='Keçi Peyniri 50gr: 25TL',variable=var3, onvalue=1, offvalue=0, command=selection1)
      sos3.pack()
      sos4 = tk.Checkbutton(classic_pizza_screen, text='Dana Eti 100gr: 32TL',   variable=var4, onvalue=1, offvalue=0, command=selection1)
      sos4.pack()
      sos5 = tk.Checkbutton(classic_pizza_screen, text='Soğan: 7TL',             variable=var5, onvalue=1, offvalue=0, command=selection1)
      sos5.pack()
      sos6 = tk.Checkbutton(classic_pizza_screen, text='Süt Mısır 35gr: 9TL',    variable=var6, onvalue=1, offvalue=0, command=selection1)
      sos6.pack()

      global labelSos

      labelSos = Label(classic_pizza_screen)
      labelSos.place(x=330,y=260)

      yazı = "-----------------------------------------------------------------------------------------------------------------"
      Label(classic_pizza_screen,text=yazı,font="verdana 11 bold").pack(anchor=N)
      Label(classic_pizza_screen,text=" ").pack()
      Label(text="İçeceğinizi Seçiniz", bg ='gray', font=('verdana 11')).place(x=350,y=420)
      Label(classic_pizza_screen, text = " ").pack()
      k = tk.Label(classic_pizza_screen, bg='white', width=50,text=' ')
      k.pack()
      def selection2():
         if (var11.get() == 1) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek1 = ayran
            
            if icecek1 not in icecekListe:
                
                if len(icecekListe) < 1:
                  icecekListe.append(icecek1)
                  k.config(text=icecek1)
                  icecekPrice.append(ayran_price)
                  print(icecekListe)
                 
                  if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                    k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 1) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek2 = cola
            
            if icecek2 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek2)
                k.config(text=icecek2)
                icecekPrice.append(cola_price)
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 1) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek3 = gazoz
            
            if icecek3 not in icecekListe:
             
              if len(icecekListe) < 1:
                icecekListe.append(icecek3)
                k.config(text=icecek3)
                icecekPrice.append(gazoz_price)                
                print(icecekListe)
               
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 1) & (var15.get() == 0) & (var16.get() == 0):
            icecek4 = fanta
            
            if icecek4 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek4)
                k.config(text=icecek4)
                icecekPrice.append(fanta_price)                
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 1) & (var16.get() == 0):
            icecek5 = icetea1
            
            if icecek5 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek5)
                k.config(text=icecek5)
                icecekPrice.append(icetea1_price)                
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 1):
            icecek6 = icetea2
            
            if icecek6 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek6)
                k.config(text=icecek6)
                icecekPrice.append(icetea2_price) 
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")
         
         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
              k.config(text=" ")
         if len(icecekPrice) == 1:
            Total()
      var11 = tk.IntVar()
      var12 = tk.IntVar()
      var13 = tk.IntVar()
      var14 = tk.IntVar()
      var15 = tk.IntVar()
      var16 = tk.IntVar()

      icecek1 = tk.Checkbutton(classic_pizza_screen, text='Ayran: 7TL',              variable=var11, onvalue=1, offvalue=0, command=selection2)
      icecek1.pack()
      icecek2 = tk.Checkbutton(classic_pizza_screen, text='Coca-Cola: 15TL',         variable=var12, onvalue=1, offvalue=0, command=selection2)
      icecek2.pack()
      icecek3 = tk.Checkbutton(classic_pizza_screen, text='Gazoz: 15TL',             variable=var13, onvalue=1, offvalue=0, command=selection2)
      icecek3.pack()
      icecek4 = tk.Checkbutton(classic_pizza_screen, text='Fanta: 15TL',             variable=var14, onvalue=1, offvalue=0, command=selection2)
      icecek4.pack()
      icecek5 = tk.Checkbutton(classic_pizza_screen, text='Ice-Tea (Şeftali): 12TL', variable=var15, onvalue=1, offvalue=0, command=selection2)
      icecek5.pack()
      icecek6 = tk.Checkbutton(classic_pizza_screen, text='Ice-Tea (Limon): 12TL',   variable=var16, onvalue=1, offvalue=0, command=selection2)
      icecek6.pack()

      def Total():
        boyut_Price   = sum(boyutlarPrice)
        totalİcecek   = sum(icecekPrice)
        classic_price = pizCls.get_cost()
        total = int(classic_price + boyut_Price + sum(sosPrice) + totalİcecek)
        print('Toplam Tutar: {toplam}'.format(toplam = total))
        x.config(text =total)
      
      global total
      total = IntVar()
      x = tk.Label(classic_pizza_screen,text = ' ', bg="gray",width="30")
      x.pack()
      Button(classic_pizza_screen,text="Siparişi Tamamla. Ödeme Yap",bg= "gray" , fg="black", font="verdana 11 bold",command=Odeme_ekranı_classic).pack()
      classic_pizza_screen.mainloop()

# Margarita Pizza TK
def margherita_pizza():
    home_screen.destroy()
    global margherita_pizza_screen
    margherita_screen_name = "Margherita"
    screens_name.append(margherita_screen_name)
    pizza_name =convertTupleName(pizMar.get_description())
    if pizza_name == "Margherita Pizza":
      margherita_pizza_screen = Tk()
      margherita_pizza_screen.title('Margherita Pizza ')
      margherita_pizza_screen.geometry('840x710+100+0')
      Button(margherita_pizza_screen,text="<",command=gohome1,bg="red",fg="black", font="verdana 11 bold").place(x=5,y=5,width=30,height=30)
      global radio 
      radio = IntVar()
      Label(text="Pizza Boyutunuzu Seçiniz", font=('Aerial 11')).pack()
      r1 = Radiobutton(margherita_pizza_screen, text="Küçük Boy", variable=radio, value=1, command=selection_size_Margherita)
      r1.pack(anchor=N)
      r2 = Radiobutton(margherita_pizza_screen, text="Orta Boy", variable=radio, value=2, command=selection_size_Margherita)
      r2.pack(anchor=N)
      r3 = Radiobutton(margherita_pizza_screen, text="Büyük Boy", variable=radio, value=3, command=selection_size_Margherita)

      r3.pack(anchor=N)
      global label
      label = Label(margherita_pizza_screen)
      label.pack()
      yazı = "-----------------------------------------------------------------------------------------------------------------"
      Label(margherita_pizza_screen,text=yazı,font="verdana 11 bold").place(x=20,y=100)
      Label(margherita_pizza_screen, text = " ").pack()
      Label(margherita_pizza_screen, text = " ").pack()
      Label(margherita_pizza_screen, text = "Pizza Sosunuzu Seçiniz 3 Adet Seçebilirsiniz.", bg ='gray', font=(' verdana 11 ')).place(x=280,y=140)
      Label(margherita_pizza_screen, text = " ").pack()
      
      Label(margherita_pizza_screen, text = "Bilgilendirme: Yeni sos eklemek için sosunuzu seçtikten sonra aynı sosu tekrar seçerek boş hale getirmelisiniz.", bg ='gray', font=('verdana 11')).place(x=10,y=160)
      Label(margherita_pizza_screen, text = " ").pack()
      
      l = tk.Label(margherita_pizza_screen, bg='white', width=50, text=' ')
      l.pack()

      def selection1():
         if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_zeytin = convertTupleName( sosZeytin.get_description() )

            if sos_name_zeytin not in sosListe:
                
              if len(sosListe) < 3:
                sosListe.append(sos_name_zeytin)
                l.config(text=sos_name_zeytin)
                zeytin_price = 5
                sosPrice.append(zeytin_price)
                print(sosListe)
                  
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_mantar = convertTupleName(sosMantar.get_description())
            
            if sos_name_mantar not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_mantar)
                l.config(text=sos_name_mantar)
                mantar_price = 12
                sosPrice.append(mantar_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_peynir = convertTupleName(sosKeciPeyniri.get_description())
           
            if sos_name_peynir not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_peynir)
                l.config(text=sos_name_peynir)
                peynir_price = 25
                sosPrice.append(peynir_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_dana = convertTupleName(sosEt.get_description())
            
            if sos_name_dana not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_dana)
                l.config(text=sos_name_dana)
                dana_price = 32
                sosPrice.append(dana_price)
                print(sosListe)
               
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 1) & (var6.get() == 0):
            sos_name_sogan = convertTupleName(sosSogan.get_description())
           
            if sos_name_sogan not in sosListe:
             
              if len(sosListe) < 3:
                sosListe.append(sos_name_sogan)
                l.config(text=sos_name_sogan)
                sogan_price = 7
                sosPrice.append(sogan_price)
                print(sosListe)
               
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 1):
            sos_name_misir = convertTupleName(sosMisir.get_description())
            
            if sos_name_misir not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_misir)
                l.config(text=sos_name_misir)
                misir_price = 9
                sosPrice.append(misir_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")
         
         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
              l.config(text=" ")
         if len(sosListe) == 3:
            Total()
         if len(sosListe) == 2:
            Total()
         if len(sosListe) == 1:
            Total()

      var1 = tk.IntVar()
      var2 = tk.IntVar()
      var3 = tk.IntVar()
      var4 = tk.IntVar()
      var5 = tk.IntVar()
      var6 = tk.IntVar()

      sos1 = tk.Checkbutton(margherita_pizza_screen, text='Siyah Zeytin: 5TL',      variable=var1, onvalue=1, offvalue=0, command=selection1)
      sos1.pack()
      sos2 = tk.Checkbutton(margherita_pizza_screen, text='Kültür Mantarı: 12TL',   variable=var2, onvalue=1, offvalue=0, command=selection1)
      sos2.pack()
      sos3 = tk.Checkbutton(margherita_pizza_screen, text='Keçi Peyniri 50gr: 25TL',variable=var3, onvalue=1, offvalue=0, command=selection1)
      sos3.pack()
      sos4 = tk.Checkbutton(margherita_pizza_screen, text='Dana Eti 100gr: 32TL',   variable=var4, onvalue=1, offvalue=0, command=selection1)
      sos4.pack()
      sos5 = tk.Checkbutton(margherita_pizza_screen, text='Soğan: 7TL',             variable=var5, onvalue=1, offvalue=0, command=selection1)
      sos5.pack()
      sos6 = tk.Checkbutton(margherita_pizza_screen, text='Süt Mısır 35gr: 9TL',    variable=var6, onvalue=1, offvalue=0, command=selection1)
      sos6.pack()

      global labelSos

      labelSos = Label(margherita_pizza_screen)
      labelSos.place(x=330,y=260)

      yazı = "-----------------------------------------------------------------------------------------------------------------"
      Label(margherita_pizza_screen, text = " ").pack()
      Label(margherita_pizza_screen,text=yazı,font="verdana 11 bold").pack(anchor=N)
      Label(margherita_pizza_screen,text=" ").pack()
      Label(text="İçeceğinizi Seçiniz", bg ='gray', font=('verdana 11')).place(x=350,y=420)
      Label(margherita_pizza_screen, text = " ").pack()
      k = tk.Label(margherita_pizza_screen, bg='white', width=50,text=' ')
      k.pack()
      def selection2():
         if (var11.get() == 1) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek1 = ayran
            
            if icecek1 not in icecekListe:
                
                if len(icecekListe) < 1:
                  icecekListe.append(icecek1)
                  k.config(text=icecek1)
                  icecekPrice.append(ayran_price)
                  print(icecekListe)
                 
                  if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                    k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 1) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek2 = cola
            
            if icecek2 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek2)
                k.config(text=icecek2)
                icecekPrice.append(cola_price)
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 1) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek3 = gazoz
            
            if icecek3 not in icecekListe:
             
              if len(icecekListe) < 1:
                icecekListe.append(icecek3)
                k.config(text=icecek3)
                icecekPrice.append(gazoz_price)                
                print(icecekListe)
               
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 1) & (var15.get() == 0) & (var16.get() == 0):
            icecek4 = fanta
            
            if icecek4 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek4)
                k.config(text=icecek4)
                icecekPrice.append(fanta_price)                
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 1) & (var16.get() == 0):
            icecek5 = icetea1
            
            if icecek5 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek5)
                k.config(text=icecek5)
                icecekPrice.append(icetea1_price)                
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 1):
            icecek6 = icetea2
            
            if icecek6 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek6)
                k.config(text=icecek6)
                icecekPrice.append(icetea2_price) 
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")
         
         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
              k.config(text=" ")
         if len(icecekPrice) == 1:
            Total()
      var11 = tk.IntVar()
      var12 = tk.IntVar()
      var13 = tk.IntVar()
      var14 = tk.IntVar()
      var15 = tk.IntVar()
      var16 = tk.IntVar()

      icecek1 = tk.Checkbutton(margherita_pizza_screen, text='Ayran: 7TL',              variable=var11, onvalue=1, offvalue=0, command=selection2)
      icecek1.pack()
      icecek2 = tk.Checkbutton(margherita_pizza_screen, text='Coca-Cola: 15TL',         variable=var12, onvalue=1, offvalue=0, command=selection2)
      icecek2.pack()
      icecek3 = tk.Checkbutton(margherita_pizza_screen, text='Gazoz: 15TL',             variable=var13, onvalue=1, offvalue=0, command=selection2)
      icecek3.pack()
      icecek4 = tk.Checkbutton(margherita_pizza_screen, text='Fanta: 15TL',             variable=var14, onvalue=1, offvalue=0, command=selection2)
      icecek4.pack()
      icecek5 = tk.Checkbutton(margherita_pizza_screen, text='Ice-Tea (Şeftali): 12TL', variable=var15, onvalue=1, offvalue=0, command=selection2)
      icecek5.pack()
      icecek6 = tk.Checkbutton(margherita_pizza_screen, text='Ice-Tea (Limon): 12TL',   variable=var16, onvalue=1, offvalue=0, command=selection2)
      icecek6.pack()

      def Total():
        boyut_Price   = sum(boyutlarPrice)
        totalİcecek   = sum(icecekPrice)
        margherita_price = pizMar.get_cost()
        total = int(margherita_price + boyut_Price + sum(sosPrice) + totalİcecek)
        print('Toplam Tutar: {toplam}'.format(toplam = total))
        x.config(text =total)
      
      global total
      total = IntVar()
      x = tk.Label(margherita_pizza_screen,text = ' ', bg="gray",width="30")
      x.pack()
      Button(margherita_pizza_screen,text="Siparişi Tamamla. Ödeme Yap",bg= "gray" , fg="black", font="verdana 11 bold",command=Odeme_Ekranı_margherita).pack()

      margherita_pizza_screen.mainloop()

# TÜRK Pizza TK
def turk_pizza():

    global turk_pizza_screen
    turk_screen_name = "Türk"
    screens_name.append(turk_screen_name)
    pizza_name =convertTupleName(pizTurk.get_description())

    if pizza_name == "Türk Pizza":
      global total
      home_screen.destroy()
      turk_pizza_screen = Tk()
      turk_pizza_screen.title('Türk Pizza ')
      turk_pizza_screen.geometry('840x710+100+0')
      Button(turk_pizza_screen,text="<",command=gohome2,bg="red", fg="black", font="verdana 11 bold").place(x=5,y=5,width=30,height=30)
      global radio 
      radio = IntVar()
      Label(text="Pizza Boyutunuzu Seçiniz", font=('Aerial 11')).pack()
      r1 = Radiobutton(turk_pizza_screen, text="Küçük Boy", variable=radio, value=1, command=selection_size_Turk)
      r1.pack(anchor=N)
      r2 = Radiobutton(turk_pizza_screen, text="Orta Boy", variable=radio, value=2, command=selection_size_Turk)
      r2.pack(anchor=N)
      r3 = Radiobutton(turk_pizza_screen, text="Büyük Boy", variable=radio, value=3, command=selection_size_Turk)
      r3.pack(anchor=N)
      global label
      label = Label(turk_pizza_screen)
      label.pack()
      yazı = "-----------------------------------------------------------------------------------------------------------------"
      Label(turk_pizza_screen,text=yazı,font="verdana 11 bold").place(x=20,y=110)
      Label(turk_pizza_screen, text = " ").pack()
      Label(turk_pizza_screen, text = " ").pack()
      Label(turk_pizza_screen, text = "Pizza Sosunuzu Seçiniz 3 Adet Seçebilirsiniz", bg ='gray', font=(' verdana 11 ')).place(x=280,y=140)
      Label(turk_pizza_screen, text = " ").pack()
      
      Label(turk_pizza_screen, text = "Bilgilendirme: Yeni sos eklemek için sosunuzu seçtikten sonra aynı sosu tekrar seçerek boş hale getirmelisiniz.", bg ='gray', font=('verdana 11')).place(x=10,y=160)
      Label(turk_pizza_screen, text = " ").pack()
      
      l = tk.Label(turk_pizza_screen, bg='white', width=50, text=' ')
      l.pack()

      def selection1():
         if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_zeytin = convertTupleName( sosZeytin.get_description() )

            if sos_name_zeytin not in sosListe:
                
              if len(sosListe) < 3:
                sosListe.append(sos_name_zeytin)
                l.config(text=sos_name_zeytin)
                zeytin_price = 5
                sosPrice.append(zeytin_price)
                print(sosListe)
                  
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_mantar = convertTupleName(sosMantar.get_description())
            
            if sos_name_mantar not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_mantar)
                l.config(text=sos_name_mantar)
                mantar_price = 12
                sosPrice.append(mantar_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_peynir = convertTupleName(sosKeciPeyniri.get_description())
           
            if sos_name_peynir not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_peynir)
                l.config(text=sos_name_peynir)
                peynir_price = 25
                sosPrice.append(peynir_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_dana = convertTupleName(sosEt.get_description())
            
            if sos_name_dana not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_dana)
                l.config(text=sos_name_dana)
                dana_price = 32
                sosPrice.append(dana_price)
                print(sosListe)
               
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 1) & (var6.get() == 0):
            sos_name_sogan = convertTupleName(sosSogan.get_description())
           
            if sos_name_sogan not in sosListe:
             
              if len(sosListe) < 3:
                sosListe.append(sos_name_sogan)
                l.config(text=sos_name_sogan)
                sogan_price = 7
                sosPrice.append(sogan_price)
                print(sosListe)
               
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 1):
            sos_name_misir = convertTupleName(sosMisir.get_description())
            
            if sos_name_misir not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_misir)
                l.config(text=sos_name_misir)
                misir_price = 9
                sosPrice.append(misir_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")
         
         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
              l.config(text=" ")
         if len(sosListe) == 3:
            Total()
         if len(sosListe) == 2:
            Total()
         if len(sosListe) == 1:
            Total()

      var1 = tk.IntVar()
      var2 = tk.IntVar()
      var3 = tk.IntVar()
      var4 = tk.IntVar()
      var5 = tk.IntVar()
      var6 = tk.IntVar()

      sos1 = tk.Checkbutton(turk_pizza_screen, text='Siyah Zeytin: 5TL',      variable=var1, onvalue=1, offvalue=0, command=selection1)
      sos1.pack()
      sos2 = tk.Checkbutton(turk_pizza_screen, text='Kültür Mantarı: 12TL',   variable=var2, onvalue=1, offvalue=0, command=selection1)
      sos2.pack()
      sos3 = tk.Checkbutton(turk_pizza_screen, text='Keçi Peyniri 50gr: 25TL',variable=var3, onvalue=1, offvalue=0, command=selection1)
      sos3.pack()
      sos4 = tk.Checkbutton(turk_pizza_screen, text='Dana Eti 100gr: 32TL',   variable=var4, onvalue=1, offvalue=0, command=selection1)
      sos4.pack()
      sos5 = tk.Checkbutton(turk_pizza_screen, text='Soğan: 7TL',             variable=var5, onvalue=1, offvalue=0, command=selection1)
      sos5.pack()
      sos6 = tk.Checkbutton(turk_pizza_screen, text='Süt Mısır 35gr: 9TL',    variable=var6, onvalue=1, offvalue=0, command=selection1)
      sos6.pack()

      global labelSos

      labelSos = Label(turk_pizza_screen)
      labelSos.place(x=330,y=260)

      yazı = "-----------------------------------------------------------------------------------------------------------------"

      Label(turk_pizza_screen,text=yazı,font="verdana 11 bold").pack(anchor=N)
      Label(turk_pizza_screen,text=" ").pack()
      Label(text="İçeceğinizi Seçiniz", bg ='gray', font=('verdana 11')).place(x=360,y=400)
      Label(turk_pizza_screen, text = " ").pack()
      k = tk.Label(turk_pizza_screen, bg='white', width=50,text=' ')
      k.pack()
      def selection2():
         if (var11.get() == 1) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek1 = ayran
            
            if icecek1 not in icecekListe:
                
                if len(icecekListe) < 1:
                  icecekListe.append(icecek1)
                  k.config(text=icecek1)
                  icecekPrice.append(ayran_price)
                  print(icecekListe)
                 
                  if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                    k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 1) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek2 = cola
            
            if icecek2 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek2)
                k.config(text=icecek2)
                icecekPrice.append(cola_price)
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 1) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek3 = gazoz
            
            if icecek3 not in icecekListe:
             
              if len(icecekListe) < 1:
                icecekListe.append(icecek3)
                k.config(text=icecek3)
                icecekPrice.append(gazoz_price)                
                print(icecekListe)
               
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 1) & (var15.get() == 0) & (var16.get() == 0):
            icecek4 = fanta
            
            if icecek4 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek4)
                k.config(text=icecek4)
                icecekPrice.append(fanta_price)                
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 1) & (var16.get() == 0):
            icecek5 = icetea1
            
            if icecek5 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek5)
                k.config(text=icecek5)
                icecekPrice.append(icetea1_price)                
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 1):
            icecek6 = icetea2
            
            if icecek6 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek6)
                k.config(text=icecek6)
                icecekPrice.append(icetea2_price) 
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")
         
         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
              k.config(text=" ")
         if len(icecekPrice) == 1:
            Total()
      var11 = tk.IntVar()
      var12 = tk.IntVar()
      var13 = tk.IntVar()
      var14 = tk.IntVar()
      var15 = tk.IntVar()
      var16 = tk.IntVar()

      icecek1 = tk.Checkbutton(turk_pizza_screen, text='Ayran: 7TL',              variable=var11, onvalue=1, offvalue=0, command=selection2)
      icecek1.pack()
      icecek2 = tk.Checkbutton(turk_pizza_screen, text='Coca-Cola: 15TL',         variable=var12, onvalue=1, offvalue=0, command=selection2)
      icecek2.pack()
      icecek3 = tk.Checkbutton(turk_pizza_screen, text='Gazoz: 15TL',             variable=var13, onvalue=1, offvalue=0, command=selection2)
      icecek3.pack()
      icecek4 = tk.Checkbutton(turk_pizza_screen, text='Fanta: 15TL',             variable=var14, onvalue=1, offvalue=0, command=selection2)
      icecek4.pack()
      icecek5 = tk.Checkbutton(turk_pizza_screen, text='Ice-Tea (Şeftali): 12TL', variable=var15, onvalue=1, offvalue=0, command=selection2)
      icecek5.pack()
      icecek6 = tk.Checkbutton(turk_pizza_screen, text='Ice-Tea (Limon): 12TL',   variable=var16, onvalue=1, offvalue=0, command=selection2)
      icecek6.pack()

      def Total():
        boyut_Price   = sum(boyutlarPrice)
        totalİcecek   = sum(icecekPrice)
        turk_price = pizTurk.get_cost()
        total = int( turk_price + boyut_Price + sum(sosPrice) + totalİcecek)
        print('Toplam Tutar: {toplam}'.format(toplam = total))
        x.config(text =total)
      
      
      total = IntVar()
      x = tk.Label(turk_pizza_screen,text = ' ', bg="gray",width="30")
      x.pack()
      Button(turk_pizza_screen,text="Siparişi Tamamla. Ödeme Yap",bg= "gray" , fg="black", font="verdana 11 bold",command=Odeme_Ekranı_Turk).pack()

      turk_pizza_screen.mainloop()

#*--------------------------------------------------------------*--------------------------------------------------------------------------*------------------------------------------------
#*--------------------------------------------------------------*--------------------------------------------------------------------------*------------------------------------------------
#*--------------------------------------------------------------*--------------------------------------------------------------------------*------------------------------------------------


# Dominos Pizza TK
def dominos_pizza():
  sosListe.clear()
  icecekListe.clear()
  home_screen.destroy()
  global dominos_pizza_screen
  global radio
  global label
  dominos_screen_name = "Dominos"
  screens_name.append(dominos_screen_name)
  pizza_name =convertTupleName(pizDo.get_description())
  if pizza_name == "Dominos Pizza":
      dominos_pizza_screen = Tk()
      dominos_pizza_screen.title(' Dominos Pizza ')
      dominos_pizza_screen.geometry('840x710+100+0')
      
      Button(dominos_pizza_screen, text="<", command=gohome3,bg="red", fg="black", font="verdana 11 bold").place( x=5,y=4, width=30,height=30)
      radio = IntVar()
      Label(text="Boyut seçiminizi lütfen 1 seferde doğru yapınız", font=('Aerial 11')).pack()

      r1 = Radiobutton(dominos_pizza_screen, text="Küçük Boy", variable=radio, value=1, command=selection_size)
      r3 = Radiobutton(dominos_pizza_screen, text="Büyük Boy", variable=radio, value=3, command=selection_size)
      r2 = Radiobutton(dominos_pizza_screen, text="Orta Boy",  variable=radio, value=2, command=selection_size)

      r1.pack(anchor=N)
      r2.pack(anchor=N)
      r3.pack(anchor=N)

      label = Label( dominos_pizza_screen )
      label.pack()

      yazı = "-----------------------------------------------------------------------------------------------------------------"
      Label(dominos_pizza_screen, text = yazı, font = "verdana 11 bold").pack( anchor=N )
      Label(dominos_pizza_screen, text = " ").pack()
      
      Label(dominos_pizza_screen, text = "Pizza Sosunuzu Seçiniz", bg ='gray', font=(' verdana 11 ')).place( x=330,y=140 )
      Label(dominos_pizza_screen, text = " ").pack()
      
      Label(dominos_pizza_screen, text = "Bilgilendirme: Yeni sos eklemek için sosunuzu seçtikten sonra aynı sosu tekrar seçerek boş hale getirmelisiniz.", bg ='gray', font=('verdana 11')).place(x=10,y=160)
      Label(dominos_pizza_screen, text = " ").pack()
      
      l = tk.Label(dominos_pizza_screen, bg='white', width=50, text=' ')
      l.pack()

      def selection1():
         if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_zeytin = convertTupleName( sosZeytin.get_description() )

            if sos_name_zeytin not in sosListe:
                
              if len(sosListe) < 3:
                sosListe.append(sos_name_zeytin)
                l.config(text=sos_name_zeytin)
                zeytin_price = 5
                sosPrice.append(zeytin_price)
                print(sosListe)
                  
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_mantar = convertTupleName(sosMantar.get_description())
            
            if sos_name_mantar not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_mantar)
                l.config(text=sos_name_mantar)
                mantar_price = 12
                sosPrice.append(mantar_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_peynir = convertTupleName(sosKeciPeyniri.get_description())
           
            if sos_name_peynir not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_peynir)
                l.config(text=sos_name_peynir)
                peynir_price = 25
                sosPrice.append(peynir_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1) & (var5.get() == 0) & (var6.get() == 0):
            sos_name_dana = convertTupleName(sosEt.get_description())
            
            if sos_name_dana not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_dana)
                l.config(text=sos_name_dana)
                dana_price = 32
                sosPrice.append(dana_price)
                print(sosListe)
               
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 1) & (var6.get() == 0):
            sos_name_sogan = convertTupleName(sosSogan.get_description())
           
            if sos_name_sogan not in sosListe:
             
              if len(sosListe) < 3:
                sosListe.append(sos_name_sogan)
                l.config(text=sos_name_sogan)
                sogan_price = 7
                sosPrice.append(sogan_price)
                print(sosListe)
               
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")

         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 1):
            sos_name_misir = convertTupleName(sosMisir.get_description())
            
            if sos_name_misir not in sosListe:
              
              if len(sosListe) < 3:
                sosListe.append(sos_name_misir)
                l.config(text=sos_name_misir)
                misir_price = 9
                sosPrice.append(misir_price)
                print(sosListe)
                
                if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
                  l.config(text=" ")
         
         if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0) & (var6.get() == 0):
              l.config(text=" ")
         if len(sosListe) == 3:
            Total()
         if len(sosListe) == 2:
            Total()
         if len(sosListe) == 1:
            Total()

      var1 = tk.IntVar()
      var2 = tk.IntVar()
      var3 = tk.IntVar()
      var4 = tk.IntVar()
      var5 = tk.IntVar()
      var6 = tk.IntVar()

      sos1 = tk.Checkbutton(dominos_pizza_screen, text='Siyah Zeytin: 5TL',      variable=var1, onvalue=1, offvalue=0, command=selection1)
      sos1.pack()
      sos2 = tk.Checkbutton(dominos_pizza_screen, text='Kültür Mantarı: 12TL',   variable=var2, onvalue=1, offvalue=0, command=selection1)
      sos2.pack()
      sos3 = tk.Checkbutton(dominos_pizza_screen, text='Keçi Peyniri 50gr: 25TL',variable=var3, onvalue=1, offvalue=0, command=selection1)
      sos3.pack()
      sos4 = tk.Checkbutton(dominos_pizza_screen, text='Dana Eti 100gr: 32TL',   variable=var4, onvalue=1, offvalue=0, command=selection1)
      sos4.pack()
      sos5 = tk.Checkbutton(dominos_pizza_screen, text='Soğan: 7TL',             variable=var5, onvalue=1, offvalue=0, command=selection1)
      sos5.pack()
      sos6 = tk.Checkbutton(dominos_pizza_screen, text='Süt Mısır 35gr: 9TL',    variable=var6, onvalue=1, offvalue=0, command=selection1)
      sos6.pack()

      global labelSos

      labelSos = Label(dominos_pizza_screen)
      labelSos.place(x=330,y=260)

      yazı = "-----------------------------------------------------------------------------------------------------------------"

      Label(dominos_pizza_screen,text=yazı,font="verdana 11 bold").pack(anchor=N)
      Label(dominos_pizza_screen,text=" ").pack()
      Label(text="İçeceğinizi Seçiniz", bg ='gray', font=('verdana 11')).place(x=330,y=400)
      Label(dominos_pizza_screen, text = " ").pack()
      k = tk.Label(dominos_pizza_screen, bg='white', width=50,text=' ')
      k.pack()
      def selection2():
         if (var11.get() == 1) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek1 = ayran
            
            if icecek1 not in icecekListe:
                
                if len(icecekListe) < 1:
                  icecekListe.append(icecek1)
                  k.config(text=icecek1)
                  icecekPrice.append(ayran_price)
                  print(icecekListe)
                 
                  if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                    k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 1) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek2 = cola
            
            if icecek2 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek2)
                k.config(text=icecek2)
                icecekPrice.append(cola_price)
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 1) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
            icecek3 = gazoz
            
            if icecek3 not in icecekListe:
             
              if len(icecekListe) < 1:
                icecekListe.append(icecek3)
                k.config(text=icecek3)
                icecekPrice.append(gazoz_price)                
                print(icecekListe)
               
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 1) & (var15.get() == 0) & (var16.get() == 0):
            icecek4 = fanta
            
            if icecek4 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek4)
                k.config(text=icecek4)
                icecekPrice.append(fanta_price)                
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 1) & (var16.get() == 0):
            icecek5 = icetea1
            
            if icecek5 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek5)
                k.config(text=icecek5)
                icecekPrice.append(icetea1_price)                
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")

         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 1):
            icecek6 = icetea2
            
            if icecek6 not in icecekListe:
              
              if len(icecekListe) < 1:
                icecekListe.append(icecek6)
                k.config(text=icecek6)
                icecekPrice.append(icetea2_price) 
                print(icecekListe)
                
                if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
                  k.config(text=" ")
         
         if (var11.get() == 0) & (var12.get() == 0) & (var13.get() == 0) & (var14.get() == 0) & (var15.get() == 0) & (var16.get() == 0):
              k.config(text=" ")
         if len(icecekPrice) == 1:
            Total()
      var11 = tk.IntVar()
      var12 = tk.IntVar()
      var13 = tk.IntVar()
      var14 = tk.IntVar()
      var15 = tk.IntVar()
      var16 = tk.IntVar()

      icecek1 = tk.Checkbutton(dominos_pizza_screen, text='Ayran: 7TL',              variable=var11, onvalue=1, offvalue=0, command=selection2)
      icecek1.pack()
      icecek2 = tk.Checkbutton(dominos_pizza_screen, text='Coca-Cola: 15TL',         variable=var12, onvalue=1, offvalue=0, command=selection2)
      icecek2.pack()
      icecek3 = tk.Checkbutton(dominos_pizza_screen, text='Gazoz: 15TL',             variable=var13, onvalue=1, offvalue=0, command=selection2)
      icecek3.pack()
      icecek4 = tk.Checkbutton(dominos_pizza_screen, text='Fanta: 15TL',             variable=var14, onvalue=1, offvalue=0, command=selection2)
      icecek4.pack()
      icecek5 = tk.Checkbutton(dominos_pizza_screen, text='Ice-Tea (Şeftali): 12TL', variable=var15, onvalue=1, offvalue=0, command=selection2)
      icecek5.pack()
      icecek6 = tk.Checkbutton(dominos_pizza_screen, text='Ice-Tea (Limon): 12TL',   variable=var16, onvalue=1, offvalue=0, command=selection2)
      icecek6.pack()

      def Total():
        boyut_Price   = sum(boyutlarPrice)
        totalİcecek   = sum(icecekPrice)
        dominos_price = pizDo.get_cost()
        total = int(dominos_price + boyut_Price + sum(sosPrice) + totalİcecek)
        print('Toplam Tutar: {toplam}'.format(toplam = total))
        x.config(text =total)
      
      global total
      total = IntVar()
      x = tk.Label(dominos_pizza_screen,text = ' ', bg="gray",width="30")
      x.pack()
      Button(dominos_pizza_screen,text="Siparişi Tamamla. Ödeme Yap",bg= "gray" , fg="black", font="verdana 11 bold",command=Odeme_Ekranı_Dominos).pack()
      dominos_pizza_screen.mainloop()

       # Ödeme işlemi için toplam tutarı hesaplama yöntemi: Tüm listelerin elemanlarının price larını alınarak bir değişkende toplanır. Bu değişken bir label da atanır.
       # Label sayfanın sağ en üstünde gösterilebilir. Temiz.....
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def selection_size():
  radio_info = str(radio.get())

  if radio_info == "1":
    label.config(text="Pizza Küçük boy seçildi")
    boyut = "Küçük Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
       if (len(boyutlar)<2):
          boyutlar.clear()
          boyutlarPrice.clear()
          boyutlar.append(boyut)
          convertList(boyutlar)
          boyutlarPrice.append(kckBoy_Price)
          hesaplama = pizDo.get_cost() + sum(boyutlarPrice)
          print(hesaplama)
    print(boyutlar)

  if radio_info == "2":
    label.config(text="Pizza Orta boy seçildi")
    boyut = "Orta Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
      if (len(boyutlar)<2):
        boyutlar.clear()
        boyutlarPrice.clear()
        boyutlar.append(boyut)
        boyutlarPrice.append(ortBoy_Price)
        convertList(boyutlar)
        hesaplama = pizDo.get_cost() + sum(boyutlarPrice)
        print(hesaplama)

    print(boyutlar)

  if radio_info == "3":
    label.config(text="Pizza Büyük boy seçildi")
    boyut = "Büyük Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
       if (len(boyutlar)<2):
          boyutlar.clear()
          boyutlarPrice.clear()
          boyutlar.append(boyut)
          boyutlarPrice.append(bykBoy_Price)
          convertList(boyutlar)
          hesaplama = pizDo.get_cost() + sum(boyutlarPrice)
          print(hesaplama)
    print(boyutlar)

def selection_size_Turk():
  radio_info = str(radio.get())

  if radio_info == "1":
    label.config(text="Pizza Küçük boy seçildi")
    boyut = "Küçük Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
       if (len(boyutlar)<2):
          boyutlar.clear()
          boyutlarPrice.clear()
          boyutlar.append(boyut)
          convertList(boyutlar)
          boyutlarPrice.append(kckBoy_Price)
          hesaplama = pizTurk.get_cost() + sum(boyutlarPrice)
          print(hesaplama)
    print(boyutlar)

  if radio_info == "2":
    label.config(text="Pizza Orta boy seçildi")
    boyut = "Orta Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
      if (len(boyutlar)<2):
        boyutlar.clear()
        boyutlarPrice.clear()
        boyutlar.append(boyut)
        boyutlarPrice.append(ortBoy_Price)
        convertList(boyutlar)
        hesaplama = pizTurk.get_cost() + sum(boyutlarPrice)
        print(hesaplama)

    print(boyutlar)

  if radio_info == "3":
    label.config(text="Pizza Büyük boy seçildi")
    boyut = "Büyük Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
       if (len(boyutlar)<2):
          boyutlar.clear()
          boyutlarPrice.clear()
          boyutlar.append(boyut)
          boyutlarPrice.append(bykBoy_Price)
          convertList(boyutlar)
          hesaplama = pizTurk.get_cost() + sum(boyutlarPrice)
          print(hesaplama)
    print(boyutlar)

def selection_size_Margherita():
  radio_info = str(radio.get())

  if radio_info == "1":
    label.config(text="Pizza Küçük boy seçildi")
    boyut = "Küçük Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
       if (len(boyutlar)<2):
          boyutlar.clear()
          boyutlarPrice.clear()
          boyutlar.append(boyut)
          convertList(boyutlar)
          boyutlarPrice.append(kckBoy_Price)
          hesaplama = pizMar.get_cost() + sum(boyutlarPrice)
          print(hesaplama)
    print(boyutlar)

  if radio_info == "2":
    label.config(text="Pizza Orta boy seçildi")
    boyut = "Orta Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
      if (len(boyutlar)<2):
        boyutlar.clear()
        boyutlarPrice.clear()
        boyutlar.append(boyut)
        boyutlarPrice.append(ortBoy_Price)
        convertList(boyutlar)
        hesaplama = pizMar.get_cost() + sum(boyutlarPrice)
        print(hesaplama)

    print(boyutlar)

  if radio_info == "3":
    label.config(text="Pizza Büyük boy seçildi")
    boyut = "Büyük Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
       if (len(boyutlar)<2):
          boyutlar.clear()
          boyutlarPrice.clear()
          boyutlar.append(boyut)
          boyutlarPrice.append(bykBoy_Price)
          convertList(boyutlar)
          hesaplama = pizMar.get_cost() + sum(boyutlarPrice)
          print(hesaplama)
    print(boyutlar)

def selection_size_classic():
  radio_info = str(radio.get())

  if radio_info == "1":
    label.config(text="Pizza Küçük boy seçildi")
    boyut = "Küçük Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
       if (len(boyutlar)<2):
          boyutlar.clear()
          boyutlarPrice.clear()
          boyutlar.append(boyut)
          convertList(boyutlar)
          boyutlarPrice.append(kckBoy_Price)
          hesaplama = pizCls.get_cost() + sum(boyutlarPrice)
          print(hesaplama)
    print(boyutlar)

  if radio_info == "2":
    label.config(text="Pizza Orta boy seçildi")
    boyut = "Orta Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
      if (len(boyutlar)<2):
        boyutlar.clear()
        boyutlarPrice.clear()
        boyutlar.append(boyut)
        boyutlarPrice.append(ortBoy_Price)
        convertList(boyutlar)
        hesaplama = pizCls.get_cost() + sum(boyutlarPrice)
        print(hesaplama)

    print(boyutlar)

  if radio_info == "3":
    label.config(text="Pizza Büyük boy seçildi")
    boyut = "Büyük Boy"
    if boyut in boyutlar:
       label.config(text="1 kez seçim yapıldı zaten")
    elif (boyut not in boyutlar):
       if (len(boyutlar)<2):
          boyutlar.clear()
          boyutlarPrice.clear()
          boyutlar.append(boyut)
          boyutlarPrice.append(bykBoy_Price)
          convertList(boyutlar)
          hesaplama = pizCls.get_cost() + sum(boyutlarPrice)
          print(hesaplama)
    print(boyutlar)
# Main Fonksiyonumuz
def main():
    Login()
if __name__ == "__main__":
    main()
