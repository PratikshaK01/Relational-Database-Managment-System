CREATE DATABASE IF NOT EXISTS forms;
CREATE TABLE IF NOT EXISTS student_info(

 Gr_no varchar(11) not null unique primary key,
rollNumber	int	not null unique,
firstName varchar(100),
surName varchar(100),
email nvarchar(320) not null unique,
mobileNumber varchar(100) not null unique,
aadhar varchar(100) not null unique,
PAN	varchar(100) unique,
passport varchar(100) unique,
nationality varchar(20),
isAadhar boolean,
isPAN boolean,
isPassport boolean,
isIndian boolean,
fathersName varchar(20),
mothersName varchar(20),
permanantAddress varchar(100),
residentialAddress varchar(100),
state varchar(255),
city varchar(255),
pincode int,
tenthCGPA float,
twelfthCGPA float,
tenthGrade float,
twelfthGrade float,
firstSemCGPA float,
secondSemCGPA float,
thirdSemCGPA float,
fourthSemCGPA float,
fifthSemCGPA float,
sixthSemCGPA float,
seventhSemCGPA float,
eightthSemGCPA float,
branch_name varchar(255),
college_name varchar(255),
isDiploma boolean,
diplomaMarks float,
isBacklog boolean,
numberOfBacklogs int,
activeBacklog int,
PassiveBacklog int,
isYD boolean,
YDYears int,
isEducationGap boolean,
educationGapYears int,
currentBatch int
)
