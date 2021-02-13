import bcrypt
import sys
import getopt

from decouple import config


MASTER_KEY = config('MASTER_KEY')

def main(argv):
  salt = None
  raw_password = None
  help_text = 'hashing.py -s <salt> -p <password>'

  if MASTER_KEY is None or MASTER_KEY == '':
    print(f'Missing Master Password.'\
           ' Either set MASTER_KEY as env variable,'\
           ' or create a .env file with MASTER_KEY=VALUE')
    sys.exit(2)

  master_secret_key = MASTER_KEY 

  try:
    opts, args = getopt.getopt(argv,"hs:p:",["salt=","password="])
  except getopt.GetoptError:
    print(help_text)
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print(help_text)
      sys.exit()
    elif opt in ("-s", "--salt"):
      salt = arg
    elif opt in ("-p", "--password"):
      raw_password = arg

  if salt is None or raw_password is None or master_secret_key is None:
    print(help_text)
    sys.exit(2)
   
 
  combo_password = raw_password + salt + master_secret_key
  hashed_password = bcrypt.hashpw(combo_password, salt)
    
  print(hashed_password)




if __name__ == "__main__":
  main(sys.argv[1:])
