//前端样式类
(function($){
    $.autotips=function(selector,text,cover){
        var cover = cover || true;
        if (cover) {
            $(selector).html(text);
            $(selector).show();
            setTimeout(function () {
                $(selector).fadeOut("slow");
            }, 4000);
            return;
        } else {
            if ($(selector).text().length > 1) {
                $(selector).show();
            } else {
                $(selector).html(text);
                $(selector).show();
            }
            setTimeout(function () {
                $(selector).fadeOut("slow");
            }, 4000);
        }
    }
})($);

+function($){
    $.indexPriceTabs=function() {
        //价格列表tab js部分,改为点击
        if($.checkIfIe()){
            $(".ptabs li.loca").on("click", function () {
                if ($(this).hasClass("active"))return;
                $(this).addClass("active").siblings().removeClass("active");
                $(this).find(".tabs ul li.lines.active").removeClass("active");
                $(this).find(".tabs ul li.lines:first").addClass("active");
            });
            //次级标签hover事件
            $(".tabs ul li.lines").on("click",function(){
                if($(this).hasClass("active")) return;
                $(this).addClass("active").siblings().removeClass("active");
            });
        }else{
            $(".ptabs li.loca").on("mouseenter", function () {
                if ($(this).hasClass("active"))return;
                $(this).addClass("active").siblings().removeClass("active");
                $(this).find(".tabs ul li.lines.active").removeClass("active");
                $(this).find(".tabs ul li.lines:first").addClass("active");
            });
            //次级标签hover事件
            $(".tabs ul li.lines").on("mouseenter",function(){
                if($(this).hasClass("active")) return;
                $(this).addClass("active").siblings().removeClass("active");
            });
        }
    }
}($);
//用于产品页面标签切换
+function($){
    $.switchTabs=function(classname,event,target,shtabs,active){
        $(classname).on(event,function(){
            if($(this).hasClass(active)) return;
            $(this).addClass(active).siblings().removeClass(active);
            if($(shtabs+"."+active))$(shtabs+"."+active).removeClass("active");
            $(shtabs).hide();
            var tab = $(this).attr(target);
            $("#"+tab).fadeIn("3000");
        });
    }
    }($);
