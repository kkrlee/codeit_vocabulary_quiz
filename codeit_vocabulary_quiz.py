in_file = open("vocabulary.txt", "r")

for line in in_file:
    data = line.strip().split(" : ")
    english_word = data[0]
    korean_meaning = data[1]
    guess = input("%s : " % korean_meaning)
    if guess == english_word:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % english_word)

in_file.close()
