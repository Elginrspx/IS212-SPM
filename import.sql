-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `systemdb`
--
DROP DATABASE IF EXISTS `systemdb`;
CREATE DATABASE IF NOT EXISTS `systemdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `systemdb`;

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
CREATE TABLE IF NOT EXISTS `courses` (
  `courseID` varchar(30) NOT NULL, 
  `courseName` varchar(30) NOT NULL, 
  `cDescription` TEXT NOT NULL,
  `cOutline` TEXT NOT NULL,
  PRIMARY KEY (`courseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Insert data into `courses` table
--

insert into courses (courseID, courseName, cDescription, cOutline) values (1, '3D Printing Software v1.0', 'A course on 3D printing software', '3D Printing Basics, 3D Printer Software Installation');
insert into courses (courseID, courseName, cDescription, cOutline) values (2, '3D Printing Hardware v1.0', 'A course on 3D printing hardware', '3D Printer Setup');
insert into courses (courseID, courseName, cDescription, cOutline) values (3, '3D Printing and Additve Manufacturing v1.0', 'This is a course on 3D printing and additive manufacturing', 'Intermediate 3D Printing, CAD Modeling');
insert into courses (courseID, courseName, cDescription, cOutline) values (4, '3D Printing Software v1.2', 'A more advanced course on 3D printing software', '3D Printer Advanced Software Installation, Basic Post-Installation Test Check');
insert into courses (courseID, courseName, cDescription, cOutline) values (5, 'Commerical Printer Repair v1.0', 'A course on repairing commercial printers', 'Basic Commercial Printer Repair');
insert into courses (courseID, courseName, cDescription, cOutline) values (6, '3D Printer Hardware v1.2', 'A more advanced course on 3D printing hardware', '3D Printer Components, Testing 3D Printer');
insert into courses (courseID, courseName, cDescription, cOutline) values (7, 'Xerox Printer Setup v1.0', 'A course on setting up Xerox printers', 'Introduction to Xerox Printer Models, Basic Xerox Printer Setup');
insert into courses (courseID, courseName, cDescription, cOutline) values (8, 'Xerox Printer Navigation v1.0', 'A course on navigating Xerox printers post-setup', 'Xerox Printer Navigation');
insert into courses (courseID, courseName, cDescription, cOutline) values (9, 'Xerox Printer Repair v1.0', 'A course on repairing Xerox printers', 'Xerox Printer Repair, Post-Repair Testing, Generating Test Reports');
insert into courses (courseID, courseName, cDescription, cOutline) values (10, 'HP Printer Setup v1.0', 'A course on setting up HP printers', 'Introduction to HP Printer Models, Basic HP Printer Setup');
insert into courses (courseID, courseName, cDescription, cOutline) values (11, 'HP Printer Navigation v1.0', 'A course on navigating HP printers post-setup', 'HP Printer Navigation');
insert into courses (courseID, courseName, cDescription, cOutline) values (12, 'HP Printer Repair v1.0', 'A course on repairing HP printers', 'HP Printer Repair, Post-Repair Testing, Generating Test Reports');
insert into courses (courseID, courseName, cDescription, cOutline) values (13, 'Canon Printer Setup v1.0', 'A course on setting up Canon printers', 'Introduction to Canon Printer Models, Basic Canon Printer Setup');
insert into courses (courseID, courseName, cDescription, cOutline) values (14, 'Canon Printer Navigation v1.0', 'A course on navigating Canon printers post-setup', 'Canon Printer Navigation');
insert into courses (courseID, courseName, cDescription, cOutline) values (15, 'Canon Printer Repair v1.0', 'A course on repairing Canon printers', 'Canon Printer Repair, Post-Repair Testing, Generating Test Reports');
insert into courses (courseID, courseName, cDescription, cOutline) values (16, 'Commercial Printer Maintenance v1.0', 'A course on Commerical Printer Basic Maintenance', 'Commercial Printer Cleaning, Commercial Printer Deep Cleaning, Commercial Printer Nozzle Check, Commercial Printer Roller Cleaning, Commercial Printer Bottom Plate Cleaning');
insert into courses (courseID, courseName, cDescription, cOutline) values (17, '3D Printer Maintenance v1.0', 'A course on 3D Printer Basic Maintenance', '3D Printer Cleaning, 3D Printer Deep Cleaning, 3D Printer Nozzle Check, 3D Printer Roller Cleaning, 3D Printer Bottom Plate Cleaning');
insert into courses (courseID, courseName, cDescription, cOutline) values (18, 'Xerox Printer Maintenance v1.0', 'A course on Xerox Printer Basic Maintenance', 'Xerox Printer Cleaning, Xerox Printer Deep Cleaning, Xerox Printer Nozzle Check, Xerox Printer Roller Cleaning, Xerox Printer Bottom Plate Cleaning');
insert into courses (courseID, courseName, cDescription, cOutline) values (19, 'HP Printer Maintenance v1.0', 'A course on HP Printer Basic Maintenance', 'HP Printer Cleaning, HP Printer Deep Cleaning, HP Printer Nozzle Check, HP Printer Roller Cleaning, HP Printer Bottom Plate Cleaning');
insert into courses (courseID, courseName, cDescription, cOutline) values (20, 'Canon Printer Maintenance v1.0', 'A course on Canon Printer Basic Maintenance', 'Canon Printer Cleaning, Canon Printer Deep Cleaning, Canon Printer Nozzle Check, Canon Printer Roller Cleaning, Canon Printer Bottom Plate Cleaning');
COMMIT;

