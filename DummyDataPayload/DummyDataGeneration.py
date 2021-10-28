from dummyDataPayload import *
import sys
import random
sys.path.append('../DatabaseConnection')
sys.path.append('../propertyFiles')
from DbConnection import *
from Utilities import *

FinalString=""

#Loweround->max(db)->insertion sathi
#Upperbound->lastvalue->lowerbound+val
result1=getQuery("SELECT MAX(Gr_no) FROM student_info;")
# print(type(result1))
lowerBound=0
upperBound=2

for RowValue in range(lowerBound,upperBound):
    fName=getFirstName()
    sName=getSurname()
    fTName=getMaleName()
    mTName=getFemaleName()

    # Encrypted-Pritesh
    arr=[fName,sName,fTName,mTName]
    #we need to add email,personaladdress,
    # PerosonalAddress,aadhar,pan,passport
    encrypted=getEncryptedValue(arr)

    fName=encrypted[0]
    sName=encrypted[1]
    fTName=encrypted[2]
    mTName=encrypted[3]

    InitialRow="('{}',{},'{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{})"
    InitialRow=InitialRow.format(Gr_no.format(RowValue),
    rollNumber.format(RowValue),
    firstName.format(fName),
    surName.format(sName),
    email.format(RowValue),
    mobileNumber.format(RowValue),
    aadhar.format(RowValue),
    PAN.format(RowValue),
    passport.format(RowValue),
    nationality,isAadhar,isPAN,isPassport,isIndian,
    fathersName.format(fTName),
    mothersName.format(mTName),
    permanantAddress.format(RowValue),
    residentialAddress.format(RowValue),
    state.format(RowValue),
    city.format(RowValue),
    pincode.format(RowValue),
    tenthCGPA,twelfthCGPA,tenthGrade,twelfthGrade,firstSemCGPA,secondSemCGPA,thirdSemCGPA,
    fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,
    branch_name.format(RowValue),
    college_name.format(RowValue),
    isDiploma,diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,PassiveBacklog,
    isYD,YDYears,isEducationGap,educationGapYears,currentBatch)

    FinalString=FinalString+InitialRow
    # print(FinalString)
    if RowValue != (upperBound-1):
        FinalString=FinalString+','
    else:
        FinalString=FinalString+';'
    # print(FinalString)
FinalResult=InsertTemplate.format(TableName,ColumnName,FinalString)
print(FinalResult)

InsertIntoDB(FinalResult)
