from cryptography.fernet import Fernet
import sys
sys.path.append('../propertyFiles')
from properties import *
#
# # we will be encryting the below string.
message = "hello geeks"

def generate_key():
    key = Fernet.generate_key()
    return key
key=b'Dd6Id2lSfHt9BO6EBXYzbHj9PCTEupe5jGlUg4GSmdg='


def encryption(key,mssgToEncrypt):
    # Instance the Fernet class with the key
    fernet = Fernet(key)
    #.encode() method will convert normal string into byte string.
    encMessage = fernet.encrypt(mssgToEncrypt.encode())

    return encMessage.decode()

def decryption(key,encMessage):
    fernet = Fernet(key)
    decMessage = fernet.decrypt(encMessage)
# to remove bString
    return decMessage.decode()

"""

"""
def decrypt(encMessage):
    return decryption(key,encMessage)

def encrypt(messageToEncrypt):
    return encryption(key,messageToEncrypt)

def getEncryptedValue(encryptedArr,decryptedArr):
    for element in decryptedArr:
        encryptedArr.append(encrypt(element))
    return encryptedArr
