//remove user
(function ($) {
    $.removems = function () {
        $(".machines_tb tr td .remove").click(function (e) {
            e.preventDefault();
            var tid = $(this).parents("tr.mlist").find(".tid").text().trim();
            var that = this;
            var obj = {
                "text": "确认删除该机器?",
                "onConfirm": function () {
                    var url = "/admin/removems/"+tid;
                    var nthat = that;
                    $(".loading").show();
                    $.post(url,{tid:tid,_xsrf:$.getCookie("_xsrf")},function(data){
                        $(".loading").hide();
                        if(data['rs'] == "1028"){
                            $(nthat).parents('tr').children('td, th').animate({padding: 0}).wrapInner('<div />').children().slideUp(function () {
                                    $(nthat).closest('tr').remove();
                                });
                            if ($(".machines_tb tr.mlist").length < 6) {
                                window.location.href = "/admin/all-machines/" + window.location.search;
                                }
                        }else if(data['rs'] == "1029"){
                            console.error(a,b,c,"删除机器失败!");
                        }
                    },"json");

                }
            };
            $.confirm(obj);
        });
    }
})($);
//get xsrf cookie
+function ($) {
    $.getCookie = function (name) {
        var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return r ? r[1] : undefined;
    }
}($);
//popup windows:confirm
+function ($) {
    $.confirm = function (obj) {
        /*
         *object passed to this function is like:
         *obj={
         * text:text,
         * onConfirm:function(){},
         * onCancel:function(){},
         * onClose:function(){}
         * }
         *
         */
        var getobj = {
            text: obj.text,
            onConfirm: function () {
                $(document).on("click", ".modal-ct-cf input.cfbtn", function () {
                    $(".modal-bg.active,.modal-ct-cf.active").removeClass("active");
                    Object.keys(obj).indexOf("onConfirm") && typeof obj.onConfirm === "function" ? obj.onConfirm() : "";//confirm callback
                });
            },
            onCancel: function () {
                $(document).on("click", ".modal-ct-cf input.ccbtn", function () {
                    $(".modal-bg.active,.modal-ct-cf.active").removeClass("active");
                    Object.keys(obj).indexOf("onCancel") && typeof obj.onCancel === "function" ? obj.onCancel() : "";//cancel callback
                });
            },
            onClose: function () {
                $(document).on("click", ".cfclose,.modal-bg.active", function () {
                    $(".modal-bg.active,.modal-ct-cf.active").removeClass("active");
                    Object.keys(obj).indexOf("onClose") && typeof obj.onClose === "function" ? obj.onClose() : "";//cancel callback
                });
            },
            displayModal: function () {
                var modalbg = '<div class="modal-bg active"></div>';
                var modalct = '<div class="modal-ct-cf active"><img id="mclose" class="cfclose" src="/static/img/close.png"><div class="modal-dt-cf"><h3>' + obj.text + '</h3><div class="btn"><input type="button" class="cfbtn" value="确定"/><input type="button" class="ccbtn" value="取消" /></div></div></div>';
                //check if modal bg exists
                !$(".modal-bg").length ? $("body").append(modalbg) : $(".modal-bg").removeClass("transition").addClass("active");
                !$(".modal-ct-cf").length ? $("body").append(modalct) : $(".modal-ct-cf").removeClass("transition").addClass("active");
            }
        };
        for (var i in getobj) {
            if (typeof getobj[i] === "function") {
                getobj[i].call();
            }
        }
    }
}($);


+function ($) {
    $.getCaptcha = function (cc) {
        //获取captcha
        $(cc).click(function () {
            var date = new Date();
            var timestamp = date.getTime();
            var url = "/captcha";
            $.ajax({
                url: url,
                data: {tstamp: timestamp},
                method: "GET",
                dataType: "Json",
                beforeSend: function () {
                    $(cc).html("<img style='width:100px;' src='/static/img/loading.gif'");
                },
                success: function (data) {
                    if (data) {
                        var imgsrc = "<img src=" + data['imgsrc'] + "/>";
                        $(cc).html(imgsrc);
                    }
                }
            });
        });
    }
}($);

//ajax get data from server
+function ($) {
    $.ajaxGet = function (url, valobj, tips, btn, crtext, extext) {
        //data[Object.keys(valobj)[0]] = Object.values(valobj)[0];
        $.ajax({
            url: url,
            data: valobj,
            method: "GET",
            dataType: "JSON",
            success: function (data) {
                if (data["cre"] == 0) {
                    $(tips).addClass("cr").text(crtext);
                    $(btn).css("background-color", "").attr("disabled", false);
                    $.checkField("#rvform", btn);

                } else if (data["cre"] == 1) {
                    $(tips).hasClass("cr") ? $(tips).removeClass("cr") : "";
                    $(tips).text(extext);
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                }
            }
        });
    }
}($);
//validate field of form
+function ($) {
    $.validateField = function (obj) {
        var field = obj.selector, tips = obj.tips, btn = obj.button, exp = obj.regexp, url = obj.cburl, callback = obj.callback, key = obj.cbkey, ngtext = obj.ngtext, crtext = obj.crtext, extext = obj.extext, rqtext = obj.rqtext;
        var pat = new RegExp(exp);
        $(field).on({
            "keyup": function () {
                if (!$(this).val()) {
                    $(tips).hasClass("cr") ? $(tips).removeClass("cr") : "";
                    $(tips).text(ngtext);
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                    return;
                }
                var tval = {};
                var turl = url;
                tval[key] = $(this).val();
                if (pat.test($(this).val())) {
                    if (typeof callback != "function") {
                        $(tips).addClass("cr").text(crtext);
                        $(btn).css("background-color", "").attr("disabled", false);
                        if ($(field).attr("name") == "unpwd") {
                            if ($("input[name=unrpwd]").val().length) {
                                if ($(field).val() != $("input[name=unrpwd]").val()) {
                                    $(tips).removeClass("cr").text("密码不一致.");
                                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                                } else {
                                    $(tips).addClass("cr").text("已经输入密码.");
                                }
                            }

                        }
                        if ($(field).attr("name") == "unrpwd") {
                            if ($(field).val() != $("input[name=unpwd]").val()) {
                                $(tips).removeClass("cr").text("密码不一致.");
                                $(btn).css("background-color", "#ccc").attr("disabled", true);
                            } else {
                                $(tips).addClass("cr").text("密码一致.");
                            }
                        }
                        !$(".regform").length ? $.checkField("#rvform", btn) : $.checkField(".regform", btn);
                        return;
                    }
                    $(tips).addClass("cr").text(crtext);
                    $(btn).css("background-color", "").attr("disabled", false);
                    typeof callback == "function" ? callback(turl, tval, tips, btn, crtext, extext) : "";
                } else {
                    $(tips).hasClass("cr") ? $(tips).removeClass("cr") : "";
                    $(tips).text(rqtext);
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                }
            },
            "blur": function () {
                if (!$(this).val()) {
                    $(tips).hasClass("cr") ? $(tips).removeClass("cr") : "";
                    $(tips).text(ngtext);
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                    return;
                }
                var turl = url;
                var tval = {};
                tval[key] = $(this).val();
                if (pat.test($(this).val())) {
                    if (typeof callback != "function") {
                        $(tips).addClass("cr").text(crtext);
                        $(btn).css("background-color", "").attr("disabled", false);
                        if ($(field).attr("name") == "unpwd") {
                            if ($("input[name=unrpwd]").val().length) {
                                if ($(field).val() != $("input[name=unrpwd]").val()) {
                                    $(tips).removeClass("cr").text("密码不一致.");
                                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                                } else {
                                    $(tips).addClass("cr").text("已经输入密码.");
                                }
                            }

                        }
                        if ($(field).attr("name") == "unrwd") {
                            if ($(field).val() != $("input[name=unpwd]").val()) {
                                $(tips).removeClass("cr").text("密码不一致.");
                                $(btn).css("background-color", "#ccc").attr("disabled", true);
                            } else {
                                $(tips).addClass("cr").text("密码一致.");
                            }
                        }
                        !$(".regform").length ? $.checkField("#rvform", btn) : $.checkField(".regform", btn);
                        return;
                    }
                    $(tips).addClass("cr").text(crtext);
                    $(btn).css({"background-color": "", "color": "#fff"}).attr("disabled", false);
                    typeof callback == "function" ? callback(turl, tval, tips, btn, crtext, extext) : "";

                } else {
                    $(tips).hasClass("cr") ? $(tips).removeClass("cr") : "";
                    $(tips).text(rqtext);
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                }
            }
        });
    }
}($);

