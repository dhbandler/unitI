#Daniel Bandler
#1/22/18
#stringAnalysis.py reports number of words and characters, and can ask for a character to search for

string1=input(str("Type a sentence here    "))
sentence=len(string1)

string2=(" ")

words = int(string1.count(string2))+1

let=input("Input what letter you want to search for")
print("There are ", string1.count(let.lower())+string1.count(let.upper()), "Occurences of that letter")

search=input("Input a word you want to count")
print("There are ", string1.count(search.lower())+string1.count(search.upper()), "occurances of that word")

print("Your sentence has", words, "words")
print("Your sentence has", sentence, "characters")