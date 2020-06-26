# for generating key from password
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# for converting from json file to python dictionatry
import json

from cryptography.fernet import Fernet

class PyCrypt:
    def __init__(self, filepath, key=None, password=None):
        '''Encrypt and decrypt strings and write them to a fil using key or password'''
        if key != None and password != None:
            raise Exception('Please use either key or password')
        if key == None and password == None:
            raise Exception('Please provide a key or password to encrypt and decrypt with')
        
        self.salt = b'\xa3\x16{\xf0\x97g\x999~\n\x87j\x8b\x1bi\x94'

        if password:
            password = password.encode()
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=self.salt,
                iterations=100000,
                backend=default_backend()
            )
            self.key = base64.urlsafe_b64encode(kdf.derive(password))

        else:
            self.key = key

        self.filepath = filepath

        with open(self.filepath) as file:
            self.file = json.loads(file.read())

    def write(self):
        '''Writes file list to file path'''

        with open(self.filepath, 'w') as file:
            file.write(json.dumps(self.file, indent=2))

    def encrypt(self, string, decode=False):
        '''Take string returns encrypted string either as bytes or string'''
        
        try:
            encoded = string.encode()
        except:
            encoded = string
        f = Fernet(self.key)
        encrypted = f.encrypt(encoded)
        if decode:
            return encrypted.decode()
        else:
            return encrypted

    def decrypt(self, string, decode=False):
        '''Take string returns decrypted string either as bytes or string'''
        
        try:
            encoded = string.encode()
        except:
            encoded = string
        f = Fernet(self.key)
        decrypted = f.decrypt(encoded)
        if decode:
            return decrypted.decode()
        else:
            return decrypted

    def append(self, message, write=True):
        '''Encrypts message and append to self.file; can write to file if selected'''
        
        encryptedMsg = self.encrypt(message, decode=True)
        self.file.append(encryptedMsg)
        if write:
            self.write()

    def remove(self, index, write=True):
        '''Removes item from self.file if it can be decrypted by key; can write to file if selected'''
        
        try:
            self.decrypt(self.file[index])
        except:
            raise Exception("you do not have permission")

        self.file.pop(index)

        if write:
            self.write()

    def getAll(self):
        '''Returns list of all logs that can be decrypted using key'''
        
        logs = []
        for log in self.file:
            try:
                logs.append(self.decrypt(log, decode=True))
            except:
                pass 
        return logs

    def get(self, index):
        '''Returns item from self.file if it can be decrypted'''

        if index > len(self.file):
            raise Exception('Index out of Bounds')
        
        try:
            return self.decrypt(self.file[index])
        except:
            raise Exception('You do not have access to this item using your key')
         

if __name__ == '__main__':
    myCrypt = PyCrypt('logs.json', password="jaden")
    print(myCrypt.getAll())
