def talk(phrase):
    def say(word):
        print(word)

    words = phrase.str(' ')
    for word in words:
        print(words)

talk(str('I am going to buy the milk'))
