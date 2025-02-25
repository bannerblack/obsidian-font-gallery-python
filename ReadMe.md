# Obsidian Font Gallery

Obsidian Font Gallery is a small, single-file python script that generates markdown files so that you can easily preview the fonts you have installed on your system.

It uses matplotlib to gather installed font files, then extracts the font-family from the font's metadata. That font-family is then used to create a font preview using a simple HTML template. A new markdown note is generated for each font.

![Screenshot of single note view](https://github.com/user-attachments/assets/b5f2efb8-0dd5-4a5e-b7e3-a18c9689152b)
![Screenshot of Font Gallery](https://github.com/user-attachments/assets/745a53ec-f63f-434f-8be8-003324cbe427)

## Features

- Creates a unique note for every TTF font installed on your system
- Optional Table of Contents note that creates a list of and links to all font notes

## To Use:

1. Download or copy the main.py file
2. Find the user settings section, then copy the path of your obsidian folder (the actual folder you want the font files to be in) into the ```obsidian_folder``` variable.
   
> [!Warning]
> This script will generate many files, so after providing the path to where you want to store the files (Step 2), it is smart to test it first by initially limiting the number of fonts generated. This can be done by modifying the following:
> ```python
> for font in installed_fonts:
> ```
> to
> ```python
> for font in installed_fonts[5]:
>```
> The 5 corresponds to how many fonts will be generated. Remove the limiter when you have verified everything is working properly.

3. Run the file (see warning above). 
   - If a module error is give, use  ```pip install``` to install it.

The folder you defined should now contain a file for each font, and if you enabled ToC, a file called FontGallery will also be in the defined folder.

> [!Warning]
> Re-running this script will overwrite all generated font notes and the TOC. I recommend editing the template in main.py or renaming files you want to edit individually so that you don't lose your changes.

> [!Note]
> Currently limited to TTF!
