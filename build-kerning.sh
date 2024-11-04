#!/bin/bash

# Add new kerning group
lilufo -u sources/spoonbender-grotesk-regular-arabic.ufo \
  --add-kerning-group \
  --group-name "T" \
  --group-side "left" \
  --group-members "T"
