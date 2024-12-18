
letters = [chr(code) for code in range(ord('a'), ord('z'))]
used = []
tries_left = 6

word = 'awesome'
guessed = [False for _ in range(len(word))]

def printKeyboard():
    for l in letters:
        if l in used:
            print(f'[{l}]', end=' ')
        else:
            print(f' {l} ', end=' ')
    print()

while not all(guessed):
    printKeyboard()
    letter = input('> ')
    if len(letter) != 1:
        print('Only enter one letter.')
        continue

    letter = letter.lower()

    if letter in used:
        print('That letter has already been used! Pick another.')
        continue
    used.append(letter)

    progress = False
    for i in range(len(word)):
        if guessed[i]:
            print(word[i], end=' ')

        else:
            if letter == word[i]:
                progress = True
                guessed[i] = progress
                print(word[i], end=' ')
            else:
                print('_', end=' ')

    print()

    if not progress:
        tries_left -= 1

        if tries_left == 0:
            print('You died!')
            exit(0)
        else:
            print(f'You have {tries_left} tries left.')
            