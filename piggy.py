# Pig Latin takes the first consonant (or consonant cluster) of an English word, moves it to the end
# of the word and suffixes an ay, or if a word begins with a vowel you just add way to the end.
# For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def make_piggy(stringy):
    piggy_list = []
    string_list = stringy.split()
    for string in string_list:
        pigstring = ''
        for index, letter in enumerate(string):
            if letter in VOWELS:
                if index == 0:
                    pigstring = string + 'way'
                else:
                    pigstring = string[index:] + string[0:index] + 'ay'
                break
        piggy_list.append(pigstring)
    return ' '.join(piggy_list)
