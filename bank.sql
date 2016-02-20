-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 22, 2015 at 10:25 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE IF NOT EXISTS `account` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CustID` int(11) NOT NULL,
  `money_amount` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  KEY `c` (`CustID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`ID`, `CustID`, `money_amount`) VALUES
(1, 0, 3562);

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE IF NOT EXISTS `transaction` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `AccID` int(11) NOT NULL,
  `Type` varchar(8) NOT NULL,
  `Amont` float NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `c1` (`AccID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`ID`, `AccID`, `Type`, `Amont`, `Time`) VALUES
(1, 1, 'deposite', 562, '2015-12-21 22:00:00'),
(4, 1, 'deposite', 1000, '2015-12-22 21:22:36');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `User_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Phone` int(11) NOT NULL,
  `Email` varchar(150) NOT NULL,
  `Adress` varchar(150) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Question` varchar(150) NOT NULL,
  `Answer` varchar(100) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Active` int(11) NOT NULL,
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`User_ID`, `Name`, `Phone`, `Email`, `Adress`, `Username`, `Password`, `Question`, `Answer`, `Type`, `Active`) VALUES
(0, 'Ahmed', 1144872926, 'mmageca36.af@gmail.com', 'cairo', 'Ahmed', '20130058', '', '', 'Customer', 1),
(4, 'Ahmed', 1144872926, 'ahmed@yahoo', 'AAAA', 'Fawzy', '20130130', '', '', 'Customer', 1),
(6, 'Ahmed Fawzy', 1115285531, 'm@yahoo.com', 'cairo', 'Ahm', 'Ahm2014!', 'What is your favorite color ?', 'red', 'Customer', 1),
(7, '', 0, 'aaaaaaaaaaaaaaaaaaaaaaaa', '', '', '', '', '', 'Customer', 1),
(8, 'Ahmed', 1144826652, '@google', 'cairo', '20130130', '20130130', 'Your Mother Name ?', 'aya', 'Customer', 1),
(9, '', 0, '', '', '', '', '', '', 'Customer', 1),
(10, 'Ahmed', 1115285531, 'fawzy@', 'giza', 'a', 'a', 'What''s your favorite color ?', 'blue', 'Admin', 1),
(11, 'a', 0, 'a', 'a', 'a', 'a', 'What''s your favorite color ?', 'a', 'Admin', 1),
(12, '', 0, '', '', '', '', 'What is your favorite color ?', '', 'Customer', 1),
(13, 'omnia', 1115285531, '@yahoo', 'nasr', 'omnia', 'omnia', 'What is your favorite color ?', 'orange', 'Customer', 1),
(14, '', 0, '', '', '', '', 'What is your favorite color ?', '', 'Customer', 1),
(15, 'omnia', 2147483647, 'aaa', 'aaaa', 'omnia', 'omnia', 'What is your favorite color ?', 'orange', 'Customer', 1),
(16, 'omnia', 1115285531, 'aaa', 'aaaa', 'omnia', 'omnia', 'What is your favorite color ?', 'orange', 'Customer', 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `c11` FOREIGN KEY (`CustID`) REFERENCES `user` (`User_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `c1` FOREIGN KEY (`AccID`) REFERENCES `account` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