+function ($) {
    $.modifypwdsettings = function (selector) {
            var selector = $(selector);
            return {
                "opwd": {
                    "selector": selector.find("input[name=opwd]"),
                    "tips": selector.find("input[name=opwd]").siblings(".tips"),
                    "button": "#mpwdform .mpbtn",
                    "regexp": /^[a-zA-Z0-9]{6,16}$/,
                    "cburl": "",//callback url
                    "callback": "",//callback function`
                    "cbkey": "",//key name in callback obj
                    "ngtext": "请输入密码.",//when input is empty
                    "crtext": "已输入密码.",//condition is met
                    "extext": "",//text shows when already exists
                    "rqtext": "请输入6-16位登陆密码,大小写字母或数字."
                },
                "unpwd": {
                    "selector": selector.find("input[name=unpwd]"),
                    "tips": selector.find("input[name=unpwd]").siblings(".tips"),
                    "button": "#mpwdform .mpbtn",
                    "regexp": /^[a-zA-Z0-9]{6,16}$/,
                    "cburl": "",//callback url
                    "callback": "",//callback function
                    "cbkey": "",//key name in callback obj
                    "ngtext": "请输入密码.",//when input is empty
                    "crtext": "已输入密码.",//condition is met
                    "extext": "",//text shows when already exists
                    "rqtext": "请输入6-16位登陆密码,大小写字母或数字."
                },
                "unrpwd": {
                    "selector": selector.find("input[name=unrpwd]"),
                    "tips": selector.find("input[name=unrpwd]").siblings(".tips"),
                    "button": "#mpwdform .mpbtn",
                    "regexp": /^[a-zA-Z0-9]{6,16}$/,
                    "cburl": "",//callback url
                    "callback": "",//callback function
                    "cbkey": "",//key name in callback obj
                    "ngtext": "请输入密码.",//when input is empty
                    "crtext": "已输入密码.",//condition is met
                    "extext": "",//text shows when already exists
                    "rqtext": "请输入6-16位登陆密码,大小写字母或数字."
                }
            };
        }
}($);

+function ($) {
    $.loginSettings = function (s) {
        var selector = $(s);
        return {
            "amname": {
                "selector": selector.find("input[name=amname]"),
                "tips": selector.find("input[name=amname]").siblings(".tips"),
                "button": "#adlgform .lgbtn",
                "regexp": /^[a-zA-Z0-9]{8,16}$/,
                "cburl": "",//callback url
                "callback": "",//callback function
                "cbkey": "",//key name in callback obj
                "ngtext": "请输入用户名.",//when input is empty
                "crtext": "已输入用户名.",//condition is met
                "extext": "",//text shows when already exists
                "rqtext": "请输入8-16位用户名,大小写字母或数字."
            },
            "cfpwd": {
                "selector": selector.find("input[name=ampwd]"),
                "tips": selector.find("input[name=ampwd]").siblings(".tips"),
                "button": "#adlgform .lgbtn",
                "regexp": /^[a-zA-Z0-9]{6,16}$/,
                "cburl": "",//callback url
                "callback": "",//callback function
                "cbkey": "",//key name in callback obj
                "ngtext": "请输入密码.",//when input is empty
                "crtext": "已输入密码.",//condition is met
                "extext": "",//text shows when already exists
                "rqtext": "请输入6-16位登陆密码,大小写字母或数字."
            },
            "captcha": {
                "selector": selector.find("input[name=captcha]"),
                "tips": selector.find("input[name=captcha]").siblings(".tips"),
                "button": "#adlgform .lgbtn",
                "regexp": /\w{4}/,
                "cburl": "/checkcaptcha/",//callback url
                "callback": $.ajaxGet,//callback function
                "cbkey": "cc",//key name in callback obj
                "ngtext": "请输入图中验证码.",//when input is empty
                "crtext": "验证码正确.",//condition is met
                "extext": "验证码出错",//text shows when already exists
                "rqtext": "请输入图片验证码."
            }
        }
    }
}($);

+function ($) {
    $.checkField = function (form, btn) {
        $(form + " " + "input[type=text]," + form + " " + "input[type=file]").each(function (i, t) {
            if ($(t).val().length == 0) {
                if ($(t).attr("name") != "memo") {
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                }
                return false;
            } else if ($(t).attr("type") == "text" && !$(t).siblings(".tips").hasClass("cr") && $(t).siblings(".tips").text().length) {
                $(btn).css("background-color", "#ccc").attr("disabled", true);
                return false;
            }
        });
        $(form + " " + "input[type=file]").on("change", function () {
            $(form + " " + "input[type=file]," + form + " " + "input[type=text]").each(function (i, t) {
                if ($(t).val().length == 0) {
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                    return;
                } else if ($(t).attr("type") == "text" && !$(t).siblings(".tips").hasClass("cr") && $(t).siblings(".tips").text().length) {
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                    return;
                }
            });
        });
    }

}($);
+function ($) {
    $.processForm = function (selector, type) {
        $(selector).empty();
        var p = /\[(.*)\]/;
        var cu = p.exec($("#wu").text())[1];
        if (type == "1") {
            //添加机房机器
            var html = "<div class='frow'><label>机器类型:</label><select id='mtype' name='mtype'><option value='0' selected>普通机器</option><option value='1'>刀片机</option></select></div>";
            html += "<div class='frow'> <label>所属机房:</label><select id='loca' name='loca'><option value='1,厦门哈曼尼'selected>厦门哈曼尼</option><option value='2,东莞枫华园'>东莞枫华园</option><option value='3,浙江绍兴'>浙江绍兴</option><option value='5,香港机房'>香港机房</option><option value='4,浙江杭州'>浙江杭州</option><option value='6,美国机房'>美国机房</option></select></div>";
            html += "<div class='frow'> <label>机柜编号:</label><input type='text' id='c_num' name='c_num' maxlength='10'/></div>";
            html += "<div class='frow asnum'> <label>利联编号:</label><input type='text' id='m_num' name='m_num' maxlength='10'/><div class='tips'><span></span></div></div>";
            html += "<div class='frow'> <label>其它编号:</label><input type='text' id='wy_m_num' name='wy_m_num' maxlength='10'/></div>";
            html += "<div class='frow ips'> <label>IP地址:</label><input type='text' id='ips' name='ips' maxlength='50' pattern='[0-9.]*'/><div class='tips'><span></span></div></div>";
            html += "<div class='frow'><label>机器配置:</label><input type='text' id='config' name='config' maxlength='20' pattern='[A-Za-z0-9]{5,20}'/></div>";
            html += "<div class='frow'> <label>带宽:</label><input type='text' id='bw' name='bw' maxlength='5' pattern='[0-9A-Z]{2,8}'/></div>";
            html += "<div class='frow'><label>机器状态:</label><select id='status' name='status'><option value='a,空闲' selected>空闲</option><option value='b,租用'>租用</option><option value='c,托管'>托管</option><option value='d,试用'>试用</option></select></div>";
            html += "<div class='frow'><label>备注:</label><input type='text' name='memo' id='memo'/></div>";
        } else if (type == '2') {
            //添加订单
            var user = $("#uid").val();
            //var html = "<div class='frow'> <label>所属机房:</label><select id='loca' name='loca'><option value='厦门哈曼尼'selected>厦门哈曼尼</option><option value='东莞枫华园'>东莞枫华园</option></select></div>";
            //html +="<div class='frow'><label>机器配置:</label><input type='text' id='config' name='config' maxlength='20' pattern='[A-Za-z0-9]{5,20}'/></div>";
            //html +="<div class='frow'> <label>带宽:</label><input type='text' id='bw' name='bw' maxlength='5' pattern='[0-9A-Z]{2,8}'/></div>";"a":"工商银行","b":"建设银行","c":"支付宝","d":"财富通","e":"微信支付"
            var html = "<div class='frow'><label>付款方式:</label><select id='pmsource' name='pmsource'><option value='a,工商银行'>工商银行</option><option value='b,建设银行'>建设银行</option><option value='c,支付宝' selected>支付宝</option><option value='d,财富通'>财富通</option><option value='e,微信支付'>微信支付</option></select></div>";
            html += "<div class='frow'><label>产品类型:</label><select id='ptype' name='ptype'><option value='r,普通机托管' selected>普通机托管</option><option value='s,普通机租用'>普通机租用</option><option value='t,高防机托管'>高防机托管</option><option value='u,高防机租用'>高防机租用</option><option value='v,代理机托管'>代理机托管</option><option value='w,代理机租用'>代理机租用</option><option value='x,机柜出租'>机柜出租</option></select></div>";
            html += "<div class='frow ips'> <label>IP地址:</label><input type='text' id='ips' name='ips' maxlength='50' pattern='[0-9.]*'/><div class='tips'><span></span></div></div>";
            html += "<input type='hidden' name='sales' id='sales' value='"+user+"'/>";
            html += "<div class='frow'> <label>业务员:</label><input type='text' readonly='readonly' value='" + cu + "'/></div>";
            html += "<div class='frow'> <label>客户账号:</label><input type='text' id='cacc' name='cacc' maxlength='10' placeholder='请输入6位客户账户' pattern='[a-zA-Z0-9]{8}'/></div>";
            html += "<div class='frow'> <label>订单金额:</label><input type='text' id='pm' name='pm' maxlength='10' pattern='\d{1,10}'/></div>";
            html += "<div class='frow'><label>出机时间:</label><input type='text' name='sdt'/></div>";
            html += "<div class='frow'><label>服务时间:</label><select name='msl' id='msl'><option value='1'>月份</option><option value='3'>季度</option><option value='6'>半年</option><option value='12'>一年</option></select></div>";
            html += "<div class='frow'><label>备注:</label><input type='text' name='memo' id='memo'/></div>";
        }
        $(selector).append(html);
        $.displayBladeMachineInput(selector);

    }
}($);
+function ($) {
    $.displayBladeMachineInput = function (selector) {
        $(selector).find("#mtype").on("change", function () {
            var val = $(this).val();
            $(selector).empty();
            if (val == "0") {
                //添加机房普通机器
                var html = "<div class='frow'><label>机器类型:</label><select id='mtype' name='mtype'><option value='0' selected>普通机器</option><option value='1'>刀片机</option></select></div>";
                html += "<div class='frow'> <label>所属机房:</label><select id='loca' name='loca'><option value='1,厦门哈曼尼'selected>厦门哈曼尼</option><option value='2,东莞枫华园'>东莞枫华园</option><option value='3,浙江绍兴'>浙江绍兴</option><option value='5,香港机房'>香港机房</option><option value='4,浙江杭州'>浙江杭州</option><option value='6,美国机房'>美国机房</option></select></div>";
                html += "<div class='frow'> <label>机柜编号:</label><input type='text' id='c_num' name='c_num' maxlength='10'/></div>";
                html += "<div class='frow'> <label>利联编号:</label><input type='text' id='m_num' name='m_num' maxlength='10'/></div>";
                html += "<div class='frow'> <label>其它编号:</label><input type='text' id='wy_m_num' name='wy_m_num' maxlength='10'/></div>";
                html += "<div class='frow'> <label>IP地址:</label><input type='text' id='ips' name='ips' maxlength='300' pattern='[0-9.]*'/></div>";
                html += "<div class='frow'><label>机器配置:</label><input type='text' id='config' name='config' maxlength='20' pattern='[A-Za-z0-9]{5,20}'/></div>";
                html += "<div class='frow'> <label>带宽:</label><input type='text' id='bw' name='bw' maxlength='5' pattern='[0-9A-Z]{2,8}'/></div>";
                html += "<div class='frow'><label>机器状态:</label><select id='status' name='status'><option value='空闲' selected>空闲</option><option value='b,租用'>租用</option><option value='c,托管'>托管</option><option value='d,试用'>试用</option></select></div>";
                html += "<div class='frow'><label>备注:</label><input type='text' name='memo' id='memo'/></div>";

            } else if (val == "1") {
                //添加机房刀片机
                var html = "<div class='frow'><label>机器类型:</label><select id='mtype' name='mtype'><option value='0'>普通机器</option><option value='1' selected>刀片机</option></select></div>";
                html += "<div class='frow'> <label>所属机房:</label><select id='loca' name='loca'><option value='1,厦门哈曼尼'selected>厦门哈曼尼</option><option value='2,东莞枫华园'>东莞枫华园</option><option value='3,浙江绍兴'>浙江绍兴</option><option value='5,香港机房'>香港机房</option><option value='4,浙江杭州'>浙江杭州</option><option value='6,美国机房'>美国机房</option></select></div>";
                html += "<div class='frow'> <label>机柜编号:</label><input type='text' id='c_num' name='c_num' maxlength='20'/></div>";
                html += "<div class='frow'> <label>母机编号:</label><input type='text' id='bm_mnum' name='bm_mnum' maxlength='20'/></div>";
                html += "<div class='frow'> <label>刀片机编号:</label><input type='text' id='bm_num' name='bm_num' maxlength='20'/></div>";
                html += "<div class='frow'> <label>内网ip地址:</label><input type='text' id='bm_ip' name='bm_ip' maxlength='50' pattern='[0-9.]*'/></div>";
                html += "<div class='frow'> <label>IP地址:</label><input type='text' id='ips' name='ips' maxlength='300' pattern='[0-9.]*'/></div>";
                html += "<div class='frow'><label>机器配置:</label><input type='text' id='config' name='config' maxlength='20' pattern='[A-Za-z0-9]{5,20}'/></div>";
                html += "<div class='frow'> <label>带宽:</label><input type='text' id='bw' name='bw' maxlength='5' pattern='[0-9A-Z]{2,8}'/></div>";
                html += "<div class='frow'><label>机器状态:</label><select id='status' name='status'><option value='a,空闲' selected>空闲</option><option value='b,租用'>租用</option><option value='c,托管'>托管</option><option value='d,试用'>试用</option></select></div>";
                html += "<div class='frow'><label>备注:</label><input type='text' name='memo' id='memo'/></div>";

            }
            $(selector).animate({"scrollTop": 0}, function () {
                $(selector).append(html);
                $.displayBladeMachineInput(selector);
            });
        });
    }
}($);
+function ($) {
    $.globaltips = function (type, text, closecb) {
        var html = "";
        html += "<div class='tmodal'></div>";
        if (type == "success") {
            html += "<div class='tipct'><i class='fa fa-check-circle-o fa-3x'></i><p class='desc'>" + text + "</p></div>";
        }
        else if (type == "error") {
            html += "<div class='tipct'><i class='fa fa-times-circle-o'></i><p class='desc'>" + text + "</p></div>";
        }
        !$(".tmodal").length ? $("body").append(html) : "";
        $(".tmodal").addClass("active");
        window.setTimeout(function () {
            $(".tmodal").removeClass("active").remove();
            $(".tipct").remove();
            typeof  closedb == "function" ? closecb.call() : "";
        }, 2000);
    }
}($);

