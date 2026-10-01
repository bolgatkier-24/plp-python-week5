-- Question. Why the number 3 does not appear when I run main.py
As I helpers.py by itself, the line:
print(tables_nneded(10, 4)

* executes and prints 3.
  But, when I run the main.py... which does import helpers, the same print statement does not run

  Why that?... it simply because the print is inside this guard:
  if --name-- = " --main--":
  print(tables_needed(10, 4))

  If the file is run directly, Python sets its special variable --name-- to the string "--main--", becuase the code inside has been block by if during execustion.
  As the file is imported by another file, --name-- is set the module's name ("helpers"), that mean the if condition is false and the test is skipped.

  that's the reason(why) main.py only shows the three expected lines and never shows the extra 3
