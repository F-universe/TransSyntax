TransSyntax

TransSyntax is a command-line tool designed to transform AI-generated text into a natural, human-like style by translating it through Armenian,
Italian, Peruvian Spanish, Spanish, and German before returning it to English. This sequence of translations reshapes the original syntax and makes the final output appear as if written by a human.

Requirements

Python 3.6 or higher

The googletrans library (version 4.0.0-rc1)

Installation

Install the required translation library:

pip install googletrans==4.0.0-rc1

Usage

Run the script and follow the prompt:

python transsyntax.py

Enter a sentence in English, observe each intermediate translation, and read the final English version, now reshaped in style and syntax.

Customization

Edit the sequence list in the transform_text function to add, remove or change languages and language codes.
