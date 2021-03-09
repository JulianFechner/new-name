# MIT License

# Copyright (c) 2021 Julian Fechner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

    print("Möchten Sie von vorne beginnen?")
    answer2 = input("j/n: ")
    
    if answer2 == "j" or answer == "J":
        print("Beginnen wir von vorne...")
        continue
    else:
        print("Auf Wiedersehen!")
        break
        
    sys.exit()
