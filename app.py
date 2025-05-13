#!/usr/bin/env python3
"""
TransSyntax: transforms an English sentence by translating it through multiple languages and back to English.

Translation sequence:
1. Armenian (hy)
2. Italian (it)
3. Peruvian Spanish (es-PE)
4. Spanish (es)
5. German (de)
6. English (en)

Dependencies:
    pip install googletrans==4.0.0-rc1

Usage:
    python transsyntax.py
"""

from googletrans import Translator

def transform_text(text):
    translator = Translator()
    sequence = [
        ('Armenian', 'hy'),
        ('Italian', 'it'),
        ('Peruvian Spanish', 'es-PE'),
        ('Spanish', 'es'),
        ('German', 'de'),
        ('English', 'en')
    ]
    current = text
    print(f"Original text: {current}\n")
    for lang_name, lang_code in sequence:
        try:
            result = translator.translate(current, dest=lang_code)
            current = result.text
            print(f"Translated to {lang_name} ({lang_code}): {current}")
        except Exception as e:
            print(f"Error translating to {lang_name} ({lang_code}): {e}")
    return current


def main():
    text = input("Enter a sentence in English: ")
    final = transform_text(text)
    print("\nFinal result in English:")
    print(final)

if __name__ == "__main__":
    main()
