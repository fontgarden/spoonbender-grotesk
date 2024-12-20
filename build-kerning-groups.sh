#!/bin/bash

# Add new left kerning group
lilufo -u sources/spoonbender-grotesk-regular-arabic.ufo \
  --add-kerning-group \
  --group-name "T" \
  --group-side "left" \
  --group-members "T"

# Add new right kerning group
lilufo -u sources/spoonbender-grotesk-regular-arabic.ufo \
  --add-kerning-group \
  --group-name "T" \
  --group-side "right" \
  --group-members "T"
