CREATE DATABASE  IF NOT EXISTS `Env` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Env`;
-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: Env
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobileno` varchar(15) DEFAULT NULL,
  `photo` varchar(500) DEFAULT 'NA',
  `usertype` int DEFAULT '0',
  `userpassword` varchar(255) DEFAULT NULL,
  `userstatus` int DEFAULT '1',
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Prem','prem@shunyaekai.tech','8929393887','NA',0,'$2a$10$CG3oXG9bXB3KqHTw7O0wSeTVnOs7.cvmPDTqUB/JBfINRd5G/EQOe',1,'2022-12-08 07:00:46'),(2,'Sukarn','sukarn@shunyaekai.tech','8929393886','NA',0,'$2a$10$lmzyvF5vBbERjrE8C4YXTuGby.l6yX1OZzF7YRp6X4J0mYVRi3oeG',1,'2022-12-08 07:19:30');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `AreaName` varchar(255) NOT NULL,
  `AreaNumber` varchar(255) NOT NULL,
  `shapetype` varchar(255) NOT NULL,
  `lat` varchar(255) NOT NULL,
  `lng` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `redius` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES (71,'1','Delhi','552356194','circle','28.670847568616374','77.17054785156252',1,'2022-12-16 04:23:30','2022-12-16 04:23:30','12144.546940015456'),(72,'1','Agra','867539400','circle','27.18577242748145','77.96156347656252',1,'2022-12-16 04:25:26','2022-12-16 04:25:26','13235.89094419321'),(73,'1','Aligarh','868119192','polygon','28.036252228527463','77.98654543246191',1,'2022-12-16 04:26:05','2022-12-16 04:26:05','0'),(74,'1','Aligarh','868119192','polygon','28.036252228527463','78.38205324496191',1,'2022-12-16 04:26:05','2022-12-16 04:26:05','0'),(75,'1','Aligarh','868119192','polygon','27.900407458139235','78.16232668246191',1,'2022-12-16 04:26:05','2022-12-16 04:26:05','0'),(76,'1','Aligarh','868119192','polygon','27.919824320802434','78.06344972933691',1,'2022-12-16 04:26:05','2022-12-16 04:26:05','0'),(77,'1','Gurugram','840699384','circle','28.464077105716928','77.00712622070314',1,'2022-12-19 07:54:48','2022-12-19 07:54:48','13880.096180133158'),(78,'1','Muradabad','901681269','circle','28.998069921363463','78.66468847656252',1,'2022-12-19 07:58:01','2022-12-19 07:58:01','27765.183220727777'),(79,'1','Jaipur','463821383','circle','27.21508657440822','75.57203710937502',1,'2022-12-19 13:34:30','2022-12-19 13:34:30','61926.992308812376'),(80,'1','Farrukhabad','844697554','polygon','28.699761473433266','79.17005957031252',1,'2022-12-26 04:37:55','2022-12-26 04:37:55','0'),(81,'1','Farrukhabad','844697554','polygon','28.216824415500625','80.63124121093752',1,'2022-12-26 04:37:55','2022-12-26 04:37:55','0'),(82,'1','Farrukhabad','844697554','polygon','27.48831269137619','79.48866308593752',1,'2022-12-26 04:37:55','2022-12-26 04:37:55','0'),(83,'1','Farrukhabad','844697554','polygon','27.97453156107905','78.18129003906252',1,'2022-12-26 04:37:55','2022-12-26 04:37:55','0'),(84,'1','Farrukhabad','844697554','polygon','28.274893194659494','78.55482519531252',1,'2022-12-26 04:37:55','2022-12-26 04:37:55','0'),(85,'1','Farrukhabad','844697554','polygon','27.906591685519786','79.41175878906252',1,'2022-12-26 04:37:55','2022-12-26 04:37:55','0'),(86,'1','Farrukhabad','844697554','polygon','28.236184187953224','79.86219824218752',1,'2022-12-26 04:37:55','2022-12-26 04:37:55','0'),(87,'1','Farrukhabad','844697554','polygon','28.487541048658017','78.91737402343752',1,'2022-12-26 04:37:55','2022-12-26 04:37:55','0'),(88,'1','Haryana Gurgaon','931481908','circle','29.353889103834057','75.49513281250002',1,'2022-12-27 05:14:23','2022-12-27 05:14:23','125002.03975165976'),(89,'1','sirsa','253978986','circle','29.659852170135515','75.00074804687502',1,'2022-12-27 05:19:34','2022-12-27 05:19:34','27116.844715838015'),(90,'1','Punjab','434583875','circle','30.458576961895844','74.63819921875002',1,'2022-12-27 05:19:37','2022-12-27 05:19:37','112871.90982655257'),(91,'1','sikar','758957688','circle','27.78121566567444','75.13258398437502',1,'2022-12-27 05:22:41','2022-12-27 05:22:41','23169.73535041234'),(92,'1','Delhi','399080175','circle','28.691027906307717','77.21998632812502',1,'2022-12-27 05:55:10','2022-12-27 05:55:10','40218.621490561534'),(93,'1','New Delhiiii','332523282','circle','28.998970764797935','76.69264257812502',1,'2022-12-27 08:56:07','2022-12-27 08:56:07','93127.18507409784'),(94,'1','new Delhi','646785749','circle','28.169317607730363','76.92335546875002',1,'2022-12-27 12:25:01','2022-12-27 12:25:01','37059.27173459816');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `devicetable`
