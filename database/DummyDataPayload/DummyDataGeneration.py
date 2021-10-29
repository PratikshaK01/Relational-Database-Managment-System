from dummyDataPayload import *
import sys
import random
sys.path.append('../DatabaseConnection')
sys.path.append('../../Backend/Utilities')
sys.path.append('../../Backend/propertyFiles')
sys.path.append('../../EncryptorsDecryptors')
from DbConnection import *
from Utilities import *
from properties import *
from encryptors import *

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

    # GET PII DATA
    fName=getFirstName()
    sName=getSurname()
    emailValue=email.format(getAlphaNumericString(emailLength))
    aadharValue=getNumericString(adharLength)
    passportValue=getAlphaNumericString(passLength)
    panValue=getAlphaNumericString(panLength)
    mobileNo=getNumericString(mobileLength)
    fTName=getMaleName()
    mTName=getFemaleName()
    residentialAddressValue = residentialAddress.format(RowValue)
    permanantAddressValue = permanantAddress.format(RowValue)

    # GET GRADES
    grade10=getGrade()
    grade12=getGrade()

    # GET SGPA
    SemCGPA1 = getSgpa()
    SemCGPA2 = getSgpa()
    SemCGPA3 = getSgpa()
    SemCGPA4 = getSgpa()
    SemCGPA5 = getSgpa()
    SemCGPA6 = getSgpa()


    # Encrypted-Pritesh
    piiValuesToBeEncrypted=[fName,sName,panValue,passportValue,aadharValue,emailValue,mobileNo,residentialAddressValue,permanantAddressValue]
    #we need to add email,personaladdress,
    # PerosonalAddress,aadhar,pan,passport
    encryptedArr=[]
    encrypted=getEncryptedValue(encryptedArr,piiValuesToBeEncrypted)

    fName=encrypted[0]
    sName=encrypted[1]
    panValue=encrypted[2]
    passportValue=encrypted[3]
    aadharValue=encrypted[4]
    emailValue=encrypted[5]
    mobileNo=encrypted[6]
    residentialAddressValue=encrypted[7]
    permanantAddressValue=encrypted[8]


    InitialRow="({},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{})"
    InitialRow=InitialRow.format(Gr_no.format(RowValue),
    rollNumber.format(RowValue),
    firstName.format(fName),
    surName.format(sName),
    email.format(emailValue),
    mobileNumber.format(mobileNo),
    aadhar.format(aadharValue),
    PAN.format(panValue),
    passport.format(passportValue),
    nationality,isAadhar,isPAN,isPassport,isIndian,
    fathersName.format(fTName),
    mothersName.format(mTName),
    permanantAddress.format(permanantAddressValue),
    residentialAddress.format(residentialAddressValue),
    state.format(RowValue),
    city.format(RowValue),
    pincode.format(RowValue),
    tenthCGPA,twelfthCGPA,tenthGrade.format(grade10),twelfthGrade.format(grade12),
    firstSemCGPA.format(SemCGPA1),
    secondSemCGPA.format(SemCGPA2),thirdSemCGPA.format(SemCGPA3),
    fourthSemCGPA.format(SemCGPA4),fifthSemCGPA.format(SemCGPA5),
    sixthSemCGPA.format(SemCGPA6),seventhSemCGPA,eightthSemGCPA,
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
# print(FinalResult)

InsertIntoDB(FinalResult)
