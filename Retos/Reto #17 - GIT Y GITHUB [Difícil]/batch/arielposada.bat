@echo off
git log --pretty=format:"%%H | %%an | %%s | %%cd" -10
pause