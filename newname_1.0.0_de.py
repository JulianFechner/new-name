import os
import sys

while True:
    print('Bitte geben Sie den vollständigen Pfad des Verzeichnisses an.')
    print(r'Beispiel: C:\Users\Black Knight\Injuries\None.')
    dirname = input()
    files = os.listdir(dirname)
    os.chdir(dirname)

    print('Bitte geben Sie die alten Zeichen ein.')
    old = input()
    print('Bitte geben Sie die neuen Zeichen ein.')
    new = input()

    print("Sind alle Angaben korrekt?")
    answer = input("j/n: ")
    
    if answer == "j" or answer == "J":
            print("Setze fort...")
    elif answer == "n" or answer == "N":
            continue
    else:
            print("Auf Wiedersehen!")
            break
        
    for src in files:
        dst = src.replace(old, new)
        os.rename(src, dst)
    sys.exit()
