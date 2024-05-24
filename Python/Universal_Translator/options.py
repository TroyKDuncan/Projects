def choose_language():
    language_map = {
        1: 'ar',
        2: 'bg',
        3: 'zh',
        4: 'nl',
        5: 'fr',
        6: 'de',
        7: 'el',
        8: 'he',
        9: 'it',
        10: 'ja',
        11: 'ko',
        12: 'pl',
        13: 'pt',
        14: 'ru',
        15: 'sm',
        16: 'sr',
        17: 'es',
        18: 'sv',
        19: 'tr',
        20: 'vi'
    }

    while True:
        try:
            choice = int(input('''
Which language would you like to translate to from English? 
Pick from one of these options by entering its number and hitting enter:
        
1. Arabic           11. Korean
2. Bulgarian        12. Polish
3. Chinese          13. Portuguese
4. Dutch            14. Russian
5. French           15. Somoan
6. German           16. Serbian
7. Greek            17. Spanish
8. Hebrew           18. Swedish
9. Italian          19. Turkish
10. Japanese        20. Vietnamese

Your choice: '''))
            if 1 <= choice <= 20:
                return language_map[choice]
            else:
                print('Must be a value from 1 to 20. Try again please.')
                continue
        except ValueError as err:
            print(err)
            print()
            print('Please enter an integer from 1 - 20')
            print()


def main_menu():
    while True:
        try:
            choice = int(input('''
What would you like to do?
Pick from one of these options by entering its number and hitting enter:

1. Enter text manually
2. Choose a txt file to translate
3. Quit
          
Your choice: '''))
            if 1 <= choice <= 3:
                return choice
            else:
                print('Must be a value from 1 to 3. Try again please.')
                continue
        except ValueError as err:
            print(err)
            print()
            print('Please enter an integer from 1 - 20')
            print()
