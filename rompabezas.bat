@echo off
pushd "%~dp0"
start "" "%LocalAppData%\Microsoft\WindowsApps\wt.exe" -d "%CD%" cmd /c "rompabezas.exe"
popd