+function ($) {
    $.tips = function (selector, text, type) {
        //type 1 correct,type2 error,type 3 info
        var chtml = "<i class='fa fa-check-circle-o'></i>";
        var ehtml = "<i class='fa fa-times-circle-o fa-2x'></i>";
        var ihtml = "<i class='fa fa-info-circle fa-2x'></i>";
        type == 1 ? $(chtml).insertBefore(selector + " span") : type == 2 ? $(ehtml).insertBefore(selector + " span") : $(ihtml).insertBefore(selector + " span");
        $(selector + " span").text(text);
        window.setTimeout(function () {
            $(selector + " span").empty();
            $(selector + " i").remove();
        }, 3000);
    }
}($);

+function ($) {
    $.checkempty = function (form, text) {
        var c = 0;
        $(form).find("input[type='text'],input[type='date']").not("#memo,#wy_m_num").each(function (i, t) {
            if (!$(t).val().length) {
                //console.log(c);
                c == 0 ? $.tips(form + " .frow input[type=submit] ~ .tips", text, "2") : "";
                c == 0 ? c += 1 : "";
                return;
            }
        });
        return c;
    }
}($);
+function () {
    $.displayOrderDetails = function (selector, data, type,sdata) {
        var html = "";
        if (type == "details") {
            //order part
            html += "<div id='odt'>";
            html += "<div class='frow'><label>订单id:</label><input type='text' readonly='readonly' name='orderid' id='orderid' value='" + data[0] + "'/></div>";
            html += "<div class='frow'><label>订单金额:</label><input type='text' readonly='readonly' name='pm' id='pm' value='" + data[3] + "'/></div>";
            html += "<div class='frow'><label>付款方式:</label><input type='text' readonly='readonly' name='pms' id='pms' value='" + data[12].split(',')[1] + "'/></div>";

            html += "<div class='frow'><label>服务类型:</label><input type='text' readonly='readonly' name='stype' id='stype' value='" + data[33].split(',')[1] + "'/></div>";
            html += "<div class='frow'><label>出机时间:</label><input type='text' readonly='readonly' name='sd' id='sd' value='" + data[4] + "'/></div>";
            html += "<div class='frow'><label>到期时间:</label><input type='text' readonly='readonly' name='ed' id='ed' value='" + data[5] + "'/></div>";
            html += "<div class='frow'><label>客户所属:</label><input type='text' readonly='readonly' name='bl' id='bl' value='" + data[7].split(',')[1] + "'/></div>";
            html += "<div class='frow'><label>审核人:</label><input type='text' readonly='readonly' name='ad' id='ad' value='" + data[8] + "'/></div>";
            html += "<div class='frow'><label>审核时间:</label><input type='text' readonly='readonly' name='at' id='at' value='" + data[11] + "'/></div>";
            html += "<div class='frow'><label>订单备注:</label><input type='text' readonly='readonly' name='omemo' id='omemo' value='" + data[9] + "'/></div>";
            html += "<input type='hidden' name = 'ptype' id='ptype' value = '" + data[10] + "'/>";
            html += "</div>";
            //client part
            html += "<div class='frow'><label>客户账号:</label><input type='text' readonly='readonly' name='c_ac' id='c_ac' value='" + data[2] + "'/></div>";
            html += "<input type='hidden' readonly='readonly' name='cid' id='cid' value='" + data[11] + "'/></div>";
            html += "<div class='frow'><label>客户姓名:</label><input type='text' readonly='readonly' name='cname' id='cname' value='" + data[16] + "'/></div>";
            html += "<div class='frow'><label>客户电话:</label><input type='text' readonly='readonly' name='cphone' id='cphone' value='" + data[18] + "'/></div>";
            html += "<div class='frow'><label>客户QQ:</label><input type='text' readonly='readonly' name='cqq' id='cqq' value='" + data[23] + "'/></div>";
            //machine part
            html += "<input type='hidden' readonly='readonly' name='mid' id='mid' value='" + data[24] + "'/></div>";
            html += "<input type='hidden' readonly='readonly' name='idcloca' id='idcloca' value='" + data[28] + "'/></div>";
            html += "<div class='frow'><label>机器IP:</label><input type='text' readonly='readonly' name='mip' id='mip' value='" + data[26] + "'/></div>";
            html += "<div class='frow'><label>机房:</label><input type='text' readonly='readonly' name='mloca' id='mloca' value='" + data[28].split(',')[1] + "'/></div>";
            html += "<div class='frow'><label>机柜编号:</label><input type='text' readonly='readonly' name='mc' id='mc' value='" + data[29] + "'/></div>";
            html += "<div class='frow'><label>利联编号:</label><input type='text' readonly='readonly' name='mnum' id='mnum' value='" + data[30] + "'/></div>";
            html += "<div class='frow'><label>其它编号:</label><input type='text' readonly='readonly' name='onum' id='onum' value='" + data[31] + "'/></div>";
            html += "<div class='frow'><label>带宽:</label><input type='text' readonly='readonly' name='bw' id='bw' value='" + data[32] + "'/></div>";
            html += "<div class='frow'><label>机器配置:</label><input type='text' readonly='readonly' name='bw' id='bw' value='" + data[35] + "'/></div>";
            html += "<div class='frow'><label>机器备注:</label><input type='text' readonly='readonly' name='st' id='st' value='" + data[37] + "'/></div>";
            if(sdata && sdata.length){
                for (var i=0;i<sdata.length;i++){
                    html +="<hr />";
                    html +="<h3 class='sotitle' style='text-align: center;margin-top: 15px;'>子订单</h3>";
                    html +="<div class='frow'><label>订单号:</label><input type='text' readonly='readonly' value='"+sdata[i][0]+"'/></div>";
                    html +="<div class='frow'><label>订单金额:</label><input type='text' readonly='readonly' value='"+sdata[i][2]+"'/></div>";
                    html +="<div class='frow'><label>付款方式:</label><input type='text' readonly='readonly' value='"+sdata[i][9].split(',')[1]+"'/></div>";
                    html +="<div class='frow'><label>订单类型:</label><input type='text' readonly='readonly' value='"+sdata[i][3].split(',')[1]+"'/></div>";
                    html +="<div class='frow'><label>录入时间:</label><input type='text' readonly='readonly' value='"+sdata[i][8]+"'/></div>";
                    html +="<div class='frow'><label>备注:</label><input type='text' readonly='readonly' value='"+sdata[i][7]+"'/></div>";
                }
            }
        } else if (type == "renew") {
            //order part
            html += "<div class='frow'><label>机房:</label><input type='text' readonly='readonly' name='mloca' id='mloca' value='" + data[28].split(',')[1] + "'/></div>";
            html += "<input type='hidden' readonly='readonly' name='idcloca' id='idcloca' value='" + data[28] + "'/></div>";
            html += "<div class='frow'><label>订单id:</label><input type='text' readonly='readonly' name='orderid' id='orderid' value='" + data[0] + "'/></div>";
            html += "<div class='frow'><label>付款方式:</label><select id='pmsource' name='pmsource'><option value='a,工商银行'>工商银行</option><option value='b,建设银行'>建设银行</option><option value='c,支付宝' selected>支付宝</option><option value='d,财富通'>财富通</option><option value='e,微信支付'>微信支付</option></select></div>";
            html += "<div class='frow'><label>订单金额:</label><input type='text' name='pm' lpm = '" + data[3] + "'id='pm'/>" + "<p class='otip'>原订单付款:" + data[3] + "元</p></div>";
            html += "<div class='frow'><label>服务类型:</label><input type='text' readonly='readonly' name='stype' id='stype' value='" + data[33].split(',')[1] + "'/></div>";
            html += "<div class='frow'><label>出机时间:</label><input type='text' readonly='readonly' name='sd' id='sd' value='" + data[4] + "'/></div>";
            html += "<div class='frow'><label>续期:</label><select name='rnt' id='rnt'><option value='1'>月份</option><option value='3'>季度</option><option value='6'>半年</option><option value='12'>1年</option></select><p class='otip exd' exd='" + data[5] + "'>原计划到期时间:" + data[5] + "</p></div>";
            html += "<input type='hidden' name = 'cid' id = 'cid' value = '" + data[11] + "'/>";
            html += "<input type='hidden' name = 'ptype' id='ptype' value = '" + data[10] + "'/>";
            html += "<input type='hidden' name = 'wsales' id='wsales' value = '" + data[7] + "'/>";
            html += "<input type='hidden' name = 'rip' id='rip' value = '" + data[26] + "'/>";
            html += "<div class='frow'><label>客户账号:</label><input type='text' readonly='readonly' name='c_ac' id='c_ac' value='" + data[2] + "'/></div>";
            html += "<div class='frow'><label>客户姓名:</label><input type='text' readonly='readonly' name='cname' id='cname' value='" + data[15] + "'/></div>";
            html += "<div class='frow'><label>客户所属:</label><input type='text' readonly='readonly' name='bl' id='bl' value='" + data[7].split(',')[1] + "'/></div>";
            html += "<div class='frow'><label>审核人:</label><input type='text' readonly='readonly' name='ad' id='ad' value='" + data[8] + "'/></div>";
            html += "<div class='frow'><label>订单备注:</label><input type='text' name='omemo' id='omemo' value='" + data[9] + "'/></div>";
        }
        $(selector).append(html);
    }
}($);

