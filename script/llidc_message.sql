/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 100113
Source Host           : localhost:3306
Source Database       : llidc

Target Server Type    : MYSQL
Target Server Version : 100113
File Encoding         : 65001

Date: 2017-08-21 08:41:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for llidc_message
-- ----------------------------
DROP TABLE IF EXISTS `llidc_message`;
CREATE TABLE `llidc_message` (
  `m_id` int(11) NOT NULL AUTO_INCREMENT,
  `m_phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'client mobile',
  `m_ip` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'client''s ip',
  `m_ua` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'user agent',
  `m_cpath` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'visiting path',
  `m_dt` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of llidc_message
-- ----------------------------
INSERT INTO `llidc_message` VALUES ('1', '13423426724', '::1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36', '/client/getcc/?phone=13423426724', '2017-08-20 17:33:42');
INSERT INTO `llidc_message` VALUES ('2', '13423426724', '::1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36', '/client/getcc/?phone=13423426724', '2017-08-20 17:37:37');
