@echo off
REM Created by Collin Fox 5/22/2019

:CheckPythonHome
if "%PYTHONHOME%"=="" (
	goto PrintError
) 
goto CallPython

:PrintError
echo(
echo ERROR: System Variable PYTHONHOME is Not Defined.
echo Ensure PATH variable also contains %%PYTHONHOME%%\bin; at beginning of the variable. Be sure to include the percent symbols, slash, and semicolon.
echo(
goto BadExit


:CallPython
REM below line enables pycomp.bat to be called from command line anywhere, as long as pycomp folder is added to PATH system variable
pushd %~dp0
REM below line has effect of printing a blank line to the screen
echo( 
echo PYTHONHOME: %PYTHONHOME%
REM uses PYTHONHOME to determine which version of py_compile to import
echo If you wish to compile using a version of python other than %PYTHONHOME%, update system variable PYTHONHOME.
%PYTHONHOME%\python.exe -B -c "import CompilePythonFiles;x=CompilePythonFiles.main();" %PYTHONHOME% %1 %2
echo ---------------------------------------------------------
goto GoodExit


:BadExit
echo Press any key to exit...
pause >nul


:GoodExit
pause