#!/bin/bash
fontmake sources/spoonbender-grotesk-regular-arabic.ufo
cp master_ttf/spoonbender-grotesk-regular-arabic.ttf fonts/
python documentation/wallpaper/bg-002.py --output documentation/wallpaper/bg-002.png &> /dev/null
feh --bg-fill documentation/wallpaper/bg-002.png 
#mtpaint -v documentation/images/pre-alpha/pre-alpha-001.png
