# Stepmania-TranslatorViewMaker
Have you ever tried to translate a program like Stepmania and wondered "Hmmmmm, now where can I find that line in the .ini?"
Now there's no need to wonder!
This program will make a translator view file for your translation .ini and make you translation job easier
## How to use it
You will need python 3 to run this program and to have configparser installed in it (python pip install configparser).
Just run the program with your favorite python enviroment, type the full name and path of your source ini file (needs to be at the same folder as the program for now, also make sure to have no duplicate lines in your file using the Translation-Toolkit).
Type a theme name or any other name as an extra note, select 1 or 2 for the type of lines you want to have (more on that later) and done!
## Line types?
Due to request I made 2 types of lines:
1. Shows the section and the key where the line is present (your_theme, Section, Key).
2. Shows the line number where the key can be found at (your_theme, line number).

## Why this and that?
Since this is my very first shared program I focused on making it just work for starters, if anybody wants to help fix up the code and make it better I'll be happy to put those fixes in.

### The program seems to crash after choosing the type
Did you check for duplicates? It seems for now to be the only way to make this script crash in purpose, but if you did run the duplicate checker on your ini and it still crashes just send me your source file and I'll check if I can fix it.
Also sadly type 2 doesn't fully work right with lines that exist in multiple sections like HeaderText and HelpText, will probably get fixed in the future.

## Screenshots
Type 1

![Type 1](https://user-images.githubusercontent.com/74380856/109875232-de27c480-7c78-11eb-81c1-81b521c40eed.jpg)

Type 2

![Type 2](https://user-images.githubusercontent.com/74380856/109876059-f6e4aa00-7c79-11eb-82bc-52a04f7cb97e.jpg)
