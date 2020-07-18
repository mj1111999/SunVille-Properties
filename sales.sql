-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 18, 2020 at 04:13 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sales`
--

-- --------------------------------------------------------

--
-- Table structure for table `agents`
--

DROP TABLE IF EXISTS `agents`;
CREATE TABLE IF NOT EXISTS `agents` (
  `AGENT_CODE` varchar(6) NOT NULL DEFAULT '',
  `AGENT_NAME` varchar(40) DEFAULT NULL,
  `WORKING_AREA` varchar(35) DEFAULT NULL,
  `COMMISSION` decimal(10,2) DEFAULT NULL,
  `PHONE_NO` varchar(15) DEFAULT NULL,
  `COUNTRY` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`AGENT_CODE`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `agents`
--

INSERT INTO `agents` (`AGENT_CODE`, `AGENT_NAME`, `WORKING_AREA`, `COMMISSION`, `PHONE_NO`, `COUNTRY`) VALUES
('A007  ', 'Ramasundar                              ', 'Bangalore                          ', '0.15', '077-25814763   ', '\r'),
('A003  ', 'Alex                                    ', 'London                             ', '0.13', '075-12458969   ', '\r'),
('A008  ', 'Alford                                  ', 'New York                           ', '0.12', '044-25874365   ', '\r'),
('A011  ', 'Ravi Kumar                              ', 'Bangalore                          ', '0.15', '077-45625874   ', '\r'),
('A010  ', 'Santakumar                              ', 'Chennai                            ', '0.14', '007-22388644   ', '\r'),
('A012  ', 'Lucida                                  ', 'San Jose                           ', '0.12', '044-52981425   ', '\r'),
('A005  ', 'Anderson                                ', 'Brisban                            ', '0.13', '045-21447739   ', '\r'),
('A001  ', 'Subbarao                                ', 'Bangalore                          ', '0.14', '077-12346674   ', '\r'),
('A002  ', 'Mukesh                                  ', 'Mumbai                             ', '0.11', '029-12358964   ', '\r'),
('A006  ', 'McDen                                   ', 'London                             ', '0.15', '078-22255588   ', '\r'),
('A004  ', 'Ivan                                    ', 'Torento                            ', '0.15', '008-22544166   ', '\r'),
('A009  ', 'Benjamin                                ', 'Hampshair                          ', '0.11', '008-22536178   ', '\r'),
('A100', 'Mohit', 'Charkop', '0.55', '8655748746', 'India'),
('A202', 'Harshit', 'Malad', '0.64', '9821460092', 'India'),
('A432', 'Nikunj', 'New York', '0.44', '7654321095', 'USA'),
('A999', 'Kushal', 'Mumbai', '0.76', '1234567890', 'India'),
('A993', 'Shivam', 'Mumbai', '0.43', '7653472534', 'India'),
('A789', 'Aniket', 'Thane', '0.88', '4543289064', 'India'),
('A344', 'Vaibhav Sharma', 'Borivali', '0.79', '7844996510', 'India'),
('A016', 'Sonu', 'Chandigarh', '0.57', '8765456432', 'India');

-- --------------------------------------------------------

--
-- Table structure for table `agent_details`
--

DROP TABLE IF EXISTS `agent_details`;
CREATE TABLE IF NOT EXISTS `agent_details` (
  `fullname` text NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL,
  `gender` text NOT NULL,
  `country` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `agent_details`
--

INSERT INTO `agent_details` (`fullname`, `email`, `password`, `gender`, `country`) VALUES
('Ramasundar', 'ramasundar@gmail.com', 'qwertyui', 'male', 'INDIA'),
('Alex', 'alex@gmail.com', 'qwertyui', 'male', 'UK'),
('Mukesh', 'mukesh@yahoo.com', 'qwerty', 'male', 'INDIA'),
('Lucida', 'lucida@yahoo.com', 'qwertyui', 'female', 'UK'),
('Anderson', 'anderson12@gmail.com', 'aqwerty1', 'male', 'UK'),
('Alford', 'alford124@yahoo.com', 'qwertyuio', 'male', 'AUSTRALIA'),
('Subbarao', 'subbarao22@gmail.com', 'qwertyui', 'male', 'INDIA'),
('Ramasundar', 'anderson12@gmail.com\n', 'aqwerty1\n', 'male', 'INDIA'),
('Lucida', 'lucida@gmail.com', 'qwertyui', 'female', 'UK'),
('Lucida', 'lucida@ygmail.com', 'qwertyui', 'female', 'UK');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
CREATE TABLE IF NOT EXISTS `company` (
  `COMPANY_ID` varchar(6) NOT NULL DEFAULT '',
  `COMPANY_NAME` varchar(25) DEFAULT NULL,
  `COMPANY_CITY` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`COMPANY_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`COMPANY_ID`, `COMPANY_NAME`, `COMPANY_CITY`) VALUES
