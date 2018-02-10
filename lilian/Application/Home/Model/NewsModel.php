<?php
namespace Home\Model;
use Think\Model;
class NewsModel extends Model {
    //protected $tableName = 'news';
    protected $tablePrefix = 'llidc_';//没有表前缀的情况必须设置，否则会获取当前配置文件中的 DB_PREFIX。

}