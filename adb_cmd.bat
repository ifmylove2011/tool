@echo off

rem 得到本机IP
for /f "tokens=4" %%a in ('route print^|findstr 0.0.0.0.*0.0.0.0') do (
 set IP=%%a
)
echo LocalHost : %IP%
echo %cd%

rem 得到局域网范围
for /f "tokens=1-3 delims=." %%i in ('echo %IP%') do (
       set local_area=%%i.%%j.%%k
)
echo LocalArea : %local_area%

:main
echo please choose execution:
echo 	1.scan IP in LAN
echo 	2.connect all host:
echo 	3.install APK:
echo 	4.start APK:
echo 	5.kill app process:
echo 	6.clear App:
echo 	7.uninstall APK:
echo 	0.exit:

set /p choose=please input choose:
if %choose%==1 goto scan
if %choose%==2 goto connect
if %choose%==3 goto install
if %choose%==4 goto startapp
if %choose%==5 goto killapp
if %choose%==6 goto clearapp
if %choose%==7 goto uninstall
if %choose%==0 exit
pause

:scan
del %~dp0reachable_list.txt
@rem ping局域网内IP
setlocal enabledelayedexpansion
set /p indexStart=input start(such as 80):
set /p indexEnd=input end(such as 100):

set /a total = 0

FOR /L %%n in (%indexStart%,1,%indexEnd%) DO (
	ping %local_area%.%%n -n 1 -w 100
	IF !ERRORLEVEL! EQU 0 (
		echo %local_area%.%%n >> %~dp0reachable_list.txt
		set /a total = total + 1
	)
) 
echo %total% alive
endlocal
pause 
goto main

:connect
setlocal enabledelayedexpansion
FOR /f %%h in (%~dp0reachable_list.txt) DO (
	adb connect %%h:5555
 	echo ----------%%h connect success
)
adb devices
endlocal
pause
goto main

:install
@rem 设置apk路径
setlocal enabledelayedexpansion
set /p apk_path=input apk_path:
if not exist %apk_path% (
	echo %apk_path% not exist!
)
FOR /f %%h in (%~dp0reachable_list.txt) DO (
	adb -s %%h:5555 install -r -t %apk_path%
	echo ----------%%h install success
)
endlocal
pause
goto main

:startapp
@rem 启动apk
setlocal enabledelayedexpansion
set /p apk_intent=input apk_intent:
FOR /f %%h in (%~dp0reachable_list.txt) DO (
	adb -s %%h:5555 shell am start -n %apk_intent%
	echo ----------%%h start success
)
endlocal
pause
goto main

:killapp
@rem 启动apk
setlocal enabledelayedexpansion
set /p apk_package1=input apk_package:
FOR /f %%h in (%~dp0reachable_list.txt) DO (
	adb -s %%h:5555 shell am force-stop %apk_package1%
	echo ----------%%h kill app success
)
endlocal
pause
goto main

:clearapp
@rem 启动apk
setlocal enabledelayedexpansion
set /p apk_package1=input apk_package:
FOR /f %%h in (%~dp0reachable_list.txt) DO (
	adb -s %%h:5555 shell pm clear %apk_package2%
	echo ----------%%h clear app success
)
endlocal
pause
goto main

:uninstall 
@rem 卸载apk
setlocal enabledelayedexpansion
set /p apk_package2=input apk_package:
FOR /f %%h in (%~dp0reachable_list.txt) DO (
	adb -s %%h:5555 uninstall %apk_package2%
	echo ----------%%h uninstall app success
)
endlocal
pause
goto main