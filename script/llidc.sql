/*
Navicat MySQL Data Transfer

Source Server         : zxgj
Source Server Version : 50626
Source Host           : localhost:3306
Source Database       : llidc

Target Server Type    : MYSQL
Target Server Version : 50626
File Encoding         : 65001

Date: 2017-03-13 16:48:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for llidc_news
-- ----------------------------
DROP TABLE IF EXISTS `llidc_news`;
CREATE TABLE `llidc_news` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '新闻id',
  `n_title` varchar(255) NOT NULL COMMENT '新闻标题',
  `n_content` text NOT NULL COMMENT '新闻的内容',
  `n_datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '新闻的录入日期',
  `n_memo` varchar(512) DEFAULT '' COMMENT '新闻备注',
  PRIMARY KEY (`n_id`),
  UNIQUE KEY `news` (`n_id`,`n_title`)
) ENGINE=InnoDB AUTO_INCREMENT=165 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of llidc_news
-- ----------------------------
INSERT INTO `llidc_news` VALUES ('155', '湛江联通康乐国总经理一行莅临利联网络调研指导工作', '\r\n        <p><strong><span style=\"font-size:16px;\">2月10日上午，湛江联通总经理康乐国、副总经理刘士卿、系统集成部经理陈耀麒莅临利联网络东莞总部参观调研。王宇杰董事长及公司领导热情接待并就业务发展做了详细的汇报。</span><br /></strong></p><div style=\"text-align: center;\"><span style=\"font-size: 12px;\"><span style=\"font-size:13px;\"><img src=\"//pic.wy.cn/Uploads/2017/2/15/7cec440d-201a-49cf-80fc-b48cee60066b.jpg\" alt=\"湛江联通康乐国总经理一行莅临利联网络调研指导工作\" /></span></span></div><p></p><p></p><div style=\"text-align: center;\">利联网络董事长特助蔡湛向考察团讲解了自主研发的云安全监控可视化平台。</div><div style=\"text-align: center;\"><br /></div><p></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2017/2/15/cd3adc04-112f-482c-a02f-1d14255e30b6.jpg\" alt=\"湛江联通康乐国总经理一行莅临利联网络调研指导工作\" /></div><p></p><p></p><div style=\"text-align: center;\">介绍利联网络企业整体情况及品牌客户</div><br /><p></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2017/2/15/75563e97-6cd8-46d5-b4fe-d708678c82f2.jpg\" alt=\"湛江联通康乐国总经理一行莅临利联网络调研指导工作\" /></div><p></p><p></p><div style=\"text-align: center;\">座谈会上，董事长王宇杰向康总一行详细汇报了利联网络目前的发展情况、近年取得的成绩以及未来的长远规划。</div><br /><p></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2017/2/15/d207dae0-a78c-4228-a591-256d721709bb.jpg\" alt=\"湛江联通康乐国总经理一行莅临利联网络调研指导工作\" /></div><p></p><p>湛江联通总经理康乐国对利联网络目前取得的成绩表示充分肯定，希望双方加强合作，扩大合作规模，并期望利联网络在充分发挥已有优势的同时，借“<strong><span style=\"color: rgb(51, 204, 255);\"><span style=\"font-size:16px;\">倍增计划</span></span></strong>”的东风，在2017年开拓新的格局！</p><p>2017年是利联网络高速发展、规模倍增的一年，将与各运营商多方面多元化地展开业务合作，加速规模发展，为更多用户提供安全、稳定、快速的互联网综合服务。</p>&#13;\n    ', '2017-02-15 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('156', '中国电信福建分公司领导一行，莅临利联网络厦门分公司调研指导工作', '\r\n        <p></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2017/2/15/b32835a3-b71e-4458-9e7b-b9a7a3bdd1a6.jpg\" alt=\"中国电信福建分公司领导一行，莅临利联网络厦门分公司调研指导工作\" /></div><div style=\"text-align: center;\">2017年新年伊始，利联网络厦门分公司也开启了新的征程。</div><p>2月10号上午，中国电信福建公司创新业务部副总经理、云业务事业部总经理梁鸿生，云事业部副总经理黄诗嵘等一行，莅临利联网络厦门分公司进行指导调研。<br /></p><p>利联网络华东分公司总经理黄小华携公司高层热情接待了考察组，参观公司办公环境，并开展了详实高效的会谈，介绍了互联网安全的现状以及利联网络打造的互联网安全生态圈。<br /><br /></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2017/2/15/33e0c776-4dc1-4a8f-9d86-083241bad7b2.jpg\" alt=\"中国电信福建分公司领导一行，莅临利联网络厦门分公司调研指导工作\" /><br /><br /><img src=\"//pic.wy.cn/Uploads/2017/2/15/48791e86-0c07-4230-9bc0-2ad128267e16.jpg\" alt=\"中国电信福建分公司领导一行，莅临利联网络厦门分公司调研指导工作\" /><br /><br /><img src=\"//pic.wy.cn/Uploads/2017/2/15/0ce12059-ce21-409a-aede-90c6fb41dc11.jpg\" alt=\"中国电信福建分公司领导一行，莅临利联网络厦门分公司调研指导工作\" /></div><p>中国电信表示近年来一直加快在IDC基础运维、云计算、云安全等互联网领域的合作发展步伐，加大与互联网公司的合作、整合和提升核心能力。</p><p style=\"text-align: left;\">此次交流，双方以DNS云安全为切入点，协同联动，探讨共建互联网安全生态。<br /><br /></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2017/2/15/f9145c69-6ea6-47a7-8601-0a99b46d699f.jpg\" alt=\"\" /></div><p>黄小华表示，利联网络长期以来，不断致力于产业创新升级，掌握核心技术，充分发挥人才优势，持续投入产品研发及运营服务管理。业务范围从IDC数据中心运营，延展到DDOS、DNS和云计算平台三个板块。为运营商、域名注册商、广大互联网企业等，解决各类DNS安全问题，保障DNS解析的稳定性与安全性，构建互联网安全、高速、稳定的安全生态圈。<br /><br /></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2017/2/15/80c8d6c8-df74-4b14-8e89-1a56db6b4ec2.jpg\" alt=\"中国电信福建分公司领导一行，莅临利联网络厦门分公司调研指导工作\" /></div><p>中国电信福建分公司一行领导表示，此次会议后对利联网络有了更深刻的了解，并对利联网络的整体情况表示充分的肯定，鼓励公司在当前的道路上持续创新，不断精进。</p><p>2017年会是利联网络更加拼搏进取的一年，为更多用户提供安全、稳定、快速的互联网综合服务。</p>&#13;\n    ', '2017-02-15 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('157', '刀片服务器托管如何管理？', '\r\n        <p>刀片服务器您否了解了，<a href=\"http://www.wy.cn\">刀片服务器托管</a>如何管理?下面跟随利联网络一起来学习。<br /><br /></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2016/9/5/fb7e0a19-5b07-48fe-a0d9-a68c22b83b12.png\" alt=\"刀片服务器托管如何管理？\" width=\"480\" /></div><p>刀片服务器本身的特性，对管理刀片服务器提出了许多新挑战刀片服务器的管理一直是一个关乎其发展的大问题，虽然管理刀片服务器与管理标准服务器没有什么太大的区别，然而，刀片服务器具备许多非常诱人的特色，例如极为灵活的扩展性和热插拔能力，因此刀片服务器也就对管理提出了一些新的挑战。</p><p>在典型的设施中，刀片服务器的数量众多，由于每个机架上可能包括数百台刀片式服务器，而且机架的数量又相当多，如果管理员无法在虚拟化机架环境中实现可扩展的流程及任务自动化，要想管理如此众多的刀片服务器根本就是无法想象的。</p><p>在<a href=\"http://www.wy.cn\">刀片服务器</a>的管理过程中，一般性硬件部署和远程访问都是非常关键的组件。</p><p>由于刀片服务器具备的特性，IT管理员还应当随时清楚地了解库存和配置情况，从而能够快速实现刀片服务器镜像，充分发挥出服务器的热插拔优势，并且在服务器运行过程中也能够对各种资源进行重新分配。</p><p>IT企业同时要求对刀片服务器的整个寿命周期进行管理，其中包括可用性和性能监视、硬件和软件库存及资产管理、维护、部署、镜像、补丁管理。在理想状况下，具备这些不同功能的管理软件都应当是基于策略的，而且与不断增强的自动化功能无缝集成为一体，同时也具备较低的管理成本和较高的维护效率。另外，还应当针对Windows和Linux开发出不同的功能，这对于满足当前市场的各种需求是非常关键的。</p><p>最后，远程管理应当成为任何刀片服务器运行过程的一部分，因为其具备的高性价比和小型化特色使之成为网络边缘应用的理想选择。<br /><br />  服务器租用/服务器托管最具实力IDC提供商！十年品牌保障 - 利联网络！<br />  转载请注明：利联网络http://www.wy.cn/</p>&#13;\n    ', '2016-09-05 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('158', '我国云计算信任体系建设显成效', '\r\n        <p>9月1日~2日，由工业和信息化部指导，中国信息通信研究院、中国通信标准化协会主办，数据中心联盟承办的“2016可信云大会”在京召开。工信部总工程师张峰出席会议并致辞，他指出，近年来我国云计算产业快速发展，产业实力不断增强、国际影响力提升，信任体系建设初显成效，不过仍存在核心竞争力不强，服务标准不够完善等问题。面对未来，我国云计算产业要以国家政策为引领，推动产业创新发展;以市场需求为导向，完善产业生态体系;以服务产业为目标，发挥行业组织作用。</p><p>张峰指出，作为近些年信息通信领域发展最迅速的产业之一，<a href=\"http://www.wy.cn\">云计算</a>对国民经济和社会发展的战略支撑与创新引领作用日益凸显，加快发展云计算产业，对加快经济增长，促进产业结构创新升级，推动与传统产业的融合发展具有重要意义。在政策和市场的双重驱动下，我国云计算产业发展呈现出三大特点。</p><p>一是产业实力不断增强。根据中国信息通信研究院的调查数据，2015年我国公共云服务市场整体规模约102.4亿元，比2014年增长45.8%，预计2016年市场规模可望达到150亿元。云计算逐渐成为政府、金融、游戏、电商等行业的重要基础支撑。</p><p>二是国际影响逐步提升。随着国内云服务企业的服务能力、技术实力不断增强，我国<a href=\"http://www.wy.cn\">云服务企业</a>已经开始向国际市场布局，金山、优刻得等国内云服务企业已经在北美、非洲等地部署数据中心，向数以万计的当地用户提供云服务。今年6月，可信云相关标准已被国际电信联盟ITU采纳，标志着可信云服务标准获得更广泛的国际关注和认可。</p><p>三是信任体系初步建立。数据中心联盟组织的可信云认证已经得到产业界的广泛认可，目前可信云认证体系已经进入3.0阶段，覆盖了10种以上的云服务，累计通过认证的云服务数量超过140个。可信云认证完善了评测、认证、持续监测、年检、不合格退出、云保险等全流程方案，对推动建立云计算信任体系具有积极作用。</p><p>目前，我国云计算产业已具备很好的基础，前景广阔，但问题和挑战依然存在。张峰指出，我国云服务市场仍然面临核心竞争力不强、服务标准尚不完善、行业需求未有效满足等问题，因此业界需要从三个方面推动云计算的发展：一是要以国家政策为引领，推动产业创新发展;二是要以市场需求为导向，完善产业生态体系;三是要以服务产业为目标，发挥行业组织作用。</p><p>会上，工信部信息通信发展司副司长陈立东对可信云服务认证的总体发展情况进行了通报。经过两年多的发展，可信云服务工作已正式进入3.0体系建设阶段，增加了可信云金牌运维专项评估以及可信云安全评估，形成了IaaS/PaaS和企业级SaaS两套评估标准，基本实现了对业界主流云服务类型的全覆盖。截至目前，共有70个云服务商的144个云服务通过了可信云服务认证。可信云保险推出1.0Plus版本，承保对象已扩展到互联网服务提供商，并新增了对数据泄露的保障内容。</p><p>在为期两天的会议中，中国信息通信研究院将陆续发布《云计算白皮书》、《全球云计算服务协议白皮书》、《中国大数据的社会经济价值分析报告》等研究成果。</p>  服务器租用/服务器托管最具实力IDC提供商！十年品牌保障 - 利联网络！<br />  转载请注明：利联网络http://www.wy.cn/<br /><br />&#13;\n    ', '2016-09-02 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('159', '四大技巧保障服务器租用“零宕机”', '\r\n        <p>在当下的应用经济时代，任何一家公司都是软件公司，客户通过软件了解企业，与企业亲密接触，即使是短暂的停机或表现不佳，都将意味着收入损失、客户抱怨并影响公司声誉。因此，企业应该将“运维”提升到一个新的高度来加以关注，而应用则是运维保障的核心和灵魂。<br /><br /></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2016/9/2/003c53c8-89b1-405e-831b-f53b53f33637.jpg\" alt=\"四大技巧保障服务器租用“零宕机”\" width=\"580\" /></div><p>四大技巧保障<a href=\"http://www.wy.cn\">服务器租用</a>“零宕机”</p><p>1. 善用自动化</p><p>将应用系统变更流程化、自动化，可以加快系统变更时间，同时最大程度降低人为错误导致的宕机。</p><p>2. 未雨绸缪，应急预案有备无患</p><p>应急预案可以帮助企业在遇到突发事件的同时，加快恢复速度，减少损失。</p><p>3. 思想问题要抓好，“应用性能管理”要重视</p><p>如今，企业都忙于将所有的资源都投入到一线业务中去，对包括应用在内的软件的运维问题相对忽视，这种大意加大了系统的风险。应用性能管理可以帮助企业更轻松的采用、管理和升级，并在性能恶化时提出预警，使企业能提前感知并采取相应的修补动作，避免宕机事件的发生，从而让每一次体验都变成建立忠诚度的互动活动。</p><p>4. 保障需有力，API成为安全新“关口”</p><p>在互联网开放经济的今天，应用程序接口(API)管理对于安全来说显得尤其重要。相对于国外，API经济在国内也已经开始成形，只是还没有引起太大关注。API的本质是一种服务，用户通过手机应用对企业服务进行访问，都与API相关。作为企业数据和安全信息的关口，API的管理应该得到CIO们的重视，从网关、服务管理、开发者门户管理等三个方面实现企业API管理的高效性和安全性。</p>  服务器租用/服务器托管最具实力IDC提供商！十年品牌保障 - 利联网络！<br />  转载请注明：利联网络http://www.wy.cn/<br />&#13;\n    ', '2016-09-02 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('160', '高防服务器的防御措施有哪些', '\r\n        <p>高防服务器主要是针对企业用户的，相对来说，这些企业用户对于网络安全的要求更高，高防服务器给用户提供了更加安全的网络运行环境，为企业客户提供安全的保证。那么，<a href=\"http://www.wy.cn\">高防服务器</a>的防御措施有哪些?<br /><br /></p><div style=\"text-align: center;\"><img src=\"//pic.wy.cn/Uploads/2016/9/2/e2e3eb08-533f-44dc-8a7c-c795140520a5.jpg\" alt=\"高防服务器的防御措施有哪些\" width=\"580\" /></div><p>(1)定期扫描高防服务器</p><p>为了查找可能存在的安全漏洞，需要对现有的网络主节点进行定期扫描，发现漏洞之后要及时清理。黑客一般会攻击骨干节点的计算机，因为它具有较高的带宽，因此对这些主机本身加强主机安全是非常重要的。而且连接到网络主节点的都是服务器级别的计算机，所以定期扫描漏洞就变得更加重要了。</p><p>(2)在<a href=\"http://www.wy.cn\">高防服务器</a>的骨干节点配置防火墙</p><p>安装防火墙可以有效的抵御DdoS攻击和其他一些攻击。当发现攻击的时候，可以将攻击导向一些不重要的牺牲主机，这样可以保护真正的主机不被攻击。牺牲主机也可以是linux以及unix等漏洞少和天生防范攻击优秀的系统。</p><p>(3)用足够的机器承受黑客攻击</p><p>这是比较理想的一种应对策略。这需要用户有足够的服务器，黑客攻击的时候会不断的访问用户，在这个期间黑客自己的资源也是在不断的消耗的，可能用户的主机还没有被攻击死，黑客已经没有多余的精力和资源了。这种方法需要投入的资金比较多，平时大多数设备处于空闲状态，和中小企业网络实际运行情况不相符。</p><p>(4)充分利用网络设备保护网络资源</p><p>网络设备一般包含路由器、防火墙等负载均衡设备，它们可将网络有效地保护起来。当网络受到外界的攻击时，路由器是最先死掉的，但其他机器没有死。死掉的路由器经过重启之后会恢复，而且启动速度会比较快，不会造成什么损失。如果是其他的服务器死掉，其中的数据会丢失，而且重启服务器又是一个漫长的过程。特别是一个公司使用了负载均衡设备，这样当一台路由器被攻击死机时，另一台将马上工作。从而最大程度的削减了DdoS的攻击。</p><p>(5)过滤不必要的服务和端口</p><p>这个指的是在路由器上过滤掉假的IP，只开放服务端口是现在高防服务器比较常见的做法，例如WWW服务器只开放80而将其他所有端口关闭或在防火墙上做阻止策略。</p><p><a href=\"http://www.wy.cn\">服务器租用</a>/服务器托管最具实力IDC提供商!十年品牌保障 - 利联网络!</p><p>转载请注明：利联网络http://www.wy.cn/</p>&#13;\n    ', '2016-09-02 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('161', '利联网络2017春节放假通知', '\r\n        <p style=\"text-align: center;\"><strong><img src=\"//pic.wy.cn/Uploads/2017/1/25/11a4b03f-e32a-4613-9941-02659662db60.jpg\" alt=\"利联网络2017春节放假通知\" align=\"middle\" width=\"640\" height=\"455\" /><br /><span style=\"color: rgb(255, 0, 0);\"><span style=\"font-size:24px;\">祝大家新春快乐！</span></span></strong></p><p><span style=\"color:#ff0000;\">尊敬的利联网络客户伙伴们：</span></p><p><span style=\"color:#ff0000;\">您好，在2017年春节来临之际，利联网络全体员工在此衷心感谢您一直以来对我们的信任和支持，祝您春节快乐！阖家幸福！根据国家2017年节假日放假安排以及我司实际情况，利联网络春节放假时间如下：</span></p><p><span style=\"color:#ff0000;\">一、放假时间：2017年1月26日至2017年2月3日，2月4日正式上班</span></p><p><span style=\"color:#ff0000;\">二、服务安排：假期期间，我司售后支撑的工作人员将24小时值班。</span></p><p><span style=\"color:#ff0000;\">24小时客服QQ：4007166188</span></p><p><span style=\"color:#ff0000;\">24小时服务热线：4007-166-188</span></p><p><span style=\"color:#ff0000;\">财务联络QQ：799175</span></p><p><span style=\"color:#ff0000;\">财务联络电话：0769-88758000</span></p><p><span style=\"color:#ff0000;\">温馨提示：</span></p><p><span style=\"color:#ff0000;\">1、春节假期期间，暂停域名白名单人工服务与网站备案服务，如需添加域名白名单的请登录http://www.wy.cn“管理中心”提交，取得工信部网站备案号的域名将在提交后10分钟内生效。</span></p><p><span style=\"color:#ff0000;\">2、春节假期期间，请加强网络信息安全的管理，保持电话、QQ等通讯畅通，做好节假日期间的应急响应工作，若发现存在违法违规内容，请在规定时限内配合处置完毕，若未能妥善处理的，我司将采取封停网站或IP地址等措施，望支持与配合。</span></p>&#13;\n    ', '2017-01-25 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('162', '利联网络元旦放假公告', '\r\n        <p>猴年已经开始向我们挥手告别了，岁月如歌！我们度过了精彩纷呈的2016，迎来了蓄势待发的2017，在过去的一年里，我们携手并进，不断进取并收获了可喜的成绩。</p><p>2017年来临之际，在这辞旧迎新的节日里，利联网络诚挚地问候大家，并向多年来一直支持利联网络的新老客户表示由衷的感谢！</p><p>祝大家：元旦快乐，在新的一年里身体健康！工作顺利！万事如意！阖家欢乐！</p><p>无限精彩、无限可能，必然属于即将到来的2017年！</p><p>2017年我们将继续为您提供优质的服务！</p><p><strong>放假安排通知：</strong></p><p>根据国家有关规定，利联网络元旦节放假3天（2016年12月31日至2017年1月2日放假），1月3日起正常上班。</p><p>放假期间，售后支撑部门正常值班：</p><p>24小时客服QQ：4007166188</p><p>24小时服务热线：4007-166-188</p><p>财务直线：0769-88758000</p><p>财务专用QQ：799175</p><p>投诉建议：13724475555</p><p>投诉建议QQ：87923</p>&#13;\n    ', '2016-12-30 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('163', '利联网络2016年国庆放假公告', '\r\n        <strong><span style=\"font-size:18px;\">尊敬的广大客户：<br /></span></strong><br /><p>值此国庆节来临之际,<a href=\"https://www.wy.cn/\">利联网络</a>全体员工祝您节日愉快！感谢您一如既往的对利联网络的支持与厚爱!为了节日期间保证我们的服务质量，我司客服中心、网管中心、机房运维、信息安全等工作人员24小时正常上班。根据国务院对2016年国庆节的放假通知精神结合我司实际情况，现将我司国庆放假具体安排通知如下：</p><p>放假时间为10月1日-10月7日，共7天，10月8日全司恢复正常上班。</p><p>休假期间我司网维、运维等技术人员正常上班，如有需要请联系：</p><p>24小时网维QQ：4007166188</p><p>24小时服务热线：0769-23015555    4007-166-188</p><p>24小时网管QQ：730012</p><p>白名单/信息安全QQ: 622103</p><p>投诉建议QQ：87923      电话：13724475555</p><p>财务联络QQ：799175    电话：0769-88758000</p><p>财务投诉QQ：435556    电话：13650165555</p><p style=\"text-align: right;\">广东利联网络科技有限公司</p><p style=\"text-align: right;\">2016-9-30</p>&#13;\n    ', '2016-09-30 00:00:00', '');
INSERT INTO `llidc_news` VALUES ('164', '利联网络2016年中秋节放假通告', '\r\n        <p style=\"text-align:center;\"><img src=\"//pic.wy.cn/Uploads/2016/9/14/4d607a09-ab66-4198-88f9-4ec6bc2542c9.jpg\" alt=\"利联网络2016年中秋节放假通告\" /></p><p style=\"text-indent:2em;\">2016年中秋佳节即将到来，利联网络全体员工祝您中秋节快乐!感谢您一如既往的对利联网络的支持与厚爱!为了节日期间保证我们的服务质量，我司网维、运维等技术人员24小时值班。根据国家相关通知，结合我司实际情况，现将我司放假具体安排通知如下：</p><br /><p style=\"text-indent:2em;\">放假时间为9月15日至9月17日，共3天，9月18日全司恢复正常上班。</p><p style=\"text-indent:2em;\">休假期间我司网维、网管、机房运维、信息安全、财务等工作人员正常上班，如有需要请联系：</p><p style=\"text-indent:2em;\">24小时技术QQ：4007166188</p><p style=\"text-indent:2em;\">24小时服务热线：0769-23015555  4007-166-188</p><p style=\"text-indent:2em;\">24小时网管QQ：730012</p><p style=\"text-indent:2em;\">企业技术支撑QQ：929066</p><p style=\"text-indent:2em;\">域名白名单与信息安全QQ: 622103</p><p style=\"text-indent:2em;\">财务联络QQ：799175  电话：0769-88758000</p><p style=\"text-indent:2em;\">投诉建议QQ：87923   电话：13724475555</p>&#13;\n    ', '2016-09-14 00:00:00', '');
