-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: springbooto2ehg
-- ------------------------------------------------------
-- Server version	5.7.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `springbooto2ehg`
--

/*!40000 DROP DATABASE IF EXISTS `springbooto2ehg`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `springbooto2ehg` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `springbooto2ehg`;

--
-- Table structure for table `baomingxinxi`
--

DROP TABLE IF EXISTS `baomingxinxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `baomingxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaxiaomingcheng` varchar(200) DEFAULT NULL COMMENT '驾校名称',
  `jiaxiaoleixing` varchar(200) DEFAULT NULL COMMENT '驾校类型',
  `baomingfeiyong` float DEFAULT NULL COMMENT '报名费用',
  `baomingshijian` datetime DEFAULT NULL COMMENT '报名时间',
  `baomingshuoming` varchar(200) DEFAULT NULL COMMENT '报名说明',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  `shhf` longtext COMMENT '审核回复',
  `ispay` varchar(200) DEFAULT '未支付' COMMENT '是否支付',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8 COMMENT='报名信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baomingxinxi`
--

LOCK TABLES `baomingxinxi` WRITE;
/*!40000 ALTER TABLE `baomingxinxi` DISABLE KEYS */;
INSERT INTO `baomingxinxi` VALUES (41,'2022-04-19 16:18:12','驾校名称1','驾校类型1',1,'2022-04-20 00:18:12','报名说明1','账号1','姓名1','是','','未支付'),(42,'2022-04-19 16:18:12','驾校名称2','驾校类型2',2,'2022-04-20 00:18:12','报名说明2','账号2','姓名2','是','','未支付'),(43,'2022-04-19 16:18:12','驾校名称3','驾校类型3',3,'2022-04-20 00:18:12','报名说明3','账号3','姓名3','是','','未支付'),(44,'2022-04-19 16:18:12','驾校名称4','驾校类型4',4,'2022-04-20 00:18:12','报名说明4','账号4','姓名4','是','','未支付'),(45,'2022-04-19 16:18:12','驾校名称5','驾校类型5',5,'2022-04-20 00:18:12','报名说明5','账号5','姓名5','是','','未支付'),(46,'2022-04-19 16:18:12','驾校名称6','驾校类型6',6,'2022-04-20 00:18:12','报名说明6','账号6','姓名6','是','','未支付');
/*!40000 ALTER TABLE `baomingxinxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caiwuxinxi`
--

DROP TABLE IF EXISTS `caiwuxinxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `caiwuxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `zhangdanmingcheng` varchar(200) DEFAULT NULL COMMENT '账单名称',
  `zhangdanleixing` varchar(200) DEFAULT NULL COMMENT '账单类型',
  `zhangdanjine` float DEFAULT NULL COMMENT '账单金额',
  `zhangdanmiaoshu` longtext COMMENT '账单描述',
  `tianjiariqi` date DEFAULT NULL COMMENT '添加日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=167 DEFAULT CHARSET=utf8 COMMENT='财务信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caiwuxinxi`
--

LOCK TABLES `caiwuxinxi` WRITE;
/*!40000 ALTER TABLE `caiwuxinxi` DISABLE KEYS */;
INSERT INTO `caiwuxinxi` VALUES (161,'2022-04-19 16:18:13','账单名称1','开支',1,'账单描述1','2022-04-20'),(162,'2022-04-19 16:18:13','账单名称2','开支',2,'账单描述2','2022-04-20'),(163,'2022-04-19 16:18:13','账单名称3','开支',3,'账单描述3','2022-04-20'),(164,'2022-04-19 16:18:13','账单名称4','开支',4,'账单描述4','2022-04-20'),(165,'2022-04-19 16:18:13','账单名称5','开支',5,'账单描述5','2022-04-20'),(166,'2022-04-19 16:18:13','账单名称6','开支',6,'账单描述6','2022-04-20');
/*!40000 ALTER TABLE `caiwuxinxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cheliangxinxi`
--

DROP TABLE IF EXISTS `cheliangxinxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cheliangxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `chexing` varchar(200) DEFAULT NULL COMMENT '车型',
  `pinpai` varchar(200) DEFAULT NULL COMMENT '品牌',
  `chepaihao` varchar(200) DEFAULT NULL COMMENT '车牌号',
  `shiyongshizhang` varchar(200) DEFAULT NULL COMMENT '使用时长',
  `weixiuxinxi` longtext COMMENT '维修信息',
  `zhaopian` varchar(200) DEFAULT NULL COMMENT '照片',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8 COMMENT='车辆信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cheliangxinxi`
--

LOCK TABLES `cheliangxinxi` WRITE;
/*!40000 ALTER TABLE `cheliangxinxi` DISABLE KEYS */;
INSERT INTO `cheliangxinxi` VALUES (51,'2022-04-19 16:18:12','车型1','品牌1','车牌号1','使用时长1','维修信息1','upload/cheliangxinxi_zhaopian1.jpg'),(52,'2022-04-19 16:18:12','车型2','品牌2','车牌号2','使用时长2','维修信息2','upload/cheliangxinxi_zhaopian2.jpg'),(53,'2022-04-19 16:18:12','车型3','品牌3','车牌号3','使用时长3','维修信息3','upload/cheliangxinxi_zhaopian3.jpg'),(54,'2022-04-19 16:18:12','车型4','品牌4','车牌号4','使用时长4','维修信息4','upload/cheliangxinxi_zhaopian4.jpg'),(55,'2022-04-19 16:18:12','车型5','品牌5','车牌号5','使用时长5','维修信息5','upload/cheliangxinxi_zhaopian5.jpg'),(56,'2022-04-19 16:18:12','车型6','品牌6','车牌号6','使用时长6','维修信息6','upload/cheliangxinxi_zhaopian6.jpg');
/*!40000 ALTER TABLE `cheliangxinxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '配置参数名称',
  `value` varchar(100) DEFAULT NULL COMMENT '配置参数值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='配置文件';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES (1,'picture1','upload/picture1.jpg'),(2,'picture2','upload/picture2.jpg'),(3,'picture3','upload/picture3.jpg');
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discussjiaxiaoxinxi`
--

DROP TABLE IF EXISTS `discussjiaxiaoxinxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discussjiaxiaoxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `refid` bigint(20) NOT NULL COMMENT '关联表id',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `nickname` varchar(200) DEFAULT NULL COMMENT '用户名',
  `content` longtext NOT NULL COMMENT '评论内容',
  `reply` longtext COMMENT '回复内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=257 DEFAULT CHARSET=utf8 COMMENT='驾校信息评论表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussjiaxiaoxinxi`
--

LOCK TABLES `discussjiaxiaoxinxi` WRITE;
/*!40000 ALTER TABLE `discussjiaxiaoxinxi` DISABLE KEYS */;
INSERT INTO `discussjiaxiaoxinxi` VALUES (251,'2022-04-19 16:18:13',1,1,'用户名1','评论内容1','回复内容1'),(252,'2022-04-19 16:18:13',2,2,'用户名2','评论内容2','回复内容2'),(253,'2022-04-19 16:18:13',3,3,'用户名3','评论内容3','回复内容3'),(254,'2022-04-19 16:18:13',4,4,'用户名4','评论内容4','回复内容4'),(255,'2022-04-19 16:18:13',5,5,'用户名5','评论内容5','回复内容5'),(256,'2022-04-19 16:18:13',6,6,'用户名6','评论内容6','回复内容6');
/*!40000 ALTER TABLE `discussjiaxiaoxinxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exampaper`
--

DROP TABLE IF EXISTS `exampaper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exampaper` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `name` varchar(200) NOT NULL COMMENT '练习题库名称',
  `time` int(11) NOT NULL COMMENT '考试时长(分钟)',
  `status` int(11) NOT NULL DEFAULT '0' COMMENT '练习题库状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='练习题库表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exampaper`
--

LOCK TABLES `exampaper` WRITE;
/*!40000 ALTER TABLE `exampaper` DISABLE KEYS */;
INSERT INTO `exampaper` VALUES (1,'2022-04-19 16:18:13','十万个为什么',60,1);
/*!40000 ALTER TABLE `exampaper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examquestion`
--

DROP TABLE IF EXISTS `examquestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `examquestion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `paperid` bigint(20) NOT NULL COMMENT '所属练习题库id（外键）',
  `papername` varchar(200) NOT NULL COMMENT '练习题库名称',
  `questionname` varchar(200) NOT NULL COMMENT '试题名称',
  `options` longtext COMMENT '选项，json字符串',
  `score` bigint(20) DEFAULT '0' COMMENT '分值',
  `answer` varchar(200) DEFAULT NULL COMMENT '正确答案',
  `analysis` longtext COMMENT '答案解析',
  `type` bigint(20) DEFAULT '0' COMMENT '试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空）',
  `sequence` bigint(20) DEFAULT '100' COMMENT '试题排序，值越大排越前面',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='试题表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examquestion`
--

LOCK TABLES `examquestion` WRITE;
/*!40000 ALTER TABLE `examquestion` DISABLE KEYS */;
INSERT INTO `examquestion` VALUES (1,'2022-04-19 16:18:13',1,'十万个为什么','下面动物不属于昆虫的是（）。','[{\"text\":\"A.苍蝇\",\"code\":\"A\"},{\"text\":\"B.蜜蜂\",\"code\":\"B\"},{\"text\":\"C.蜂鸟\",\"code\":\"C\"}]',20,'C','蜂鸟',0,1),(2,'2022-04-19 16:18:13',1,'十万个为什么','油着火后可以用水扑灭。','[{\"text\":\"A.对\",\"code\":\"A\"},{\"text\":\"B.错\",\"code\":\"B\"}]',20,'B','油着火后不可以用水扑灭',2,2),(3,'2022-04-19 16:18:13',1,'十万个为什么','地球是个球体，中间是（ ）。','[]',30,'赤道','赤道',3,3),(4,'2022-04-19 16:18:13',1,'十万个为什么','下面动物中会流汗的有（ ）。','[{\"text\":\"A.马\",\"code\":\"A\"},{\"text\":\"B.猫\",\"code\":\"B\"},{\"text\":\"C.狗\",\"code\":\"C\"}]',30,'A,B','狗不会流汗',1,4);
/*!40000 ALTER TABLE `examquestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examrecord`
--

DROP TABLE IF EXISTS `examrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `examrecord` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `username` varchar(200) DEFAULT NULL COMMENT '用户名',
  `paperid` bigint(20) NOT NULL COMMENT '练习题库id（外键）',
  `papername` varchar(200) NOT NULL COMMENT '练习题库名称',
  `questionid` bigint(20) NOT NULL COMMENT '试题id（外键）',
  `questionname` varchar(200) NOT NULL COMMENT '试题名称',
  `options` longtext COMMENT '选项，json字符串',
  `score` bigint(20) DEFAULT '0' COMMENT '分值',
  `answer` varchar(200) DEFAULT NULL COMMENT '正确答案',
  `analysis` longtext COMMENT '答案解析',
  `myscore` bigint(20) NOT NULL DEFAULT '0' COMMENT '试题得分',
  `myanswer` varchar(200) DEFAULT NULL COMMENT '考生答案',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='考试记录表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examrecord`
--

LOCK TABLES `examrecord` WRITE;
/*!40000 ALTER TABLE `examrecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `examrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum`
--

DROP TABLE IF EXISTS `forum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `title` varchar(200) DEFAULT NULL COMMENT '帖子标题',
  `content` longtext NOT NULL COMMENT '帖子内容',
  `parentid` bigint(20) DEFAULT NULL COMMENT '父节点id',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `username` varchar(200) DEFAULT NULL COMMENT '用户名',
  `isdone` varchar(200) DEFAULT NULL COMMENT '状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=177 DEFAULT CHARSET=utf8 COMMENT='论坛交流';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum`
--

LOCK TABLES `forum` WRITE;
/*!40000 ALTER TABLE `forum` DISABLE KEYS */;
INSERT INTO `forum` VALUES (171,'2022-04-19 16:18:13','帖子标题1','帖子内容1',0,1,'用户名1','开放'),(172,'2022-04-19 16:18:13','帖子标题2','帖子内容2',0,2,'用户名2','开放'),(173,'2022-04-19 16:18:13','帖子标题3','帖子内容3',0,3,'用户名3','开放'),(174,'2022-04-19 16:18:13','帖子标题4','帖子内容4',0,4,'用户名4','开放'),(175,'2022-04-19 16:18:13','帖子标题5','帖子内容5',0,5,'用户名5','开放'),(176,'2022-04-19 16:18:13','帖子标题6','帖子内容6',0,6,'用户名6','开放');
/*!40000 ALTER TABLE `forum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genghuanjiaolian`
--

DROP TABLE IF EXISTS `genghuanjiaolian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genghuanjiaolian` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoliangonghao` varchar(200) DEFAULT NULL COMMENT '教练工号',
  `jiaolianxingming` varchar(200) DEFAULT NULL COMMENT '教练姓名',
  `genghuanjiaolian` varchar(200) DEFAULT NULL COMMENT '更换教练',
  `shenqingshijian` datetime DEFAULT NULL COMMENT '申请时间',
  `genghuanyuanyin` longtext COMMENT '更换原因',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  `shhf` longtext COMMENT '审核回复',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8 COMMENT='更换教练';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genghuanjiaolian`
--

LOCK TABLES `genghuanjiaolian` WRITE;
/*!40000 ALTER TABLE `genghuanjiaolian` DISABLE KEYS */;
INSERT INTO `genghuanjiaolian` VALUES (71,'2022-04-19 16:18:12','教练工号1','教练姓名1','更换教练1','2022-04-20 00:18:12','更换原因1','账号1','姓名1','是',''),(72,'2022-04-19 16:18:12','教练工号2','教练姓名2','更换教练2','2022-04-20 00:18:12','更换原因2','账号2','姓名2','是',''),(73,'2022-04-19 16:18:12','教练工号3','教练姓名3','更换教练3','2022-04-20 00:18:12','更换原因3','账号3','姓名3','是',''),(74,'2022-04-19 16:18:12','教练工号4','教练姓名4','更换教练4','2022-04-20 00:18:12','更换原因4','账号4','姓名4','是',''),(75,'2022-04-19 16:18:12','教练工号5','教练姓名5','更换教练5','2022-04-20 00:18:12','更换原因5','账号5','姓名5','是',''),(76,'2022-04-19 16:18:12','教练工号6','教练姓名6','更换教练6','2022-04-20 00:18:12','更换原因6','账号6','姓名6','是','');
/*!40000 ALTER TABLE `genghuanjiaolian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jiaochexinxi`
--

DROP TABLE IF EXISTS `jiaochexinxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jiaochexinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `pinpai` varchar(200) DEFAULT NULL COMMENT '品牌',
  `chexing` varchar(200) DEFAULT NULL COMMENT '车型',
  `chepaihao` varchar(200) DEFAULT NULL COMMENT '车牌号',
  `jiaocheriqi` date DEFAULT NULL COMMENT '缴车日期',
  `baosunmingxi` longtext COMMENT '报损明细',
  `jiaoliangonghao` varchar(200) DEFAULT NULL COMMENT '教练工号',
  `jiaolianxingming` varchar(200) DEFAULT NULL COMMENT '教练姓名',
  `sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  `shhf` longtext COMMENT '审核回复',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8 COMMENT='缴车信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jiaochexinxi`
--

LOCK TABLES `jiaochexinxi` WRITE;
/*!40000 ALTER TABLE `jiaochexinxi` DISABLE KEYS */;
INSERT INTO `jiaochexinxi` VALUES (141,'2022-04-19 16:18:12','品牌1','车型1','车牌号1','2022-04-20','报损明细1','教练工号1','教练姓名1','是',''),(142,'2022-04-19 16:18:12','品牌2','车型2','车牌号2','2022-04-20','报损明细2','教练工号2','教练姓名2','是',''),(143,'2022-04-19 16:18:12','品牌3','车型3','车牌号3','2022-04-20','报损明细3','教练工号3','教练姓名3','是',''),(144,'2022-04-19 16:18:12','品牌4','车型4','车牌号4','2022-04-20','报损明细4','教练工号4','教练姓名4','是',''),(145,'2022-04-19 16:18:12','品牌5','车型5','车牌号5','2022-04-20','报损明细5','教练工号5','教练姓名5','是',''),(146,'2022-04-19 16:18:13','品牌6','车型6','车牌号6','2022-04-20','报损明细6','教练工号6','教练姓名6','是','');
/*!40000 ALTER TABLE `jiaochexinxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jiaolian`
--

DROP TABLE IF EXISTS `jiaolian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jiaolian` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoliangonghao` varchar(200) NOT NULL COMMENT '教练工号',
  `mima` varchar(200) NOT NULL COMMENT '密码',
  `jiaolianxingming` varchar(200) NOT NULL COMMENT '教练姓名',
  `xingbie` varchar(200) DEFAULT NULL COMMENT '性别',
  `nianling` int(11) DEFAULT NULL COMMENT '年龄',
  `shouji` varchar(200) DEFAULT NULL COMMENT '手机',
  `zhidaokemu` varchar(200) DEFAULT NULL COMMENT '指导科目',
  `touxiang` varchar(200) DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`id`),
  UNIQUE KEY `jiaoliangonghao` (`jiaoliangonghao`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COMMENT='教练';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jiaolian`
--

LOCK TABLES `jiaolian` WRITE;
/*!40000 ALTER TABLE `jiaolian` DISABLE KEYS */;
INSERT INTO `jiaolian` VALUES (21,'2022-04-19 16:18:12','222','222','教练姓名1','男',1,'13823888881','指导科目1','upload/jiaolian_touxiang1.jpg'),(22,'2022-04-19 16:18:12','教练工号2','123456','教练姓名2','男',2,'13823888882','指导科目2','upload/jiaolian_touxiang2.jpg'),(23,'2022-04-19 16:18:12','教练工号3','123456','教练姓名3','男',3,'13823888883','指导科目3','upload/jiaolian_touxiang3.jpg'),(24,'2022-04-19 16:18:12','教练工号4','123456','教练姓名4','男',4,'13823888884','指导科目4','upload/jiaolian_touxiang4.jpg'),(25,'2022-04-19 16:18:12','教练工号5','123456','教练姓名5','男',5,'13823888885','指导科目5','upload/jiaolian_touxiang5.jpg'),(26,'2022-04-19 16:18:12','教练工号6','123456','教练姓名6','男',6,'13823888886','指导科目6','upload/jiaolian_touxiang6.jpg');
/*!40000 ALTER TABLE `jiaolian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jiaolianfenpei`
--

DROP TABLE IF EXISTS `jiaolianfenpei`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jiaolianfenpei` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoliangonghao` varchar(200) DEFAULT NULL COMMENT '教练工号',
  `jiaolianxingming` varchar(200) DEFAULT NULL COMMENT '教练姓名',
  `xingbie` varchar(200) DEFAULT NULL COMMENT '性别',
  `nianling` int(11) DEFAULT NULL COMMENT '年龄',
  `shouji` varchar(200) DEFAULT NULL COMMENT '手机',
  `zhidaokemu` varchar(200) DEFAULT NULL COMMENT '指导科目',
  `fenpeishijian` datetime DEFAULT NULL COMMENT '分配时间',
  `beizhu` varchar(200) DEFAULT NULL COMMENT '备注',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8 COMMENT='教练分配';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jiaolianfenpei`
--

LOCK TABLES `jiaolianfenpei` WRITE;
/*!40000 ALTER TABLE `jiaolianfenpei` DISABLE KEYS */;
INSERT INTO `jiaolianfenpei` VALUES (61,'2022-04-19 16:18:12','教练工号1','教练姓名1','性别1',1,'13823888881','指导科目1','2022-04-20 00:18:12','备注1','账号1','姓名1'),(62,'2022-04-19 16:18:12','教练工号2','教练姓名2','性别2',2,'13823888882','指导科目2','2022-04-20 00:18:12','备注2','账号2','姓名2'),(63,'2022-04-19 16:18:12','教练工号3','教练姓名3','性别3',3,'13823888883','指导科目3','2022-04-20 00:18:12','备注3','账号3','姓名3'),(64,'2022-04-19 16:18:12','教练工号4','教练姓名4','性别4',4,'13823888884','指导科目4','2022-04-20 00:18:12','备注4','账号4','姓名4'),(65,'2022-04-19 16:18:12','教练工号5','教练姓名5','性别5',5,'13823888885','指导科目5','2022-04-20 00:18:12','备注5','账号5','姓名5'),(66,'2022-04-19 16:18:12','教练工号6','教练姓名6','性别6',6,'13823888886','指导科目6','2022-04-20 00:18:12','备注6','账号6','姓名6');
/*!40000 ALTER TABLE `jiaolianfenpei` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jiaxiaoxinxi`
--

DROP TABLE IF EXISTS `jiaxiaoxinxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jiaxiaoxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaxiaomingcheng` varchar(200) DEFAULT NULL COMMENT '驾校名称',
  `jiaxiaoleixing` varchar(200) DEFAULT NULL COMMENT '驾校类型',
  `jiaxiaodizhi` varchar(200) DEFAULT NULL COMMENT '驾校地址',
  `baomingfeiyong` float DEFAULT NULL COMMENT '报名费用',
  `jiaxiaojieshao` longtext COMMENT '驾校介绍',
  `jiaxiaodianhua` varchar(200) DEFAULT NULL COMMENT '驾校电话',
  `jiaxiaotupian` varchar(200) DEFAULT NULL COMMENT '驾校图片',
  `thumbsupnum` int(11) DEFAULT '0' COMMENT '赞',
  `crazilynum` int(11) DEFAULT '0' COMMENT '踩',
  `clicktime` datetime DEFAULT NULL COMMENT '最近点击时间',
  `clicknum` int(11) DEFAULT '0' COMMENT '点击次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='驾校信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jiaxiaoxinxi`
--

LOCK TABLES `jiaxiaoxinxi` WRITE;
/*!40000 ALTER TABLE `jiaxiaoxinxi` DISABLE KEYS */;
INSERT INTO `jiaxiaoxinxi` VALUES (31,'2022-04-19 16:18:12','驾校名称1','驾校类型1','驾校地址1',1,'驾校介绍1','13823888881','upload/jiaxiaoxinxi_jiaxiaotupian1.jpg',1,1,'2022-04-20 00:18:12',1),(32,'2022-04-19 16:18:12','驾校名称2','驾校类型2','驾校地址2',2,'驾校介绍2','13823888882','upload/jiaxiaoxinxi_jiaxiaotupian2.jpg',2,2,'2022-04-20 00:18:12',2),(33,'2022-04-19 16:18:12','驾校名称3','驾校类型3','驾校地址3',3,'驾校介绍3','13823888883','upload/jiaxiaoxinxi_jiaxiaotupian3.jpg',3,3,'2022-04-20 00:18:12',3),(34,'2022-04-19 16:18:12','驾校名称4','驾校类型4','驾校地址4',4,'驾校介绍4','13823888884','upload/jiaxiaoxinxi_jiaxiaotupian4.jpg',4,4,'2022-04-20 00:18:12',4),(35,'2022-04-19 16:18:12','驾校名称5','驾校类型5','驾校地址5',5,'驾校介绍5','13823888885','upload/jiaxiaoxinxi_jiaxiaotupian5.jpg',5,5,'2022-04-20 00:18:12',5),(36,'2022-04-19 16:18:12','驾校名称6','驾校类型6','驾校地址6',6,'驾校介绍6','13823888886','upload/jiaxiaoxinxi_jiaxiaotupian6.jpg',6,6,'2022-04-20 00:18:12',6);
/*!40000 ALTER TABLE `jiaxiaoxinxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kaoqindaka`
--

DROP TABLE IF EXISTS `kaoqindaka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kaoqindaka` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoliangonghao` varchar(200) DEFAULT NULL COMMENT '教练工号',
  `jiaolianxingming` varchar(200) DEFAULT NULL COMMENT '教练姓名',
  `dakaleixing` varchar(200) DEFAULT NULL COMMENT '打卡类型',
  `dakadidian` varchar(200) DEFAULT NULL COMMENT '打卡地点',
  `dakashijian` datetime DEFAULT NULL COMMENT '打卡时间',
  `beizhu` varchar(200) DEFAULT NULL COMMENT '备注',
  `sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  `shhf` longtext COMMENT '审核回复',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8 COMMENT='考勤打卡';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kaoqindaka`
--

LOCK TABLES `kaoqindaka` WRITE;
/*!40000 ALTER TABLE `kaoqindaka` DISABLE KEYS */;
INSERT INTO `kaoqindaka` VALUES (121,'2022-04-19 16:18:12','教练工号1','教练姓名1','上班','打卡地点1','2022-04-20 00:18:12','备注1','是',''),(122,'2022-04-19 16:18:12','教练工号2','教练姓名2','上班','打卡地点2','2022-04-20 00:18:12','备注2','是',''),(123,'2022-04-19 16:18:12','教练工号3','教练姓名3','上班','打卡地点3','2022-04-20 00:18:12','备注3','是',''),(124,'2022-04-19 16:18:12','教练工号4','教练姓名4','上班','打卡地点4','2022-04-20 00:18:12','备注4','是',''),(125,'2022-04-19 16:18:12','教练工号5','教练姓名5','上班','打卡地点5','2022-04-20 00:18:12','备注5','是',''),(126,'2022-04-19 16:18:12','教练工号6','教练姓名6','上班','打卡地点6','2022-04-20 00:18:12','备注6','是','');
/*!40000 ALTER TABLE `kaoqindaka` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kaoshiyuyue`
--

DROP TABLE IF EXISTS `kaoshiyuyue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kaoshiyuyue` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `kaoshikemu` varchar(200) DEFAULT NULL COMMENT '考试科目',
  `kaoshichangci` varchar(200) DEFAULT NULL COMMENT '考试场次',
  `kaoshididian` varchar(200) DEFAULT NULL COMMENT '考试地点',
  `yuyueshijian` datetime DEFAULT NULL COMMENT '预约时间',
  `yuyueshuoming` longtext COMMENT '预约说明',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  `shhf` longtext COMMENT '审核回复',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8 COMMENT='考试预约';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kaoshiyuyue`
--

LOCK TABLES `kaoshiyuyue` WRITE;
/*!40000 ALTER TABLE `kaoshiyuyue` DISABLE KEYS */;
INSERT INTO `kaoshiyuyue` VALUES (111,'2022-04-19 16:18:12','考试科目1','考试场次1','考试地点1','2022-04-20 00:18:12','预约说明1','账号1','姓名1','是',''),(112,'2022-04-19 16:18:12','考试科目2','考试场次2','考试地点2','2022-04-20 00:18:12','预约说明2','账号2','姓名2','是',''),(113,'2022-04-19 16:18:12','考试科目3','考试场次3','考试地点3','2022-04-20 00:18:12','预约说明3','账号3','姓名3','是',''),(114,'2022-04-19 16:18:12','考试科目4','考试场次4','考试地点4','2022-04-20 00:18:12','预约说明4','账号4','姓名4','是',''),(115,'2022-04-19 16:18:12','考试科目5','考试场次5','考试地点5','2022-04-20 00:18:12','预约说明5','账号5','姓名5','是',''),(116,'2022-04-19 16:18:12','考试科目6','考试场次6','考试地点6','2022-04-20 00:18:12','预约说明6','账号6','姓名6','是','');
/*!40000 ALTER TABLE `kaoshiyuyue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kechenganpai`
--

DROP TABLE IF EXISTS `kechenganpai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kechenganpai` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `kechengmingcheng` varchar(200) DEFAULT NULL COMMENT '课程名称',
  `kemuleixing` varchar(200) DEFAULT NULL COMMENT '科目类型',
  `kechengneirong` longtext COMMENT '课程内容',
  `kechengshijian` datetime DEFAULT NULL COMMENT '课程时间',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `jiaoliangonghao` varchar(200) DEFAULT NULL COMMENT '教练工号',
  `jiaolianxingming` varchar(200) DEFAULT NULL COMMENT '教练姓名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8 COMMENT='课程安排';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kechenganpai`
--

LOCK TABLES `kechenganpai` WRITE;
/*!40000 ALTER TABLE `kechenganpai` DISABLE KEYS */;
INSERT INTO `kechenganpai` VALUES (91,'2022-04-19 16:18:12','课程名称1','科目类型1','课程内容1','2022-04-20 00:18:12','账号1','姓名1','教练工号1','教练姓名1'),(92,'2022-04-19 16:18:12','课程名称2','科目类型2','课程内容2','2022-04-20 00:18:12','账号2','姓名2','教练工号2','教练姓名2'),(93,'2022-04-19 16:18:12','课程名称3','科目类型3','课程内容3','2022-04-20 00:18:12','账号3','姓名3','教练工号3','教练姓名3'),(94,'2022-04-19 16:18:12','课程名称4','科目类型4','课程内容4','2022-04-20 00:18:12','账号4','姓名4','教练工号4','教练姓名4'),(95,'2022-04-19 16:18:12','课程名称5','科目类型5','课程内容5','2022-04-20 00:18:12','账号5','姓名5','教练工号5','教练姓名5'),(96,'2022-04-19 16:18:12','课程名称6','科目类型6','课程内容6','2022-04-20 00:18:12','账号6','姓名6','教练工号6','教练姓名6');
/*!40000 ALTER TABLE `kechenganpai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `menujson` longtext COMMENT '菜单',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='菜单';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'2022-04-19 16:18:13','[{\"backMenu\":[{\"child\":[{\"appFrontIcon\":\"cuIcon-rank\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"学员\",\"menuJump\":\"列表\",\"tableName\":\"xueyuan\"}],\"menu\":\"学员管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-brand\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"教练\",\"menuJump\":\"列表\",\"tableName\":\"jiaolian\"}],\"menu\":\"教练管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-discover\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\",\"查看评论\",\"报名\"],\"menu\":\"驾校信息\",\"menuJump\":\"列表\",\"tableName\":\"jiaxiaoxinxi\"}],\"menu\":\"驾校信息管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-copy\",\"buttons\":[\"查看\",\"删除\",\"审核\",\"报表\",\"教练分配\"],\"menu\":\"报名信息\",\"menuJump\":\"列表\",\"tableName\":\"baomingxinxi\"}],\"menu\":\"报名信息管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-similar\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"车辆信息\",\"menuJump\":\"列表\",\"tableName\":\"cheliangxinxi\"}],\"menu\":\"车辆信息管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"查看\",\"修改\",\"删除\"],\"menu\":\"教练分配\",\"menuJump\":\"列表\",\"tableName\":\"jiaolianfenpei\"}],\"menu\":\"教练分配管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-wenzi\",\"buttons\":[\"查看\",\"删除\",\"审核\"],\"menu\":\"更换教练\",\"menuJump\":\"列表\",\"tableName\":\"genghuanjiaolian\"}],\"menu\":\"更换教练管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"查看\",\"删除\"],\"menu\":\"课程安排\",\"menuJump\":\"列表\",\"tableName\":\"kechenganpai\"}],\"menu\":\"课程安排管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-phone\",\"buttons\":[\"查看\",\"删除\"],\"menu\":\"取消课程\",\"menuJump\":\"列表\",\"tableName\":\"quxiaokecheng\"}],\"menu\":\"取消课程管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-link\",\"buttons\":[\"查看\",\"删除\",\"审核\"],\"menu\":\"考试预约\",\"menuJump\":\"列表\",\"tableName\":\"kaoshiyuyue\"}],\"menu\":\"考试预约管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"查看\",\"删除\",\"审核\"],\"menu\":\"考勤打卡\",\"menuJump\":\"列表\",\"tableName\":\"kaoqindaka\"}],\"menu\":\"考勤打卡管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-phone\",\"buttons\":[\"查看\",\"删除\",\"审核\"],\"menu\":\"请假申请\",\"menuJump\":\"列表\",\"tableName\":\"qingjiashenqing\"}],\"menu\":\"请假申请管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"查看\",\"删除\",\"审核\"],\"menu\":\"缴车信息\",\"menuJump\":\"列表\",\"tableName\":\"jiaochexinxi\"}],\"menu\":\"缴车信息管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-pic\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"资源备份\",\"menuJump\":\"列表\",\"tableName\":\"ziyuanbeifen\"}],\"menu\":\"资源备份管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-list\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"财务信息\",\"menuJump\":\"列表\",\"tableName\":\"caiwuxinxi\"}],\"menu\":\"财务信息管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-group\",\"buttons\":[\"查看\",\"修改\",\"删除\"],\"menu\":\"论坛交流\",\"tableName\":\"forum\"}],\"menu\":\"论坛交流\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-copy\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"练习题库管理\",\"tableName\":\"exampaper\"}],\"menu\":\"练习题库管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-message\",\"buttons\":[\"查看\",\"修改\",\"回复\",\"删除\"],\"menu\":\"留言反馈\",\"tableName\":\"messages\"}],\"menu\":\"留言反馈\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-taxi\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"试题管理\",\"tableName\":\"examquestion\"}],\"menu\":\"试题管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-wenzi\",\"buttons\":[\"查看\",\"修改\",\"删除\"],\"menu\":\"轮播图管理\",\"tableName\":\"config\"},{\"appFrontIcon\":\"cuIcon-attentionfavor\",\"buttons\":[\"查看\",\"编辑名称\",\"编辑父级\",\"删除\"],\"menu\":\"菜单列表\",\"tableName\":\"menu\"},{\"appFrontIcon\":\"cuIcon-news\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"新闻公告\",\"tableName\":\"news\"}],\"menu\":\"系统管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-attentionfavor\",\"buttons\":[\"查看\",\"删除\"],\"menu\":\"考试记录\",\"tableName\":\"examrecord\"},{\"appFrontIcon\":\"cuIcon-brand\",\"buttons\":[\"查看\",\"删除\"],\"menu\":\"错题本\",\"tableName\":\"examfailrecord\"}],\"menu\":\"考试管理\"}],\"frontMenu\":[{\"child\":[{\"appFrontIcon\":\"cuIcon-newshot\",\"buttons\":[\"查看\",\"报名\"],\"menu\":\"驾校信息列表\",\"menuJump\":\"列表\",\"tableName\":\"jiaxiaoxinxi\"}],\"menu\":\"驾校信息模块\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-form\",\"buttons\":[\"查看\"],\"menu\":\"车辆信息列表\",\"menuJump\":\"列表\",\"tableName\":\"cheliangxinxi\"}],\"menu\":\"车辆信息模块\"}],\"hasBackLogin\":\"是\",\"hasBackRegister\":\"否\",\"hasFrontLogin\":\"否\",\"hasFrontRegister\":\"否\",\"roleName\":\"管理员\",\"tableName\":\"users\"},{\"backMenu\":[{\"child\":[{\"appFrontIcon\":\"cuIcon-copy\",\"buttons\":[\"查看\",\"支付\"],\"menu\":\"报名信息\",\"menuJump\":\"列表\",\"tableName\":\"baomingxinxi\"}],\"menu\":\"报名信息管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"查看\",\"更换教练\",\"预约练车\"],\"menu\":\"教练分配\",\"menuJump\":\"列表\",\"tableName\":\"jiaolianfenpei\"}],\"menu\":\"教练分配管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-wenzi\",\"buttons\":[\"查看\",\"修改\",\"删除\"],\"menu\":\"更换教练\",\"menuJump\":\"列表\",\"tableName\":\"genghuanjiaolian\"}],\"menu\":\"更换教练管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-vipcard\",\"buttons\":[\"查看\",\"修改\",\"删除\"],\"menu\":\"预约练车\",\"menuJump\":\"列表\",\"tableName\":\"yuyuelianche\"}],\"menu\":\"预约练车管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"查看\",\"取消课程\"],\"menu\":\"课程安排\",\"menuJump\":\"列表\",\"tableName\":\"kechenganpai\"}],\"menu\":\"课程安排管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-phone\",\"buttons\":[\"查看\",\"修改\",\"删除\"],\"menu\":\"取消课程\",\"menuJump\":\"列表\",\"tableName\":\"quxiaokecheng\"}],\"menu\":\"取消课程管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-link\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"考试预约\",\"menuJump\":\"列表\",\"tableName\":\"kaoshiyuyue\"}],\"menu\":\"考试预约管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-baby\",\"buttons\":[\"查看\"],\"menu\":\"练习题库列表\",\"tableName\":\"exampaperlist\"},{\"appFrontIcon\":\"cuIcon-attentionfavor\",\"buttons\":[\"查看\"],\"menu\":\"考试记录\",\"tableName\":\"examrecord\"},{\"appFrontIcon\":\"cuIcon-brand\",\"buttons\":[\"查看\"],\"menu\":\"错题本\",\"tableName\":\"examfailrecord\"}],\"menu\":\"考试管理\"}],\"frontMenu\":[{\"child\":[{\"appFrontIcon\":\"cuIcon-newshot\",\"buttons\":[\"查看\",\"报名\"],\"menu\":\"驾校信息列表\",\"menuJump\":\"列表\",\"tableName\":\"jiaxiaoxinxi\"}],\"menu\":\"驾校信息模块\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-form\",\"buttons\":[\"查看\"],\"menu\":\"车辆信息列表\",\"menuJump\":\"列表\",\"tableName\":\"cheliangxinxi\"}],\"menu\":\"车辆信息模块\"}],\"hasBackLogin\":\"是\",\"hasBackRegister\":\"否\",\"hasFrontLogin\":\"是\",\"hasFrontRegister\":\"是\",\"roleName\":\"学员\",\"tableName\":\"xueyuan\"},{\"backMenu\":[{\"child\":[{\"appFrontIcon\":\"cuIcon-vipcard\",\"buttons\":[\"查看\",\"审核\",\"课程安排\"],\"menu\":\"预约练车\",\"menuJump\":\"列表\",\"tableName\":\"yuyuelianche\"}],\"menu\":\"预约练车管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"查看\",\"修改\",\"删除\"],\"menu\":\"课程安排\",\"menuJump\":\"列表\",\"tableName\":\"kechenganpai\"}],\"menu\":\"课程安排管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-phone\",\"buttons\":[\"查看\",\"审核\"],\"menu\":\"取消课程\",\"menuJump\":\"列表\",\"tableName\":\"quxiaokecheng\"}],\"menu\":\"取消课程管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"考勤打卡\",\"menuJump\":\"列表\",\"tableName\":\"kaoqindaka\"}],\"menu\":\"考勤打卡管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-phone\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"请假申请\",\"menuJump\":\"列表\",\"tableName\":\"qingjiashenqing\"}],\"menu\":\"请假申请管理\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-time\",\"buttons\":[\"新增\",\"查看\",\"修改\",\"删除\"],\"menu\":\"缴车信息\",\"menuJump\":\"列表\",\"tableName\":\"jiaochexinxi\"}],\"menu\":\"缴车信息管理\"}],\"frontMenu\":[{\"child\":[{\"appFrontIcon\":\"cuIcon-newshot\",\"buttons\":[\"查看\",\"报名\"],\"menu\":\"驾校信息列表\",\"menuJump\":\"列表\",\"tableName\":\"jiaxiaoxinxi\"}],\"menu\":\"驾校信息模块\"},{\"child\":[{\"appFrontIcon\":\"cuIcon-form\",\"buttons\":[\"查看\"],\"menu\":\"车辆信息列表\",\"menuJump\":\"列表\",\"tableName\":\"cheliangxinxi\"}],\"menu\":\"车辆信息模块\"}],\"hasBackLogin\":\"是\",\"hasBackRegister\":\"是\",\"hasFrontLogin\":\"否\",\"hasFrontRegister\":\"否\",\"roleName\":\"教练\",\"tableName\":\"jiaolian\"}]');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `userid` bigint(20) NOT NULL COMMENT '留言人id',
  `username` varchar(200) DEFAULT NULL COMMENT '用户名',
  `content` longtext NOT NULL COMMENT '留言内容',
  `cpicture` varchar(200) DEFAULT NULL COMMENT '留言图片',
  `reply` longtext COMMENT '回复内容',
  `rpicture` varchar(200) DEFAULT NULL COMMENT '回复图片',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=237 DEFAULT CHARSET=utf8 COMMENT='留言反馈';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (231,'2022-04-19 16:18:13',1,'用户名1','留言内容1','upload/messages_cpicture1.jpg','回复内容1','upload/messages_rpicture1.jpg'),(232,'2022-04-19 16:18:13',2,'用户名2','留言内容2','upload/messages_cpicture2.jpg','回复内容2','upload/messages_rpicture2.jpg'),(233,'2022-04-19 16:18:13',3,'用户名3','留言内容3','upload/messages_cpicture3.jpg','回复内容3','upload/messages_rpicture3.jpg'),(234,'2022-04-19 16:18:13',4,'用户名4','留言内容4','upload/messages_cpicture4.jpg','回复内容4','upload/messages_rpicture4.jpg'),(235,'2022-04-19 16:18:13',5,'用户名5','留言内容5','upload/messages_cpicture5.jpg','回复内容5','upload/messages_rpicture5.jpg'),(236,'2022-04-19 16:18:13',6,'用户名6','留言内容6','upload/messages_cpicture6.jpg','回复内容6','upload/messages_rpicture6.jpg');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `title` varchar(200) NOT NULL COMMENT '标题',
  `introduction` longtext COMMENT '简介',
  `picture` varchar(200) NOT NULL COMMENT '图片',
  `content` longtext NOT NULL COMMENT '内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=227 DEFAULT CHARSET=utf8 COMMENT='新闻公告';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (221,'2022-04-19 16:18:13','有梦想，就要努力去实现','不管你想要怎样的生活，你都要去努力争取，不多尝试一些事情怎么知道自己适合什么、不适合什么呢?你说你喜欢读书，让我给你列书单，你还问我哪里有那么多时间看书;你说自己梦想的职业是广告文案，问我如何成为一个文案，应该具备哪些素质;你说你计划晨跑，但总是因为学习、工作辛苦或者身体不舒服第二天起不了床;你说你一直梦想一个人去长途旅行，但是没钱，父母觉得危险。','upload/news_picture1.jpg','<p>不管你想要怎样的生活，你都要去努力争取，不多尝试一些事情怎么知道自己适合什么、不适合什么呢?</p><p>你说你喜欢读书，让我给你列书单，你还问我哪里有那么多时间看书;你说自己梦想的职业是广告文案，问我如何成为一个文案，应该具备哪些素质;你说你计划晨跑，但总是因为学习、工作辛苦或者身体不舒服第二天起不了床;你说你一直梦想一个人去长途旅行，但是没钱，父母觉得危险。其实，我已经厌倦了你这样说说而已的把戏，我觉得就算我告诉你如何去做，你也不会照做，因为你根本什么都不做。</p><p>真正有行动力的人不需要别人告诉他如何做，因为他已经在做了。就算碰到问题，他也会自己想办法，自己动手去解决或者主动寻求可以帮助他的人，而不是等着别人为自己解决问题。</p><p>首先要学习独立思考。花一点时间想一下自己喜欢什么，梦想是什么，不要别人说想环游世界，你就说你的梦想是环游世界。</p><p>很多人说现实束缚了自己，其实在这个世界上，我们一直都可以有很多选择，生活的决定权也—直都在自己手上，只是我们缺乏行动力而已。</p><p>如果你觉得安于现状是你想要的，那选择安于现状就会让你幸福和满足;如果你不甘平庸，选择一条改变、进取和奋斗的道路，在这个追求的过程中，你也一样会感到快乐。所谓的成功，即是按照自己想要的生活方式生活。最糟糕的状态，莫过于当你想要选择一条不甘平庸、改变、进取和奋斗的道路时，却以一种安于现状的方式生活，最后抱怨自己没有得到想要的人生。</p><p>因为喜欢，你不是在苦苦坚持，也因为喜欢，你愿意投入时间、精力，长久以往，获得成功就是自然而然的事情。</p>'),(222,'2022-04-19 16:18:13','又是一年毕业季','又是一年毕业季，感慨万千，还记的自己刚进学校那时候的情景，我拖着沉重的行李箱站在偌大的教学楼前面，感叹自己未来的日子即将在这个陌生的校园里度过，而如今斗转星移，浮光掠影，弹指之间，那些青葱岁月如同白驹过隙般悄然从指缝溜走。过去的种种在胸口交集纠结，像打翻的五味瓶，甜蜜，酸楚，苦涩，一并涌上心头。','upload/news_picture2.jpg','<p>又是一年毕业季，感慨万千，还记的自己刚进学校那时候的情景，我拖着沉重的行李箱站在偌大的教学楼前面，感叹自己未来的日子即将在这个陌生的校园里度过，而如今斗转星移，浮光掠影，弹指之间，那些青葱岁月如同白驹过隙般悄然从指缝溜走。</p><p>过去的种种在胸口交集纠结，像打翻的五味瓶，甜蜜，酸楚，苦涩，一并涌上心头。一直都是晚会的忠实参与者，无论是台前还是幕后，忽然间，角色转变，那种感觉确实难以用语言表达。</p><p>	过去的三年，总是默默地期盼着这个好雨时节，因为这时候，会有灿烂的阳光，会有满目的百花争艳，会有香甜的冰激凌，这是个毕业的季节，当时不经世事的我们会殷切地期待学校那一大堆的活动，期待穿上绚丽的演出服或者礼仪服，站在大礼堂镁光灯下尽情挥洒我们的澎拜的激情。</p><p>百感交集，隔岸观火与身临其境的感觉竟是如此不同。从来没想过一场晚会送走的是我们自己的时候会是怎样的感情，毕业就真的意味着结束吗?倔强的我们不愿意承认，谢谢学弟学妹们慷慨的将这次的主题定为“我们在这里”。我知道，这可能是他们对我们这些过来人的尊敬和施舍。</p><p>没有为这场晚会排练、奔波，没有为班级、学生会、文学院出点力，还真有点不习惯，百般无奈中，用“工作忙”个万能的借口来搪塞自己，欺骗别人。其实自己心里明白，那只是在逃避，只是不愿面对繁华落幕后的萧条和落寞。大四了，大家各奔东西，想凑齐班上的人真的是难上加难，敏燕从越南回来，刚落地就匆匆回了学校，那么恋家的人也启程回来了，睿睿学姐也是从家赶来跟我们团圆。大家—如既往的寒暄、打趣、调侃对方，似乎一切又回到了当初的单纯美好。</p><p>看着舞台上活泼可爱的学弟学妹们，如同一群机灵的小精灵，清澈的眼神，稚嫩的肢体，轻快地步伐，用他们那热情洋溢的舞姿渲染着在场的每一个人，我知道，我不应该羡慕嫉妒他们，不应该顾自怜惜逝去的青春，不应该感叹夕阳无限好，曾经，我们也拥有过，曾经，我们也年轻过，曾经，我们也灿烂过。我深深地告诉自己，人生的每个阶段都是美的，年轻有年轻的活力，成熟也有成熟的魅力。多—份稳重、淡然、优雅，也是漫漫时光掠影遗留下的.珍贵赏赐。</p>'),(223,'2022-04-19 16:18:13','挫折路上，坚持常在心间','回头看看，你会不会发现，曾经的你在这里摔倒过;回头看看，你是否发现，一次次地重复着，却从没爬起过。而如今，让我们把视线转向前方，那一道道金色的弧线，是流星飞逝的痕迹，或是成功运行的轨道。今天的你，是否要扬帆起航，让幸福来敲门?清晨的太阳撒向大地，神奇的宇宙赋予它神奇的色彩，大自然沐浴着春光，世界因太阳的照射而精彩，林中百鸟啾啾，河水轻轻流淌，汇成清宁的山间小调。','upload/news_picture3.jpg','<p>回头看看，你会不会发现，曾经的你在这里摔倒过;回头看看，你是否发现，一次次地重复着，却从没爬起过。而如今，让我们把视线转向前方，那一道道金色的弧线，是流星飞逝的痕迹，或是成功运行的轨道。今天的你，是否要扬帆起航，让幸福来敲门?</p><p>清晨的太阳撒向大地，神奇的宇宙赋予它神奇的色彩，大自然沐浴着春光，世界因太阳的照射而精彩，林中百鸟啾啾，河水轻轻流淌，汇成清宁的山间小调。</p><p>是的，面对道途上那无情的嘲讽，面对步伐中那重复的摔跤，面对激流与硬石之间猛烈的碰撞，我们必须选择那富于阴雨，却最终见到彩虹的荆棘路。也许，经历了那暴风雨的洗礼，我们便会变得自信，幸福也随之而来。</p><p>司马迁屡遭羞辱，却依然在狱中撰写《史记》，作为一名史学家，不因王权而极度赞赏，也不因卑微而极度批判，然而他在坚持自己操守的同时，却依然要受统治阶级的阻碍，他似乎无权选择自己的本职。但是，他不顾于此，只是在面对道途的阻隔之时，他依然选择了走下去的信念。终于一部开山巨作《史记》诞生，为后人留下一份馈赠，也许在他完成毕生的杰作之时，他微微地笑了，没有什么比梦想实现更快乐的了......</p><p>	或许正如“长风破浪会有时，直挂云帆济沧海”一般，欣欣然地走向看似深渊的崎岖路，而在一番耕耘之后，便会发现这里另有一番天地。也许这就是困难与快乐的交融。</p><p>也许在形形色色的社会中，我们常能看到一份坚持，一份自信，但这里却还有一类人。这类人在暴风雨来临之际，只会闪躲，从未懂得这也是一种历炼，这何尝不是一份快乐。在阴暗的角落里，总是独自在哭，带着伤愁，看不到一点希望。</p><p>我们不能堕落于此，而要像海燕那般，在苍茫的大海上，高傲地飞翔，任何事物都无法阻挡，任何事都是幸福快乐的。</p>'),(224,'2022-04-19 16:18:13','挫折是另一个生命的开端','当遇到挫折或失败，你是看见失败还是看见机会?挫折是我们每个人成长的必经之路，它不是你想有就有，想没有就没有的。有句名言说的好，如果你想一生摆脱苦难，你就得是神或者是死尸。这句话形象地说明了挫折是伴随着人生的，是谁都逃不掉的。','upload/news_picture4.jpg','<p>当遇到挫折或失败，你是看见失败还是看见机会?</p><p>挫折是我们每个人成长的必经之路，它不是你想有就有，想没有就没有的。有句名言说的好，如果你想一生摆脱苦难，你就得是神或者是死尸。这句话形象地说明了挫折是伴随着人生的，是谁都逃不掉的。</p><p>人生在世，从古到今，不分天子平民，机遇虽有不同，但总不免有身陷困境或遭遇难题之处，这时候唯有通权达变，才能使人转危为安，甚至反败为胜。</p><p>大部分的人，一生当中，最痛苦的经验是失去所爱的人，其次是丢掉一份工作。其实，经得起考验的人，就算是被开除也不会惊慌，要学会面对。</p><p>	“塞翁失马，焉知非福。”人生的道路，并不是每一步都迈向成功，这就是追求的意义。我们还要认识到一点，挫折作为一种情绪状态和一种个人体验，各人的耐受性是大不相同的，有的人经历了一次次挫折，就能够坚忍不拔，百折不挠;有的人稍遇挫折便意志消沉，一蹶不振。所以，挫折感是一种主观感受，因为人的目的和需要不同，成功标准不同，所以同一种活动对于不同的人可能会造成不同的挫折感受。</p><p>凡事皆以平常心来看待，对于生命顺逆不要太执著。能够“破我执”是很高层的人生境界。</p><p>人事的艰难就是一种考验。就像—支剑要有磨刀来磨，剑才会利:一块璞玉要有粗石来磨，才会发出耀眼的光芒。我们能够做到的，只是如何减少、避免那些由于自身的原因所造成的挫折，而在遇到痛苦和挫折之后，则力求化解痛苦，争取幸福。我们要知道，痛苦和挫折是双重性的，它既是我们人生中难以完全避免的，也是我们在争取成功时，不可缺少的一种动力。因为我认为，推动我们奋斗的力量，不仅仅是对成功的渴望，还有为摆脱痛苦和挫折而进行的奋斗。</p>'),(225,'2022-04-19 16:18:13','你要去相信，没有到不了的明天','有梦想就去努力，因为在这一辈子里面，现在不去勇敢的努力，也许就再也没有机会了。你要去相信，一定要相信，没有到不了的明天。不要被命运打败，让自己变得更强大。不管你现在是一个人走在异乡的街道上始终没有找到一丝归属感，还是你在跟朋友们一起吃饭开心址笑着的时候闪过一丝落寞。','upload/news_picture5.jpg','<p>有梦想就去努力，因为在这一辈子里面，现在不去勇敢的努力，也许就再也没有机会了。你要去相信，一定要相信，没有到不了的明天。不要被命运打败，让自己变得更强大。</p><p>不管你现在是一个人走在异乡的街道上始终没有找到一丝归属感，还是你在跟朋友们一起吃饭开心址笑着的时候闪过一丝落寞。</p><p>	不管你现在是在图书馆里背着怎么也看不进去的英语单词，还是你现在迷茫地看不清未来的方向不知道要往哪走。</p><p>不管你现在是在努力着去实现梦想却没能拉近与梦想的距离，还是你已经慢慢地找不到自己的梦想了。</p><p>你都要去相信，没有到不了的明天。</p><p>	有的时候你的梦想太大，别人说你的梦想根本不可能实现;有的时候你的梦想又太小，又有人说你胸无大志;有的时候你对死党说着将来要去环游世界的梦想，却换来他的不屑一顾，于是你再也不提自己的梦想;有的时候你突然说起将来要开个小店的愿望，却发现你讲述的那个人，并没有听到你在说什么。</p><p>不过又能怎么样呢，未来始终是自己的，梦想始终是自己的，没有人会来帮你实现它。</p><p>也许很多时候我们只是需要朋友的一句鼓励，一句安慰，却也得不到。但是相信我，世界上还有很多人，只是想要和你说说话。</p><p>因为我们都一样。一样的被人说成固执，一样的在追逐他们眼里根本不在意的东西。</p><p>所以，又有什么关系呢，别人始终不是你、不能懂你的心情，你又何必多去解释呢。这个世界会来阻止你，困难也会接踵而至，其实真正关键的只有自己，有没有那个倔强。</p><p>这个世界上没有不带伤的人，真正能治愈自己的，只有自己。</p>'),(226,'2022-04-19 16:18:13','离开是一种痛苦，是一种勇气，但同样也是一个考验，是一个新的开端','无穷无尽是离愁，天涯海角遍寻思。当离别在即之时，当面对着相濡以沫兄弟般的朋友时，当面对着经历了四年的磨合而形成的真挚友谊之时，我内心激动无语，说一声再见，道一声珍重都很难出口。回想自己四年大学的风风雨雨，回想我们曾经共同经历的岁月流年，我感谢大家的相扶相依，感谢朋友们的莫大支持与帮助。虽然舍不得，但离别的脚步却不因我们的挚情而停滞。','upload/news_picture6.jpg','<p>无穷无尽是离愁，天涯海角遍寻思。当离别在即之时，当面对着相濡以沫兄弟般的朋友时，当面对着经历了四年的磨合而形成的真挚友谊之时，我内心激动无语，说一声再见，道一声珍重都很难出口。回想自己四年大学的风风雨雨，回想我们曾经共同经历的岁月流年，我感谢大家的相扶相依，感谢朋友们的莫大支持与帮助。虽然舍不得，但离别的脚步却不因我们的挚情而停滞。离别的确是一种痛苦，但同样也是我们走入社会，走向新环境、新领域的一个开端，希望大家在以后新的工作岗位上能够确定自己的新起点，坚持不懈，向着更新、更高的目标前进，因为人生最美好的东西永远都在最前方!</p><p>忆往昔峥嵘岁月，看今朝潮起潮落，望未来任重而道远。作为新时代的我们，就应在失败时，能拼搏奋起，去谱写人生的辉煌。在成功时，亦能居安思危，不沉湎于一时的荣耀、鲜花和掌声中，时时刻刻怀着一颗积极寻找自己新的奶酪的心，处变不惊、成败不渝，始终踏着自己坚实的步伐，从零开始，不断向前迈进，这样才能在这风起云涌、变幻莫测的社会大潮中成为真正的弄潮儿!</p>');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qingjiashenqing`
--

DROP TABLE IF EXISTS `qingjiashenqing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `qingjiashenqing` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoliangonghao` varchar(200) DEFAULT NULL COMMENT '教练工号',
  `jiaolianxingming` varchar(200) DEFAULT NULL COMMENT '教练姓名',
  `qingjiashijian` datetime DEFAULT NULL COMMENT '请假时间',
  `jiezhishijian` datetime DEFAULT NULL COMMENT '截止时间',
  `qingjiashiyou` longtext COMMENT '请假事由',
  `sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  `shhf` longtext COMMENT '审核回复',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8 COMMENT='请假申请';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qingjiashenqing`
--

LOCK TABLES `qingjiashenqing` WRITE;
/*!40000 ALTER TABLE `qingjiashenqing` DISABLE KEYS */;
INSERT INTO `qingjiashenqing` VALUES (131,'2022-04-19 16:18:12','教练工号1','教练姓名1','2022-04-20 00:18:12','2022-04-20 00:18:12','请假事由1','是',''),(132,'2022-04-19 16:18:12','教练工号2','教练姓名2','2022-04-20 00:18:12','2022-04-20 00:18:12','请假事由2','是',''),(133,'2022-04-19 16:18:12','教练工号3','教练姓名3','2022-04-20 00:18:12','2022-04-20 00:18:12','请假事由3','是',''),(134,'2022-04-19 16:18:12','教练工号4','教练姓名4','2022-04-20 00:18:12','2022-04-20 00:18:12','请假事由4','是',''),(135,'2022-04-19 16:18:12','教练工号5','教练姓名5','2022-04-20 00:18:12','2022-04-20 00:18:12','请假事由5','是',''),(136,'2022-04-19 16:18:12','教练工号6','教练姓名6','2022-04-20 00:18:12','2022-04-20 00:18:12','请假事由6','是','');
/*!40000 ALTER TABLE `qingjiashenqing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quxiaokecheng`
--

DROP TABLE IF EXISTS `quxiaokecheng`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quxiaokecheng` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `kechengmingcheng` varchar(200) DEFAULT NULL COMMENT '课程名称',
  `kemuleixing` varchar(200) DEFAULT NULL COMMENT '科目类型',
  `quxiaoshijian` datetime DEFAULT NULL COMMENT '取消时间',
  `quxiaoyuanyin` longtext COMMENT '取消原因',
  `jiaoliangonghao` varchar(200) DEFAULT NULL COMMENT '教练工号',
  `jiaolianxingming` varchar(200) DEFAULT NULL COMMENT '教练姓名',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  `shhf` longtext COMMENT '审核回复',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8 COMMENT='取消课程';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quxiaokecheng`
--

LOCK TABLES `quxiaokecheng` WRITE;
/*!40000 ALTER TABLE `quxiaokecheng` DISABLE KEYS */;
INSERT INTO `quxiaokecheng` VALUES (101,'2022-04-19 16:18:12','课程名称1','科目类型1','2022-04-20 00:18:12','取消原因1','教练工号1','教练姓名1','账号1','姓名1','是',''),(102,'2022-04-19 16:18:12','课程名称2','科目类型2','2022-04-20 00:18:12','取消原因2','教练工号2','教练姓名2','账号2','姓名2','是',''),(103,'2022-04-19 16:18:12','课程名称3','科目类型3','2022-04-20 00:18:12','取消原因3','教练工号3','教练姓名3','账号3','姓名3','是',''),(104,'2022-04-19 16:18:12','课程名称4','科目类型4','2022-04-20 00:18:12','取消原因4','教练工号4','教练姓名4','账号4','姓名4','是',''),(105,'2022-04-19 16:18:12','课程名称5','科目类型5','2022-04-20 00:18:12','取消原因5','教练工号5','教练姓名5','账号5','姓名5','是',''),(106,'2022-04-19 16:18:12','课程名称6','科目类型6','2022-04-20 00:18:12','取消原因6','教练工号6','教练姓名6','账号6','姓名6','是','');
/*!40000 ALTER TABLE `quxiaokecheng` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storeup`
--

DROP TABLE IF EXISTS `storeup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storeup` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `refid` bigint(20) DEFAULT NULL COMMENT '收藏id',
  `tablename` varchar(200) DEFAULT NULL COMMENT '表名',
  `name` varchar(200) NOT NULL COMMENT '收藏名称',
  `picture` varchar(200) NOT NULL COMMENT '收藏图片',
  `type` varchar(200) DEFAULT '1' COMMENT '类型(1:收藏,21:赞,22:踩)',
  `inteltype` varchar(200) DEFAULT NULL COMMENT '推荐类型',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='收藏表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storeup`
--

LOCK TABLES `storeup` WRITE;
/*!40000 ALTER TABLE `storeup` DISABLE KEYS */;
/*!40000 ALTER TABLE `storeup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `tablename` varchar(100) DEFAULT NULL COMMENT '表名',
  `role` varchar(100) DEFAULT NULL COMMENT '角色',
  `token` varchar(200) NOT NULL COMMENT '密码',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  `expiratedtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '过期时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='token表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token`
--

LOCK TABLES `token` WRITE;
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
INSERT INTO `token` VALUES (1,1,'abo','users','管理员','0kg3vyve53w82vfxcsh0rg31ds9anopu','2022-04-19 16:21:56','2022-04-19 17:23:21'),(2,11,'111','xueyuan','学员','b7hr8zzjaqj5mduqczww615vq8h2bous','2022-04-19 16:22:07','2022-04-19 17:22:08'),(3,21,'222','jiaolian','教练','5kz6hm406w83sbx6u28i4h6matl016bb','2022-04-19 16:22:48','2022-04-19 17:22:48');
/*!40000 ALTER TABLE `token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `role` varchar(100) DEFAULT '管理员' COMMENT '角色',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'abo','abo','管理员','2022-04-19 16:18:13');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xueyuan`
--

DROP TABLE IF EXISTS `xueyuan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xueyuan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `zhanghao` varchar(200) NOT NULL COMMENT '账号',
  `mima` varchar(200) NOT NULL COMMENT '密码',
  `xingming` varchar(200) NOT NULL COMMENT '姓名',
  `xingbie` varchar(200) DEFAULT NULL COMMENT '性别',
  `nianling` int(11) DEFAULT NULL COMMENT '年龄',
  `shouji` varchar(200) DEFAULT NULL COMMENT '手机',
  `touxiang` varchar(200) DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`id`),
  UNIQUE KEY `zhanghao` (`zhanghao`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COMMENT='学员';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xueyuan`
--

LOCK TABLES `xueyuan` WRITE;
/*!40000 ALTER TABLE `xueyuan` DISABLE KEYS */;
INSERT INTO `xueyuan` VALUES (11,'2022-04-19 16:18:12','111','111','111','男',1,'13823888881','upload/xueyuan_touxiang1.jpg'),(12,'2022-04-19 16:18:12','账号2','123456','姓名2','男',2,'13823888882','upload/xueyuan_touxiang2.jpg'),(13,'2022-04-19 16:18:12','账号3','123456','姓名3','男',3,'13823888883','upload/xueyuan_touxiang3.jpg'),(14,'2022-04-19 16:18:12','账号4','123456','姓名4','男',4,'13823888884','upload/xueyuan_touxiang4.jpg'),(15,'2022-04-19 16:18:12','账号5','123456','姓名5','男',5,'13823888885','upload/xueyuan_touxiang5.jpg'),(16,'2022-04-19 16:18:12','账号6','123456','姓名6','男',6,'13823888886','upload/xueyuan_touxiang6.jpg');
/*!40000 ALTER TABLE `xueyuan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `yuyuelianche`
--

DROP TABLE IF EXISTS `yuyuelianche`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yuyuelianche` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoliangonghao` varchar(200) DEFAULT NULL COMMENT '教练工号',
  `jiaolianxingming` varchar(200) DEFAULT NULL COMMENT '教练姓名',
  `liancheshijian` datetime DEFAULT NULL COMMENT '练车时间',
  `yuyueshuoming` longtext COMMENT '预约说明',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  `shhf` longtext COMMENT '审核回复',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8 COMMENT='预约练车';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yuyuelianche`
--

LOCK TABLES `yuyuelianche` WRITE;
/*!40000 ALTER TABLE `yuyuelianche` DISABLE KEYS */;
INSERT INTO `yuyuelianche` VALUES (81,'2022-04-19 16:18:12','教练工号1','教练姓名1','2022-04-20 00:18:12','预约说明1','账号1','姓名1','是',''),(82,'2022-04-19 16:18:12','教练工号2','教练姓名2','2022-04-20 00:18:12','预约说明2','账号2','姓名2','是',''),(83,'2022-04-19 16:18:12','教练工号3','教练姓名3','2022-04-20 00:18:12','预约说明3','账号3','姓名3','是',''),(84,'2022-04-19 16:18:12','教练工号4','教练姓名4','2022-04-20 00:18:12','预约说明4','账号4','姓名4','是',''),(85,'2022-04-19 16:18:12','教练工号5','教练姓名5','2022-04-20 00:18:12','预约说明5','账号5','姓名5','是',''),(86,'2022-04-19 16:18:12','教练工号6','教练姓名6','2022-04-20 00:18:12','预约说明6','账号6','姓名6','是','');
/*!40000 ALTER TABLE `yuyuelianche` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ziyuanbeifen`
--

DROP TABLE IF EXISTS `ziyuanbeifen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ziyuanbeifen` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `ziyuanmingcheng` varchar(200) DEFAULT NULL COMMENT '资源名称',
  `ziyuanleixing` varchar(200) DEFAULT NULL COMMENT '资源类型',
  `ziyuanwenjian` varchar(200) DEFAULT NULL COMMENT '资源文件',
  `ziyuanjianjie` longtext COMMENT '资源简介',
  `beifenshijian` date DEFAULT NULL COMMENT '备份时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8 COMMENT='资源备份';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ziyuanbeifen`
--

LOCK TABLES `ziyuanbeifen` WRITE;
/*!40000 ALTER TABLE `ziyuanbeifen` DISABLE KEYS */;
INSERT INTO `ziyuanbeifen` VALUES (151,'2022-04-19 16:18:13','资源名称1','资源类型1','','资源简介1','2022-04-20'),(152,'2022-04-19 16:18:13','资源名称2','资源类型2','','资源简介2','2022-04-20'),(153,'2022-04-19 16:18:13','资源名称3','资源类型3','','资源简介3','2022-04-20'),(154,'2022-04-19 16:18:13','资源名称4','资源类型4','','资源简介4','2022-04-20'),(155,'2022-04-19 16:18:13','资源名称5','资源类型5','','资源简介5','2022-04-20'),(156,'2022-04-19 16:18:13','资源名称6','资源类型6','','资源简介6','2022-04-20');
/*!40000 ALTER TABLE `ziyuanbeifen` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-20 11:30:47
