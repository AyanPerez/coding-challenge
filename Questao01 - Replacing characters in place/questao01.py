# Question 01
# Replace characters in place - space with &32


def substituir(sentence):
    new_sentence = ""
    for character in sentence:
        if character == ' ':
            new_sentence = new_sentence + '&32'
        else:
            new_sentence = new_sentence + character
    return new_sentence


# Input: string and length of string
array = input('Sentence: ')
length = int(input('Length: '))

# Check only until this limit
array = array[:length]

print('New Sentence: ', substituir(array))