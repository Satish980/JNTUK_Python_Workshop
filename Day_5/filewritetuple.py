#writing list to a file

wordList = ["Red\n", "Blue\n", "Green\n"]
filePath = "output.txt"

file = open(filePath, 'w')
file.writelines(wordList)
 
file.close()


 
