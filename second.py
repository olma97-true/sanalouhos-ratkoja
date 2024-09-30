import json
from string import ascii_uppercase as alc

def adjacent_letters(y, x):
    possibilities = [[x-1,y-1],[x,y-1],[x+1, y-1], [x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
    possibilities2 = possibilities.copy()
    adj_letters = []
    for pos in possibilities:
        if pos[0] < 0 or pos[1] < 0 or pos[0]>=len(boggle[0]) or pos[1]>=len(boggle):
            possibilities2.remove(pos)
        else:
            adj_letters.append(boggle[pos[1]][pos[0]])

    return possibilities2, adj_letters

def check_adjacency(word_to_check: str, ik: int, jk: int, letter: str, found_word: str, visited_positions: list, x=0):
    if word_to_check[x] == letter:
        visited_positions.append([jk, ik])

        found_word = found_word + boggle[ik][jk]
        if found_word == word_to_check:
            print(found_word, visited_positions)
        pos2, adj_let = adjacent_letters(ik, jk)
        pos = pos2.copy()
        for position in pos2:
            if position in visited_positions:
                if word_to_check == "AHAA":
                    print("AHAA")
                adj_let.pop(pos.index(position))
                pos.remove(position)

        for position in pos:
            if x<len(word_to_check)-1:
                check_adjacency(word, position[1], position[0], boggle[position[1]][position[0]], found_word, visited_positions, x+1)
        
        found_word = "" + found_word[-1]
        visited_positions.remove([jk, ik])

with open('csvjson.json') as file:
    dictionary = json.load(file)

for idx in range(len(dictionary)):
    dictionary[idx] = dictionary[idx]["Hakusana"].upper()

boggle = [["E", "G", "M", "E", "N"], 
          ["R", "S", "M", "A", "T"], 
          ["R", "E", "A", "H", "T"],
          ["A", "H", "T", "U", "I"],
          ["D", "E", "P", "S", "A"],
          ["O", "T", "O", "R", "K"]]

letter_counter = {}
empty_dict = {}
letters = alc + "ÅÄÖ"
for char in letters:
    empty_dict[char] = 0
letter_counter = empty_dict.copy()

for i in range(len(boggle)):
    for j in range(len(boggle[i])):
        letter_counter[boggle[i][j]] += 1

print(letter_counter)


forbidden_chars = ['Õ','Û','Ñ','À','’','Ô','Á','Ê','È','Â','É','Š','Ž',' ','‑','-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

dictionary2 = dictionary.copy()
for word in dictionary:
    remove = False
    
    for char in forbidden_chars:
        if char in word:
            remove = True
    if remove:
        dictionary2.remove(word)


dictionary3 = dictionary2.copy()
for word in dictionary2:
    remove = False
    word_dict = empty_dict.copy()
    for char in word:
        word_dict[char] +=1

    for char in letters:
        if word_dict[char] > letter_counter[char]:
            remove = True
            break

    if remove:
        dictionary3.remove(word)
        
for word in dictionary3:
    for i in range(len(boggle)):
        for j in range(len(boggle[i])):
            found_word = ""
            visited_positions = []
            check_adjacency(word, i, j, boggle[i][j], found_word, visited_positions)
                


