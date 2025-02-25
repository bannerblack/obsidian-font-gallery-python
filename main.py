# ┌────────────────────────────────────────────────────────────────────────────────┐
# │░█▀█░█▀▄░█▀▀░▀█▀░█▀▄░▀█▀░█▀█░█▀█░░░█▀▀░█▀█░█▀█░▀█▀░░░█▀▀░█▀█░█░░░█░░░█▀▀░█▀▄░█░█│
# │░█░█░█▀▄░▀▀█░░█░░█░█░░█░░█▀█░█░█░░░█▀▀░█░█░█░█░░█░░░░█░█░█▀█░█░░░█░░░█▀▀░█▀▄░░█░│
# │░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀░▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░│
# └────────────────────────────────────────────────────────────────────────────────┘

# Obsidian Font Gallery
# A python script to generate Obsidian notes to display each font installed on your system.
# V0.1 by bannerblack - Feb 24, 2025

import os
# get fonts from system
from matplotlib import font_manager
# get metadata from fonts
from fontTools.ttLib import TTFont

# USER SETTINGS -------------------------------------------------------------------------------

# path to obsidian folder where you want to store the notes
obsidian_folder = r"C:\path\to\obsidian\folder\ie\fonts"

# Create Table of Contents? (True or False)
# Note: The ToC will add links to your graph view
# "FontGallery.md" in fonts folder
create_toc = True

# Font sizes for the notes
# Must be valid CSS font-size (ex "4em", "48px", "16pt")
toc_font_size = "5em"

# Sort fonts alphabetically? (True or False)
# Note: If False, fonts are random? I'm not sure if there's a rhyme
sort_fonts = False

# END USER SETTINGS -------------------------------------------------------------------------------

# check if obsidian folder exists
if os.path.exists(obsidian_folder): 
    obsidian_path = os.path.abspath(obsidian_folder)
else:
    print("Error: Obsidian folder does not exist.")
    exit()

# get font metadata - only currently selecting font_family
def get_font_metadata(font_path):
    """
    Extracts metadata from a font file.

    Args:
        font_path (str): The path to the font file.

    Returns:
        dict: A dictionary containing font metadata.
    """
    try:
        font = TTFont(font_path)
        names = {}
        for record in font['name'].names:
            name_id = record.nameID
            if name_id not in names:
                names[name_id] = record.toUnicode()
        metadata = {
            "font_family": names.get(1),
        }
        font.close()
        return metadata
    except Exception as e:
        print(f"Error: {e}")
        return None

# get installed fonts
installed_fonts = font_manager.findSystemFonts()

# sort fonts
if sort_fonts:
    installed_fonts.sort()

# font table of contents
all_fonts = []

# create a note for each font
for font in installed_fonts:
    # Get font metadata
    metadata = get_font_metadata(font)

    if metadata:
        # Add to all fonts for ToC
        if create_toc:
            all_fonts.append(metadata["font_family"])

        # Create a note for the font
        with open(os.path.join(obsidian_path, metadata["font_family"] + ".md"), "w", encoding='utf-8') as f:
            # Note: Explicit inline styles required for all text-containing elements. 
            # Space between will break obsidian view.

            ff = "font-family: '" + metadata["font_family"] + "';"

            f.write(f'''
                <body style="{ff} font-gallery">
                <!-- Headline -->
                <h1 style="{ff} font-size: 4em;">{metadata["font_family"]}<h1>
                <h4 style="{ff} text-align: left; font-weight: normal; font-size: 1.5rem; font-style:italic; margin-top: -20px">A brief introduction to a font.</h4>
                <hr>
                <!-- Font Sizes -->
                <p style="{ff} font-size: 48px;">A Sensationalist Headline!</p>
                <p style="{ff} font-size: 30px;">A Quarterly Concern</p>
                <p style="{ff} font-size: 16px;">A simple blog post</p>
                <p style="{ff} font-size: 10px;">The comment you want no one to see.</p>
                <hr>
                <!-- Weights and Decorations -->
                <p style="{ff} font-weight: bold;">Bold Text Sample</p>
                <p style="{ff} font-style: italic;">Italic Text Sample</p>
                <p style="{ff} text-decoration: underline;">Underlined Text Sample</p>
                <p style="{ff} text-decoration: line-through;">Strikethrough Text Sample</p>
                <p style="{ff} letter-spacing: 2px;">Spaced Out Text Sample</p>
                <hr>
                <!-- All caps and line spacing -->
                <h2 style="{ff}">NO ONE WILL EVER SEE THIS!</h2>
                <p style="{ff} line-height: 2;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                <p style="{ff}">Etiam ac ipsum ut nisi blandit ultrices ut imperdiet magna. Sed egestas ligula quam, sollicitudin ultrices erat sagittis ut. Curabitur sed magna orci. Vestibulum semper rhoncus dignissim. Mauris eget finibus elit, a posuere enim. Nulla eget dignissim sapien, vel finibus ipsum. Donec odio nulla, lobortis et porttitor vel, aliquet quis dolor. Sed nec faucibus leo. </p>
                <hr>
                <!-- Columns -->
                <div style="{ff} column-count: 2;"><h1 style="{ff}">Columnar & Du</h1>
                <p style="{ff}">There once was an animal so grotesk, so devilish, I couldn't think about anything but sinking my teeth into its pulsing neck. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                <p style="">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                </div>
                </body>
                '''.strip())

if create_toc:
    # create a table of contents
    with open(os.path.join(obsidian_path, "FontGallery.md"), "w", encoding='utf-8') as f:
        # Write heading of the ToC
        f.write(f'''
            <h1 style="font-size: 4em;">Font Gallery</h1><h4 style="text-align: left; font-weight: normal; font-size: 1.5rem; font-style:italic; margin-top: -20px">A collection of fonts installed on your system.</h4><hr>'''.strip())

        # Write preview and links to each font note
        for font in all_fonts:
            # Note: newlines required to keep markdown links separate from html so they render properly
            f.write(f'<p style="font-size: {toc_font_size}; font-family: {font}">{font}</p>\n\n')
            f.write(f'[[{font}]]\n\n<hr>')