@echo off
setlocal

:: Default command if no argument is provided
set COMMAND=build

:: Check if an argument is provided and use it as the command
if not "%~1"=="" set COMMAND=%~1

:: Run the Docker Compose command
docker-compose run --rm astro-doc %COMMAND%
endlocal