('18', 'Order All', 'Boston\r'),
('15', 'Jack Hill Ltd', 'London\r'),
('16', 'Akas House', 'Delhi\r'),
('17', 'Foilos housing.', 'London\r'),
('19', 'stop-and-buy', 'New York\r'),
('20', 'Magic Bricks', 'Mumbai'),
('21', 'Property Bazaar', 'Ladakh'),
('88', 'Property Dekho', 'Nallasopara'),
('89', 'Property wale', 'Virar'),
('45', 'Avenue Realty', 'Boston'),
('22', 'Lodha Group', 'Jammu'),
('12345', 'Godrej prop', 'Mumbai'),
('555', 'Godrej prop', 'Mumbai'),
('5556', 'Godrej prop', 'Mumbai');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `CUST_CODE` varchar(6) NOT NULL,
  `CUST_NAME` varchar(40) NOT NULL,
  `CUST_CITY` varchar(35) DEFAULT NULL,
  `WORKING_AREA` varchar(35) NOT NULL,
  `CUST_COUNTRY` varchar(20) NOT NULL,
  `GRADE` decimal(10,0) DEFAULT NULL,
  `OPENING_AMT` decimal(12,2) NOT NULL,
  `RECEIVE_AMT` decimal(12,2) NOT NULL,
  `PAYMENT_AMT` decimal(12,2) NOT NULL,
  `OUTSTANDING_AMT` decimal(12,2) NOT NULL,
  `PHONE_NO` varchar(17) NOT NULL,
  `AGENT_CODE` varchar(6) DEFAULT NULL,
  KEY `CUSTCITY` (`CUST_CITY`),
  KEY `CUSTCITY_COUNTRY` (`CUST_CITY`,`CUST_COUNTRY`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`CUST_CODE`, `CUST_NAME`, `CUST_CITY`, `WORKING_AREA`, `CUST_COUNTRY`, `GRADE`, `OPENING_AMT`, `RECEIVE_AMT`, `PAYMENT_AMT`, `OUTSTANDING_AMT`, `PHONE_NO`, `AGENT_CODE`) VALUES
