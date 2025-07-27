-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 31, 2023 at 01:28 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25
use clg;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clg`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_table`
--

CREATE TABLE `admin_table` (
  `id` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_table`
--

INSERT INTO `admin_table` (`id`, `password`) VALUES
('admin', '123');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `name`, `email`, `gender`, `contact`, `dob`, `address`) VALUES
('4', '45', '4', 'Female', '655464', '56356', '465534'),
('45', '444', '4', 'Female', '655464', '56356', '465534'),
('6', '455', '4', 'Female', '655464', '56356', '465534');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `roll_no` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `class` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `std_password` varchar(100) NOT NULL,
  `sub1` varchar(100) NOT NULL,
  `om1` varchar(100) NOT NULL,
  `tm1` varchar(100) NOT NULL,
  `sub2` varchar(100) NOT NULL,
  `om2` varchar(100) NOT NULL,
  `tm2` varchar(100) NOT NULL,
  `sub3` varchar(100) NOT NULL,
  `om3` varchar(100) NOT NULL,
  `tm3` varchar(100) NOT NULL,
  `sub4` varchar(100) NOT NULL,
  `om4` varchar(100) NOT NULL,
  `tm4` varchar(100) NOT NULL,
  `sub5` varchar(100) NOT NULL,
  `om5` varchar(100) NOT NULL,
  `tm5` varchar(100) NOT NULL,
  `sub6` varchar(100) NOT NULL,
  `om6` varchar(100) NOT NULL,
  `tm6` varchar(100) NOT NULL,
  `sub7` varchar(100) NOT NULL,
  `om7` varchar(100) NOT NULL,
  `tm7` varchar(100) NOT NULL,
  `sub8` varchar(100) NOT NULL,
  `om8` varchar(100) NOT NULL,
  `tm8` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`roll_no`, `name`, `class`, `gender`, `contact`, `dob`, `address`, `std_password`, `sub1`, `om1`, `tm1`, `sub2`, `om2`, `tm2`, `sub3`, `om3`, `tm3`, `sub4`, `om4`, `tm4`, `sub5`, `om5`, `tm5`, `sub6`, `om6`, `tm6`, `sub7`, `om7`, `tm7`, `sub8`, `om8`, `tm8`) VALUES
('20BCA101', 'Aman kumar', 'BCA 3rd year', 'Male', '8219733957', '16/12/2002', 'vill ma', '12345', 'hindi', '50', '100', 'english', '50', '500', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('20BCA104', 'Aman2222', 'BCA 3rd year', 'Male', '8219733957', '16/12/2002', 'vill ma', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('20BCA105', 'Aman ', 'BCA 3rd year', 'Male', '8219733955', '16/12/2002', 'vill ma', '16/12/2002', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('20BCA106', 'Aman ', 'BCA 3rd year', 'Male', '8219733955', '16/12/2002', 'vill ma', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('20BCA113', 'keshav124', 'BCA 3rd year', 'Male', '8219733957', '16/12/2002', 'vill malag ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('20BCA114', 'keshav124', 'BBA 1st year', 'Male', '8219733957', '16/12/2002', 'vill malag ', '16/12/2002', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_table`
--
ALTER TABLE `admin_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`roll_no`) USING BTREE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
