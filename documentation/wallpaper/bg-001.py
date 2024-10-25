# Usage example:
# $ python3 image_001.py --output image_001.png


import argparse
import drawbot_skia.drawbot as db
from fontTools.ttLib import TTFont


# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, UNIT, FRAMES = 3840, 2160, 80, 40, 1
MAIN_FONT_PATH = "fonts/spoonbender-grotesk-regular-arabic.ttf"
AUXILIARY_FONT = "Helvetica"


# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()


# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(MAIN_FONT_PATH)


# Draws a grid
def grid():
    """Draws a grid using DrawBot-Skia"""
    db.stroke(0.3, 0.3, 0.3, 0.250)
    db.strokeWidth(2)
    step_x = 0
    step_y = 0
    increment_x, increment_y = MARGIN / 2, MARGIN / 2
    db.rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(92):
        db.polygon((MARGIN + step_x, MARGIN), (MARGIN + step_x, HEIGHT - MARGIN))
        step_x += increment_x
    for y in range(50):
        db.polygon((MARGIN, MARGIN + step_y), (WIDTH - MARGIN, MARGIN + step_y))
        step_y += increment_y
    db.polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    db.polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    db.newPage(WIDTH, HEIGHT)
    db.fill(0.2)
    db.fill(0.025)
    db.fill(0.075)
    db.rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw main text
GRID_VIEW = True  # Toggle this for a grid overlay
def draw_main_text():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    db.fill(0.9)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    
    db.fontSize(192)
    db.text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", (MARGIN * 2, UNIT * 46.0))
    db.text("abcdefghijklmnopqrstuvwxyz", (MARGIN * 2, UNIT * 41.0))
    db.text("Interaction Ritual", (MARGIN * 2, UNIT * 36.0))
    db.text("The Improbable", (MARGIN * 2, UNIT * 31.0))
    db.text("Dome Builders", (MARGIN * 2, UNIT * 26.0))
    db.text("با با با", (MARGIN * 6, UNIT * 21.0))
    
    db.fontSize(64)
    #db.text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", (MARGIN * 2, UNIT * 22.0))
    #db.text("abcdefghijklmnopqrstuvwxyz", (MARGIN * 2, UNIT * 20.0))
    db.text("Interaction Ritual", (MARGIN * 2, UNIT * 18.0))
    db.text("The Improbable", (MARGIN * 2, UNIT * 16.0))
    db.text("Dome Builders AHO Ano AHAH AOAO Hnn HnHn AVA", (MARGIN * 2, UNIT * 14.0))
    db.text("nonono nnnn oooo ononon noon onno", (MARGIN * 2, UNIT * 12.0))
    db.text("HOHOHO HHHH OOOO OHOHOH HOOH OHHO", (MARGIN * 2, UNIT * 10.0))
    


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    # Save output, using the "--output" flag location
    db.saveImage(args.output)
    # Print done in the terminal
    print("DB-Skia: Done")
