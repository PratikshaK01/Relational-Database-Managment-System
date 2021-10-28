import random
import sys
sys.path.append('../Functions')
from NameFunc import *

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
    finalRandomName=random.choice(MaleFemaleName)
    return finalRandomName
