<a href="https://github.com/wervlad/anki-card-converter/blob/main/LICENSE">
    <img alt="license" src="https://img.shields.io/github/license/wervlad/anki-card-converter.svg?color=blue">
</a>
<a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a>
<a href="https://github.com/wervlad/anki-card-converter/actions/workflows/tests.yml">
    <img alt="tests" src="https://github.com/wervlad/anki-card-converter/actions/workflows/tests.yml/badge.svg">
</a>

# Anki Card Converter

This converter is intended for use with the [Multiple Choice for Anki add-on](https://ankiweb.net/shared/info/1566095810).

It converts Basic Card quiz questions

<img src="https://user-images.githubusercontent.com/24524555/234809499-364c2c19-9fcc-4455-b163-34387c62996a.png" alt="basic card front" width="50%" height="auto">

<img src="https://user-images.githubusercontent.com/24524555/234809596-0b65399f-9cfa-49b8-83ca-7a98631e038a.png" alt="basic card back" width="50%" height="auto">

into AllInOne Card format, which allows selecting options like in interactive mode

<img src="https://user-images.githubusercontent.com/24524555/234809631-0ebbbe32-f722-4a21-a3da-810648f26553.png" alt="allinone card front" width="50%" height="auto">

and highlights the correct answers

<img src="https://user-images.githubusercontent.com/24524555/234811516-4b7f4bea-50bd-4fb7-9266-87547d42c413.png" alt="allinone card back" width="50%" height="auto">

## Usage

1. Clone this repository to your local machine.
2. Ensure that you have Python 3.10 and [Poetry](https://python-poetry.org/docs/) installed on your machine. The author used Poetry 1.3.1.
3. Install the project dependencies using the following command:
```sh
poetry install --no-dev
```
4. Export cards as "Notes in Plain Text (.txt)" by choosing menu item "File -> Export (Ctrl + E)".
<img src="https://user-images.githubusercontent.com/24524555/234874211-cd166bd2-2931-4950-a36e-b509cfba00f9.png" alt="export anki cards" width="50%" height="auto">

**Note**: only "Basic Cards" are supported currently.

5. Run the convert script
```sh
poetry run convert -i <input file.txt> -o <output file.txt>
```
7. Import converted file in Anki.

**Note**: to replace oritinal cards with converted, first change their type to AllInOne. Go to "Browse" window, select cards, right click on them and select Notes -> Change Note Type (Ctrl + Shift + M). In drop down menu select "AllInOne (kprim, mc, sc)" and click "Save".
