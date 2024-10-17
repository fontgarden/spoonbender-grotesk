# Usage example:
# $ python3 image_001.py --output image_001.png


import argparse
import drawbot_skia.drawbot as db
from fontTools.ttLib import TTFont


# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 1080, 1920, 80, 1
MAIN_FONT_PATH = "fonts/spoonbender-grotesk-regular.ttf"
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
    db.stroke(1, 0, 0, 0.75)
    db.strokeWidth(2)
    step_x = 0
    step_y = 0
    increment_x, increment_y = MARGIN / 2, MARGIN / 2
    db.rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(24):
        db.polygon((MARGIN + step_x, MARGIN), (MARGIN + step_x, HEIGHT - MARGIN))
        step_x += increment_x
    for y in range(44):
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
    db.fill(0.05)
    db.rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw main text
GRID_VIEW = False  # Toggle this for a grid overlay
def draw_main_text():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    db.fill(0.975)
    db.fill(0.9)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.fontSize(512 + 32)
    db.fontSize(80)
    
    
    #db.text("nnnn oooo nononono on", (MARGIN - 0, MARGIN * 22.0))
    #db.text("nnoonnoo onononon no", (MARGIN - 0, MARGIN * 21.0))
    #db.text("i no no", (MARGIN - 0, MARGIN * 20.0))

    #db.fontSize(80*2)
    #db.text("nnnn", (MARGIN - 0, MARGIN * 16.0))

    #db.fontSize(80)
    #db.font("Helvetica")
    #db.font(None)
    #db.text("nnnn oooo nononono on", (MARGIN - 0, MARGIN * 12.0))
    #db.text("nnoonnoo onononon no", (MARGIN - 0, MARGIN * 11.0))
    #db.text("i no no", (MARGIN - 0, MARGIN * 10.0))

    #db.font("Helvetica")
    #db.font(None)
    #db.text("nnnn oooo nononono on", (MARGIN - 0, MARGIN * 9.0))
    #db.text("nnoonnoo onononon no", (MARGIN - 0, MARGIN * 8.0))
    #db.text("i no no", (MARGIN - 0, MARGIN * 7.0))

    db.text("The Improbable", (MARGIN - 8, MARGIN * 22.0))
    db.text("Dome Builders", (MARGIN - 8, MARGIN * 21.0))
    
    db.text("Interaction", (MARGIN - 8, MARGIN * 19.0))
    db.text("Ritual HOno HOno", (MARGIN - 8, MARGIN * 18.0))
    
    #db.text("Grid Systems", (MARGIN - 8, MARGIN * 16.0))
    #db.text("Raster Systeme", (MARGIN - 8, MARGIN * 15.0))
    db.text("abcdefghijklm", (MARGIN - 8, MARGIN * 16.0))
    db.text("nopqrstuvwxy", (MARGIN - 8, MARGIN * 15.0))
    
    #db.text("THE OASIS OF", (MARGIN - 8, MARGIN * 13.0))
    #db.text("MATISSE", (MARGIN - 8, MARGIN * 12.0))
    
    #db.text("KLMNOPQRS", (MARGIN - 8, MARGIN * 11.0))
    #db.text("TUVWXYZ", (MARGIN - 8, MARGIN * 9.0))
    #db.text("1234567890", (MARGIN - 8, MARGIN * 7.0))
    #db.text("abcdefghijklm", (MARGIN - 8, MARGIN * 5.0))
    #db.text("nopqrstuvwxy", (MARGIN - 8, MARGIN * 3.0))
    #db.text("Rena Regular", (MARGIN - 8, MARGIN * 1.0))
    # db.text("Rena Regular", (MARGIN - 8, MARGIN * 1.0))
    # db.text("NOPQRSTUVWXY", (MARGIN - 24, MARGIN * 12.0))
    # db.text("abcdefghijklmnopq", (MARGIN - 24, MARGIN * 10.5))
    # db.text("rstuvwxyz", (MARGIN - 24, MARGIN * 9.0))
    # db.text("1234567890", (MARGIN - 24, MARGIN * 7.5))
    # db.text("Rena Regular ", (MARGIN - 24, MARGIN * 6.0))
    # db.text("Rena Regular ", (MARGIN - 24, MARGIN * 4.5))
    # db.text("Rena Regular ", (MARGIN - 24, MARGIN * 3.0))
    # db.text("Rena Regular ", (MARGIN - 24, MARGIN * 1.5))
    # db.text("Rena Regular ", (MARGIN - 24, MARGIN * 0.0))


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    # Save output, using the "--output" flag location
    db.saveImage(args.output)
    # Print done in the terminal
    print("DB-Skia: Done")
