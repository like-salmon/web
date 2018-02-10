<?php if (!defined('THINK_PATH')) exit();?><!-- 加载头部模板文件-->
<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>利联科技_服务器租用_服务器托管</title>
    <meta name="application-name" content="利联网络"/>
    <meta name="renderer" content="webkit"><!-- 强制360用webkit内核 -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta content="idc,服务器,高防服务器" name="keywords"/>
    <meta name="description" content="利联网络，专业互联网IDC服务商"/>
    <link rel="shortcut icon" href="/Public/img/favicon.ico" type="image/x-icon" />
    <!-- uslider css-->
    <link rel="stylesheet" href="/Public/css/unslider.css"/>
    <link rel="stylesheet" href="/Public/css/unslider-dots.css"/>
    <link rel="stylesheet" href="/Public/css/style.css?v=20170209">
    <script type="text/javascript" src="/Public/js/scrollreveal.js"></script>
</head>

<body>

<!-- 加载导航模板文件-->
<div class="subnav">
    <div class="nav">
        <div class="content">
            <div class="left">
                <span>您好，欢迎访问利联科技-高防服务器、机柜大带宽等一站式服务平台!</span>
            </div>
            <div class="right">
                <a href="/auth/login/" class="btn login-btn">登陆</a>
                <a href="http://llidc.com:83/machine/Zcustomer.aspx" class="btn reg-btn">注册</a>
                <a href="javascript:;" class="btn reg-btn">购买流程</a>
                <a href="javascript:;" class="btn reg-btn">付款方式</a>
                <a href="javascript:;" class="btn reg-btn tel"><i class="telicon"></i>0769-878-5555</a>
            </div>
        </div>
    </div>
    <div class="sncont">
    <a href="#" class="logo">
        <img src="/Public/img/logoandtext.png"/>
    </a>
    <ul class="navul">
        <li <?php if($active == "index"){echo 'class="active"';}?>><a href="/">首页</a></li><i></i>
        <li <?php if($active == "lilian"){echo 'class="active"';}?>><a href="/products/lilian/">服务器租用</a></li><i></i>
        <li <?php if($active == "gaofang"){echo 'class="active"';}?>><a href="/products/gaofang/">服务器托管</a></li><i></i>
        <li <?php if($active == "server"){echo 'class="active"';}?>><a href="/products/server/">解决方案</a></li><i></i>
        <li <?php if($active == "visitus"){echo 'class="active"';}?>><a href="/products/visit/">参观机房</a></li><i></i>
        <li <?php if($active == "contact"){echo 'class="active"';}?>><a href="/products/contact/">关于我们</a></li>
    </ul>
    <form id="sform" action="#" method="get">
        <input type="text" placeholder="输入..."/><i></i>
        {__TOKEN__}
    </form>
    </div>
</div>
<div id="rbar">
    <ul class="rbul top">
        <li class="qp">
            <div class="qqicon"></div>
            <p class="contact">点击咨询</p>
            <div class="rtab">
                    <h4>客服QQ</h4>
                    <ul class="ful left">
                        <li target-qq="613669588"><i></i>销售总监-华</li>
                        <li target-qq="613669599"><i></i>销售经理-梅</li>
                        <li target-qq="613669595"><i></i>销售客服-琪琪</li>
                        <li target-qq="613669597"><i></i>销售客服-娟娟</li>
                        <li target-qq="613669589"><i></i>销售客服-琳</li>
                        <!--<li target-qq="613669594"><i></i>售前7</li>-->
                    </ul>
                    <ul class="ful right">
                        <li target-qq="613669590"><i></i>销售客服-小美</li>
                        <li target-qq="613669596"><i></i>销售客服-小婷</li>
                        <li target-qq="613669591"><i></i>销售客服-文</li>
                        <li target-qq="613669592"><i></i>销售客服-小爱</li>
                        <li target-qq="613669593"><i></i>销售客服-君君</li>
                    </ul>
                    <h4>故障申报处理</h4>
                    <ul>
                        <li target-qq="613669582"><i></i>24小时技术</li>
                        <li target-qq="613669583"><i></i>24小时技术</li>
                    </ul>
                    <h4>域名白名单,备案咨询</h4>
                    <dl>
                        <dt target-qq="613669578"><i></i>白名单审核</dt>
                        <dd></dd>
                        <dt target-qq="613669579"><i></i>备案专员</dt>
                        <dd></dd>
                    </dl>
                    <h4>财务续费、发票</h4>
                    <dl>
                        <dt target-qq="613669580"><i></i>财务</dt>
                        <dt target-qq="613669581"><i></i>财务续费</dt>
                    </dl>
                    <h4>投诉、建议</h4>
                    <ul><li target-qq="613669586"><i></i>企业技术支撑</li></ul>
            </div>
        </li>
        <li class="tp">
            <div class="telicon"></div>
            <p class="tel">服务热线</p>
            <div class="rtab telnum">
            <p class="fp">0769-878-55555</p>
                <p>15382809627</p>
            </div>
        </li>

    </ul>
    <ul class="rbul bottom">
        <li class="barcode"></li>
        <li class="gototop"></li>
        <li class="close"></li>
    </ul>
