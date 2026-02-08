@echo off
SETLOCAL EnableDelayedExpansion
echo ========================================
echo RaidBot Updater
echo ========================================
echo.
REM Set paths
set "BACKUP_DIR=backup_%DATE:~-4%-%DATE:~3,2%-%DATE:~0,2%_%TIME:~0,2%-%TIME:~3,2%"
set "GIT_REPO=https://github.com/ItzPopelka/raidbot.github.io"
set "EXCLUDE_FILES=token.json assets/pfp.webp"
echo Creating backup directory...
mkdir "%BACKUP_DIR%"
echo.
echo Backing up files to %BACKUP_DIR%...
echo.
REM Backup all current files
for /r %%f in (*) do (
    set "filepath=%%f"
    set "relpath=!filepath:%CD%\=!"
    
    REM Check if file should be excluded from backup
    set "skip=0"
    for %%e in (%EXCLUDE_FILES%) do (
        if "!relpath!"=="%%e" set "skip=1"
    )
    
    if !skip!==0 (
        echo Backing up: !relpath!
        xcopy "%%f" "%BACKUP_DIR%\!relpath!" /Y /Q >nul 2>&1
    )
)
echo.
echo ========================================
echo Downloading latest files from GitHub...
echo ========================================
echo.
REM Create temporary directory
mkdir temp_update
cd temp_update
REM Download repository as zip
echo Downloading repository...
powershell -Command "Invoke-WebRequest -Uri '%GIT_REPO%/archive/main.zip' -OutFile 'repo.zip'"
echo Extracting files...
powershell -Command "Expand-Archive -Path 'repo.zip' -DestinationPath '.' -Force"
REM Find the extracted folder
for /d %%d in (*) do (
    if exist "%%d\" (
        echo Copying files from %%d...
        
        REM Copy files while excluding specified ones
        for /r "%%d" %%f in (*) do (
            set "source=%%f"
            set "relpath=!source:%%d\=!"
            
            REM Check if file should be excluded
            set "exclude=0"
            for %%e in (%EXCLUDE_FILES%) do (
                if "!relpath!"=="%%e" set "exclude=1"
            )
            
            if !exclude!==0 (
                echo Updating: !relpath!
                copy "%%f" "..\!relpath!" /Y >nul 2>&1
            ) else (
                echo Skipping: !relpath!
            )
        )
    )
)
cd ..
rmdir /s /q temp_update
echo.
echo ========================================
echo Update completed!
echo ========================================
echo.
echo Original files backed up to: %BACKUP_DIR%
echo Excluded from update: %EXCLUDE_FILES%
echo.
pause