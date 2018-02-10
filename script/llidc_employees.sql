/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 100113
Source Host           : localhost:3306
Source Database       : llidc

Target Server Type    : MYSQL
Target Server Version : 100113
File Encoding         : 65001

Date: 2017-07-31 15:45:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for llidc_employees
-- ----------------------------
DROP TABLE IF EXISTS `llidc_employees`;
CREATE TABLE `llidc_employees` (
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_acc` varchar(255) NOT NULL DEFAULT '' COMMENT 'user account',
  `u_name` varchar(255) NOT NULL COMMENT '用户名称',
  `u_pwd` varchar(255) NOT NULL COMMENT '用户密码',
  `u_dept` varchar(255) DEFAULT NULL COMMENT '用户所属部门 ',
  `u_type` int(1) DEFAULT NULL COMMENT '用户的类型,1业务员，2网维，3财务，4管理员，5总经理',
  `u_mobile` varchar(255) DEFAULT NULL COMMENT '用户手机号',
  `u_qq` varchar(255) DEFAULT NULL COMMENT '用户QQ账号',
  `u_regtime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`u_id`),
  UNIQUE KEY `user` (`u_name`,`u_mobile`,`u_qq`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of llidc_employees
-- ----------------------------
INSERT INTO `llidc_employees` VALUES ('1', 'admin', '管理员', '7e0900feefd3ef9942db8e6690a1fe0e', null, '5', '13423426724', null, '2017-07-27 20:49:38');
INSERT INTO `llidc_employees` VALUES ('2', 'lfc', '李富城', '7e5f35195b61e5ae875136a60f4cfb80', null, '3', '', null, '2017-07-31 10:45:00');
INSERT INTO `llidc_employees` VALUES ('3', 'ywd', '袁伟东', '33515595b8e183d200dd2db4a4c4814d', null, '2', '', null, '2017-07-30 21:16:34');
INSERT INTO `llidc_employees` VALUES ('4', 'yfh', '杨丰华', '6f09260ef62fb17f9336f8c7524b81da', null, '2', '', null, '2017-07-30 21:16:34');
INSERT INTO `llidc_employees` VALUES ('18', 'llidc-vU', '劳兴华', '0f188acd5e71d356dc9d5f8ab5a33f65', null, '3', null, null, '2017-07-31 10:44:57');
INSERT INTO `llidc_employees` VALUES ('19', 'llidc-Me', '陶秋梅', '37707d8f9a43fff98abf298449c2d577', null, '1', null, null, '2017-07-27 20:21:31');
INSERT INTO `llidc_employees` VALUES ('20', 'llidc-xz', '唐晓珍', 'cef666cfd76f5894cbb72a29d3ef98e4', null, '1', null, null, '2017-07-27 20:14:19');
INSERT INTO `llidc_employees` VALUES ('21', 'llidc-xe', '黄小恩', '48831b3b44fb858d82e6073e5df20166', null, '1', null, null, '2017-07-27 20:14:16');
INSERT INTO `llidc_employees` VALUES ('22', 'llidc-lc', '廖超', '35ca2b598722539c2c491999f0d75406', null, '1', null, null, '2017-07-27 20:14:13');
INSERT INTO `llidc_employees` VALUES ('23', 'bjl', '闭健龙', '6531bd0e4f6d08ed22cbbcc9af467e19', null, '4', '', null, '2017-07-31 10:45:09');
INSERT INTO `llidc_employees` VALUES ('25', 'ky', '可艳', '31ebc91d47ee21224f1eff0b8ce4e443', null, '4', '', null, '2017-07-31 10:45:12');