</div>
<div id="showup">
    <div id="suicon"></div>
</div>
<img src="/Public/img/contacttop.png"/>
<!-- 产品内容-->
<div class="content ctus-cont">
    <ul class="ctul">
        <li data-target="tab1" class="conli active"></li
        ><li data-target="tab2" class="conli"></li
        ><li data-target="tab3" class="conli"></li
        ><li data-target="tab4" class="conli"></li
        ><li data-target="tab5" class="conli"></li
        ><li data-target="tab6" class="conli"></li
        ><li data-target="tab7" class="conli"></li
        ><li data-target="tab8" class="conli"></li>
    </ul>
    <!-- 公司介绍 -->
    <div class="shtabs active" id="tab1">
        <div class="text1">
        <h3>广东利联科技有限公司</h3>
        <p>利联网络，全称：广东利联科技有限公司，isp证号：粤ICP备******，初创于2004年。利联从事的行业是通讯行业中的互联网接入服务，为国内各大信息服务提供商
            、网络文化传播、媒体、传统行业信息化等类型的企业提供服务。</p>
        <p>利联始终致力于为客户提供优质的网络环境、接入带宽及高稳定性的网络服务，为此，我们已建立了多点7*24小时的服务机构，其中包括：7*24小时的客户服务中心，7*24
            小时的网管中心，7*24小时的安全中心以及大多数IDC机房的7*24小时现场驻点工程师。利联的售后服务团队占公司人数的30%，技术团队占40%其余的分别为销售团队及其它后勤服务人员，
            我们目前在售后服务上已经取得了一定的成绩，但我们仍然在不断的努力改进，追求极致。我们推出的每一项服务，都本着客户至上的原则，我们每一个前进的脚步，都充分体现了对客户
            的尊重与关怀。面对未来，我们承诺在保持现有优势的基础上，为客户提供更全面、更优质的互联网接入服务。</p>
        <p>利联倡导“诚信”的企业经营理念，无论对客户、对员工、还是第三方合作方，我们都始终秉承诚信的合作态度。利联网络的服务目标是“诚心、诚信”的贴心优质服务。
            我们坚持以人为本，鼓励员工充分发挥他们的才智和潜能，并尽一切力量为员工提供施展才能的机会，使他们与利联提供的通讯服务，能够长久屹立在行业的尖端。</p>
        <h2 style="text-align: right;">相信利联,有您,有利联.</h2>
        </div>
        <!--<div class="text2">
        <h3>董事长致辞</h3>
        <p>在日新月异的市场变化中，广东利联网络有限公司秉承着一贯踏实进取的做事风格，致力于在公司主体业务上做深、做透、做强、做大，为社会丰富多彩的网络生活，为智
            慧中国、数字中国、平安中国竭诚服务，逐步成为一个受人尊敬、有价值的公司。这不仅是我们的使命和未来愿望，更是我们每一利联人士为之女里的强大动源。</p>
        <p>广东利联网络有限公司是一个崇尚科技，尊重人才的公司，公司认为我们最大的核心竞争力就是我们每一个不管创新与奋斗的利联人士，我们更愿意为这些公司为之骄傲的
            同事们，努力营造轻松、和谐的氛围，通过积极完善独特、合理的管理模式，创造一个可以最大限度发挥平台，让我们的同事可以“快乐工作，幸福生活”。</p>
        <p>作为一个具有社会责任感的公司，我们深感肩上的责任重大，无论是技术的创新，新业务的拓展，还是人才培养等都时时刻刻提醒着我们。如何在残酷的市场变化中立于不
            败之地，是我们管理者需要持续思考的课题。但是同时，我们也对次充满了信心，只要坚持我们的理念，实施科学的战略，付出更多的努力。在新的挑战和机遇面前广东利联网络有限公司
            必将会创造卓越，勇往直前。</p>
        <h2 style="text-align: right;">广东利联网络有限公司董事长 ***</h2>
        </div>-->

    </div>

    <!-- 资质证书-->
    <div class="shtabs" id="tab3">
        <ul>
            <li><img src="/Public/img/333_03.png" alt=""></li>
            <li><img src="/Public/img/333_05.png" alt=""></li>
            <li><img src="/Public/img/333_07.png" alt=""></li>
        </ul>
    </div>
    <!-- 员工风采-->
    <div class="shtabs" id="tab4">
        <p>员工风采</p>
    </div>
    <!-- 新闻资讯-->
    <div class="shtabs" id="tab5">
        <ul class="nul">
            <li data-target="news-tab1" class="nli active">利联动态</li>
            <li data-target="news-tab2" class="nli">最新公告</li>
            <li data-target="news-tab3" class="nli">新闻资讯</li>
        </ul>
        <div id="news-tab1" class="news-sub-shtabs active">
            <ul class="ndul">
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_01.png"/>
                        <h4>利联网络新版官网上线通知</h4>
                        <p>尊敬的各位用户：您好！首先感谢大家长期
                            以来对利联网络的关心和支持！ 2016年12
                            月02日利联网络迎来了一次历史性的变革。</p>
                        <p class="date">2016-12-02</p>
                    </div>
                </li>
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_02.png"/>
                        <h4>关于2015年中秋节和国庆节的放假
                            通知</h4>
                        <p>关于2015年中秋节和国庆节的放假通知尊敬
                            的客户：您好！根据国家规定， 结合实际情
                            况，我司将中秋节和国庆节假期安排如下：</p>
                        <p class="date">2016-12-02</p>
                    </div>
                </li>
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_03.png"/>
                        <h4>第十一届中国IDC产业年度大典在
                            京盛大开</h4>
                        <p>2016年，我国数据中心产业持续快速发展，
                            各地大型数据中心相继崛起；越来越多IDC
                            企业在国内外成功上市；地产、金融等行业</p>
                        <p class="date">2016-12-02</p>
                    </div>
                </li>
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_03.png"/>
                        <h4>第十一届中国IDC产业年度大典在
                            京盛大开</h4>
                        <p>2016年，我国数据中心产业持续快速发展，
                            各地大型数据中心相继崛起；越来越多IDC
                            企业在国内外成功上市；地产、金融等行业</p>
                        <p class="date">2016-12-02</p>
                    </div>
                </li>
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_03.png"/>
                        <h4>第十一届中国IDC产业年度大典在
                            京盛大开</h4>
                        <p>2016年，我国数据中心产业持续快速发展，
                            各地大型数据中心相继崛起；越来越多IDC
                            企业在国内外成功上市；地产、金融等行业</p>
                        <p class="date">2016-12-02</p>
                    </div>
                </li>
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_03.png"/>
                        <h4>第十一届中国IDC产业年度大典在
                            京盛大开</h4>
                        <p>2016年，我国数据中心产业持续快速发展，
                            各地大型数据中心相继崛起；越来越多IDC
                            企业在国内外成功上市；地产、金融等行业</p>
                        <p class="date">2016-12-02</p>
                    </div>
                </li>
            </ul>
        </div>
        <div id="news-tab2" class="news-sub-shtabs">
            <ul class="ndul">
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_01.png"/>
                        <h4>张寰：高水平集约式和体系化引领
                            未来IDC产业</h4>
                        <p>12月20日报道，12月20-22日，第十一届中
                            国IDC产业年度大典 （IDCC2016） 在北京
                            国家会议中心隆重召开。</p>
                        <p class="date">2016-12-02</p>
                    </div>

                </li>
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_02.png"/>
                        <h4>优化机架配电-为您的数据中心环境
                            选择最合适的机架配电装置的最佳
                            方案</h4>
                        <p>随着数据信息日益成为许多企业组织背后最
                            为强大的驱动力，数据中心现在业已成为了
                            企业业务成功运营的基础。在这种环境下，
                            峰值期</p>
                        <p class="date">2016-12-02</p>
                    </div>
                </li>
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_03.png"/>
                        <h4>2015年中国IDC市场规模达518.6亿
                            元</h4>
                        <p>据该报告数据显示，2015年中国IDC市场延
                            续了高速增长态势， 市场总规模达到518.6
                            亿元人民币，同比增长39.3</p>
                        <p class="date">2016-12-02</p>
                    </div>
                </li>
            </ul>
        </div>
        <div id="news-tab3" class="news-sub-shtabs">
            <ul class="ndul">
                <li>
                    <div class="ncont">
                        <img src="/Public/img/news_01.png"/>
                        <h4>中国数据中心联盟华南区工作委员
                            会正式成立</h4>
                        <p>文章摘自腾讯大粤网，原文标题：中国数据
                            中心联盟华南区工作委员会主席团名单出炉
                            7月17日，中国数据中心产业发展联盟华南
                            区工</p>
                        <p class="date">2016-12-02</p>
                    </div>

                </li>

            </ul>
        </div>
    </div>
    <!-- 商务合作-->
    <div class="shtabs" id="tab6">
        <ul class="corpul">
            <li class="odd">
                <div class="cimg li1"></div>
                <div class="details">
                    <h3>商务合作</h3>
                    <p>利联网络为有志在互联网基础业务领域深耕细作的企业提供了良好的运营条件和丰
                        富资源，并提供高水平、高效率的技术支持和客户服务。诚征精诚合作，倡导互惠
                        共赢。</p>
                    <p>合作要求：</p>
                    <ul class="dotul">
                        <li> 1. 具有互联网业务基础知识和相关业务的销售经验</li>
                        <li> 2. 具有工商营业执照等业务合法经营资格</li>
                        <li> 3. 具有出色的行业推广和客户服务能力</li>
                        <li>4. 对客户重承诺，守信用，忠于并时刻维护代理品牌的公司形象</li>
                        <li> 5. 在互联网行业内具有很好的用户基础</li>
                    </ul>
                </div>
            </li>
            <li class="even">

                <div class="details">
                    <h3>宣传合作</h3>
                    <p>无论是IDC，还是网站建设，只要您稍有研究，就会看到或听到利联网络的名字。
                        在这个领域里，利联网络已经深耕细作了3年，我们的资源、我们的产品、我们的
                        服务、我们的品牌，每一个都是市场高度关注的亮点，我们期望这些亮点能够通过
                        您的平台反射到互联网的每一个角落，同时也能装点您的无限远景。</p>
                    <p>合作对象：</p>
                    <ul class="dotul">
                        <li> 1. IT行业内报纸杂志媒体</li>
                        <li> 2. IT行业内网站</li>
                        <li> 3. 各种与IT行业相关的大型会议，展览，论坛等活动组织</li>
                    </ul>
                </div>
                <div class="cimg li2"></div>
            </li>
            <li class="odd">
                <div class="cimg li3"></div>
                <div class="details">
                    <h3>资源合作</h3>
                    <p>3年前，利联网络以专业的IDC服务商形象进入互联网市场，如今， 利联网络已经
                        发展成为专业的互联网业务平台提供商，汇集海量的电信和互联网资源，为分布在
                        全国各地的客户提供“一站式”服务，本着资源共享、互惠互利的原则，利联网络
                        积极寻求与合作伙伴的共同发展。 资源有限，发展无界，  利联网络期待更多的合
                        作伙伴加入资源共享计划</p>
                    <p>合作对象：</p>
                    <ul class="dotul">
                        <li> 1. 各大基础电信运营商IDC资源</li>
                        <li> 2. 各大系统内网络、卫星通讯网、无线网络、3G网络资源</li>
                        <li> 3. 各大ISP带宽机房资源</li>
                    </ul>
                </div>
            </li>
            <li class="even">

                <div class="details">
                    <h3>销售服务</h3>
                    <p>利联网络是国内领先的互联网业务平台提供商，持有中华人民共和国信息产业部颁
                        发的省市经营增值电信业务（IDC、ISP）经营许可证；  利联网络面向国内外用户
                        提供包括数据中心业务（IDC）主机租用业务、专线组网业务等方面的专业服务。</p>
                    <p>服务对象：</p>
                    <ul class="dotul">
                        <li> 1. 对主机托管、主机租用以及专线接入有购买需求的客户</li>
                        <li> 2. 希望了解利联网络产品、技术、解决方案的客户</li>
                        <li> 3. 利联网络代理商、合作伙伴、媒体报道</li>
                    </ul>

                </div>
                <div class="cimg li4"></div>
            </li>
        </ul>

    </div>

    <!-- 支付方式-->
    <div class="shtabs"id="tab7" style="text-align: center;">
            <div class="pmcont">
            <ul class="left icbc">
                <li></li>
            </ul>
            <ul class="right">
                <li>工商银行</li>
                <li>开户名称:闭健龙</li>
                <li>银行账号:6212262010028109822</li>
                <li>开户银行：中国工商银行东莞市常平支行</li>
            </ul>
        </div>
        <div class="pmcont">
            <ul class="left cbc">
                <li></li>
            </ul>
            <ul class="right">
                <li>建设银行</li>
                <li>开户名称:闭健龙</li>
                <li>银行账号:6227003230310150118</li>
                <li>开户银行：中国建设银行东莞市常平汇众支行</li>
            </ul>
        </div>
        <div class="pmcont">
            <ul class="left alp">
                <li></li>
            </ul>
            <ul class="right">
                <li>支付宝</li>
                <li>账户名称：613669580@qq.com</li>
                <li>账户名称：闭健龙</li>
            </ul>
        </div>
        <div class="pmcont">
            <ul class="left cft">
                <li></li>
            </ul>
            <ul class="right">
                <li>财付通</li>
                <li>账户名称：613669580</li>
                <li>账户名称：闭健龙</li>
            </ul>
        </div>
        <div class="pmcont">
            <div id="wxpay"></div>
        </div>
        <!--<img src="/Public/img/payment.png" style="width: 1000px"/>
        <ul>
            <li>
                <div class="topimg bk1"></div>
                <div class="details">
                    <p>开户银行:工商银行</p>
                    <p>账号名称:闭健龙</p>
                    <p>银行支行:东莞常平支行</p>
                    <p>卡号:6212262010028109822</p>
                </div>
            </li>
            <li>
                <div class="topimg bk2"></div>
                <div class="details">
                    <p>支付宝</p>
                    <p>账号:15322935395</p>
                    <p>闭健龙</p>
                </div>
            </li>
            <li>
                <div class="topimg bk3"></div>

                <div class="details">
                    <p>开户银行:建设银行</p>
                    <p>账号名称:闭健龙</p>
                    <p>银行支行:东莞常平汇众支行</p>
                    <p>卡号:6227003230310150118</p>
                </div>
            </li>
            <li>
                <div class="topimg bk4"></div>

                <div class="details">
                    <p>支付宝</p>
                    <p>账号:15322935395</p>
                    <p>闭健龙</p>
                </div>
            </li>
            <li>
                <div class="topimg bk5"></div>
                <div class="details">
                    <p>支付宝</p>
                    <p>账号:15322935395</p>
                    <p>闭健龙</p>
                </div>
            </li>
            <li>
                <div class="topimg bk6"></div>

                <div class="details">
                    <p>开户名称:***</p>
                    <p>银行账号:****************</p>
                    <p>开户银行:********************************</p>
                </div>
            </li>
            <li style="height: 160px;">
                <div class="topimg bk7"></div>

                <div class="details" style="text-align: center;padding:0;margin-top:5px;">
                    <img src="/Public/img/wxpay.png" style="width: 100px"/>
                </div>
            </li>
            <li id="bklast">
                <div class="topimg bk8"></div>

                <div class="details">
                    <p>财付通</p>
                    <p>账号:613669580</p>
                    <p>闭健龙</p>
                </div>
            </li>
        </ul>-->
    </div>
    <!--联系我们 -->
    <div class="shtabs" id="tab8">
        <img class="limg" src="/Public/img/location.png"/>
            <ul class="ctul">
                <li class="tel">
                    <i></i>
                    <div class="details">
                    <p>总机热线:******</p>
                    <p>投诉热线:******</p>
                    <p>24小时售后网维:******</p>
                    <p>总机:******</p>
                    <p>网维热线:*******</p>
                    <p>值班热线:******</p>
                    </div>
                </li>
                <li class="mail">
                    <i></i>
                    <div class="details">
                    <p>邮箱:********</p>
                    <p>企业网站:********</p>
                </div>
                </li>
                <li class="add">
                    <i></i><div class="details">
                    <p>广东省东莞市东城区东昇路33号
                        三十三小镇文化创意产业园29栋3楼B325</p>
                </div>
                </li>
            </ul>
    </div>

