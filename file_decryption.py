import sys

from base64 import b64encode, b64decode
from getpass import getpass
from simplecrypt import decrypt, DecryptionException


def main(argv):
  filename_in = sys.argv[1]
  filename_out = sys.argv[2]
  password = getpass() 

  with open(filename_in, "r") as input:
    with open(filename_out, "w+") as output:
      lines = input.readlines()
      line_num = 1
      total_lines = len(lines)

      if line_num > total_lines:
        print('File contains no lines')
        sys.exit(2)

      for line in lines:
        if ',' not in line:
          print('Only csv files are supported')
          sys.exit(2) 
        
        print(f'Processing line {line_num} out of {total_lines}')
        words = line.split(',')
        for i in range(len(words)):
          word = words[i].replace('\n', '').strip()
          try:
            cipher = b64decode(word)
            plaintext = decrypt(password, cipher)
            output.write(plaintext.decode("utf-8"))
            if i < len(words) - 1:
              output.write(',')
          except DecryptionException:
            print('Bad password or corrupt / modified data')
            sys.exit(2)
        output.write('\n')
        line_num += 1

if __name__ == "__main__":
  main(sys.argv[1:])
