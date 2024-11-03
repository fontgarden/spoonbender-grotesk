#!/bin/bash
fontmake sources/spoonbender-grotesk-regular-arabic.ufo
cp master_ttf/spoonbender-grotesk-regular-arabic.ttf fonts/
python documentation/images/pre-alpha/pre-alpha-001.py --output documentation/images/pre-alpha/pre-alpha-001.png &> /dev/null
#feh --bg-fill documentation/wallpaper/bg-001.png 
#mtpaint -v documentation/images/pre-alpha/pre-alpha-001.png
mtpaint documentation/images/pre-alpha/pre-alpha-001.png
