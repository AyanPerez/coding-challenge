# Question 03
# Check words with typos


def is_typo_replace(string1, string2, total):
    # Replace a character
    i = 0
    changed = 0
    while i < total:
        if string1[i] != string2[i]:
            changed = changed + 1
        i = i + 1
    if changed == 1:
        return 'true'
    else:
        return 'false'


def is_equal(string1, string2):
    i = 0
    for character in string1:
        if character == string2[i]:
            i = i + 1
        else:
            return 0
    return 1


def is_typo_remove(string1, string2, total2):
    # Remove at the begin a character
    i = 0
    k = 0
    typo = 0
    if string1[i] != string2[i]:
        if is_equal(string1[(i + 1):], string2):
            return 'true'
        else:
            return 'false'
    else:
        while i < total2 and string1[i] == string2[i]:
            i = i + 1
        # Remove at the middle a character
        if string1[(i+1):] and string2[i:]:
            if is_equal(string1[(i+1):], string2[i:]):
                return 'true'
            else:
                return 'false'
        # Remove at the end a character
        elif string1[i:] and string2[i:] == "":
            return 'true'
        else:
            return 'false'


def size(word):
    x = 0
    if word:
        for character in word:
            x = x + 1
        return x
    else:
        return 0


first_word = input('First word > ')
second_word = input('Second word > ')
first_length = size(first_word)
second_length = size(second_word)

# print(is_equal(first_word, second_word))

if first_length > 0 and second_length > 0:
    if first_length == second_length:
        is_typo = is_typo_replace(first_word, second_word, first_length)
    elif first_length > second_length:
        is_typo = is_typo_remove(first_word, second_word, second_length)
    elif first_length < second_length:
        is_typo = is_typo_remove(second_word, first_word, first_length)
    print(is_typo)
else:
    print('Empty Word!')
