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
<img src="/Public/img/visitidc.png"/>
<!-- 产品内容-->
<div class="content visit-cont">
    <div class="topleft">
        <img style="margin-left: -8px;" src="/Public/img/visitus.png"/>
    </div>
    <img class="imgrv" src="/Public/img/visitus01.png"/>
    <img class="imgrv" src="/Public/img/visitus02.png"/>
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
<script type="text/javascript" src="/Public/js/frontend.js?v=20170209"></script>


</body>
</html>