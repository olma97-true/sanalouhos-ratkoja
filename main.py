import json

with open('csvjson.json') as file:
    dictionary2 = json.load(file)

dictionary = []
for entry in dictionary2:
    dictionary.append(entry["Hakusana"])
print(dictionary)
# Python3 program for Boggle game
# Let the given dictionary be following

n = len(dictionary)
M = 6
N = 5

# A given function to check if a given string
# is present in dictionary. The implementation is
# naive for simplicity. As per the question
# dictionary is given to us.
def isWord(Str):
  
    # Linearly search all words
    for i in range(n):
        if (Str == dictionary[i]):
            return True
    return False

# A recursive function to print all words present on boggle
def findWordsUtil(boggle, visited, i, j, Str):
    # Mark current cell as visited and
    # append current character to str
    visited[i][j] = True
    Str = Str + boggle[i][j]
    
    # If str is present in dictionary,
    # then print it
    if (isWord(Str)):
        print(f'{Str} is a word in the dictionary')
        found_words.append(Str)
    else:
        print(f'{Str} is not a word in the dictionary')
    
    # Traverse 8 adjacent cells of boggle[i,j]
    row = i - 1
    while row <= i + 1 and row < M:
        col = j - 1
        while col <= j + 1 and col < N:
            if (row >= 0 and col >= 0 and not visited[row][col]):
                findWordsUtil(boggle, visited, row, col, Str)
            col+=1
        row+=1
    
    # Erase current character from string and
    # mark visited of current cell as false
    Str = "" + Str[-1]
    visited[i][j] = False

# Prints all words present in dictionary.
def findWords(boggle):
  
    # Mark all characters as not visited
    visited = [[False for i in range(N)] for j in range(M)]
    
    # Initialize current string
    Str = ""
    
    # Consider every character and look for all words
    # starting with this character
    for i in range(M):
      for j in range(N):
        findWordsUtil(boggle, visited, i, j, Str)



# Driver Code
boggle = [["E", "G", "M", "E", "N"], 
          ["R", "S", "M", "A", "T"], 
          ["R", "E", "A", "H", "T"],
          ["A", "H", "T", "U", "I"],
          ["D", "E", "P", "S", "A"],
          ["O", "T", "O", "R", "K"]]

found_words = []
print("Following words of", "dictionary are present")
findWords(boggle)
print(f"\n \n \nThe following words were found in the boggle")
for word in found_words:
    print(word)
print("The process is complete")
