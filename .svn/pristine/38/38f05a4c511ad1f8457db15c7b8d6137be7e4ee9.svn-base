/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 100113
Source Host           : localhost:3306
Source Database       : llidc

Target Server Type    : MYSQL
Target Server Version : 100113
File Encoding         : 65001

Date: 2017-08-24 15:24:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for llidc_clients
-- ----------------------------
DROP TABLE IF EXISTS `llidc_clients`;
CREATE TABLE `llidc_clients` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_acc` varchar(255) DEFAULT NULL COMMENT 'client''s account',
  `c_name` varchar(255) DEFAULT NULL COMMENT 'client''s name',
  `c_real_name` varchar(255) DEFAULT NULL COMMENT 'client''s realname',
  `c_pwd` varchar(255) DEFAULT NULL COMMENT 'client''s password',
  `c_mobile` varchar(255) NOT NULL COMMENT 'client''s mobile',
  `c_balance` varchar(255) DEFAULT NULL COMMENT 'client''s balance',
  `c_id_card` varchar(255) DEFAULT NULL COMMENT 'which sales this client belongs to',
  `c_belongsto` varchar(255) DEFAULT NULL COMMENT 'client''s id card number',
  `c_address` varchar(255) DEFAULT NULL COMMENT 'client''s address',
  `c_qq` varchar(255) DEFAULT NULL COMMENT 'client''s qq number',
  `c_memo` varchar(255) DEFAULT NULL COMMENT 'client''s memo details',
  `c_regdt` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`c_id`,`c_mobile`),
  KEY `client` (`c_name`,`c_mobile`,`c_belongsto`,`c_qq`)
) ENGINE=InnoDB AUTO_INCREMENT=772 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of llidc_clients
-- ----------------------------
INSERT INTO `llidc_clients` VALUES ('495', '654213', '190201008', '网飞支付', 'c33367701511b4f6020ec61ded352059', '', null, '330821198301111000', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('496', '654214', '46489009', '黄金裁决', 'c33367701511b4f6020ec61ded352059', '', null, '450731198910213000', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('497', '654215', '54327907', '54327907', 'c33367701511b4f6020ec61ded352059', '', null, '230722197902219000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('498', '654216', '286268084', '雷生', 'c33367701511b4f6020ec61ded352059', '', null, '455533198910201000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('499', '654217', '天诚', '天诚', 'c33367701511b4f6020ec61ded352059', '', null, '13070119911113033X', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('500', '654218', '15415010', '180毁灭精品火龙', 'c33367701511b4f6020ec61ded352059', '', null, '450804197610111000', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('501', '654219', '530220018', '灰太狼', 'c33367701511b4f6020ec61ded352059', '', null, '455553199105204000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('502', '654220', '2693260783', '共和国', 'c33367701511b4f6020ec61ded352059', '', null, '612415198903221000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('503', '654221', '179636555', '網絡尐蟲', 'c33367701511b4f6020ec61ded352059', '', null, '641214198701023000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('504', '654222', '413080704', '我的清高 敌不过你的风骚', 'c33367701511b4f6020ec61ded352059', '', null, '420529198808292000', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('505', '654223', 'fb0915', '梁杰伟', 'c33367701511b4f6020ec61ded352059', '', null, '612501198606270000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('506', '654224', '圣斗士', '圣斗士', 'c33367701511b4f6020ec61ded352059', '', null, '650106197908228000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('507', '654225', '974005914', '914F嘟嘟传奇', 'c33367701511b4f6020ec61ded352059', '', null, '500222198503128000', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('508', '654226', '170514030', '新起点', 'c33367701511b4f6020ec61ded352059', '', null, '32068419861130366X', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('509', '654227', '89342668', '郝生', 'c33367701511b4f6020ec61ded352059', '', null, '453332198610201024', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('510', '654228', '易信科技', '易信科技', 'c33367701511b4f6020ec61ded352059', '', null, '411525197503041024', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('511', '654229', '唯心数据小乐', '唯心数据小乐', 'c33367701511b4f6020ec61ded352059', '', null, '441800198811027968', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('512', '654230', '623100077', '火', 'c33367701511b4f6020ec61ded352059', '', null, '453332199102014976', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('513', '654231', '76787530', '老根儿', 'c33367701511b4f6020ec61ded352059', '', null, '455531198909064000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('514', '654232', '409645901', '早睡晚起', 'c33367701511b4f6020ec61ded352059', '', null, '410503195811281024', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('515', '654233', '289926888', '289926888', 'c33367701511b4f6020ec61ded352059', '', null, '511501198410212992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('516', '654234', '421330345', '九游雷', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002110976', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('517', '654235', '3177553956', '绝剑客服', 'c33367701511b4f6020ec61ded352059', '', null, '433325199101062016', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('518', '654236', '492750974', '沉默的熊', 'c33367701511b4f6020ec61ded352059', '', null, '350425196703033024', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('519', '654237', '3332171', '無与倫比', 'c33367701511b4f6020ec61ded352059', '', null, '422243198708073984', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('520', '654238', '584435821', '叶无道。', 'c33367701511b4f6020ec61ded352059', '', null, '652929201202194048', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('521', '654239', '2121326', 'root', 'c33367701511b4f6020ec61ded352059', '', null, '522627200310102016', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('522', '654240', '77795852', 'Daren', 'c33367701511b4f6020ec61ded352059', '', null, '230902199012224000', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('523', '654241', '小太阳', '小太阳', 'c33367701511b4f6020ec61ded352059', '', null, '51152519771014703X', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('524', '654242', '546337338', '湛江IDC(杰)', 'c33367701511b4f6020ec61ded352059', '', null, '450721199203212032', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('525', '654243', '120354103', 'Jason', 'c33367701511b4f6020ec61ded352059', '', null, '450731198512313984', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('526', '654244', '569781250', '伊人', 'c33367701511b4f6020ec61ded352059', '', null, '422223199212120000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('527', '654245', '258961893', '笑看人生', 'c33367701511b4f6020ec61ded352059', '', null, '360281199204062976', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('528', '654246', '370846935', '王佳宁', 'c33367701511b4f6020ec61ded352059', '', null, '612414199001142016', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('529', '654247', '3391385608', '好不容易', 'c33367701511b4f6020ec61ded352059', '', null, '455553199105064000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('530', '654248', '426404', '一笑哥', 'c33367701511b4f6020ec61ded352059', '', null, '453332199010201024', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('531', '654249', '133145207', '张完', 'c33367701511b4f6020ec61ded352059', '', null, '652223198908071936', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('532', '654250', '123410174', '哈尼', 'c33367701511b4f6020ec61ded352059', '', null, '612415198902114944', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('533', '654251', '3529541681', '帝欣', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002112000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('534', '654252', '3491792310', 'fakjfaj', 'c33367701511b4f6020ec61ded352059', '', null, '320681199209028992', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('535', '654253', '光头强', '光头强', 'c33367701511b4f6020ec61ded352059', '', null, '320106198703076992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('536', '654254', '799000515', 'Perfect-小柒', 'c33367701511b4f6020ec61ded352059', '', null, '330723197708051968', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('537', '654255', '602069172', '中山市宏达包装材料有限公司', 'c33367701511b4f6020ec61ded352059', '', null, '222401198407094016', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('538', '654256', '654298', 'hyqs', 'c33367701511b4f6020ec61ded352059', '', null, '422223199202033984', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('539', '654257', '4578955', 'Andy', 'c33367701511b4f6020ec61ded352059', '', null, '465552199108041984', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('540', '654258', '腾亿网络', '腾亿网络', 'c33367701511b4f6020ec61ded352059', '', null, '310110198909070016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('541', '654259', '1076611010', '美博互联', 'c33367701511b4f6020ec61ded352059', '', null, '140502197311051008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('542', '654260', '1149873216', '囩淡Ψ颩轻', 'c33367701511b4f6020ec61ded352059', '', null, '465552198908091008', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('543', '654261', '468593', '搜网张', 'c33367701511b4f6020ec61ded352059', '', null, '612415198502210944', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('544', '654262', '315894725', 'QY技术', 'c33367701511b4f6020ec61ded352059', '', null, '450731199111035008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('545', '654263', '2376037900', '么么', 'c33367701511b4f6020ec61ded352059', '', null, '465553198910054976', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('546', '654264', '923141', 'Blue', 'c33367701511b4f6020ec61ded352059', '', null, '130121198110090000', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('547', '654265', '183054361', 'Smile', 'c33367701511b4f6020ec61ded352059', '', null, '653332199105095040', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('548', '654266', 'Charm', 'Charm', 'c33367701511b4f6020ec61ded352059', '', null, '652723198508240000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('549', '654267', '小懿', '小懿', 'c33367701511b4f6020ec61ded352059', '', null, '652824197810108032', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('550', '654268', '2778876', '李清风', 'c33367701511b4f6020ec61ded352059', '', null, '455551199202035008', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('551', '654269', '812297', '憨厚先生', 'c33367701511b4f6020ec61ded352059', '', null, '342401198910028032', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('552', '654270', '290560178', 'Maybd', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002221056', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('553', '654271', '581673', '581673', 'c33367701511b4f6020ec61ded352059', '', null, '433122197612020992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('554', '654272', '2319509010', '迅飞支付', 'c33367701511b4f6020ec61ded352059', '', null, '330103198501091008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('555', '654273', '839180800', '龙一网络', 'c33367701511b4f6020ec61ded352059', '', null, '321084198004204992', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('556', '654274', '845873222', '涂生', 'c33367701511b4f6020ec61ded352059', '', null, '522301198007070976', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('557', '654275', '1772858121', '锁定灵魂', 'c33367701511b4f6020ec61ded352059', '', null, '452224198910204032', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('558', '654276', '956188404', '阳光男孩', 'c33367701511b4f6020ec61ded352059', '', null, '455552198909091968', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('559', '654277', '4938713', '4938713', 'c33367701511b4f6020ec61ded352059', '', null, '532300199208033024', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('560', '654278', '502437122', 'No problem', 'c33367701511b4f6020ec61ded352059', '', null, '653332199002014976', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('561', '654279', '295325922', '大鱼', 'c33367701511b4f6020ec61ded352059', '', null, '422201198309161984', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('562', '654280', '红星集团运营中心', '红星集团运营中心', 'c33367701511b4f6020ec61ded352059', '', null, '42282719870722229X', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('563', '654281', '824048286', '岁月', 'c33367701511b4f6020ec61ded352059', '', null, '544431198907033984', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('564', '654282', '铁血战神', '铁血战神', 'c33367701511b4f6020ec61ded352059', '', null, '130435198805023008', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('565', '654283', '阿斗哥', '何斗歌', 'c33367701511b4f6020ec61ded352059', '', null, '455553199003064000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('566', '654284', '无产阶级', '元老', 'c33367701511b4f6020ec61ded352059', '', null, '320202198910260992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('567', '654285', 'adsgswyh', 'adsgswyh', 'c33367701511b4f6020ec61ded352059', '', null, '445122198210164992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('568', '654286', '1817943731', '红尘', 'c33367701511b4f6020ec61ded352059', '', null, '530111198702243008', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('569', '654287', '2877598388', '2877598388', 'c33367701511b4f6020ec61ded352059', '', null, '140106198411111008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('570', '654288', '30791934', '诉说', 'c33367701511b4f6020ec61ded352059', '', null, '140109198203180000', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('571', '654289', '2012302730', '张淼', 'c33367701511b4f6020ec61ded352059', '', null, '463331198902035008', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('572', '654290', '80001251', '秦网维', 'c33367701511b4f6020ec61ded352059', '', null, '422261993103052992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('573', '654291', '381648223', '复古传奇管理', 'c33367701511b4f6020ec61ded352059', '', null, '320211197112161984', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('574', '654292', '2783685467', '大黄蜂', 'c33367701511b4f6020ec61ded352059', '', null, '612519198802222976', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('575', '654293', '247918234', '欧俊', 'c33367701511b4f6020ec61ded352059', '', null, '422253199108094016', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('576', '654294', '358925313', '故事', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002120960', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('577', '654295', '641821797', '午夜风铃', 'c33367701511b4f6020ec61ded352059', '', null, '612519198903219968', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('578', '654296', '189688598', '龙少', 'c33367701511b4f6020ec61ded352059', '', null, '453334199005084032', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('579', '654297', '173565619', '173565619', 'c33367701511b4f6020ec61ded352059', '', null, '431225199212036992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('580', '654298', '87516074', '111111', 'c33367701511b4f6020ec61ded352059', '', null, '420121199806220032', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('581', '654299', '生活', '生活', 'c33367701511b4f6020ec61ded352059', '', null, '542523198910185984', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('582', '654300', '613276730', '张小姐', 'c33367701511b4f6020ec61ded352059', '', null, '652223199510305024', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('583', '654301', 'happu123', 'happu123', 'c33367701511b4f6020ec61ded352059', '', null, '230505198301304992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('584', '654302', '249915920', '249915920', 'c33367701511b4f6020ec61ded352059', '', null, '330723199205185024', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('585', '654303', '284610833', '秦风', 'c33367701511b4f6020ec61ded352059', '', null, '651112199503011968', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('586', '654304', 'tangbing', 'tangbing', 'c33367701511b4f6020ec61ded352059', '', null, '450731199005219008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('587', '654305', '535814', 'FAN', 'c33367701511b4f6020ec61ded352059', '', null, '330723197708051968', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('588', '654306', '896318', '莫言', 'c33367701511b4f6020ec61ded352059', '', null, '432225199208091008', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('589', '654307', '188686662', '用户', 'c33367701511b4f6020ec61ded352059', '', null, '612415199001223040', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('590', '654308', '277414241', '李枫', 'c33367701511b4f6020ec61ded352059', '', null, '653332199105062016', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('591', '654309', '80553532', 'Somnus', 'c33367701511b4f6020ec61ded352059', '', null, '652223199310204032', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('592', '654310', '完美主义', '完美主义', 'c33367701511b4f6020ec61ded352059', '', null, '530121197008214016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('593', '654311', '就是我', '就是我', 'c33367701511b4f6020ec61ded352059', '', null, '542129197902252992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('594', '654312', '1415888430', '单职业', 'c33367701511b4f6020ec61ded352059', '', null, '612425199012113024', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('595', '654313', '8486881', '狼', 'c33367701511b4f6020ec61ded352059', '', null, '612541199003213952', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('596', '654314', '378249180', '无尽繁华', 'c33367701511b4f6020ec61ded352059', '', null, '430702197507305024', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('597', '654315', '27815201', '五魁首', 'c33367701511b4f6020ec61ded352059', '', null, '320305197002150016', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('598', '654316', '9925591', '李州', 'c33367701511b4f6020ec61ded352059', '', null, '654442199310301056', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('599', '654317', '200891663', 'boss', 'c33367701511b4f6020ec61ded352059', '', null, '321281199006080000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('600', '654318', '173272141', '李福建', 'c33367701511b4f6020ec61ded352059', '', null, '652223199009085056', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('601', '654319', '99033222', '刘霸', 'c33367701511b4f6020ec61ded352059', '', null, '51310119800305513X', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('602', '654320', '浅斟红颜醉梦洛', '浅斟红颜醉梦洛', 'c33367701511b4f6020ec61ded352059', '', null, '330182198907292032', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('603', '654321', '82093759', '亿飞IDC', 'c33367701511b4f6020ec61ded352059', '', null, '341227198312128000', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('604', '654322', '1269368', '五一九', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002145024', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('605', '654323', '31877343', '梧州游易网络科技有限公司', 'c33367701511b4f6020ec61ded352059', '', null, '341227198312128000', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('606', '654324', '75612657', '可乐喵喵', 'c33367701511b4f6020ec61ded352059', '', null, '142226198702103008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('607', '654325', '小伟哥', '小伟哥', 'c33367701511b4f6020ec61ded352059', '', null, '612415198903220992', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('608', '654326', '桂林力港网络科技股份有限公司', '韩晖', 'c33367701511b4f6020ec61ded352059', '', null, '452228198910300992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('609', '654327', '無雙网络', '無雙网络', 'c33367701511b4f6020ec61ded352059', '', null, '420900199407014016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('610', '654328', 'yaoming', 'yaoming', 'c33367701511b4f6020ec61ded352059', '', null, '450222199306115008', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('611', '654329', '常乐', '常乐', 'c33367701511b4f6020ec61ded352059', '', null, '420982198310296000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('612', '654330', '3095595214', '3095595214', 'c33367701511b4f6020ec61ded352059', '', null, '652324199112035968', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('613', '654331', '342601057', 'new一个地球', 'c33367701511b4f6020ec61ded352059', '', null, '52252919860413297X', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('614', '654332', '274786948', '一切随缘', 'c33367701511b4f6020ec61ded352059', '', null, '513329198806078016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('615', '654333', 'mx116', 'mx116', 'c33367701511b4f6020ec61ded352059', '', null, '433123199110176000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('616', '654334', '909978', '2017工作室', 'c33367701511b4f6020ec61ded352059', '', null, '420711197509192000', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('617', '654335', 'ai184489382', '黄俊强', 'c33367701511b4f6020ec61ded352059', '', null, '45092319890106281X', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('618', '654336', '7001690', '江湖', 'c33367701511b4f6020ec61ded352059', '', null, '450721198906211968', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('619', '654337', '涂勇辉', '涂勇辉', 'c33367701511b4f6020ec61ded352059', '', null, '432402197390153024', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('620', '654338', '413140653', '手倒影', 'c33367701511b4f6020ec61ded352059', '', null, '612419199002110976', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('621', '654339', '我喜欢真露', '我喜欢真露', 'c33367701511b4f6020ec61ded352059', '', null, '130703198011036000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('622', '654340', '3967720', 'szlxk', 'c33367701511b4f6020ec61ded352059', '', null, '33072619901128271X', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('623', '654341', '401703929', '宝哥', 'c33367701511b4f6020ec61ded352059', '', null, '45032619840627183x', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('624', '654342', 'jsnjsf', '李俊', 'c33367701511b4f6020ec61ded352059', '', null, '632722197607074048', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('625', '654343', '115772098', '风月', 'c33367701511b4f6020ec61ded352059', '', null, '450731198910302016', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('626', '654344', '79787962', '漫不经心', 'c33367701511b4f6020ec61ded352059', '', null, '612415199001010048', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('627', '654345', '3407967984', '3407967984', 'c33367701511b4f6020ec61ded352059', '', null, '522301197610056000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('628', '654346', '604551568', '.', 'c33367701511b4f6020ec61ded352059', '', null, '533527198909209984', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('629', '654347', '1485569988', '永恒', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002232960', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('630', '654348', '2872912191', '原来是后来的哥', 'c33367701511b4f6020ec61ded352059', '', null, '330224196702265024', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('631', '654349', '小和尚', '马歌', 'c33367701511b4f6020ec61ded352059', '', null, '453332199202060992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('632', '654350', 'liqqailaopo', '李樯', 'c33367701511b4f6020ec61ded352059', '', null, '413001199109022976', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('633', '654351', '2952425180', 'MU', 'c33367701511b4f6020ec61ded352059', '', null, '152531198812108000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('634', '654352', '625159999', '深圳印刷图库', 'c33367701511b4f6020ec61ded352059', '', null, '450721199010252992', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('635', '654353', '那些年', '那些年', 'c33367701511b4f6020ec61ded352059', '', null, '520326198808204032', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('636', '654354', '天黑就睡了', '天黑就睡了', 'c33367701511b4f6020ec61ded352059', '', null, '445102198204291008', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('637', '654355', '杭州瑞州', '杭州瑞州', 'c33367701511b4f6020ec61ded352059', '', null, '612415198901223040', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('638', '654356', '匆匆岁月过', '匆匆岁月过', 'c33367701511b4f6020ec61ded352059', '', null, '140421198901051008', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('639', '654357', 'xudejun', 'xudejun', 'c33367701511b4f6020ec61ded352059', '', null, '130983198906132992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('640', '654358', '1307186171', '知秋', 'c33367701511b4f6020ec61ded352059', '', null, '450721199210302016', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('641', '654359', 'a5520511', '李富城', 'c33367701511b4f6020ec61ded352059', '', null, '120104198203282000', '李富城', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('642', '654360', '测试测试测试', '测试测试测试', 'c33367701511b4f6020ec61ded352059', '', null, '120104198203282000', '李富城', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('643', '654361', '1808280035', '浅斟红颜醉梦洛', 'c33367701511b4f6020ec61ded352059', '', null, '452722197507190016', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('644', '654362', '4991665', 'xiyifen', 'c33367701511b4f6020ec61ded352059', '', null, '450721199005062016', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('645', '654363', '532211009', '小伍', 'c33367701511b4f6020ec61ded352059', '', null, '432503197505027968', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('646', '654364', '859999366', '许隐', 'c33367701511b4f6020ec61ded352059', '', null, '542224199002035008', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('647', '654365', '682833', '九游销售', 'c33367701511b4f6020ec61ded352059', '', null, '612415199003223040', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('648', '654366', '8755216', '别太耀眼', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002110976', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('649', '654367', '3526744847', '增凯', 'c33367701511b4f6020ec61ded352059', '', null, '463334198602035008', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('650', '654368', '715837', 'phoenix', 'c33367701511b4f6020ec61ded352059', '', null, '370882197811107008', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('651', '654369', '英俊哥', '英俊哥', 'c33367701511b4f6020ec61ded352059', '', null, '350783198607070016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('652', '654370', '2012386103', '谢万岁爷', 'c33367701511b4f6020ec61ded352059', '', null, '621425199002032000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('653', '654371', '775977077', '风之恋', 'c33367701511b4f6020ec61ded352059', '', null, '612514199002009984', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('654', '654372', '燃烧', 'bulijing', 'c33367701511b4f6020ec61ded352059', '', null, '41042319840531135X', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('655', '654373', '718952807', '东方红', 'c33367701511b4f6020ec61ded352059', '', null, '450721199010214976', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('656', '654374', '7824545', '张西', 'c33367701511b4f6020ec61ded352059', '', null, '653331198910200960', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('657', '654375', '云悫网络', '云悫网络', 'c33367701511b4f6020ec61ded352059', '', null, '450721198908256000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('658', '654376', 'zhangyan1016', '成真', 'c33367701511b4f6020ec61ded352059', '', null, '643331199505060992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('659', '654377', '我是传奇', '我是传奇', 'c33367701511b4f6020ec61ded352059', '', null, '420301198712297984', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('660', '654378', 'xiaowu1986', '苍穹', 'c33367701511b4f6020ec61ded352059', '', null, '140502198701187008', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('661', '654379', '420517595', '创新插件', 'c33367701511b4f6020ec61ded352059', '', null, '371581198203163008', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('662', '654380', '49444675', '畅游', 'c33367701511b4f6020ec61ded352059', '', null, '411381197508161024', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('663', '654381', '250097096', '郭露', 'c33367701511b4f6020ec61ded352059', '', null, '450721199010252992', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('664', '654382', '635467454', '李明', 'c33367701511b4f6020ec61ded352059', '', null, '652223199510305024', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('665', '654383', '437305400', 'Mr.殷', 'c33367701511b4f6020ec61ded352059', '', null, '431222197708166976', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('666', '654384', '3969558', '爱好者', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002112000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('667', '654385', '492604778', '花儿开', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002112000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('668', '654386', '2500045911', '阿斗哥', 'c33367701511b4f6020ec61ded352059', '', null, '450731199010236032', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('669', '654387', '852082529', '千浔', 'c33367701511b4f6020ec61ded352059', '', null, '450721198910302016', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('670', '654388', '32298516', '小9', 'c33367701511b4f6020ec61ded352059', '', null, '612415199003211008', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('671', '654389', '83757758', '高军', 'c33367701511b4f6020ec61ded352059', '', null, '652221198802011008', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('672', '654390', '175207119', '王子', 'c33367701511b4f6020ec61ded352059', '', null, '450721198905062016', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('673', '654391', '526689888', '缘起缘灭', 'c33367701511b4f6020ec61ded352059', '', null, '510623197307180992', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('674', '654392', '407937417', '冰舞ヤ开心果', 'c33367701511b4f6020ec61ded352059', '', null, '542225198101014976', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('675', '654393', '1332203386', '文艺青年', 'c33367701511b4f6020ec61ded352059', '', null, '450721199010201984', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('676', '654394', '369321769', '情缘客服', 'c33367701511b4f6020ec61ded352059', '', null, '450721198910235008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('677', '654395', 'ting25205652', 'ting25205652', 'c33367701511b4f6020ec61ded352059', '', null, '372301198910073024', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('678', '654396', '1930508', '4f.cm', 'c33367701511b4f6020ec61ded352059', '', null, '210204197008044992', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('679', '654397', '682052', '九九网络', 'c33367701511b4f6020ec61ded352059', '', null, '150203199512020000', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('680', '654398', '346527511', '宇锦贸易', 'c33367701511b4f6020ec61ded352059', '', null, '450924198301171968', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('681', '654399', '168886663', '张白', 'c33367701511b4f6020ec61ded352059', '', null, '645321199009124992', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('682', '654400', 'deng_8322611', '邓敏聪', 'c33367701511b4f6020ec61ded352059', '', null, '565551199202054976', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('683', '654401', '89690292', '热血青年', 'c33367701511b4f6020ec61ded352059', '', null, '410711198309169024', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('684', '654402', '2968795118', '再接再厉', 'c33367701511b4f6020ec61ded352059', '', null, '360481198906224000', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('685', '654403', '280633395', '高端手表', 'c33367701511b4f6020ec61ded352059', '', null, '431230199402190016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('686', '654404', '97201060', '97201060', 'c33367701511b4f6020ec61ded352059', '', null, '450721199105062016', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('687', '654405', '1351367585', '1351367585', 'c33367701511b4f6020ec61ded352059', '', null, '450721198910214976', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('688', '654406', '139idc', '许杰', 'c33367701511b4f6020ec61ded352059', '', null, '342201198712110016', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('689', '654407', '1003196665', 'Ｘˊ.strive', 'c33367701511b4f6020ec61ded352059', '', null, '513328198009076992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('690', '654408', '415090997', '鸿运', 'c33367701511b4f6020ec61ded352059', '', null, '370829197702073024', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('691', '654409', '657522106', '657522106', 'c33367701511b4f6020ec61ded352059', '', null, '450731199105123008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('692', '654410', 'suoai88', '董虎', 'c33367701511b4f6020ec61ded352059', '', null, '420802197410080000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('693', '654411', '2710234064', '李白', 'c33367701511b4f6020ec61ded352059', '', null, '230882198710071000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('694', '654412', '2471419198', 'ssssa', 'c33367701511b4f6020ec61ded352059', '', null, '430822198304021000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('695', '654413', '133151377', '张大宇', 'c33367701511b4f6020ec61ded352059', '', null, '612415199002211000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('696', '654414', '1209221155', '李静', 'c33367701511b4f6020ec61ded352059', '', null, '564443199510201024', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('697', '654415', '147897241', '执着', 'c33367701511b4f6020ec61ded352059', '', null, '450731199206051008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('698', '654416', '34298', '╰妃我莫屬╯', 'c33367701511b4f6020ec61ded352059', '', null, '210282198901300992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('699', '654417', '150365888', '150365888', 'c33367701511b4f6020ec61ded352059', '', null, '422201198306129984', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('700', '654418', '2885874125', '刘凯旋', 'c33367701511b4f6020ec61ded352059', '', null, '453337199512120000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('701', '654419', '776709939', '776709939', 'c33367701511b4f6020ec61ded352059', '', null, '650101198604183040', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('702', '654420', '95874732', '似水流年', 'c33367701511b4f6020ec61ded352059', '', null, '320981198912307008', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('703', '654421', 'qq2281657550', '杨涛', 'c33367701511b4f6020ec61ded352059', '', null, '522131198805052032', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('704', '654422', '715536911', '张水', 'c33367701511b4f6020ec61ded352059', '', null, '612415198902210944', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('705', '654423', '烽火网络', '仇庆兵', 'c33367701511b4f6020ec61ded352059', '', null, '320911197806203008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('706', '654424', '114319700', '朱联', 'c33367701511b4f6020ec61ded352059', '', null, '612415199003220992', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('707', '654425', '1220426', '老牛', 'c33367701511b4f6020ec61ded352059', '', null, '450721199211252992', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('708', '654426', '854698878', '854698878', 'c33367701511b4f6020ec61ded352059', '', null, '450731199008214976', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('709', '654427', '4289518', '王午儿', 'c33367701511b4f6020ec61ded352059', '', null, '612425199003212032', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('710', '654428', '313075085', '金必春', 'c33367701511b4f6020ec61ded352059', '', null, '546661199010204992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('711', '654429', '280298524', '柏利华', 'c33367701511b4f6020ec61ded352059', '', null, '500105199008260992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('712', '654430', '756772333', '756772333', 'c33367701511b4f6020ec61ded352059', '', null, '450502199009249984', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('713', '654431', '3088008228', '3088008228', 'c33367701511b4f6020ec61ded352059', '', null, '350982197103164992', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('714', '654432', '1815802101', '周鲁', 'c33367701511b4f6020ec61ded352059', '', null, '450721199002124032', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('715', '654433', '848362', '848362', 'c33367701511b4f6020ec61ded352059', '', null, '450731199210252992', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('716', '654434', '330555777', 'hupo', 'c33367701511b4f6020ec61ded352059', '', null, '542426197503292992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('717', '654435', '343615000', 'cc', 'c33367701511b4f6020ec61ded352059', '', null, '510502198509110016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('718', '654436', '2039840884', '2039840884', 'c33367701511b4f6020ec61ded352059', '', null, '450721199008123008', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('719', '654437', '1326232323', 'wangxiaoyou', 'c33367701511b4f6020ec61ded352059', '', null, '513328198310110016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('720', '654438', '65636618', '晏小平', 'c33367701511b4f6020ec61ded352059', '', null, '513030198710052992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('721', '654439', '591306063', '来互相伤害啊~', 'c33367701511b4f6020ec61ded352059', '', null, '320204198212224000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('722', '654440', '262530829', '久病成欢孤独成瘾', 'c33367701511b4f6020ec61ded352059', '', null, '430412198605244992', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('723', '654441', '173721854', '孙天', 'c33367701511b4f6020ec61ded352059', '', null, '612415198902113024', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('724', '654442', '616946738', '铁汉柔情', 'c33367701511b4f6020ec61ded352059', '', null, '530302197808305984', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('725', '654443', '307083906', '霸气网络', 'c33367701511b4f6020ec61ded352059', '', null, '430821197503094016', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('726', '654444', '407084795', '蔡白', 'c33367701511b4f6020ec61ded352059', '', null, '543331198605044992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('727', '654445', '124195144', 'Lemon', 'c33367701511b4f6020ec61ded352059', '', null, '131100199107148000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('728', '654446', '734049', '天成', 'c33367701511b4f6020ec61ded352059', '', null, '612429198802210944', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('729', '654447', '3271179414', '3271179414', 'c33367701511b4f6020ec61ded352059', '', null, '411222197708257024', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('730', '654448', '307164939', '金牌者', 'c33367701511b4f6020ec61ded352059', '', null, '612425198802123008', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('731', '654449', '787503735', '余桂文', 'c33367701511b4f6020ec61ded352059', '', null, '521113198610204992', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('732', '654450', '97435021', '宝马科技', 'c33367701511b4f6020ec61ded352059', '', null, '470721199008214976', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('733', '654451', '634618617', '别世军', 'c33367701511b4f6020ec61ded352059', '', null, '421083196411190016', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('734', '654452', '87677771', '王天才', 'c33367701511b4f6020ec61ded352059', '', null, '332501198207190016', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('735', '654453', 'xiaoqun', '123', 'c33367701511b4f6020ec61ded352059', '', null, '330327199901012992', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('736', '654454', '330194351', '随风', 'c33367701511b4f6020ec61ded352059', '', null, '612415198802151936', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('737', '654455', '512253729', '宋志承', 'c33367701511b4f6020ec61ded352059', '', null, '1201051981011160064', '19,陶秋梅', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('738', '654456', '529188888', '对 对', 'c33367701511b4f6020ec61ded352059', '', null, '614214198803220992', '20,唐晓珍', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('739', '654457', '390803258', 'TOP工作室', 'c33367701511b4f6020ec61ded352059', '', null, '420521198704240000', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('740', '654458', '138620093', '霸王别姬', 'c33367701511b4f6020ec61ded352059', '', null, '450201197801275008', '22,廖超', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('741', '654459', '四川世纪金沙国际旅行社有限公司', '四川世纪金沙国际旅行社有限公司', 'c33367701511b4f6020ec61ded352059', '', null, '51080219911012415X', '18,劳兴华', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('742', '654460', '84845094', '白开水2o1⁷', 'c33367701511b4f6020ec61ded352059', '', null, '622921199404021000', '21,黄小恩', null, null, null, '2017-08-24 15:22:20');
INSERT INTO `llidc_clients` VALUES ('743', '654461', '905222555', '江南style', 'c33367701511b4f6020ec61ded352059', '', null, '222406198110088000', '21,黄小恩', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('744', '654462', '286768210', '大师兄！师傅被抓走了', 'c33367701511b4f6020ec61ded352059', '', null, '420682197903255000', '21,黄小恩', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('745', '654463', 'geoidc', '张楠', 'c33367701511b4f6020ec61ded352059', '', null, '542223198910105000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('746', '654464', '10040191', '陈永安', 'c33367701511b4f6020ec61ded352059', '', null, '320381198608176000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('747', '654465', '3311030006', '张理', 'c33367701511b4f6020ec61ded352059', '', null, '612546198902143000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('748', '654466', '1602794971', '2鑫', 'c33367701511b4f6020ec61ded352059', '', null, '641241198802124000', '20,唐晓珍', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('749', '654467', '7207165', 'ㄣ痞子ㄨ虎ㄣ', 'c33367701511b4f6020ec61ded352059', '', null, '511526198106104000', '22,廖超', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('750', '654468', '鼎点网络', '王楠', 'c33367701511b4f6020ec61ded352059', '', null, '452213198310304000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('751', '654469', '620gg', '620gg', 'c33367701511b4f6020ec61ded352059', '', null, '130204198009024000', '18,劳兴华', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('752', '654470', '346911930', 'sunyong 雪', 'c33367701511b4f6020ec61ded352059', '', null, '350502199003238000', '22,廖超', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('753', '654471', '福鑫', '李君', 'c33367701511b4f6020ec61ded352059', '', null, '320303199308110000', '19,陶秋梅', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('754', '654472', '12355660', '12355660', 'c33367701511b4f6020ec61ded352059', '', null, '32101119790706152X', '18,劳兴华', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('755', '654473', '红日科技', 'IDC慧', 'c33367701511b4f6020ec61ded352059', '', null, '450981199203218000', '18,劳兴华', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('756', '654474', '2227893', '2227893', 'c33367701511b4f6020ec61ded352059', '', null, '410503195811281000', '18,劳兴华', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('757', '654475', '李富城', '李富城', 'c33367701511b4f6020ec61ded352059', '', null, '441900199306012000', '李富城', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('758', '654476', '98723', '98723', 'c33367701511b4f6020ec61ded352059', '', null, '33072619901128271X', '18,劳兴华', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('759', '654477', '383554220', '疯狂的兔子', 'c33367701511b4f6020ec61ded352059', '', null, '150923197202268000', '22,廖超', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('760', '654478', '胡蕴斌', '胡蕴斌', 'c33367701511b4f6020ec61ded352059', '', null, '654226198903181952', '19,陶秋梅', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('761', '654479', '艾米', '陈辉', 'c33367701511b4f6020ec61ded352059', '', null, '420885198811086976', '19,陶秋梅', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('762', '654480', '247128474', '247128474', 'c33367701511b4f6020ec61ded352059', '', null, '360425198612112000', '18,劳兴华', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('763', '654481', '625529', '长卿', 'c33367701511b4f6020ec61ded352059', '', null, '421123197903316992', '21,黄小恩', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('764', '654482', '3572990', '华哥', 'c33367701511b4f6020ec61ded352059', '', null, '210323198305265984', '22,廖超', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('765', '654483', '阿华', '无效的', 'c33367701511b4f6020ec61ded352059', '', null, '421001198301097024', '22,廖超', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('766', '654484', '琪琪', '琪琪', 'c33367701511b4f6020ec61ded352059', '', null, '450721199305123968', '21,黄小恩', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('767', '654485', 'liaochao', '无效的', 'c33367701511b4f6020ec61ded352059', '', null, '411024198208300032', '22,廖超', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('768', '654486', '寒露', '王飞', 'c33367701511b4f6020ec61ded352059', '', null, '350500196304275008', '19,陶秋梅', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('769', '654487', '鹅鹅鹅', '鹅鹅鹅', 'c33367701511b4f6020ec61ded352059', '', null, '441900199306012032', '18,劳兴华', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('770', '654488', 'ceshi02', '中科4', 'c33367701511b4f6020ec61ded352059', '', null, '430211198712052992', 'admin', null, null, null, '2017-08-24 15:22:21');
INSERT INTO `llidc_clients` VALUES ('771', '654489', 'ceshi01', '中科1', 'c33367701511b4f6020ec61ded352059', '', null, '430211198712052992', 'admin', null, null, null, '2017-08-24 15:22:21');
