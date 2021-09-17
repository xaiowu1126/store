DROP DATABASE IF EXISTS bank;
CREATE DATABASE IF NOT EXISTS bank CHARACTER SET utf8;
USE bank;

DROP TABLE IF EXISTS `person`;
CREATE TABLE `person` (
  `account` INT(8) NOT NULL,
  `username` VARCHAR(20) NOT NULL,
  `password` VARCHAR(40) NOT NULL,
  `country` VARCHAR(40) NOT NULL,
  `province` VARCHAR(40) NOT NULL,
  `street` VARCHAR(40) NOT NULL,
  `door` VARCHAR(40) NOT NULL,
  `money` INT(40) NOT NULL,
  `bank_name` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

LOCK TABLES `person` WRITE;
INSERT INTO `person` VALUES (11110001,'贾生','123456','中国','北京','七马路','001',10,'工商银行起码路分行'),
			    (10000001,'张三','666','中国','河南','紫荆山南路','666',0,'工商银行起码路分行'),
			    (20010001,'旺财','aaa','中国','浙江','文昌路','333',200,'工商银行起码路分行');
UNLOCK TABLES;

SELECT * FROM person;


