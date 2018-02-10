/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 100113
Source Host           : localhost:3306
Source Database       : llidc

Target Server Type    : MYSQL
Target Server Version : 100113
File Encoding         : 65001

Date: 2017-07-21 10:10:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for llidc_log
-- ----------------------------
DROP TABLE IF EXISTS `llidc_log`;
CREATE TABLE `llidc_log` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_path` varchar(255) DEFAULT NULL COMMENT 'visiting path',
  `l_visiter` varchar(255) DEFAULT NULL COMMENT 'visiter''s name',
  `l_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`l_id`),
  KEY `log` (`l_path`,`l_visiter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of llidc_log
-- ----------------------------
