# CompileAnyVersionPython

-It works for any python .py file because it uses the built in python module “py_compile” depending on PYTHONHOME 

-You can have the pycomp folder be located anywhere and it will still work (e.g. the desktop, c drive, doesn’t matter.) 

-Tells you if the input folder is empty 

-Tells you if the output folder is not an existing directory 

-Tells you what version of python you’re compiling 

-Tells you if the input is not an existing file or directory

----------------------------------------------------------------------------
pycomp.bat can be called in any of the following 5 ways:

1.	you put your .py files in the Input folder & double click pycomp.bat

2. you call pycomp.bat with an input path (e.g. "pycomp.bat C:\users\cjf\desktop")

3. you call pycomp.bat with both an input AND output path (e.g. "pycomp.bat C:\users\cjf\desktop C:\workspace")

4. you call pycomp.bat with a path to just one file, no output path given (e.g. "pycomp.bat C:\users\cjf\desktop\GetDBInfo.py")

5. you call pycomp.bat with a path to just one file, AND give an output path (e.g. "pycomp.bat C:\users\cjf\desktop\GetDBInfo.py C:\workspace")

*If you do not give a specific output path, the output .pyc files will appear in pycomp->Output folder.
*If you do not give a specific input path, the scripts that are in the pycomp->Input folder will be compiled. 
