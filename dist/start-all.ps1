# File: start-all.ps1
# Start terminals to hold http-server and tailwindcss-watch

Start-Process powershell -ArgumentList "-File", ".\start-tailwindcss-watch.ps1"
Start-Process powershell -ArgumentList "-File", ".\start-http-server.ps1"