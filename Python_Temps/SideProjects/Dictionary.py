from PyDictionary import PyDictionary

dictionary = PyDictionary

def main():
    word_dictionary = {
        'vibe': "the energy/feeling in the air",
        'jawn': "an object or female",
        'factz': "a very true statement",
        'young bol': "a kid or child"
    }
    while True:
        word = input("Enter word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

main()
