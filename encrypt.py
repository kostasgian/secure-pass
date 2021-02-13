import sys

from base64 import b64encode, b64decode
from getpass import getpass
from simplecrypt import encrypt, decrypt


def main(argv):
  message = sys.argv[1]
  password = getpass() 

  cipher = encrypt(password, message)
  encoded_cipher = b64encode(cipher)
  print(encoded_cipher)

if __name__ == "__main__":
  main(sys.argv[1:])
