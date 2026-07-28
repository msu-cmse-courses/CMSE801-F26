@echo off
cd 
REM Clean up the previous build
jupyter-book clean .

REM Build the project
jupyter-book build .

REM If you want to make the repo private and publish from a specific branch, uncomment the following line
ghp-import -n -p -f _build/html

