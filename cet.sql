-- phpMyAdmin SQL Dump
-- version phpStudy 2014
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2018 �?12 �?04 �?09:38
-- 服务器版本: 5.5.53
-- PHP 版本: 5.6.27

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `test`
--

-- --------------------------------------------------------

--
-- 表的结构 `cet`
--

CREATE TABLE IF NOT EXISTS `cet` (
  `id` mediumint(6) NOT NULL AUTO_INCREMENT,
  `zkzh` varchar(50) NOT NULL COMMENT '准考证',
  `name` varchar(50) NOT NULL COMMENT '姓名',
  `sfzh` varchar(50) NOT NULL COMMENT '身份证',
  `xuehao` varchar(50) NOT NULL COMMENT '学号',
  `time` varchar(50) NOT NULL COMMENT '考试时间',
  `type` varchar(50) NOT NULL COMMENT '考试类型',
  `where` varchar(255) NOT NULL COMMENT '考试地点',
  `kc` varchar(50) NOT NULL COMMENT '考场号',
  `zw` varchar(50) NOT NULL COMMENT '座位号',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