</div>
<!-- 发展历程 -->
<div class="shtabs" id="tab2">
    <div class="cont">
    <div class="topbar"></div>
    <ul class="lcul">
        <li data-target="sub-lctab1" class="lcli active"></li>
        <li data-target="sub-lctab2" class="lcli"></li>
        <li data-target="sub-lctab3" class="lcli"></li>
        <li data-target="sub-lctab4" class="lcli"></li>
        <li data-target="sub-lctab5" class="lcli"></li>
        <li data-target="sub-lctab6" class="lcli"></li>
    </ul>
    <div class="sub-shtabs active" id="sub-lctab1">
        <ul>
            <li>12月，凭借良好的防御能力及带宽资源，乐视网正式与利联网络签订了长期战略合作伙伴协议。</li>
            <li>12月，抗拒绝服务攻击保护系统升级到40G，为更好的服务公司客户，利联网络在佛山顺德机房成立了专门的运维中心，
                <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;德胜机房跻身为国内领先的流量攻击保护机房。</li>
            <li>11月，利联网络正式运营佛山电信德胜机房，德胜机房拥有20G抗拒绝服务攻击保护能力。</li>
            <li>10月，利联网络正式与广东电信佛山分公司签订协议，并进入佛山顺德机房。</li>
            <li>10月，利联网络获得广东省通管局颁发《中华人民共和国增值电信业务许可证》，同时拥有ICP/ISP/IDC/SP四种经营许可证，
                <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;强势进军互联网基础业务行列。</li>
            <li>6月，东莞市利联网络有限公司正式成立，公司办公地点设立于东莞市东城区联合大厦，利联网络倡导“诚信”的企业经营理念，
                <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;无论对客户、对员工、还是对第三方合作方，我们都始终秉承诚信的合作态度。</li>
        </ul>
    </div>
    <div class="sub-shtabs" id="sub-lctab2">
        <ul>
            <li>11月，奇虎360与利联网络签订长期战略合作协议。</li>
            <li>10月，利联网络投入巨资，对德胜机房将进行抗拒绝服务攻击保护系统升级，及流量清洗设备架设，将抗拒绝服务攻击
                <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;保护系统防御提升至100G，并架设40G流量清洗设备，总防御能力达到140G。</li>
            <li>7月，利联网络对德胜机房核心抗拒绝服务攻击保护系统进行换代升级，抗拒绝服务攻击保护系统全部更换为“中新金盾”，
                <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;同时防御能力升级至80G。</li>
            <li>4月，利联网络员工增加至40余人。</li>
            <li>3月，利联网络为完善服务体系，正式启动24小时客户服务，用心服务每一天。</li>
            <li>1月，利联网络因业务发展需求，团队扩展人数达到25余人，并初步制定了公司组织架构、管理流程、规章制度等
                <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;内部管理措施。</li>
        </ul>
    </div>
    <div class="sub-shtabs" id="sub-lctab3">
        <ul>
            <li>11月，“东莞市利联网络有限公司”变更为“广东利联网络有限公司”。</li>
            <li>9月，德胜机房流量清洗设备升级防御能力至80G，总防御能力达240G。</li>
            <li>7月，德胜机房抗拒绝服务攻击保护系统升级至160G，总防御达200G，成为业内流量攻击保护能力最强的网络供应商。</li>
            <li>6月，利联网络员工超过100人，利联网络大步迈向IDC行业的顶端。</li>
            <li>5月，利联网络办公地址从东城区乔迁至南城区高盛科技园，办公场所占地面积达1300平方米</li>
            <li>3月，德胜机房抗拒绝服务攻击系统升级至120G，总防御能力达160G。</li>
            <li>1月，春节前夕，利联网络在高盛科技园员工之家举行年终晚会，在晚会上，利联网络董事长和总经理分别致辞。
                <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在年会上，公司评选了2012年度“利联之星”优秀员工，并颁发了奖金和奖状。</li>
        </ul>
    </div>
    <div class="sub-shtabs" id="sub-lctab4">
        <ul>
            <li>4月，我司荣获第七届中国数据中心大会颁发的《2014年度中国高能效数据中心优秀产品》奖项。— 详情</li>
            <li>1月，公司成立了云事业部，专门负责云服务业务的运营。</li>
            <li>1月，春节前夕，利联网络在东莞市悦景酒店举行了年终晚会，利联网络以视频形式向全国各界客户进行了网络拜年。</li>
        </ul>
    </div>
    <div class="sub-shtabs" id="sub-lctab5">
        <ul>
            <li>3月，广东利联网络有限公司广州分公司正式挂牌成立。</li>
            <li>1月，春节前夕，利联网络在东莞市富盈美爵大酒店举行了年终晚会，所有部门均载歌载舞表达祝愿公司步入新的时代！</li>
        </ul>
    </div>
    <div class="sub-shtabs" id="sub-lctab6">
        <ul>
            <li>3月，广东利联网络有限公司荣获中国计算机报2016年中国数据中心最具影响力企业奖</li>
        </ul>
    </div>
    </div><!-- cont -->
