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
                $(".subnav").css({"position":"fixed","z-index":"9999"});
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
        $("#rbar .rbul .qp .rtab ul li,#rbar .rbul .qp .rtab dl dt").on("click",function(){
            var qq = $(this).attr("target-qq");
            var url = "http://wpa.qq.com/msgrd?v=3&uin="+qq+"&site=qq&menu=yes";
            window.open(url, '_blank');
        });
    }
//#talktokf
    $(".talktokf,.products .hpul li,.products li[class^=p] a.right").on("click",function(){
        //选择任一客服
        var qq=$($("#rbar .rbul .qp .rtab ul.ful li")[Math.ceil(Math.random()*$("#rbar .rbul .qp .rtab ul li").length)]).attr("target-qq");
        var url = "http://wpa.qq.com/msgrd?v=3&uin="+qq+"&site=qq&menu=yes";
        window.open(url, '_blank');
    });
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

    //Ie系列浏览器不应用scrollreveal
    if(!$.checkIfIe()){
        window.sr = new ScrollReveal({ reset: true, move: '100px'});//修正IE8的BUG
        $(".content ul li").each(function(){
            if($(this).width()>=450){
                //$(this).addClass("reveal");
            }
        });
        //添加额外样式
        $(".products .pul li[class^=p],.products .hpul li[class^=hp]").each(function(){
            $(this).addClass("reveal");
        })
        sr.reveal(".reveal",$.intro);
        $("#showup ~ img").each(function(){
            if($(this).width()>1024 & $("body").find(".unslider").length!=1){$(this).addClass("imgrv")};
        });
        sr.reveal(".imgrv",$.hero);
    }


});

