# File: start-tailwindcss-watch.ps1
# It generates ./src/tailwindcss.output.css
# The --watch option keeps it running for file changes.

# npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i ./src/tailwindcss.config.css -o ./src/tailwindcss.output.css --watch