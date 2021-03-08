import os
import sys

while True:
    print('Please enter directory name.')
    print(r'Example: C:\Users\Black Knight\Injuries\None.')
    dirname = input()
    files = os.listdir(dirname)
    os.chdir(dirname)

    print('Please enter old character/s.')
    old = input()
    print('Please enter new character/s.')
    new = input()
    
    print("Is everthing correct?")
    answer = input("y/n: ")
    
    if answer == "y" or answer == "Y":
            print("Continuing...")
    elif answer == "n" or answer == "N":
            continue
    else:
            print("Goodbye!")
            break
        
    for src in files:
        dst = src.replace(old, new)
        os.rename(src, dst)
    sys.exit()
