Mysql Tablolarını oluşturmak için öncelikle kodlardaki bağlantı kısımlarının değiştirilmesi gerekmektedir.

Database ismini projeglobalaıhub olarak yapabilir veyahut kendi database isminizi girebilirsiniz.

Register Tablosu için;

CREATE TABLE `dbregister` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name_surname` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `email` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `phone` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `sifre` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


--------------------------------------------------------------

Order System Tablosu için ;

CREATE TABLE `ordersystemtk` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `card_name_surname` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `order_description` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `order_time` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit_card_number` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit_crat_last_date` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit_card_cvv` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit_card_password` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


şeklinde kodlarınızı yeni querylere yazıp çalıştırınız.

Gerekli bağlantıları yaptıktan sonra proje sorunsuz çalışacaktır.