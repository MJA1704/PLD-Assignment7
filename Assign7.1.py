#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#input: Bahala kayo dyan, #output:, #words: 3, #vowels: 6, #consonants: 

sentence =input("What do you want to say to me?(minimum of 2 sentences): \n     ")

words = 1
vowels=0
consonants=0

for i in sentence:
    if i == ' ' :
        words = words + 1 
    elif(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1
    elif (i == 'b' or i == 'c' or i == 'd' or i == 'f' or i == 'g' or i == 'h' or i == 'j' or i == 'k' or i == 'l' or 
        i == 'm' or i == 'n' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i == 'v' or i == 'w' or 
        i == 'x' or i == 'y' or i == 'z' or
        i == 'B' or i == 'C' or i == 'D' or i == 'F' or i == 'G' or i == 'H' or i == 'J' or i == 'K' or i == 'L' or 
        i == 'M' or i == 'N' or i == 'P' or i == 'Q' or i == 'R' or i == 'S' or i == 'T' or i == 'V' or i == 'W' or 
        i == 'X' or i == 'Y' or i == 'Z'):
            consonants=consonants+1

print(f"\nMessage for me: \n     {sentence}")           
print(f"Words: \n     The sentences have {words} words.")
print(f"Vowels: \n     The sentences have {vowels} vowels.")
print(f"Consonants: \n     The sentences have {consonants} consonants.")