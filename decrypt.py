import sys
from base64 import b64encode, b64decode
from getpass import getpass
from simplecrypt import (encrypt, 
                         decrypt,
                         DecryptionException)


def main(argv):
  encoded_cipher = sys.argv[1]
  password = getpass() 

  try:
    cipher = b64decode(encoded_cipher)
    plaintext = decrypt(password, cipher)
    print(plaintext)
  except DecryptionException:
    print('Bad password or corrupt / modified data')

if __name__ == "__main__":
  main(sys.argv[1:])
