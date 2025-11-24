:loop
timeout /t 5
git add .
git commit -m "Auto update model"
git push
goto loop