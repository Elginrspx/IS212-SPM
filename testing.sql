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
DROP DATABASE IF EXISTS `testdb`;
CREATE DATABASE IF NOT EXISTS `testdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `testdb`;

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
  `have` boolean NOT NULL,
  PRIMARY KEY (`courseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Insert data into `courses` table
--

insert into courses (courseID, courseName, cDescription, cOutline, have) values (1, '3D Printing Software v1.0', 'A course on 3D printing software', '3D Printing Basics, 3D Printer Software Installation', False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (2, '3D Printing Hardware v1.0', 'A course on 3D printing hardware', '3D Printer Setup',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (3, '3D Printing and Additve Manufacturing v1.0', 'This is a course on 3D printing and additive manufacturing', 'Intermediate 3D Printing, CAD Modeling', True);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (4, '3D Printing Software v1.2', 'A more advanced course on 3D printing software', '3D Printer Advanced Software Installation, Basic Post-Installation Test Check', True);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (5, 'Commerical Printer Repair v1.0', 'A course on repairing commercial printers', 'Basic Commercial Printer Repair',True);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (6, '3D Printer Hardware v1.2', 'A more advanced course on 3D printing hardware', '3D Printer Components, Testing 3D Printer',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (7, 'Xerox Printer Setup v1.0', 'A course on setting up Xerox printers', 'Introduction to Xerox Printer Models, Basic Xerox Printer Setup',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (8, 'Xerox Printer Navigation v1.0', 'A course on navigating Xerox printers post-setup', 'Xerox Printer Navigation',True);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (9, 'Xerox Printer Repair v1.0', 'A course on repairing Xerox printers', 'Xerox Printer Repair, Post-Repair Testing, Generating Test Reports',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (10, 'HP Printer Setup v1.0', 'A course on setting up HP printers', 'Introduction to HP Printer Models, Basic HP Printer Setup',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (11, 'HP Printer Navigation v1.0', 'A course on navigating HP printers post-setup', 'HP Printer Navigation',True);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (12, 'HP Printer Repair v1.0', 'A course on repairing HP printers', 'HP Printer Repair, Post-Repair Testing, Generating Test Reports',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (13, 'Canon Printer Setup v1.0', 'A course on setting up Canon printers', 'Introduction to Canon Printer Models, Basic Canon Printer Setup',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (14, 'Canon Printer Navigation v1.0', 'A course on navigating Canon printers post-setup', 'Canon Printer Navigation',True);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (15, 'Canon Printer Repair v1.0', 'A course on repairing Canon printers', 'Canon Printer Repair, Post-Repair Testing, Generating Test Reports', False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (16, 'Commercial Printer Maintenance v1.0', 'A course on Commerical Printer Basic Maintenance', 'Commercial Printer Cleaning, Commercial Printer Deep Cleaning, Commercial Printer Nozzle Check, Commercial Printer Roller Cleaning, Commercial Printer Bottom Plate Cleaning',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (17, '3D Printer Maintenance v1.0', 'A course on 3D Printer Basic Maintenance', '3D Printer Cleaning, 3D Printer Deep Cleaning, 3D Printer Nozzle Check, 3D Printer Roller Cleaning, 3D Printer Bottom Plate Cleaning',False);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (18, 'Xerox Printer Maintenance v1.0', 'A course on Xerox Printer Basic Maintenance', 'Xerox Printer Cleaning, Xerox Printer Deep Cleaning, Xerox Printer Nozzle Check, Xerox Printer Roller Cleaning, Xerox Printer Bottom Plate Cleaning',True);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (19, 'HP Printer Maintenance v1.0', 'A course on HP Printer Basic Maintenance', 'HP Printer Cleaning, HP Printer Deep Cleaning, HP Printer Nozzle Check, HP Printer Roller Cleaning, HP Printer Bottom Plate Cleaning',True);
insert into courses (courseID, courseName, cDescription, cOutline, have) values (20, 'Canon Printer Maintenance v1.0', 'A course on Canon Printer Basic Maintenance', 'Canon Printer Cleaning, Canon Printer Deep Cleaning, Canon Printer Nozzle Check, Canon Printer Roller Cleaning, Canon Printer Bottom Plate Cleaning',True);
COMMIT;

--
-- Table structure for table `students`
--
DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `studentID` INT NOT NULL,
  `studentName` varchar(30) NOT NULL,
  `sPosition` varchar(30) NOT NULL,
  PRIMARY KEY (`studentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Insert data into `students` table
--
insert into students (studentID, studentName, sPosition) values (001, 'Lim Ah Hock', 'Repair Engineer (Senior)');
insert into students (studentID, studentName, sPosition) values (002, 'David Balakrishnan', 'Repair Engineer (Senior)');
insert into students (studentID, studentName, sPosition) values (003, 'Chew Pek Ham', 'Repair Engineer (Senior)');
insert into students (studentID, studentName, sPosition) values (004, 'Muhammad Zulaiddin', 'Roving Service Engineer (Senior)');
insert into students (studentID, studentName, sPosition) values (005, 'Muhammad Danial Hakim', 'Roving Service Engineer (Senior)');
insert into students (studentID, studentName, sPosition) values (006, 'Fong Heng Heng', 'Roving Service Engineer (Senior)');
insert into students (studentID, studentName, sPosition) values (007, 'Andrew Chong', 'Roving Service Engineer (Senior)');
insert into students (studentID, studentName, sPosition) values (008, 'Tan Lim Kiu', 'Roving Service Engineer (Senior)');
insert into students (studentID, studentName, sPosition) values (009, 'Joshua Wyman', 'Roving Service Engineer (Junior)');
insert into students (studentID, studentName, sPosition) values (010, 'Jack Tan Jun Jie', 'Roving Service Engineer (Junior)');
insert into students (studentID, studentName, sPosition) values (011, 'Sevi Bala', 'Roving Service Engineer (Junior)');
insert into students (studentID, studentName, sPosition) values (012, 'Sridhar Tulawa', 'Roving Service Engineer (Junior)');
insert into students (studentID, studentName, sPosition) values (013, 'Anthony Wilson', 'Roving Service Engineer (Junior)');
insert into students (studentID, studentName, sPosition) values (014, 'Richard Goh', 'Roving Service Engineer (Junior)');
insert into students (studentID, studentName, sPosition) values (015, 'Muhammad Shahrudin', 'Roving Service Engineer (Junior)');
COMMIT;


--
-- Table structure for table `studentBadges`
--
DROP TABLE IF EXISTS `completedCourses`;
CREATE TABLE IF NOT EXISTS `completedCourses` (
  `ccStudentID` INT NOT NULL,
  `completedCName` varchar(31) NOT NULL,
  PRIMARY KEY (`ccStudentID`, `completedCName`),

  CONSTRAINT FK_Student FOREIGN KEY (`ccStudentID`)
  REFERENCES students(`studentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Insert data into `completedCourses` table
--
insert into completedCourses (ccStudentID, completedCName) values (1, '3D Printing Software v1.0');
insert into completedCourses (ccStudentID, completedCName) values (1, '3D Printing Hardware v1.0');
COMMIT;

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
  `clsLimit` int NOT NULL,
  `regPeriod` varchar(30) NOT NULL,
  PRIMARY KEY (`clsCourseID`, `classID`),
  CONSTRAINT FK_COURSE FOREIGN KEY (`clsCourseID`)
    REFERENCES courses(`courseID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Insert data into `classes` table
--
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (1,3, "Lim Ah Hock", "12-Sept-2021", "14-Sept-2023", 35, "9 October, 2021 to 9 November, 2021");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (2,2, "David Balakrishnan", "12-Sept-2021", "14-Sept-2022", 35, "11 October, 2021 to 11 November, 2021");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (1,2, "Chew Pek Ham", "12-Sept-2021", "14-Sept-2022", 40, "9 August, 2021 to 1 September, 2021");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (3,3, "Lim Ah Hock", "12-Sept-2021", "14-Sept-2022", 40, "9 August, 2021 to 1 September, 2021");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (4,3, "Lim Ah Hock", "12-Sept-2021", "14-Sept-2022", 40, "9 August, 2021 to 1 September, 2021");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (5,3, "Muhammad Zulaiddin", "12-Sept-2021", "14-Sept-2022", 40, "9 August, 2021 to 1 September, 2021");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (6,3, "Muhammad Danial Hakim", "12-Sept-2022", "14-Sept-2023", 30, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (7,3, "David Balakrishnan", "12-Sept-2022", "14-Sept-2023", 35, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (8,3, "David Balakrishnan", "12-Sept-2022", "14-Sept-2023", 35, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (9,3, "Muhammad Zulaiddin", "12-Sept-2022", "14-Sept-2023", 35, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (10,3, "Chew Pek Ham", "12-Sept-2022", "14-Sept-2023", 35, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (11,3, "Chew Pek Ham", "12-Sept-2022", "14-Sept-2023", 35, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (12,3, "Muhammad Danial Hakim", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (13,3, "Andrew Chong", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (14,3, "Andrew Chong", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (15,3, "Muhammad Danial Hakim", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (16,3, "David Balakrishnan", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (17,3, "Andrew Chong", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (18,3, "Fong Heng Heng", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (19,3, "Fong Heng Heng", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");
insert into classes (clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod) values (20,3, "Andrew Chong", "12-Sept-2022", "14-Sept-2023", 45, "9 August, 2022 to 1 September, 2022");

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
    PRIMARY KEY (`prereqCourseID`, `prereqName`),
    CONSTRAINT FK_COURSEE FOREIGN KEY (`prereqCourseID`)
    REFERENCES courses(`courseID`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

--
-- Table structure for table `registration`
--
DROP TABLE IF EXISTS `registrations`;
CREATE TABLE IF NOT EXISTS `registrations` (
  `regStudentID` INT NOT NULL,
  `regCourseID` varchar(30) NOT NULL,
  `regClassID` INT NOT NULL,
  `regStatus` varchar(30) NOT NULL,
  PRIMARY KEY (`regCourseID`,`regClassID`,`regStudentID`),
  CONSTRAINT FK_CLASSSS FOREIGN KEY (`regCourseID`,`regClassID`)
  REFERENCES classes(`clsCourseID`,`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Insert data into `registrations` table (regStatus can be "enrolled", "accepted", or "rejected")
--
insert into `registrations` (regStudentID, regCourseID, regClassID, regStatus) values (1, 6, 3, "enrolled");
insert into `registrations` (regStudentID, regCourseID, regClassID, regStatus) values (2, 6, 3, "enrolled");
insert into `registrations` (regStudentID, regCourseID, regClassID, regStatus) values (3, 6, 3, "enrolled");
insert into `registrations` (regStudentID, regCourseID, regClassID, regStatus) values (2, 7, 3, "enrolled");
insert into `registrations` (regStudentID, regCourseID, regClassID, regStatus) values (3, 7, 3, "accepted");
insert into `registrations` (regStudentID, regCourseID, regClassID, regStatus) values (2, 9, 3, "enrolled");
insert into `registrations` (regStudentID, regCourseID, regClassID, regStatus) values (3, 9, 3, "enrolled");
COMMIT;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;