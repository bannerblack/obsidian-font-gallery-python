# Obsidian Font Gallery

Obsidian Font Gallery is a small, single-file python script that generates markdown files to preview the fonts you have installed on your system.

It uses matplotlib to gather installed font files, then extracts the font-family from the font's metadata, which is the naming convention that is then used to reference the font from your system within the generated files.

[Screenshot 2025-02-24 224316](https://github.com/user-attachments/assets/b5f2efb8-0dd5-4a5e-b7e3-a18c9689152b)

## To Use:

1. Download the main.py file
2. Find user settings, then copy the path of your obsidian folder (the actual folder you want the font files to be in) into the ```obsidian_folder``` variable.
3. Run the file (see warning below). If a module error is give, use  ```pip install matplotlib```, etc. to install it.
4. The folder you defined should now contain a file for each font, and if you enabled ToC, a file called FontGallery will also be in the defined folder.
   

> [!Warning]
> This script will likely generate many files, so after providing the path to where you want to store the files, it is smart to test it first by limiting the number of fonts initially generated. This can be done by modifying the following:
> ```
> for font in installed_fonts:
> ```
> to
> ```
> for font in installed_fonts[5]:
>```
> 5 corresponds to how many fonts will be generated. Remove the limiter when you have verified everything is working properly.

> [!Note]
> Currently limited to TTF!