//滚动时固定导航条
+function($){
    $.fixNavBar=function(){
        $(window).on("scroll",function(){
            if($(window).scrollTop()>=52){
                $(".subnav").css({"position":"fixed","z-index":"9999","top":0});
            }else{
                $(".subnav").css({"position":"relative","z-index":''});
            }
        })
    }
}($);
//到顶
+function($){
    $.gotoTop=function(){
        $("#rbar .gototop").hover(function(){
            $("body").animate({scrollTop:0});
        });
    }
}($);
//隐藏侧边栏
+function($){
    $.hideSb=function(){
     $("#rbar .close").hover(function(){

         $("#rbar").animate({right:-40}, 500);
         $("#showup").show();
     })
    }
}($);
//展示侧边栏
+function($){
   $.showRpanel=function () {
       $("#showup").on("click",function(){
           $(this).fadeOut();
           $("#rbar").animate({right:0},500);
       });
   }
}($);
//首页侧边栏QQ显示
+function($){
    $.showQQpanel=function(){
        $("#rbar .rbul.top > li").on("mouseenter",function(){
            $(this).hasClass("qp")?$("#rbar .qp .qqicon").addClass("active"):$(this).hasClass("tp")?$("#rbar .tp .telicon").addClass("active"):"";
            $(this).find(".rtab").addClass("active");
           $(this).css({"background-color":"#fff","color":"#79a8f2"});
        }).on("mouseleave",function(){
            $(this).hasClass("qp")?$("#rbar .qp .qqicon").removeClass("active"):$(this).hasClass("tp")?$("#rbar .tp .telicon").removeClass("active"):"";
            $(this).find(".rtab").removeClass("active");
            $(this).css({"background-color":"#79a8f2","color":""});
        });
}
}($);
//QQ客服
+function($){
    $.talktoUs=function(){
        $("#rbar .rbul .qp .rtab ul li,#rbar .rbul .qp .rtab dl dt,.ctus-cont #tab8 .ct-table tr td i.qqicon").on("click",function(){
            var qq = $(this).attr("target-qq");
            var url = "http://wpa.qq.com/msgrd?v=3&uin="+qq+"&site=qq&menu=yes";
            window.open(url, '_blank');
        });
    }
//#talktokf
    $(".talktokf,.products .hpul li,.products li[class^=p] a.right,.product-desc .details span,.news .cservice ul li").on("click",function(){
        //选择任一客服
        $.talktoAny();
    });
}($);
+function($){
    $.talktoAny = function(){
        var qq=$($("#rbar .rbul .qp .rtab ul.ful li")[Math.ceil(Math.random()*$("#rbar .rbul .qp .rtab ul li").length)]).attr("target-qq");
        var url = "http://wpa.qq.com/msgrd?v=3&uin="+qq+"&site=qq&menu=yes";
        window.open(url, '_blank');
    }
}($);
//hover tab
+function($){
    $.hoverTab = function (selector,parent) {
        var h = 0;
        $(selector).each(function(index,item){
            $(this).on("mouseenter",function(){
                if($(this).hasClass("active")){return;}
                $(this).addClass("active").siblings().removeClass("active");
                h>0?$(selector).eq($(selector).length-1).remove():"";
                var dom = $(this).outerHTML();
                var left = index==4?index*$(this).width()+47:index*$(this).width()+43;
                var top =$(this).offset().top;
                $(parent).append(dom);
                $(selector+".active").eq(1).find(".pbox .top").css("background-color","#0498f7");
                $(selector+".active").eq(1).find("h4").css("color","#fff");
                $(selector+".active").eq(1).find(".pbox .top p").css("color","#fff");
                $(selector+".active").eq(1).find(".pbox button").css({"background-color":"#0498f7","color":"#fff"});
                $(".pdesc .ptli button").click(function(){
                    $.talktoAny();
                });
                index==4?$(selector+".active").eq(1).css({"position":"absolute","border-color":"#b4eeff","box-shadow":"1px 1px 1px 1px #b4eeff","width":$(this).width()+20,"left":left-10,"top":-20,"height":364}):$(selector+".active").eq(1).css({"position":"absolute","border-color":"#b4eeff","box-shadow":"1px 1px 1px 1px #b4eeff","width":$(this).width()+20,"left":left-10,"top":-20,"height":364});
            }).on("mouseleave",function(){
                $(selector+".active").eq(0).removeClass("active");
                $(selector+".active").eq(1).remove();
                h+=1;
            });
        });

    }
}($);
//兼容性
+function($){
    $.placeHoldercp=function(){
        (function ($) {
            $.support.placeholder = ('placeholder' in document.createElement('input'));
        })(jQuery);
        //fix for IE7 and IE8
        $(function () {
            if (!$.support.placeholder) {
                $("[placeholder]").focus(function () {
                    if ($(this).val() == $(this).attr("placeholder")) $(this).val("");
                }).blur(function () {
                    if ($(this).val() == "") $(this).val($(this).attr("placeholder"));
                }).blur();

                $("[placeholder]").parents("form").submit(function () {
                    $(this).find('[placeholder]').each(function() {
                        if ($(this).val() == $(this).attr("placeholder")) {
                            $(this).val("");
                        }
                    });
                });
            }
        });
    }
}($);
//add outerHtml to jquery
(function($) {
    $.fn.outerHTML = function () {
        return $(this).clone().wrap('<div></div>').parent().html();
    };
})($);
//fixed nav ul
+function($){
    $.fixNavUl = function(){
        //fix nav ul lis and ul lis goes parallelly on scroll
        $(document).on("scroll",function(){
                    var lis = [];
                    $("li[id^=ct],th[id^=state]").each(function(i,t){
                    lis.push($(this).offset().top- $(window).scrollTop());//offset().top will change on scroll
                    });
            if($(window).scrollTop() > 300 && $(window).scrollTop() < $(document).height()-500){
                $(".as-service ul.nul").css({"position":"fixed","right":($(document).width()-1200)/2+78});
                $(".service-contract ul.nul").css({"position":"fixed","right":($(document).width()-1200)/2});
                $("li[id^=ct],th[id^=state]").each(function(i,t){
                    if( $(window).scrollTop() > $(this).offset().top-100 && $(window).scrollTop() < $(this).offset().top+$(this).height()+100){
                        var index = lis.indexOf($(this).offset().top- $(window).scrollTop());
                        var that = $(".as-service ul.nul li,.service-contract ul.nul li").eq(index);
                        that.addClass("active").siblings().removeClass("active");
                    }
                });
            }
            if($(document).height()>2000){
                if($(window).scrollTop()<300 || $(window).scrollTop() > $(document).height()-1000){
                $(".as-service ul.nul,.service-contract ul.nul").css({"position":"","right":""});
            }
            }else{
                if($(window).scrollTop()<300 || $(window).scrollTop() > $(document).height()-500){
                $(".as-service ul.nul,.service-contract ul.nul").css({"position":"","right":""});
            }
            }
        });
    }
}($);
//nav li
+function($){
    $.navLi=function(){
        $(".as-service ul.nul li,.service-contract ul.nul li").click(function(){
            if($(this).hasClass("active")){return}
            $(this).addClass("active").siblings().removeClass("active");
            $("body").animate({scrollTop:$("#"+$(this).attr("data-target")).offset().top-63});
        });
    }
}($);
//检测是否是IE浏览器
+function($){
   $.checkIfIe=function(){
       var ua = window.navigator.userAgent;
       var msie = ua.indexOf("MSIE ");
       return msie>0;
   }
}($);

//立即执行部分
+function($) {
$.fixNavBar();//滚动时固定导航条
//nav as-service li
$.navLi();
//到顶
$.gotoTop();
//隐藏侧边栏
$.hideSb();
//展示侧边栏
$.showRpanel();
//展示QQ面板
$.showQQpanel();
//QQ客服
$.talktoUs();
//兼容性
//placeholder
$.placeHoldercp();

        }($);

//config
+function($){
    //box
    $.intro={
        origin   : "bottom",
        distance : "64px",
        duration : 900,
        delay    : 200,
        scale    : 1
    };
    //img
    $.hero = {
        origin   : "top",
        distance : "24px",
        duration : 1500,
        scale    : 1.05
    };
}($);
//after document ready
$(document).ready(function(){
    //hover tab
    $.hoverTab(".pdesc .ptli",".pdesc");
    //fixed nav
    $.fixNavUl();
    //Ie系列浏览器不应用scrollreveal
    if(!$.checkIfIe()){
        window.sr = new ScrollReveal({ reset: true, move: '100px'});//修正IE8的BUG
        $(".content ul li").each(function(){
            if($(this).width()>=450){
            }
        });
        //添加额外样式
        $(".products .pul li[class^=p],.products .hpul li[class^=hp],#advantage .content .imgcont .right ul li,#service .content .sdesc li").each(function(){
            $(this).addClass("reveal");
        });
        sr.reveal(".reveal",$.intro);
        $("#showup ~ img,#service").each(function(){
            if($(this).width()>1024 && $("body").find(".unslider").length!=1){$(this).addClass("imgrv")}
        });
        sr.reveal(".imgrv",$.hero);
    }
    window.setTimeout(function(){
        $("#showup").click();
    },5000);

    //解决方案部分

});

