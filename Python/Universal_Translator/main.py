import options
import modes

if __name__ == '__main__':

    print('\nThanks for checking out my Universal Translator!')
    desired_language = options.choose_language()

    while True:
        action = options.main_menu()

        if action == 1:
            modes.live_translate(desired_language)
            continue

        elif action == 2:
            modes.translate_file(desired_language)
            continue

        elif action == 3:
            break
