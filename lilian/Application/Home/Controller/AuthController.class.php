<?php
namespace Home\Controller;
use Think\Controller;
class AuthController extends Controller {
    //登陆页面
    public function login(){
        $this->display();
    }
    //注册页面
    public function reg(){
        $this->display();
    }
}