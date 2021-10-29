import random
import string
import sys
sys.path.append('../propertyFiles')
from Names import *
from properties import *

# THIS FUNCTION WILL RETURN FIRSTNAME OF MALE
# CALL THIS FUNCTION WHEN WE NEED FIRST NAME OF MALE CANDIDATE
def getMaleName():
    male=random.choice(MaleName)
    return male

# THIS FUNCTION WILL RETURN FIRSTNAME OF FEMALE
# CALL THIS FUNCTION WHEN WE NEED FIRST NAME OF FEMALE CANDIDATE
def getFemaleName():
    female=random.choice(FemaleName)
    return female

# THIS FUNCTION RETURN SURNAME
def getSurname():
    surName=random.choice(lastName)
    return surName

# THIS FUNCTION WILL RETURN FIRSTNAME OF RANDOM CANDIDATE
def getFirstName():
    maleFemaleName=[getMaleName(),getFemaleName()]
    finalRandomName=random.choice(maleFemaleName)
    return finalRandomName

def getAlphaNumericString(lengthOfString):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=lengthOfString))


def getGrade():
    return round(random.uniform(55.0,99.9),1)


def getSgpa():
    return round(random.uniform(5.5,9.9),1)

def getNumericString(lengthOfString):
    return ''.join(random.choices(string.digits, k=lengthOfString))
