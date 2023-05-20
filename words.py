def print_upper_words(words, letters):
    """accepts list of words and a set of indivual letters and prints each word that begins with any of the letters on a separate line in uppercase
    
    For example: 
        print_upper_words(["ello", "hey", "hi", "hello", "howgoesit", "ei", "Eeyellow,sir"])

    should print:
        'ELLO',
        'EI',
        'EEYELLOW,SIR'
    """

    for word in words:
        for letter in letters:
            if word[0].upper() == letter.upper():
                print(word.upper())
    
print_upper_words(["hi", "yo", "heya", "eek!", "whatup", "ello"], {'h', 'e'})
print("should print 'HI', 'HEYA', 'EEK!', 'ELLO'")