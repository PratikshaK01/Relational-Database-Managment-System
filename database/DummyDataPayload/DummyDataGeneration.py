from dummyDataPayload import *
import sys
import random
sys.path.append('../DatabaseConnection')
sys.path.append('../../Backend/Utilities')
sys.path.append('../../Backend/propertyFiles')
from DbConnection import *
from Utilities import *
from properties import *

FinalString=""

#Loweround->max(db)->insertion sathi
#Upperbound->lastvalue->lowerbound+val
maxValue=getQuery(getMaxValue.format(TableName))[0][0]
if(maxValue==None):
    lowerBound=0
else:
    lowerBound=int(maxValue)+1
upperBound=lowerBound + rowsToBeInserted

for RowValue in range(lowerBound,upperBound):
    fName=getFirstName()
    sName=getSurname()
    fTName=getMaleName()
    mTName=getFemaleName()

    # Encrypted-Pritesh
    arr=[fName,sName,fTName,mTName]
    #we need to add email,personaladdress,
    # PerosonalAddress,aadhar,pan,passport
    # encrypted=getEncryptedValue(arr)

    # fName=encrypted[0]
    # sName=encrypted[1]
    # fTName=encrypted[2]
    # mTName=encrypted[3]

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
