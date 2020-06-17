# Question 02
# Check words with jumbled letters

# ­ The first letter hasn’t changed place
# - If word has more than 3 letters, up to 2/3 of the letters have changed place


def is_partial_permutation(string1, string2, total):
    changed = 0
    i = 0
    if string1 and string2:
          if string1[0]==string2[0]:
              if total == 1:
                  return 'true'
              elif total == 2 and string1[1]==string2[1]:
                  return 'true'
              elif total == 3 and ((string1[1] == string2[2] and string1[2] == string2[1]) or
                                   (string1[1] == string2[1] and string1[2] == string2[2])):
                  return 'true'
              elif total >= 3:
                  while (i < total):
                      if string1[i] != string2[i]:
                          changed = changed + 1
                      i = i + 1
                  if changed <= ((2/3) * total):
                      return 'true'
                  else:
                      return 'false'
              else:
                  return 'false'
          else:
              return 'false'
    return 'Empty word!'


def size(word):
    x = 0
    for character in word:
        x = x + 1
    return x


first_word = input('First word > ')
second_word = input('Second word > ')
first_length = size(first_word)
second_length = size(second_word)

if first_length == second_length:
    print(is_partial_permutation(first_word, second_word, first_length))
else:
    print('false')
