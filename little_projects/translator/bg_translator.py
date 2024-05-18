from translate import Translator
import sys

translator = Translator(to_lang='bg')

try:
    with open(sys.argv[1], mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        my_file.close()
except (FileNotFoundError, IndexError) as err:
    print(err)
    print()
    print('Usage: python3 translator.py [original filepath] [target filepath]')
