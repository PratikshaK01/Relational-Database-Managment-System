password=b'gAAAAABhaxV695eDS7jTSEGP7Xw-Q3veZR7kW38WFLSvnKhoQ6ejECT5OjXRGSaGwoOmZGaXaQyquLO6-cpNjKmJSNiTBTgoVw=='

database='forms'

TableName='student_info'

ColumnName='Gr_no,rollNumber,firstName,surName,email,mobileNumber,aadhar,PAN,passport,nationality,isAadhar,isPAN,isPassport,isIndian,fathersName,mothersName,permanantAddress,residentialAddress,state,city,pincode,tenthCGPA,twelfthCGPA,tenthGrade,twelfthGrade,firstSemCGPA,secondSemCGPA,thirdSemCGPA,fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,branch_name,college_name,isDiploma,diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,currentBatch'


pIIColoumn=['FirstName','SurName','aadhar','pan','passport','mobileNumber','permanantAddress','residentialAddress']

InsertTemplate = "INSERT INTO {} ({}) VALUES {}"

getMaxValue="SELECT MAX(Gr_no) FROM {};"

emailLength=9
passLength=9
adharLength=12
panLength=10
mobileLength=10


rowsToBeInserted=300
