CREATE DATABASE IF NOT EXISTS `phasetwo` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `phasetwo`;


DROP TABLE IF EXISTS `chanel`;
CREATE TABLE IF NOT EXISTS `chanel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `client`;
CREATE TABLE IF NOT EXISTS `client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_name` (`uuid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `event`;
CREATE TABLE IF NOT EXISTS `event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chanel_id` int(11) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `notification`;
CREATE TABLE IF NOT EXISTS `notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `subscription`;
CREATE TABLE IF NOT EXISTS `subscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `chanel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;