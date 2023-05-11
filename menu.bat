@echo off
cls
:menu
echo ==Menu==
echo ........
echo Nacisnij 1-4 aby wybrac opcje.
echo ........

echo 1 - Uruchom program
echo 2 - Wyswietl informacje
echo 3 - Backup
echo 4 - Zakoncz

SET /p M=Type 1-4 i wcisnij Enter:

IF %M%==1 goto uruchom
IF %M%==2 goto info
IF %M%==3 goto backup
IF %M%==4 goto wyjscie

:uruchom

IF NOT EXIST output mkdir output
py main.py
py raport.py
start raport.html
echo 


:info
echo Projekt szukajacy "ciagu bez zajakniec" opracowany przez Roberta Wozniaka
goto :menu

:backup
IF NOT EXIST backups mkdir backups
set name=%date%--%TIME:~1,7%
set name=%name::=-%
IF EXIST raport.html mkdir backups\%name%
robocopy input backups\%name%\input
robocopy output backups\%name%\output
copy raport.html backups\%name%\raport.html
goto :menu

:wyjscie
exit
PAUSE