('C00013', 'Holmes', 'London                             ', 'London', 'UK', '2', '6000.00', '5000.00', '7000.00', '4000.00', 'BBBBBBB', 'A003  '),
('C00001', 'Micheal', 'New York                           ', 'New York', 'USA', '2', '3000.00', '5000.00', '2000.00', '6000.00', 'CCCCCCC', 'A008  '),
('C00020', 'Albert', 'New York                           ', 'New York', 'USA', '3', '5000.00', '7000.00', '6000.00', '6000.00', 'BBBBSBB', 'A008  '),
('C00025', 'Ravindran', 'Bangalore                          ', 'Bangalore', 'India', '2', '5000.00', '7000.00', '4000.00', '8000.00', 'AVAVAVA', 'A011  '),
('C00024', 'Cook', 'London                             ', 'London', 'UK', '2', '4000.00', '9000.00', '7000.00', '6000.00', 'FSDDSDF', 'A006  '),
('C00015', 'Stuart', 'London                             ', 'London', 'UK', '1', '6000.00', '8000.00', '3000.00', '11000.00', 'GFSGERS', 'A003  '),
('C00002', 'Bolt', 'New York                           ', 'New York', 'USA', '3', '5000.00', '7000.00', '9000.00', '3000.00', 'DDNRDRH', 'A008  '),
('C00018', 'Fleming', 'Brisban                            ', 'Brisban', 'Australia', '2', '7000.00', '7000.00', '9000.00', '5000.00', 'NHBGVFC', 'A005  '),
('C00021', 'Jacks', 'Brisban                            ', 'Brisban', 'Australia', '1', '7000.00', '7000.00', '7000.00', '7000.00', 'WERTGDF', 'A005  '),
('C00019', 'Yearannaidu', 'Chennai                            ', 'Chennai', 'India', '1', '8000.00', '7000.00', '7000.00', '8000.00', 'ZZZZBFV', 'A010  '),
('C00005', 'Sasikant', 'Mumbai                             ', 'Mumbai', 'India', '1', '7000.00', '11000.00', '7000.00', '11000.00', '147-25896312', 'A002  '),
('C00007', 'Ramanathan', 'Chennai                            ', 'Chennai', 'India', '1', '7000.00', '11000.00', '9000.00', '9000.00', 'GHRDWSD', 'A010  '),
('C00022', 'Avinash', 'Mumbai                             ', 'Mumbai', 'India', '2', '7000.00', '11000.00', '9000.00', '9000.00', '113-12345678', 'A002  '),
('C00004', 'Winston', 'Brisban                            ', 'Brisban', 'Australia', '1', '5000.00', '8000.00', '7000.00', '6000.00', 'AAAAAAA', 'A005  '),
('C00023', 'Karl', 'London                             ', 'London', 'UK', '0', '4000.00', '6000.00', '7000.00', '3000.00', 'AAAABAA', 'A006  '),
('C00006', 'Shilton', 'Torento                            ', 'Torento', 'Canada', '1', '10000.00', '7000.00', '6000.00', '11000.00', 'DDDDDDD', 'A004  '),
('C00010', 'Charles', 'Hampshair                          ', 'Hampshair', 'UK', '3', '6000.00', '4000.00', '5000.00', '5000.00', 'MMMMMMM', 'A009  '),
('C00017', 'Srinivas', 'Bangalore                          ', 'Bangalore', 'India', '2', '8000.00', '4000.00', '3000.00', '9000.00', 'AAAAAAB', 'A007  '),
('C00012', 'Steven', 'San Jose                           ', 'San Jose', 'USA', '1', '5000.00', '7000.00', '9000.00', '3000.00', 'KRFYGJK', 'A012  '),
('C00008', 'Karolina', 'Torento                            ', 'Torento', 'Canada', '1', '7000.00', '7000.00', '9000.00', '5000.00', 'HJKORED', 'A004  '),
('C00003', 'Martin', 'Torento                            ', 'Torento', 'Canada', '2', '8000.00', '7000.00', '7000.00', '8000.00', 'MJYURFD', 'A004  '),
('C00009', 'Ramesh', 'Mumbai                             ', 'Mumbai', 'India', '3', '8000.00', '7000.00', '3000.00', '12000.00', 'Phone No', 'A002  '),
('C00014', 'Rangarappa', 'Bangalore                          ', 'Bangalore', 'India', '2', '8000.00', '11000.00', '7000.00', '12000.00', 'AAAATGF', 'A001  '),
('C00016', 'Venkatpati', 'Bangalore                          ', 'Bangalore', 'India', '2', '8000.00', '11000.00', '7000.00', '12000.00', 'JRTVFDD', 'A007  '),
('C00011', 'Sundariya', 'Chennai                            ', 'Chennai', 'India', '3', '7000.00', '11000.00', '7000.00', '11000.00', 'PPHGRTS', 'A010  '),
('C00007', 'Prithvi', 'Mumbai', 'Maharashtra', 'India', '1', '13534.00', '32156.00', '564563.00', '2223123.00', '12345678', 'A003'),
('C12345', 'Mohit ', 'Mumbai', 'Maharashtra', 'India', '1', '1234.00', '4321.00', '4321.00', '1234.00', '7977648194', 'A009'),
('C00078', 'Neelam Jain', 'Mumbai', 'Bihar', 'India', '3', '1234.00', '4320.00', '1111.00', '3000.00', '1234567890', 'A1'),
('C10000', 'Kaushal', 'Mumbai', 'Lower Parel', 'India', '3', '1256.00', '4456.00', '3456.00', '5456.00', '9821460092', 'A009'),
('C11111', 'Shivam', 'Andheri', 'Mumbai', 'India', '1', '5674.00', '3456.00', '5674.00', '3332.00', '2635435463', 'A100'),
('C11111', '26314', '5324', '3524361', 'India', '1', '5674.00', '3456.00', '5674.00', '3332.00', '2635435463', 'A100'),
('C78936', 'Vimlesh', 'Mumbai ', 'Bhayandar', 'India', '1', '1234.00', '234.00', '2222.00', '9876.00', '7546454521', 'A101'),
('C99654', 'Dhruvik', 'Bhavnagar', 'Gujarat', 'India', '1', '2234.00', '1000.00', '1234.00', '2222.00', '7977101774', 'A222'),
('C99654', 'Dhruvik', 'Bhavnagar', 'Gujarat', 'India', '1', '2234.00', '1000.00', '1234.00', '2222.00', '7977101774', 'A222'),
('C99654', 'Dhruvik', 'Bhavnagar', 'Gujarat', 'India', '1', '2234.00', '1000.00', '1234.00', '2222.00', '7977101774', 'A222'),
('C99654', 'Dhruvik', 'Bhavnagar', 'Gujarat', 'India', '1', '2234.00', '1000.00', '1234.00', '2222.00', '7977101774', 'A222'),
('C99654', 'Dhruvik', 'Bhavnagar', 'Gujarat', 'India', '1', '2234.00', '1000.00', '1234.00', '2222.00', '7977101774', 'A222'),
('C99654', 'Dhruvik', 'Bhavnagar', 'Gujarat', 'India', '1', '2234.00', '1000.00', '1234.00', '2222.00', '7977101774', 'A222');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `ORD_NUM` decimal(6,0) NOT NULL,
  `ORD_AMOUNT` decimal(12,2) NOT NULL,
  `ADVANCE_AMOUNT` decimal(12,2) NOT NULL,
  `ORD_DATE` date NOT NULL,
  `CUST_CODE` varchar(6) NOT NULL,
  `AGENT_CODE` varchar(6) NOT NULL,
  `ORD_DESCRIPTION` varchar(60) NOT NULL,
  `Agent_Name` varchar(30) NOT NULL,
  `Balance_Amount` int(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`ORD_NUM`, `ORD_AMOUNT`, `ADVANCE_AMOUNT`, `ORD_DATE`, `CUST_CODE`, `AGENT_CODE`, `ORD_DESCRIPTION`, `Agent_Name`, `Balance_Amount`) VALUES
