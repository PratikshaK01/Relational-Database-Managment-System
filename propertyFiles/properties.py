password=b'gAAAAABhaxV695eDS7jTSEGP7Xw-Q3veZR7kW38WFLSvnKhoQ6ejECT5OjXRGSaGwoOmZGaXaQyquLO6-cpNjKmJSNiTBTgoVw=='

database='forms'

TableName='student_info'

ColumnName='Gr_no,rollNumber,firstName,surName,email,mobileNumber,aadhar,PAN,passport,nationality,isAadhar,isPAN,isPassport,isIndian,fathersName,mothersName,permanantAddress,residentialAddress,state,city,pincode,tenthCGPA,twelfthCGPA,tenthGrade,twelfthGrade,firstSemCGPA,secondSemCGPA,thirdSemCGPA,fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,branch_name,college_name,isDiploma,diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,currentBatch'

pIIColoumn=['FirstName,SurName,FathersName,MothersName,PerosonalAddress,aadhar,pan,passport']

InsertTemplate = "INSERT INTO {} ({}) VALUES {}"



noOfRecordsTobeInserted=1000