--
-- Table structure for table `students`
--
DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `studentID` INT NOT NULL,
  `sPosition` varchar(30) NOT NULL,
  PRIMARY KEY (`studentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `studentBadges`
--
DROP TABLE IF EXISTS `studentBadges`;
CREATE TABLE IF NOT EXISTS `studentBadges` (
  `sbStudentID` INT NOT NULL,
  `sBadge` varchar(31) NOT NULL,
  PRIMARY KEY (`sbStudentID`, `sBadge`),

  CONSTRAINT FK_Student FOREIGN KEY (`sbStudentID`)
  REFERENCES students(`studentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `classes`
--
DROP TABLE IF EXISTS `classes`;
CREATE TABLE IF NOT EXISTS `classes` (
  `clsCourseID` varchar(30) NOT NULL,
  `classID` int NOT NULL,
  `clsTrainer` varchar(30) NOT NULL,
  `clsStartTime` varchar(30) NOT NULL,
  `clsEndTime` varchar(30) NOT NULL,
  PRIMARY KEY (`clsCourseID`, `classID`),
  CONSTRAINT FK_COURSE FOREIGN KEY (`clsCourseID`)
    REFERENCES courses(`courseID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Table structure for table `sections`
--
DROP TABLE IF EXISTS `sections`;
CREATE TABLE IF NOT EXISTS `sections` (
    `secCourseID` varchar(30) NOT NULL,
    `secClassID` int NOT NULL,
    `sectionID` varchar(30) NOT NULL,
    PRIMARY KEY (`secCourseID`,`secClassID`,`sectionID`),
    CONSTRAINT FK_CLASSS FOREIGN KEY (`secCourseID`,`secClassID`)
    REFERENCES classes(`clsCourseID`,`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `classlists`
--
DROP TABLE IF EXISTS `classlists`;
CREATE TABLE IF NOT EXISTS `classlists` (
    `clCourseID` varchar(30) NOT NULL,
    `clClassID` int NOT NULL,
    `clStudentID` varchar(30) NOT NULL,
    PRIMARY KEY (`clCourseID`, `clClassID`,`clStudentID`),
    CONSTRAINT FK_CLASS FOREIGN KEY (`clCourseID`, `clClassID`)
    REFERENCES classes(`clsCourseID`, `classID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Table structure for table `prerequisites`
--
DROP TABLE IF EXISTS `prerequisites`;
CREATE TABLE IF NOT EXISTS `prerequisites` (
    `prereqCourseID` varchar(30) NOT NULL,
    `prereqName` varchar(30) NOT NULL,  
    PRIMARY KEY (`reqCourseID`, `reqBadgeID`),
    CONSTRAINT FK_COURSEE FOREIGN KEY (`prereqCourseID`)
    REFERENCES courses(`courseID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

<<<<<<< Updated upstream
=======
--
-- Insert data into `prerequisites` table
--
insert into prerequisites (prereqCourseID, prereqName) values (4, '3D Printing Software v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (8, 'Xerox Printer Setup v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (11, 'HP Printer Setup v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (14, 'Canon Printer Setup v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (3, '3D Printing Software v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (3, '3D Printing Hardware v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (18, 'Xerox Printer Navigation v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (19, 'HP Printer Navigation v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (20, 'Canon Printer Navigation v1.0');
insert into prerequisites (prereqCourseID, prereqName) values (5, 'Commercial Printer Maintenance v1.0');
COMMIT;
>>>>>>> Stashed changes

--
-- Table structure for table `registration`
--
DROP TABLE IF EXISTS `registration`;
CREATE TABLE IF NOT EXISTS `registration` (
  `regStudentID` INT NOT NULL,
  `regCourseID` varchar(30) NOT NULL,
  `regClassID` INT NOT NULL,
  `regStatus` varchar(30) NOT NULL,
  PRIMARY KEY (`regCourseID`,`regClassID`,`regStudentID`),
  CONSTRAINT FK_CLASSSS FOREIGN KEY (`regCourseID`,`regClassID`)
  REFERENCES classes(`clsCourseID`,`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;





/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;