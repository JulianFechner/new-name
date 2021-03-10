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
    print('Please enter directory name.')
    print(r'Example: C:\Users\Black Knight\Injuries\None.')
    dirname = input()
    files = os.listdir(dirname)
    os.chdir(dirname)

    print('Please enter old character/s.')
    old = input()
    print('Please enter new character/s.')
    new = input()
    
    print("Is everything correct?")
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

    print("Would you like to go again?")
    answer2 = input("y/n: ")
    
    if answer2 == "y" or answer == "Y":
        print("Let's go again...")
        continue
    else:
        print("Goodbye!")
        break
