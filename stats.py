# makes a count of every word in the entirety of the book
def word_counter(string):
    list = string.split()
    count = len(list)
    return count


#want to have a function that counts each character in the book
def character_counter(string):
    X = string.lower()
    dictor = {}
    splits = list(X)
    for item in splits:
        if item.isalpha() == False:
            continue
        elif item not in dictor:
            dictor[item] = 1
        else:
            dictor[item] += 1
    return dictor


#format the dictionary made by character_counter and word counter
def dictor_format(counter, dictor, file_path):
    print('============ BOOKBOT ============')
    print("Analyzing book found at " + file_path)
    print("----------- Word Count ----------")
    print("Found " + str(counter) + " total words")
    print("--------- Character Count -------")

    sort = dict(reversed((sorted(dictor.items(), key = lambda x: x[1]))))


    for item in sort:
        print(item + ": " + str(dictor[item]))

    print("============= END ===============")