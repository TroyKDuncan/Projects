from translate import Translator


def live_translate(language_code):
    translator = Translator(to_lang=language_code)
    while True:
        text = input('What would you like to translate? Or enter "q" to quit\n')
        print()
        if text.lower() != 'q':
            print(f'Translation: {translator.translate(text)}')
            print()
        else:
            return


def translate_file(language_code):
    translator = Translator(to_lang=language_code)
    while True:
        try:
            file_name = input('What txt file would you like to translate? ')
            print()
            with open(file_name, mode='r') as my_file:
                text = my_file.read()
                translation = translator.translate(text)
                print(translation)
                my_file.close()
                return
        except FileNotFoundError as err:
            print(err)
            print()
            print(
                'Make sure the specified filepath is correct!')
            print()
            continue