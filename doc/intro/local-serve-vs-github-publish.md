---
title: Local serve vs. github publish
author: Listenzcc
date: 2025-7-16
tags: intro github shell
---

I want the project is both locally and remotely (with github) useable.
I also want they are consistent **free of 3rd-part framework**.

Why? Since the network is not so well in my place, the local serve is crucial in some times.

---

## Page

At the project level, the pages are in the `dist` directory.
The files are pre-built static `html` files and assets.
There are also `npm` packages for convince and `shell` scripts to serve locally.

## Local Serve

I want it small and simple,
so the `npm` packages and `node` scripts are required to serve the files locally.

```powershell
# File: start-http-server.ps1
# Install and start http server
# -o refers open the web browser

npm install http-server
./node_modules/.bin/http-server -o
```

At this point, I suggest to add the [node_modules]() into [.gitignore]() file.

### Tailwindcss (v4.1) support

I want the page style consistence across the project,
so the `tailwindcss` is used.
The url is <https://tailwindcss.com/docs/installation/tailwind-cli>

Then, create [src/tailwindcss.config.css]() file to init the custom styles.
The `@import "tailwindcss";` is necessary on the init.

```powershell
# File: start-tailwindcss-watch.ps1
# It generates ./src/tailwindcss.output.css
# The --watch option keeps it running for file changes.

npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i ./src/tailwindcss.config.css -o ./src/tailwindcss.output.css --watch
```

For my own case, the [start-all.ps1]() script is used to create terminals to serve both http and tailwindcss

```powershell
# File: start-all.ps1
# Start terminals to hold http-server and tailwindcss-watch

Start-Process powershell -ArgumentList "-File", ".\start-tailwindcss-watch.ps1"
Start-Process powershell -ArgumentList "-File", ".\start-http-server.ps1"
```

## Github Publish

### Code work

Conversion on publish.