</div>
<!-- 加载底部模板文件-->
﻿
<div id="footer">
    <div class="content">
        <div class="about-lilian">
            <h3>关于利联</h3>
            <i></i>
        <ul>
            <li><a href="javascript:;">利联简介</a></li>
            <li><a href="javascript:;">企业文化</a></li>
            <li><a href="javascript:;">企业资质</a></li>
            <li><a href="javascript:;">发展历程</a></li>
            <li><a href="/products/contact/">联系我们</a></li>
        </ul>
            <div class="rline"></div>
        </div>
        <div class="our-products">
            <h3>服务指南</h3>
            <i></i>
            <ul>
                <li><a href="/products/lilian/">注册与登陆</a></li>
                <li><a href="/products/lilian/">购买流程</a></li>
                <li><a href="/products/gaofang/">支付方式</a></li>
                <li><a href="javascript:;">服务协议</a></li>
            </ul>
            <div class="rline"></div>
        </div>
        <div class="our-service">
            <h3>技术支持</h3>
            <i></i>
            <ul>
                <li><a href="javascript:;">24H售后服务标准</a></li>
                <li><a href="javascript:;">备案中心</a></li>
                <li><a href="javascript:;">常见问题</a></li>

            </ul>
            <div class="rline"></div>
        </div>
        <div class="about-us">
            <h3>关于我们</h3>
            <i></i>
            <ul>
                <li><a href="/products/contact/">公司简介</a></li>
                <li><a href="products/contact/">企业资质</a></li>
                <li><a href="products/contact/">商务合作</a></li>
                <li><a href="products/contact/">联系我们</a></li>
            </ul>
            <div class="rline"></div>
        </div>
        <div class="contact-us">
            <h3>关于我们</h3>
            <i></i>
            <label>服务热线:</label>
            <p>+86 0769-878-55555(总机)</p>

                <label>通讯地址:</label>
            <p>广东省东莞市东城区东昇路33号</p>
            <p>三十三小镇文化创意产业园29栋3楼B325</p>

        </div>

    </div>
</div>
<div class="copyright">
    <p>Copyright©2016  广东省利联网络科技有限公司版权所有</p>
    <p>ISP许可证:粤B2-20051022 备案号:粤ICP备 ****** 粤公网安备********号</p>
</div>
<!-- body 最后 -->
<script type="text/javascript" src="/Public/js/jquery-1.9.1.min.js?v=20170209"></script>
<script type="text/javascript" src="/Public/js/custom.js?v=20170209"></script>

<script type="text/javascript">
    $.switchTabs(".ctus-cont .ctul li.conli","click","data-target",".shtabs","active");
    $.switchTabs(".ctus-cont ~ .shtabs .lcul .lcli","click","data-target",".sub-shtabs","active");
    $.switchTabs(".ctus-cont .shtabs#tab5 ul.nul li","click","data-target",".news-sub-shtabs","active");
</script>

</body>
</html>