+function ($) {
    $.closeModal = function (url) {
        $(".modal-bg.active,.mclose,#oform .blockbtn").on("click.last", function () {
            $("body").css("overflow", "auto");
            $(".modal-ct").animate({top: -200, opacity: 0.4}, function () {
                $(this).fadeOut();
                $(".modal-bg.active,div[class^=modal-ct].active").removeClass("active");
                if (window.location.search) {
                    window.location.href = url + window.location.search;
                } else {
                    window.location.href = url;
                }
            });
        });
    }
}($);

+function ($) {
    $.datepicker = function (selector) {
        $.datetimepicker.setLocale('ch');
        $(selector).datetimepicker({
            lang: "ch", //语言选择中文 注：旧版本 新版方法：$.datetimepicker.setLocale('ch');
            format: "Y/m/d",      //格式化日期
            timepicker: false,    //关闭时间选项
            yearStart: 2000,     //设置最小年份
            yearEnd: 2050,        //设置最大年份
            todayButton: false    //关闭选择今天按钮
        });
    }
}($);

+function ($) {
    $(document).ready(function () {
        //on remove machine
        $.removems();
        $.getCaptcha(".ccha");
        $("#nav ul li.add-machines").click(function () {
            $(".modal-ct,.modal-bg").removeClass("active");
            $(this).addClass("active").siblings().removeClass("active");
            $.processForm("#add_machines .data", "1");
            $(".modal-ct-s-1,.modal-bg").toggleClass("active");
            //$(".modal-ct-s-1.active").css("top", $(window).scrollTop() + 29);
            $("body").css("overflow", "hidden");
            //check if ip exists
            $.parseip = function(data){
                var data = typeof data == "object"?data:JSON.parse(data);
                if (data['rs'] == "1047") {
                    !$("#add_machines .frow.ips .tips span").text().length?$.tips("#add_machines .frow.ips .tips", "当前IP可用", 1):"";
                    if($("#add_machines .m_addbtn").attr("hold") == "ip" || $("#add_machines .m_addbtn").attr("hold") == "init") {
                        $("#add_machines .m_addbtn").css({"background-color": "#17578d"}).attr("disabled", false);
                    }
                    //callback
                } else if (data["rs"] == "1046") {
                    !$("#add_machines .frow.ips .tips span").text().length?$.tips("#add_machines .frow.ips .tips", "已有机器使用该IP", 2):"";
                    $("#add_machines .m_addbtn").css({"background-color":"#ccc"}).attr({"disabled":true,"hold":"ip"});
                }
            };
            //check if machine's ip exists
            $.checkip = function (tinput){
                    var ip = tinput.val().trim();
                    var that = tinput;
                    var pat = /^(([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)/g;
                    //check if it is ip
                    if (pat.test(ip)) {
                        //check if chinese commas there
                        var cpat = /[^\x00-\xff]/g;
                        if (cpat.test(ip)) {
                            !$("#add_machines .frow.ips .tips span").text().length?$.tips("#add_machines .frow.ips .tips", "请输入英文字符!", 2):"";
                             $("#add_machines .m_addbtn").css({"background-color":"#ccc"}).attr("disabled",true);
                            return false;
                        }
                        //if many ips
                        if (ip.indexOf(",") != -1) {
                            var iparr = ip.split(",");
                            var all = true;//if all is ip
                            $(iparr).each(function (i, t) {
                                console.log(pat.test(t),t);
                                all ? pat.test(t) ? '' : all = false : "";
                            });
                            if (!all) {
                                 !$("#add_machines .frow.ips .tips span").text().length?$.tips("#add_machines .frow.ips .tips", "IP格式不对!", 2):"";
                            }else{
                                $.get("/admin/machine/checkms/", {ip: ip, multi:1}, function (data) {
                                $.parseip(data);
                            }, "json");
                            }
                        } else {
                            //single entry
                            $.get("/admin/machine/checkms/", {ip:ip, multi:0}, function (data) {
                                $.parseip(data);
                            }, "json");
                        }
                    }else{
                         $("#add_machines .m_addbtn").css({"background-color":"#ccc"}).attr("disabled",true);
                    }
                };
            $("#add_machines input[name=ips]").on({"keyup":function(){
                var tinput = $(this);
                $.checkip(tinput);
            },"blur":function(){
                var tinput = $(this);
                $.checkip(tinput);
            }});
            $("#add_machines input[name=m_num]").on({"keyup":function(){
                var num = $(this).val();
                var pat = /[0-9]{2}\-[0-9]{4}/;
                if(pat.test(num)){
                    $.get("/admin/machine/checkms/",{asnum:num},function(data){
                        if(data['rs']=="1048"){
                            !$("#add_machines .frow.asnum .tips span").text().length?$.tips("#add_machines .frow.asnum .tips", "当前编号不可用", 2):"";
                            $("#add_machines .m_addbtn").css({"background-color":"#ccc"}).attr({"disabled":true,"hold":"asnum"});
                        }else if(data['rs'] == '1049'){
                            !$("#add_machines .frow.asnum .tips span").text().length?$.tips("#add_machines .frow.asnum .tips", "当前编号可用", 1):"";
                            if($("#add_machines .m_addbtn").attr("hold") == "asnum" || $("#add_machines .m_addbtn").attr("hold") == "init") {
                                $("#add_machines .m_addbtn").css({"background-color": "#17578d"}).attr("disabled", false);
                            }
                        }
                    },"json")
                }
            },"blur":function(){
                var num = $(this).val();
                var pat = /[0-9]{2}\-[0-9]{4}/;
                if(pat.test(num)){
                    $.get("/admin/machine/checkms/",{asnum:num},function(data){
                        if(data['rs']=="1048"){
                            !$("#add_machines .frow.asnum .tips span").text().length?$.tips("#add_machines .frow.asnum .tips", "当前编号不可用", 2):"";
                            $("#add_machines .m_addbtn").css({"background-color":"#ccc"}).attr({"disabled":true,"hold":"asnum"});
                        }else if(data['rs'] == '1049'){
                            !$("#add_machines .frow.asnum .tips span").text().length?$.tips("#add_machines .frow.asnum .tips", "当前编号可用", 1):"";
                            if($("#add_machines .m_addbtn").attr("hold") == "asnum" || $("#add_machines .m_addbtn").attr("hold") == "init") {
                                $("#add_machines .m_addbtn").css({"background-color": "#17578d"}).attr("disabled", false);
                            }
                        }
                    },"json")
                }
            }});
            //取消模态框vnbtn
            $(".modal-bg.active,.mclose").on("click.last", function () {
                $("body").css("overflow", "auto");
                $(".modal-ct").animate({top: -200, opacity: 0.4}, 200, function () {
                    $(this).fadeOut();
                    $(".modal-bg.active,div[class^=modal-ct].active").removeClass("active");
                    if (window.location.search.indexOf("m") != -1) {
                        console.log("here");
                        window.location.href = "/admin/all-machines/" + window.location.search;
                    } else {
                        window.location.href = "/admin/all-machines/?mtype=0";
                    }
                });

            });

        });
        $("#nav ul li.add-orders").click(function () {
            //restore modal status
            $(".modal-ct,.modal-bg").removeClass("active");
            $(this).addClass("active").siblings().removeClass("active");
            $.processForm("#add_orders .data", "2");
            //datepicker
            $.datepicker("#add_orders input[name=sdt]");
            $(".modal-ct-s-2,.modal-bg").toggleClass("active");
            //$(".modal-ct-s-2.active").css("top", $(window).scrollTop() + 29);
            $("body").css("overflow", "hidden");
            $.parseip = function(data){
                var data = typeof data == "object"?data:JSON.parse(data);
                if (data['rs'] == "1044") {
                    !$("#add_orders .frow.ips .tips span").text().length?$.tips("#add_orders .frow.ips .tips", "IP正确", 1):"";
                    //add idc location
                    !$("#idcloca").length?$("#add_orders").append("<input type=hidden name='idcloca' id='idcloca' value='"+data['loca']+"'/>"):"";
                    $("#add_orders .o_addbtn").css({"background-color":"#17578d"}).attr("disabled",false);
                    //callback
                } else if (data["rs"] == "1045") {
                    !$("#add_orders .frow.ips .tips span").text().length?$.tips("#add_orders .frow.ips .tips", "当前输入的IP不存在", 2):"";
                    $("#add_orders .o_addbtn").css({"background-color":"#ccc"}).attr("disabled",true);
                }
            };
            //check machine's ip
            $.checkip = function (tinput){
                    var ip = tinput.val().trim();
                    //console.log(ip);
                    var that = tinput;
                    var pat = /((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))/g;
                    //check if it is ip
                    //console.log(pat.test(ip),pat.exec(ip));
                    if (pat.test(ip)) {
                        //check if chinese commas there
                        var cpat = /[^\x00-\xff]/g;
                        if (cpat.test(ip)) {
                            !$("#add_orders .frow.ips .tips span").text().length?$.tips("#add_orders .frow.ips .tips", "请输入英文字符!", 2):"";
                             $("#add_orders .o_addbtn").css({"background-color":"#ccc"}).attr("disabled",true);
                            return false;
                        }
                        //if many ips
                        if (ip.indexOf(",") != -1) {
                            var iparr = ip.split(",");
                            var all = true;//if all is ip
                            $(iparr).each(function (i, t) {
                                console.log(pat.test(t),t);
                                all ? pat.test(t) ? '' : all = false : "";
                            });
                            if (!all) {
                                //not all is ip
                                !$("#add_orders .frow.ips .tips span").text().length?$.tips("#add_orders .frow.ips .tips", "IP格式不对!", 2):"";
                            }else{
                                $.get("/admin/orders/checkip/", {ip: ip, multi: 1}, function (data) {
                                    $.parseip(data);
                                }, "json")
                            }
                        } else {
                            //single entry
                            $.get("/admin/orders/checkip/", {ip: ip, multi: 0}, function (data) {
                                $.parseip(data);
                            }, "json");
                        }
                    }else{
                         $("#add_orders .o_addbtn").css({"background-color":"#ccc"}).attr("disabled",true);
                    }
                };
            $("#add_orders input[name=ips]").on({"keyup":function(){
                var tinput = $(this);
                $.checkip(tinput);
            },"blur":function(){
                var tinput = $(this);
                $.checkip(tinput);
            }});
            //取消模态框vnbtn
            $(".modal-bg.active,.mclose").on("click.last", function () {
                $("body").css("overflow", "auto");
                $(".modal-ct-s-2").animate({top: -200, opacity: 0.4}, 200, function () {
                    $(this).fadeOut();
                    $(".modal-bg.active,div[class^=modal-ct].active").removeClass("active");
                    if (!window.location.search.indexOf("m")) {
                        window.location.href = "/admin/orders/" + window.location.search;
                    } else {
                        window.location.href = "/admin/orders/";
                    }
                });

            });
        });
    });

    //submit new machine info
    $(".m_addbtn").click(function (e) {
        e.preventDefault();
        //check if input value is empty
        var empty = $.checkempty("#add_machines", "机器信息不能为空");
        //console.log(empty);

        if (!empty) {
            $(".loadding").show();
            $.post("/admin/machines/", $("#add_machines").serialize(), function (data) {
                var data = JSON.parse(data);
                if (data["rs"] == "1024") {
                    $(".modal-ct-s-1 .modal-dt").animate({scrollTop: 0}, function () {
                        $("#add_machines .data").empty();
                        $.processForm("#add_machines .data", "1");
                        $(".loadding").hide();
                    });
                } else if (data.rs == "1025") {
                    $.tips("#add_machines .tips", "提交机器信息到服务器出错.", "2");
                }
            });
        }
    });
    $(".o_addbtn").click(function (e) {
        e.preventDefault();
        //check if input value is empty
        var empty = $.checkempty("#add_orders", "订单信息不能为空");
        if (!empty) {
            $(".loadding").show();
            $.post("/admin/orders/", $("#add_orders").serialize(), function (data) {
                var data = JSON.parse(data);
                if (data["rs"] == "1026") {
                    $.tips("#add_orders .o_addbtn ~ .tips", "订单提交成功.", "1");
                    $(".modal-ct-s-2 .modal-dt").animate({scrollTop: 0}, function () {
                        $("#add_orders .data").empty();
                        $.processForm("#add_orders .data", "2");
                        $(".loadding").hide();
                    });
                } else if (data.rs == "1027") {
                    $.tips("#add_orders .tips", "提交订单信息到服务器出错.", "2");
                }
            });
        }
    });
    $(".orders_tb tr td .modify").click(function () {
        var oid = $(this).parents("tr").find(".tid").text().trim();
        var upower = parseInt($("#power").val());
        $(".loadding").show();
        $.get("/admin/order/modify/" + oid, function (data) {
            var mdata = JSON.parse(data)["order"];
            var sdata = JSON.parse(data)["suborder"];
            if (mdata) {
                //console.log(data,data[8]);
                $("#add_orders .data").empty();
                if (!mdata[8].length && [5].indexOf(upower) != -1) {
                    var ihtml = '<input type="button" class="auditbtn sbtn" value="审核" style=""/>';
                    ihtml +='<input type="button" class="mbtn sbtn" value="修改" style="margin-left: 15px;background: #17578d"/>';
                    ihtml +='<input type="button" class="blockbtn sbtn" value="驳回" style="margin-left: 15px;background: #49700e"/>';
                } else if(mdata[8].length && [5].indexOf(upower) != -1) {
                    //var ihtml = '<input type="submit" disabled="disabled" class="auditbtn sbtn" value="审核" style=""/>';
                    ihtml ='<input type="button" class="mbtn sbtn" value="修改" style="margin-left: 15px;background: #17578d"/>';
                }

                $(ihtml).insertAfter("#oform .n_addbtn");
                $.displayOrderDetails("#oform .data", mdata, "details",sdata);
                //if boss then modify
                $("#oform .data").find("#odt input[type=text]").not("input[name=orderid],input[name=pm],input[name=stype],input[name=sd],input[name=bl],input[name=ad]").each(function(i,t){
                   $(t).attr("readonly",false);
                   //modify datepicker

                });
                $.datepicker("#odt input[name=ed]");
                //hide submit btn
                $("#oform .n_addbtn").hide();
                $(".modal-ct-s-4,.modal-bg").toggleClass("active");
                //$(".modal-ct-s-4.active").css("top", $(window).scrollTop() + 29);
                $("body").css("overflow", "hidden");
                $(".loadding").hide();
                //when auditbtn is click
                $("#oform .auditbtn").click(function () {
                    var cu = $("#uid").val();
                    var that = $(this);
                    $.post("/admin/order/audit/", {
                        "oid": oid,
                        "auditor": cu,
                        "_xsrf": $.getCookie("_xsrf")
                    }, function (data) {
                        var data = JSON.parse(data);
                        if (data["rs"] == "1032") {
                            that.attr("disabled", true).val("已审核.").css({"background": "#af7d38", "color": "#fff"});
                        } else if (data["rs"] == "1033") {
                            that.attr("disabled", true).val("审核失败.").css({"background": "#ccc", "color": "#fff"});
                        }
                    })
                });
                //when modify
                $("#oform .mbtn").click(function(){
                    var that = $(this);
                    var moid = $("#odt #orderid").val().trim();
                    var med = $("#odt #ed").val();
                    var mmemo = $("#odt #omemo").val();
                    $.post("/admin/order/modify/"+moid,{med:med,mmemo:mmemo,_xsrf:$.getCookie("_xsrf")},function(data){
                        var data = JSON.parse(data);
                        if (data['rs'] == '1042'){
                            that.val("已修改").attr("disabled",true);
                        }else if (data['rs']=='1043'){
                            that.val("提交修改失败.");
                            console.error(a,b,c,"提交修改数据到服务器失败");
                        }
                    });
                });
                $.closeModal("/admin/orders/");
                /*$(".modal-ct-s-4 .modal-dt").animate({scrollTop: 0}, function (){

                 });*/
            }
        });
    });
    $(".orders_tb tr td .renew").click(function () {

        var oid = $(this).parents("tr").find(".tid").text().trim();

        $(".loadding").show();
        $.get("/admin/order/modify/" + oid, function (data) {
            var data = JSON.parse(data)["order"];
            if (data) {
                $("#add_orders .data").empty();
                $.displayOrderDetails("#oform .data", data, "renew");
                $("#oform .sbtn").addClass("renew");
                $(".modal-ct-s-4,.modal-bg").toggleClass("active");
                //$(".modal-ct-s-4.active").css("top", $(window).scrollTop() + 29);
                $("body").css("overflow", "hidden");
                $(".loadding").hide();
                $.closeModal("/admin/orders/");
                /*$(".modal-ct-s-4 .modal-dt").animate({scrollTop: 0}, function (){
                 });*/
                $("#oform .sbtn.renew").click(function (e) {
                    e.preventDefault();
                    //check if payment is empty
                    if(!$("#oform input[name=pm]").val()){
                        $.tips("#oform .tips","订单金额不能为空!",2);
                        return false;
                    }
                    var tid = $("#oform #orderid").val();
                    var pm = parseInt($("#oform #pm").val()) + parseInt($("#oform #pm").attr("lpm"));//latest payment value,this will be ignored now
                    var tpm = parseInt($("#oform #pm").val());
                    var renew = $("#oform #rnt").val();
                    var memo = $("#oform #omemo").val();
                    var exd = $("#oform .otip.exd").attr("exd");
                    var cacc = $("#oform #c_ac").val();
                    var ptype = $("#oform #ptype").val();
                    var wsales = $("#oform #wsales").val();
                    var rip = $("#oform #rip").val();
                    var pmsource = $("#oform #pmsource").val();
                    var idcloca = $("#oform #idcloca").val();
                    $(this).attr("disabled", true).val("正在提交...").css({"background": "#ccc", "color": "#fff"});
                    var that = $(this);
                    $.post("/admin/order/renew/", {
                        "tid": tid,
                        "pm": pm,
                        "renew": renew,
                        "memo": memo,
                        "exd": exd,
                        "cacc": cacc,
                        "wsales": wsales,
                        "tpm": tpm,
                        "ptype": ptype,
                        "pmsource":pmsource,
                        'rip': rip,
                        'idcloca':idcloca,
                        "_xsrf": $.getCookie("_xsrf")
                    }, function (data) {
                        if (data["rs"] == "1030") {
                            that.attr("disabled", true).css({"background": "#af7d38"}).val("订单续期成功!");

                        } else if (data["rs"] == "1031") {
                            $.tips("#oform .tips","订单续期失败!",2);
                        }
                    },'json');
                });
            }
        });
    });

    +function ($) {
        $.modifyMs = function () {
            function modifyms() {
                $(".machines_tb tr td .modify").off().click(function () {
                    var d = {};
                    $(this).parents("tr").find("input").each(function (i, t) {
                        //restore to disabled status
                        $(t).attr("disabled", true);
                        d[$(t).attr("name")] = $(t).val();
                    });
                    //restore select status
                    var tr = $(this).parents("tr");
                    var sem = tr.find("#wsales").val();
                    var sst = tr.find("#status").val();
                    //restore
                    tr.find(".wstd").empty().text(sem.split(',')[1]);
                    tr.find(".std").empty().text(sst.split(',')[1]);

                    d["tid"] = $(this).parents("tr").find(".tid").text().trim();
                    d["_xsrf"] = $.getCookie("_xsrf");
                    d['wsales'] = sem;
                    d['status'] = sst;
                    var that = $(this);
                    if (Object.keys(d).length) {
                        $(this).siblings(".loading").show();
                        $.post("/admin/machine/modify", d, function (data) {
                            that.siblings(".loading").hide();
                            var data = JSON.parse(data);
                            $(this).siblings(".loading").hide();
                            if (data["rs"] == "1032") {
                                //successfully modify the machine record
                                that.text("已修改").removeClass("modify");


                            } else if (data["rs"] == "1033") {
                                //successfully modify the machine record
                                console.error(data);
                                that.text("提交失败").removeClass("modify");
                            }
                        });
                        window.setTimeout(function () {
                            that.text("编辑").addClass("edit");
                            $(".machines_tb tr td .edit").off().click(function () {
                                that.text("修改").removeClass("edit").addClass("modify");
                                $(this).parents("tr").find("input").not("input[name=status],input[name=wsales],input[name=loca]").each(function (i, t) {
                                    $(t).attr("disabled", false);
                                });
                                $.modifyMs();
                            });
                        }, 2000)
                    }
                });
            }

            $(".machines_tb tr td .edit").off().click(function () {
                $(this).text("修改").removeClass("edit").addClass("modify");
                $(this).parents("tr").find("input").not("input[name=loca]").each(function (i, t) {
                    $(t).attr("disabled", false);
                });
                var ehtml = '<select id="wsales"> <option value=""></option> <option value="18,劳兴华">劳兴华</option> <option value="19,陶秋梅">陶秋梅</option> <option value="20,唐晓珍">唐晓珍</option> <option value="21,黄小恩">黄小恩</option> <option value="22,廖超">廖超</option> </select>';
                var shtml = "<select id='status'><option value='a,空闲' selected>空闲</option><option value='b,租用'>租用</option><option value='c,托管'>托管</option><option value='d,试用'>试用</option></select>";
                $(this).parents("tr").find(".wstd").empty().html(ehtml);
                $(this).parents("tr").find(".std").empty().html(shtml);
                modifyms()
            });
            modifyms()
        }
    }($);
    $.modifyMs();
    $("#smsf .frow #mtype").on("change", function () {
        var s = $(this).val().trim();
        $("#smsf .frow.area").empty();
        var html = "";
        if (s == "0") {
            html += '<div class="nums"> <label>机柜编号:</label><input type="text" name="cnum" class="cnum"/> </div>';
            html += '<div class="nums"> <label>资产编号:</label><input type="text" name="anum" class="anum"/> </div>';
            html += '<div class="nums"> <label>外部编号:</label><input type="text" name="onum" class="onum"/> </div>';
            html += '<div class="nums"> <label>机器IP:</label><input type="text" name="ips" class="ips"/> </div>';

        } else if (s == "1") {
            html += '<div class="nums"> <label>机柜编号:</label><input type="text" name="cnum" class="cnum"/> </div>';
            html += '<div class="nums"> <label>母机编号:</label><input type="text" name="bm_mnum" class="bm_mnum"/> </div>';
            html += '<div class="nums"> <label>内网ip:</label><input type="text" name="lip" class="lip"/> </div>';
            html += '<div class="nums"> <label>外网ip:</label><input type="text" name="ips" class="ips"/> </div>';
        }
        html += '<div class="nums"> <input type="submit" value="搜索"/> </div>';
        $("#smsf .frow.area").append(html);
    });

    //set order/ms status when order expires
    $(".orders_tb tr td .release").click(function () {
        console.log("release");
        var tr = $(this).parents("tr");
        var ip = $(this).parents("tr").find("input.ip").val().trim();
        var oid = $(this).parents("tr").find(".tid").text().trim();
        var that = $(this);
        var obj = {
            "text": "确认回收该订单?",
                "onConfirm": function () {
                    var url = "/admin/order/release/";
                    var nthat = that;
                    $(".loading").show();
                    $.post(url,{"oid": oid, "ip": ip,"_xsrf":$.getCookie("_xsrf")},function(data){
                        $(".loading").hide();
                        if(data['rs'] == "1034"){
                            tr.find(".empty").remove();
                            nthat.text("已回收").addClass("empty").removeClass("release");
                            window.setTimeout(function () {
                                $(nthat).parents('tr').children('td, th').animate({padding: 0}).wrapInner('<div />').children().slideUp(function () {
                                    $(nthat).closest('tr').remove();
                                });

                            }, 2000);

                            if ($(".orders_tb tr.olist").length < 6) {
                                window.location.href = "/admin/orders/" + window.location.search;
                                }
                        }else if(data['rs'] == "1035"){
                            console.error(a,b,c,"回收订单失败!");
                        }
                    },"json");

                }
        };
        $.confirm(obj);

    });
    //relesae machine when order expires
    $(".machines_tb tr td span.release").click(function () {
        var tr = $(this).parents("tr");
        var that = $(this);
        var mid = $(this).parents("tr").find(".tid").text().trim();
        $.post("/admin/machine/release/", {"mid": mid}, function (data) {
            var data = JSON.parse(data);
            if (data['rs'] == "1036") {
                that.text("已回收").addClass("empty").removeClass("release");
                window.setTimeout(function () {
                    tr.find(".empty").remove();
                }, 2000)
            } else if (data['rs'] == '1037') {
                console.error(a, b, c, "回收机器失败");
            }
        })
    });

    //add suborder
    $(".orders_tb tr td span.sorder").click(function () {
        var tr = $(this).parents("tr");
        var oid = tr.find(".tid").text().trim();
        var oip = tr.find("input[name=ip]").val();
        var smonth = tr.find("input[name=smonth]").val();
        var cacc = tr.find("input[name=uacc]").val();
        var wsales = tr.find("input[name=wsales]").val();
        var mloca = tr.find("input[name=idcloca]").val();
        var html = '';
        //主订单相关信息
        html += "<div class='frow'><label>主订单ID:</label><input type='text' name='mid' id='mid' readonly='readonly' value='" + oid + "'/></div>";
        html += "<input type='hidden' name='cacc' id='cacc' value='" + cacc + "'/>";
        html += "<input type='hidden' name='oip' id='oip' value='" + oip + "'/>";
        html += "<input type='hidden' name='osales' id='osales' value='" + wsales + "'/>";
        html += "<input type='hidden' name='mloca' id='mloca' value='" + mloca + "'/>";
        html += "<div class='frow'><label>主订单服务月份:</label><input type='text' readonly='readonly' value='" + smonth + "'/></div>";
        html += "<div class='frow'><label>服务类型:</label><select name='ostype' id='ostype'><option value='h,加内存'>加内存</option><option value='i,加硬盘'>加硬盘</option><option value='j,加IP'>加IP</option><option value='k,加带宽'>加带宽</option><option value='l,加防护'>加防护</option><option value='m,其它'>其它(请填写备注内容)</option></select></div>";
        html += "<div class='frow'><label>订单价格:</label><input type='text' name='spm' id='spm'/></div>";
        html += "<div class='frow'><label>付款方式:</label><select id='pmsource' name='pmsource'><option value='a,工商银行'>工商银行</option><option value='b,建设银行'>建设银行</option><option value='c,支付宝' selected>支付宝</option><option value='d,财富通'>财富通</option><option value='e,微信支付'>微信支付</option></select></div>"
        html += "<div class='frow'><label>子订单备注:</label><input type='text' name='smemo' id='smemo' /></div>";
        $("#soform .data").append(html);
        $(".modal-bg,.modal-ct-s-5").toggleClass("active");
        $("body").css("overflow", "hidden");
        //取消模态框vnbtn
        $(".modal-bg.active,.mclose").on("click.last", function () {
            $("body").css("overflow", "auto");
            $(".modal-ct").addClass("hide");
            $(".modal-ct").animate({opacity: 0.4}, 200, function () {
                $(this).fadeOut();
                $(".modal-bg.active,div[class^=modal-ct].active").removeClass("active");
                if (window.location.search) {
                    window.location.href = "/admin/orders/" + window.location.search;
                } else {
                    window.location.href = "/admin/orders/?mtype=0";
                }
            });
        });
         //submit suborder and add machine/financial/order log
    $("#soform .n_sobtn").click(function (e) {
        e.preventDefault();
        var that = $(this);
        var empty = $.checkempty("#soform", "子订单信息不能为空!");
        if (!empty) {
            var mid = $("#soform input[name=mid]").val();
            var spm = $("#soform input[name=spm]").val();
            var oip = $("#soform input[name=oip]").val();
            var smemo = $("#soform input[name=smemo]").val();
            var stype = $("#soform #ostype").val();
            var cacc = $("#soform input[name=cacc]").val();
            var wsales = $("#soform input[name=osales]").val();
            var pmsource = $("#soform #pmsource").val();
            var mloca = $("#soform #mloca").val();
            if (!/^[1-9]\d+$/.test(spm)) {
                $.tips("#soform .frow .tips", "请输入数字!", 2);
                return false;
            } else {
                $.post("/admin/order/suborder/", {
                    "spm": spm,
                    "smemo": smemo,
                    "ostype": stype,
                    "osales": wsales,
                    "mid": mid,
                    "cacc": cacc,
                    "oip": oip,
                    "mloca":mloca,
                    "pmsource":pmsource,
                    "_xsrf": $.getCookie("_xsrf")
                }, function (data) {
                    var data = JSON.parse(data);
                    if(data['rs'] == "1038"){
                        that.attr("disabled",true).css({"background":"#af7d38"}).val("已提交子订单.");
                    }else if(data['rs'] == '1039'){
                        that.attr("disabled",true).val("提交子订单失败.").css({"background":"#ccc","color":"#fff"});
                    }
                })
            }
        }
    });
    });
//live modify client details
+function($){
    $.livemodify = function(){
        function modifyagain(){
            $(".clients_tb tr td .modify").click(function(){
            var tr = $(this).parents("tr");
            var cid = tr.find(".tid").text();
            var rname = tr.find("input[name=rname]").val();
            var mobile = tr.find("input[name=mobile]").val();
            var idc = tr.find("input[name=idc]").val();
            var qq = tr.find("input[name=qq]").val();
            var memo = tr.find("input[name=memo]").val();
            var add = tr.find('input[name=add]').val();
            $.post("/admin/client/edit/",{"cid":cid,"rname":rname,"mobile":mobile,"idc":idc,"qq":qq,"memo":memo,"_xsrf":$.getCookie("_xsrf"),"add":add},function(data){
                if(data['rs'] == "1059"){
                    $(".clients_tb tr td span.modify").text("已提交");
                    window.setTimeout(function(){
                       $(".clients_tb tr td span.modify").text("编辑").removeClass("modify").addClass("edit");
                       tr.find("input[type=text]").attr("disabled",true).css({"border":"0"});
                       $.livemodify();
                    },2500)
                }else if(data['rs'] == "1060"){
                    $(".clients_tb tr td span.modify").removeClass("modify").text("提交出错");
                    console.error(a,b,c,"修改提成数据出错！");
                }
            },"json");
        });
        };
         //renew agent order commission
    $(".clients_tb tr td .edit").click(function(){
        var tr = $(this).parents("tr");
        var that = $(this);
        that.addClass("modify").text("修改");
        tr.find("input[name=rname],input[name=mobile],input[name=idc],input[name=qq],input[name=memo],input[name=add]").attr("disabled",false).css({"border":"1px solid red"});
        modifyagain();
    });
    }
}($);
$.livemodify();

+function($){
    $.modifyComs = function(){
        function modifyagain(){
            $(".financial_tb tr td .modify").click(function(){
            var tr = $(this).parents("tr");
            var comid = tr.find("input[name=comid]").val();
            var comval = tr.find("input[name=com]").val();
            $.post("/admin/financial/edit/",{"comid":comid,"comval":comval,"_xsrf":$.getCookie("_xsrf")},function(data){
                var data = JSON.parse(data);
                if(data['rs'] == "1040"){
                    $(".financial_tb tr td span.modify").text("已提交");
                    window.setTimeout(function(){
                       $(".financial_tb tr td span.modify").text("编辑").removeClass("modify").addClass("edit");
                       tr.find("input[name=com]").attr("disabled",true).css({"border":"0"});
                       $.modifyComs();
                    },2500)
                }else if(data['rs'] == "1041"){
                    $(".financial_tb tr td span.modify").removeClass("modify").text("已提交");
                    console.error(a,b,c,"修改提成数据出错！");
                }
            });
        });
        };
         //renew agent order commission
    $(".financial_tb tr td .edit").click(function(){
        var tr = $(this).parents("tr");
        var that = $(this);
        that.addClass("modify").text("修改");
        tr.find("input[name=com]").attr("disabled",false).css({"border":"1px solid red"});
        modifyagain();
    });
    }
}($);
$.modifyComs();
//add clients
    $("#smsf.cform #addc").click(function(){
        var html ="";
        //添加客户
        html += "<div class='frow'> <label>客户账户:</label></div>";
        html += "<div class='frow'> <label>真实姓名:</label><input type='text' id='rname' name='rname' maxlength='10'/></div>";
        html += "<div class='frow'> <label>手机号:</label><input type='text' id='mobile' name='mobile' maxlength='11'/></div>";
        html += "<div class='frow'> <label>身份证号:</label><input type='text' id='idc' name='idc' maxlength='20'/></div>";
        html += "<div class='frow'> <label>所属业务:</label><input type='text' id='wsales' name='wsales' maxlength='20' pattern='^[\u4e00-\u9fa5]{2,4}$'/></div>";
        html += "<div class='frow'><label>地址:</label><input type='text' id='add' name='add' maxlength='50' pattern='\w{6,50}'/></div>";
        html += "<div class='frow'> <label>QQ:</label><input type='text' id='qq' name='qq' maxlength='18' pattern='[0-9]{2,18}'/></div>";
        html += "<div class='frow'><label>备注:</label><input type='text' name='memo' id='memo'/></div>";
    });
    //response  ip input
    $(".machines_tb tr td.ips,.orders_tb tr td.ips").hover(function(){
        var sw = $(this).outerWidth();
        var len = $(this).find("input").val().length*13;
        if($(this).parents("table").hasClass("orders_tb")){
            len>sw?$(this).find("input").addClass("odresp"):"";

        }else{
            len>sw?$(this).find("input").addClass("resp"):"";

        }
        $("body").css("overflow-x","hidden");

    },function(){
        $(this).find("input").removeClass("resp odresp");
        $("body").css("overflow-x","auto");
    });
    //remove orders
    $(".orders_tb tr td .remove").click(function (e) {
            e.preventDefault();
            var tid = $(this).parents("tr.olist").find(".tid").text().trim();
            var that = this;
            var obj = {
                "text": "确认删除该订单?",
                "onConfirm": function () {
                    var url = "/admin/order/remove/"+tid;
                    var nthat = that;
                    $(".loading").show();
                    $.post(url,{tid:tid,_xsrf:$.getCookie("_xsrf")},function(data){
                        $(".loading").hide();
                        if(data['rs'] == "1052"){
                            $(nthat).parents('tr').children('td, th').animate({padding: 0}).wrapInner('<div />').children().slideUp(function () {
                                    $(nthat).closest('tr').remove();
                                });
                            if ($(".orders_tb tr.olist").length < 6) {
                                window.location.href = "/admin/orders/" + window.location.search;
                                }
                        }else if(data['rs'] == "1053"){
                            console.error(a,b,c,"删除订单失败!");
                        }else if(data['rs'] == "1054"){
                            $.globaltips("error","删除失败，未到订单失效时间");
                        }
                    },"json");

                }
            };
            $.confirm(obj);
        });
    //remove client
    $(".clients_tb tr td .remove").click(function (e) {
            e.preventDefault();
            var tid = $(this).parents("tr.clist").find(".tid").text().trim();
            var that = this;
            var obj = {
                "text": "确认删除该客户?",
                "onConfirm": function () {
                    var url = "/admin/client/remove/"+tid;
                    var nthat = that;
                    $(".loading").show();
                    $.post(url,{tid:tid,_xsrf:$.getCookie("_xsrf")},function(data){
                        $(".loading").hide();
                        if(data['rs'] == "1055"){
                            $(nthat).parents('tr').children('td, th').animate({padding: 0}).wrapInner('<div />').children().slideUp(function () {
                                    $(nthat).closest('tr').remove();
                                });
                            if ($(".orders_tb tr.olist").length < 6) {
                                window.location.href = "/admin/orders/" + window.location.search;
                                }
                        }else if(data['rs'] == "1056"){
                            //console.error(a,b,c,"删除客户失败!");
                        }else if(data['rs'] == "1057"){
                            $.globaltips("error","删除失败，有成交的客户无法删除!");
                        }
                    },"json");
                }
            };
            $.confirm(obj);
        });
    //only admin can modify the password
    $("#mdpwd").click(function(e){
        e.preventDefault();
        var uid = parseInt($("#power").val());
        if ([3,4,5].indexOf(uid) == -1){
            $.confirm({"text":"只有管理员才可以修改密码!"});
        }else{
            window.location.href=$(this).attr("href");
        }
    });
    //add to my client

+function($){
    $.addclient = function(){
        function addagain(){
            $(".clients_tb tr td .bind").click(function(){
            var tr = $(this).parents("tr");
            var cid = tr.find("input[name=tid]").val();
            var sales = $("#uid").val();
            $.post("/admin/client/bind/",{"cid":cid,"sales":sales,"_xsrf":$.getCookie("_xsrf")},function(data){
                var data = JSON.parse(data);
                if(data['rs'] == "1061"){
                    $(".clients_tb tr td span.bind").addclass('binded').removeClass("bind").text("已添加");
                    window.setTimeout(function(){
                       $(".clients_tb tr td span.binded").text("添加").removeClass("binded").addClass("bind");
                       $.addclient();
                    },2500)
                }else if(data['rs'] == "1062"){
                    $(".clients_tb tr td span.bind").removeClass("bind").text("添加失败");
                    console.error(a,b,c,"修改提成数据出错！");
                }
            });
        });
        };
         //renew agent order commission
    $(".clients_tb tr td .bind").click(function(){
        var tr = $(this).parents("tr");
        var that = $(this);
        addagain();
    });
    }
}($);

+function ($) {
    $.regconfig = function (selector) {
            var selector = $(selector);
            var btn = ".rform .regbtn";
            return {
                "uacc": {
                "selector": selector.find("input[name=uacc]"),
                "tips": selector.find("input[name=uacc]").siblings(".tips"),
                "button": btn,
                "regexp": /^llidc-[a-zA-Z0-9]{2,3}$/,
                "cburl": "",//callback url
                "callback": "",//callback function
                "cbkey": "",//key name in callback obj
                "ngtext": "请输入用户名.",//when input is empty
                "crtext": "已输入用户名.",//condition is met
                "extext": "",//text shows when already exists
                "rqtext": "请输入6位用户名."
                },
                "mobile": {
                "selector": selector.find("input[name=mobile]"),
                "tips": selector.find("input[name=mobile]").siblings(".tips"),
                "button": btn,
                "regexp": /\d{11}/,
                "cburl": "/client/checkmobile/",//callback url
                "callback": $.ajaxGet,//callback function
                "cbkey": "mobile",//key name in callback obj
                "ngtext": "手机号码不能为空.",//when input is empty
                "crtext": "已输入手机号码.",//condition is met
                "extext": "当前手机号码已被注册!",//text shows when already exists
                "rqtext": "请输入可用的手机号码."
            },
                "unpwd": {
                    "selector": selector.find("input[name=unpwd]"),
                    "tips": selector.find("input[name=unpwd]").siblings(".tips"),
                    "button": btn,
                    "regexp": /^[a-zA-Z0-9]{6,16}$/,
                    "cburl": "",//callback url
                    "callback": "",//callback function
                    "cbkey": "",//key name in callback obj
                    "ngtext": "请输入密码.",//when input is empty
                    "crtext": "已输入密码.",//condition is met
                    "extext": "",//text shows when already exists
                    "rqtext": "请输入6-16位登陆密码,大小写字母或数字."
                },
                "unrpwd": {
                    "selector": selector.find("input[name=unrpwd]"),
                    "tips": selector.find("input[name=unrpwd]").siblings(".tips"),
                    "button": btn,
                    "regexp": /^[a-zA-Z0-9]{6,16}$/,
                    "cburl": "",//callback url
                    "callback": "",//callback function
                    "cbkey": "",//key name in callback obj
                    "ngtext": "请输入密码.",//when input is empty
                    "crtext": "已输入密码.",//condition is met
                    "extext": "",//text shows when already exists
                    "rqtext": "请输入6-16位登陆密码,大小写字母或数字."
                },
                "msgcc": {
                    "selector": selector.find("input[name=msgcc]"),
                    "tips": selector.find("input[name=msgcc]").siblings(".tips"),
                    "button": btn,
                    "regexp": /^[0-9]{6}$/,
                    "cburl": "/client/checkmsg/",//callback url
                    "callback": $.ajaxGet,//callback function
                    "cbkey": "msgcc",//key name in callback obj
                    "ngtext": "请输入验证码.",//when input is empty
                    "crtext": "验证码正确.",//condition is met
                    "extext": "",//text shows when already exists
                    "rqtext": "请输入6位数字验证码."
                },
                "rname": {
                "selector": selector.find("input[name=rname]"),
                "tips": selector.find("input[name=rname]").siblings(".tips"),
                "button": btn,
                "regexp": /^[\u4e00-\u9fa5]{2,4}$/,
                "cburl": "",//callback url
                "callback": "",//callback function
                "cbkey": "",//key name in callback obj
                "ngtext": "用户姓名不能为空.",//when input is empty
                "crtext": "已输入会员姓名.",//condition is met
                "extext": "",//text shows when already exists
                "rqtext": "请输入2-4位用户姓名."
            }
            };
        }
}($);
$.addclient();
//export orders
    $('#export a').click(function(e){
     e.preventDefault();
     if(!$("#smsf select[name=wsales]").val()){
         $.confirm({"text":"请先选择业务员搜索订单后再导出!"});
         return false;

     }else{
         window.location.href = $(this).attr("href");
     }
    })
}($);