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
                    //$.checkField("#rvform", btn);

                } else if (data["cre"] == 1) {
                    $(tips).hasClass("cr") ? $(tips).removeClass("cr") : "";
                    $(tips).text(extext);
                    $(btn).css("background-color", "#ccc").attr("disabled", true);
                }
            }
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
                "regexp": /\d{6}$/,
                "cburl": "",//callback url
                "callback": "",//callback function
                "cbkey": "",//key name in callback obj
                "ngtext": "请输入用户名.",//when input is empty
                "crtext": "已输入用户名.",//condition is met
                "extext": "",//text shows when already exists
                "rqtext": "请输入6位数字用户名."
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
                }
            };
        }
}($);
+function($){
    $(document).ready(function(){


    })
}($);

