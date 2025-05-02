def replace_word():# a function to replace a word
    sentence = input('Enter a simple sentence: ') # major sentence
    word_to_replace = input('Enter a word to be replaced: ')
    word_replacement = input('Enter a replacement word: ')
    print(sentence.replace(word_to_replace, word_replacement))# replace a word in the sentence
replace_word()