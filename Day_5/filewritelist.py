#writing list to a file

wordList = ["Red", "Blue", "Green"]
filePath = "output.txt"

file = open(filePath, 'w')
file.writelines(wordList)
file.close()