('200100', '1000.00', '600.00', '2008-01-08', 'C00015', 'A003  ', 'SOD\r', 'Alex', 400),
('200110', '3000.00', '500.00', '2008-04-15', 'C00019', 'A010  ', 'SOD\r', 'Santakumar', 2500),
('200107', '4500.00', '900.00', '2008-08-30', 'C00007', 'A010  ', 'SOD\r', 'Santakumar', 3600),
('200112', '2000.00', '400.00', '2008-05-30', 'C00016', 'A007  ', 'SOD\r', 'Ramasundar', 1600),
('200113', '4000.00', '600.00', '2008-06-10', 'C00022', 'A002  ', 'SOD\r', 'Mukesh', 3400),
('200102', '2000.00', '300.00', '2008-05-25', 'C00012', 'A012  ', 'SOD\r', 'Lucida', 1700),
('200114', '3500.00', '2000.00', '2008-08-15', 'C00002', 'A008  ', 'SOD\r', 'Alford', 1500),
('200122', '2500.00', '400.00', '2008-09-16', 'C00003', 'A004  ', 'SOD\r', 'Ivan', 2100),
('200118', '500.00', '100.00', '2008-07-20', 'C00023', 'A006  ', 'SOD\r', 'McDen', 400),
('200119', '4000.00', '700.00', '2008-09-16', 'C00007', 'A010  ', 'SOD\r', 'Santakumar', 3600),
('200121', '1500.00', '600.00', '2008-09-23', 'C00008', 'A004  ', 'SOD\r', 'Ivan', 900),
('200130', '2500.00', '400.00', '2008-07-30', 'C00025', 'A011  ', 'SOD\r', 'Ravikumar', 2100),
('200134', '4200.00', '1800.00', '2008-09-25', 'C00004', 'A005  ', 'SOD\r', 'Anderson', 2400),
('200115', '2000.00', '1200.00', '2008-02-08', 'C00013', 'A013  ', 'SOD\r', '', 800),
('200108', '4000.00', '600.00', '2008-02-15', 'C00008', 'A004  ', 'SOD\r', 'Ivan', 3400),
('200103', '1500.00', '700.00', '2008-05-15', 'C00021', 'A005  ', 'SOD\r', 'Anderson', 800),
('200105', '2500.00', '500.00', '2008-07-18', 'C00025', 'A011  ', 'SOD\r', 'Ravikumar', 2000),
('200109', '3500.00', '800.00', '2008-07-30', 'C00011', 'A010  ', 'SOD\r', 'Santakumar', 2700),
('200101', '3000.00', '1000.00', '2008-07-15', 'C00001', 'A008  ', 'SOD\r', 'Alford', 2000),
('200111', '1000.00', '300.00', '2008-07-10', 'C00020', 'A008  ', 'SOD\r', 'Alford', 700),
('200104', '1500.00', '500.00', '2008-03-13', 'C00006', 'A004  ', 'SOD\r', 'Ivan', 1000),
('200106', '2500.00', '700.00', '2008-04-20', 'C00005', 'A002  ', 'SOD\r', 'Mukesh', 1800),
('200125', '2000.00', '600.00', '2008-10-10', 'C00018', 'A005  ', 'SOD\r', 'Anderson', 1400),
('200117', '800.00', '200.00', '2008-10-20', 'C00014', 'A001  ', 'SOD\r', 'Subbaro', 600),
('200123', '500.00', '100.00', '2008-09-16', 'C00022', 'A002  ', 'SOD\r', 'Mukesh', 400),
('200120', '500.00', '100.00', '2008-07-20', 'C00009', 'A002  ', 'SOD\r', 'Mukesh', 400),
('200116', '500.00', '100.00', '2008-07-13', 'C00010', 'A009  ', 'SOD\r', 'Benjamin', 400),
('200124', '500.00', '100.00', '2008-06-20', 'C00017', 'A007  ', 'SOD\r', 'Ramasundar', 400),
('200126', '500.00', '100.00', '2008-06-24', 'C00022', 'A002  ', 'SOD\r', 'Mukesh', 400),
('200129', '2500.00', '500.00', '2008-07-20', 'C00024', 'A006  ', 'SOD\r', 'McDen', 2000),
('200127', '2500.00', '400.00', '2008-07-20', 'C00015', 'A003  ', 'SOD\r', 'Alex', 2100),
('200128', '3500.00', '1500.00', '2008-07-20', 'C00009', 'A002  ', 'SOD\r', 'Mukesh', 2000),
('200135', '2000.00', '800.00', '2008-09-16', 'C00007', 'A010  ', 'SOD\r', 'Santakumar', 1200),
('200131', '900.00', '150.00', '2008-08-26', 'C00012', 'A012  ', 'SOD\r', 'Lucida', 750),
('200133', '1200.00', '400.00', '2008-06-29', 'C00009', 'A002  ', 'SOD\r', 'Mukesh', 800),
('200132', '4000.00', '2000.00', '2008-08-15', 'C00013', 'A013  ', 'SOD\r', '', 2000),
('200100', '1000.00', '600.00', '2008-01-08', 'C00015', 'A003', 'SOD ', 'Alex', 400),
('200111', '1000.00', '300.00', '2008-07-10', 'C00020', 'A008', 'SOD', 'Alford', 700),
('200116', '500.00', '100.00', '2008-07-13', 'C00010', 'A009  ', 'SOD', 'Benjamin', 400),
('201045', '4000.00', '2000.00', '2008-12-10', 'C12345', 'A016', 'SOD', 'Sonu', 2000),
('200999', '8000.00', '1000.00', '2009-01-08', 'C23437', 'A016', 'SOD', 'Sonu', 7000);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
