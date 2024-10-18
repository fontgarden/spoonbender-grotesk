#!/bin/bash
fontmake sources/spoonbender-grotesk-regular.ufo
cp master_ttf/spoonbender-grotesk-regular.ttf fonts/
python documentation/wallpaper/bg-001.py --output documentation/wallpaper/bg-001.png
feh --bg-fill documentation/wallpaper/bg-001.png 
#mtpaint -v documentation/images/pre-alpha/pre-alpha-001.png
