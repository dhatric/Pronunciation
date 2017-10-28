@echo off  
cd C:\Giridhar\Projects\python\Pronunciation\Pronunciation\com\dhatric\video
set pyexePath="C:\Python27\python.exe"  
set pylogPath="C:\Giridhar\Projects\python\Pronunciation\Pronunciation\com\dhatric\video\logger.txt"  
set pronunciation_pyPath="C:\Giridhar\Projects\python\Pronunciation\Pronunciation\com\dhatric\video\Main.py"  
echo Start time: %time% > %pylogPath%  
  
REM Run the python script  
echo Starting the P task: %time%  

%pyexePath% %pronunciation_pyPath% >> %pylogPath%  
  
echo End time: %time% >> %pylogPath%  
pause