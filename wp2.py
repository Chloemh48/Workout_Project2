import sys 
from pathlib import Path
import decrypt_
import encrypt_


def run():
    user_input =input ("Enter your command:")

    if len(sys.argv)!= 4:
        print("Usage: python wp2.py -e|-d <inputfile> <outputfile> <key>")
        raise SystemExit(1)
    
    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    key = sys.argv[4]

    if command == 'e':
        encrypt_.encrypt(input_file, output_file, key)
    elif command == 'd':
        decrypt_.decrypt(input_file, output_file, key)
    else:
        print('Invalid Cammand')

if __name__ == "__main__":
   run()



   
    