--

DROP TABLE IF EXISTS `devicetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `devicetable` (
  `id` int NOT NULL AUTO_INCREMENT,
  `devicename` varchar(100) DEFAULT NULL,
  `deviceid` varchar(100) DEFAULT NULL,
  `userid` varchar(100) DEFAULT NULL,
  `latitude` varchar(45) DEFAULT NULL,
  `longitude` varchar(45) DEFAULT NULL,
  `areaid` varchar(45) DEFAULT NULL,
  `temperature` varchar(45) DEFAULT '0',
  `humidity` varchar(45) DEFAULT '0',
  `moisture` varchar(45) DEFAULT '0',
  `fire` varchar(45) DEFAULT '0',
  `alerttemp` varchar(45) DEFAULT '0',
  `alerthumi` varchar(45) DEFAULT '0',
  `alertmoisture` varchar(45) DEFAULT '0',
  `alerttypetemp` int DEFAULT '0',
  `alerttypehumi` int DEFAULT '0',
  `alerttypemoisture` int DEFAULT '0',
  `devicestatus` int DEFAULT '0',
  `createdat` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `count_temp` int DEFAULT '0',
  `count_humi` int DEFAULT '0',
  `count_moist` int DEFAULT '0',
  `count_fire` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `deviceid_UNIQUE` (`deviceid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devicetable`
--

LOCK TABLES `devicetable` WRITE;
/*!40000 ALTER TABLE `devicetable` DISABLE KEYS */;
INSERT INTO `devicetable` VALUES (1,'1001','1001','1','28.691027906307717','77.21998632812502','DT001','10','40','10','0','36.0','26','20',1,1,0,0,'2022-12-12 05:02:51','2022-12-29 05:07:54',1,1,0,0),(6,'1002','1002','1','27.21508657440822','75.57203710937502','463821383','0','0','0','0','0','0','0',0,0,0,0,'2022-12-26 11:25:52','2022-12-29 07:04:18',0,0,0,0),(7,'DT003','1003','1','27.019513551703806','75.38526953125002','463821383','0','0','0','0','0','0','0',0,0,0,1,'2022-12-26 11:26:26','2022-12-27 06:23:03',0,0,0,0),(8,'DT004','1004','1','27.019513551703806','75.38526953125002','463821383','0','0','0','0','0','0','0',0,0,0,0,'2022-12-26 11:26:31','2022-12-26 11:27:51',0,0,0,0),(9,'DT1006','1006','1','27.23462505556147','75.76979101562502','463821383','0','0','0','0','0','0','0',0,0,0,0,'2022-12-26 11:50:18','2022-12-26 11:50:18',0,0,0,0),(10,'DT1007','1007','1','28.998069921363463','78.66468847656252','901681269','0','0','0','0','0','0','0',0,0,0,0,'2022-12-26 12:19:15','2022-12-26 12:19:15',0,0,0,0),(11,'DT1009','1009','1','28.54636658221505','77.38478125000002','399080175','0','0','0','0','0','0','0',0,0,0,0,'2022-12-27 12:23:51','2022-12-27 12:23:51',0,0,0,0);
/*!40000 ALTER TABLE `devicetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history_table`
--

DROP TABLE IF EXISTS `history_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(100) DEFAULT NULL,
  `deviceid` varchar(100) DEFAULT NULL,
  `devicename` varchar(100) DEFAULT NULL,
  `temperature` varchar(45) DEFAULT NULL,
  `humidity` varchar(45) DEFAULT NULL,
  `moisture` varchar(45) DEFAULT NULL,
  `fire` varchar(45) DEFAULT NULL,
  `alertTemp` int DEFAULT '0',
  `alertHumi` int DEFAULT '0',
  `alertMoist` int DEFAULT '0',
  `createdat` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history_table`
--

LOCK TABLES `history_table` WRITE;
/*!40000 ALTER TABLE `history_table` DISABLE KEYS */;
INSERT INTO `history_table` VALUES (42,'1','1001','DT001','18.0','15','22','0',1,0,0,'2022-12-19 05:44:19','2022-12-21 06:02:51'),(43,'1','1001','DT001','39.0','35','22','0',1,0,0,'2022-12-19 05:45:09','2022-12-19 05:45:09'),(44,'1','1001','DT001','39.0','35','22','0',0,1,0,'2022-12-19 05:45:10','2022-12-19 05:45:10'),(45,'1','1001','DT001','39.0','35','10','0',0,0,1,'2022-12-19 05:49:20','2022-12-19 05:49:20'),(46,'1','1001','DT001','39.0','35','30','0',0,0,0,'2022-12-19 05:49:47','2022-12-19 05:49:47'),(47,'1','1001','DT001','30.0','15','30','0',0,0,0,'2022-12-19 05:50:49','2022-12-19 05:50:49'),(48,'1','1001','DT001','30.0','15','30','0',0,0,0,'2022-12-19 05:50:49','2022-12-19 05:50:49'),(49,'1','1001','DT001','30.0','15','30','1',0,0,0,'2022-12-19 05:56:47','2022-12-19 05:56:47'),(52,'1','1001','DT001','30.0','15','30','0',0,0,0,'2022-12-19 06:00:08','2022-12-19 06:00:08'),(53,'1','1001','DT001','39.0','35','20','1',1,0,0,'2022-12-19 06:01:07','2022-12-19 06:01:07'),(54,'1','1001','DT001','39.0','35','20','1',0,1,0,'2022-12-19 06:01:08','2022-12-19 06:01:08'),(55,'1','1001','DT001','39.0','35','20','1',0,0,1,'2022-12-19 06:01:08','2022-12-19 06:01:08'),(56,'1','1001','DT001','39.0','35','20','1',0,0,0,'2022-12-19 06:01:08','2022-12-19 06:01:08'),(57,'1','1001','DT001','20.0','16','30','0',0,0,0,'2022-12-19 06:03:04','2022-12-19 06:03:04'),(58,'1','1001','DT001','20.0','16','30','0',0,0,0,'2022-12-19 06:03:04','2022-12-19 06:03:04'),(59,'1','1001','DT001','20.0','16','30','0',0,0,0,'2022-12-19 06:03:04','2022-12-19 06:03:04'),(60,'1','1001','DT001','20.0','16','30','0',1,0,0,'2022-12-19 06:03:04','2022-12-21 06:03:28'),(61,'1','1001','DT001','50.0','10','80','0',1,0,0,'2022-12-26 09:14:30','2022-12-26 09:14:30'),(62,'1','1001','DT001','18.0','10','80','0',0,0,0,'2022-12-26 09:36:30','2022-12-26 09:36:30'),(63,'1','1001','DT001','45.0','10','80','0',1,0,0,'2022-12-26 09:36:55','2022-12-26 09:36:55'),(64,'1','1001','DT001','90','40','10','0',0,1,0,'2022-12-26 10:20:29','2022-12-28 06:29:20');
/*!40000 ALTER TABLE `history_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-05 13:23:03
