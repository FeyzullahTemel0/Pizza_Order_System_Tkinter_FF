

1) Dosya içerisinde yer alan mysql bağlanıtısı için user ve password değiştirilmelidir.

2) Database'in aynısını oluşturabilmek için yeni bir şema oluşturup o şema içerisinde yeni query açarak
   query içerisine bu kodları yapıştırın. Şema isminizin 'projeglobalaıhub' olmasına dikkat edin!!!

3) vs Code kullanıyorsanız pymysql kütüphanesini pip install pymysql şeklinde indirmeyi unutmayın!!!

CREATE TABLE `ordersystem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `credit_card_username` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `userid` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `order_description` varchar(100) NOT NULL,
  `order_time` datetime NOT NULL,
  `credit_card_number` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit_card_last_time` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `cvv` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit_cadt_password` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    
    -----------------------------------------------------------------------------------------------------------
    
*** Mysql sütun düzenleme kodları

SELECT id as 'ID',
credit_card_username as 'Kart Sahibi',
userid as 'TC Kimlik',
order_description as 'Sipariş Bilgisi',
order_time as 'Sipariş Zamanı',
credit_card_number as 'KK Numarası',
credit_card_last_time as 'KK Son Geçerlilik Tarihi',
cvv as 'CVV',
credit_cadt_password as 'Kart Şifresi'
FROM projeglobalaıhub.ordersystem;

    
