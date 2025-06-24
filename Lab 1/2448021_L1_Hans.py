#Import+ing necessory libraries
import nltk
from nltk import *
from nltk.book import *


#Question 1
print("Question 1\n")


print(text1)


print(sent1)

print(sent2)


print("\nOccurance of the word monstorous with some context: ")
text1.concordance("monstrous")


print("\nWords that are in similar range of context: ")
text1.similar("monstrous")

print("\nCommon contexts shared by two words: ")
text2.common_contexts(["monstrous", "very"])

#Question 2
print("\nQuestion 2")

#a
str_para = """Formula One (F1) is the highest class of worldwide
 racing for open-wheel single-seater formula racing cars sanctioned by the Fédération 
 Internationale de l'Automobile (FIA). The FIA Formula One World Championship has been one of the world's 
 premier forms of motorsport since its inaugural running in 1950 and is often considered to be the pinnacle of 
 motorsport. The word formula in the name refers to the set of rules all participant cars must follow. 
 A Formula One season consists of a series of races, known as Grands Prix. Grands Prix take place in multiple 
 countries and continents on either purpose-built circuits or closed roadsz."""

#b
print("\nQ2 b")
str_list = str_para.split()
print(str_list)

print("\nLength of the paragraph: ", len(str_list))
print("\nNumber of unique words: ", len(set(str_list)))


Freq_Words = FreqDist(str_para)
print(Freq_Words.most_common(20))

#c
print("\nQ2 c")

tokenised_str = word_tokenize(str_para)
Freq_tokenwords = FreqDist(tokenised_str).most_common()
print("Tokenized List: ",tokenised_str)
print("\nFrequency of words: ",Freq_tokenwords)

#Most frequent and less frequent word
print("\nMost frequent word is '", Freq_tokenwords[0][0],"' with frequency: ", Freq_tokenwords[0][1])
print("\nLeast frequent words: ", [w for w in Freq_tokenwords if w[1]==1])


#d
print("\nQ2 d")

word_lengths = [(tokenised_str.index(w),len(w)) for w in tokenised_str]
longest_word = tokenised_str[max(word_lengths, key = lambda x:x[1])[0]]
print("Longest word: ",longest_word)


#Daniel Jurafsky and Team
print("\nQuestion 3")
print("\nExercise 2.1")
#1.

print("\n1.")

pattern = r'^[a-zA-Z]*$'
test_strings = ["Hans", "test123", "ABC", "lucky05", "hi_there", "123", "hey!"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Alphabetic string: {s}")
    else:
        print(f"Not alphabetic: {s}")

#2. 
print("\n2.")

pattern2  = r'[a-zA-z]*b'
test_strings2 = ["Job","Live", "347","job123","lob"]
for s in test_strings2:
    if re.fullmatch(pattern2, s):
        print("String ending in b:", s)
    else:
        print("String not ending in b: ", s)

#3. 
print("\n3.")

pattern3 = 'b*(bab)*b*'
test_strings3 = ["bbbbbabbbb", "ab", "baba","bbabbb","abb"]
for s in test_strings3:
    if re.fullmatch(pattern3, s):
        print("Correct String:", s)
    else:
        print("Wrong String: ", s)

#2.2
#1.
print("\n2.2\n1.")

pattern = r'\b(\w+)\b(?:[\s,.!?;:-]+)\b\1\b'

test_sent = "My grandma is the the mayor of Kerala."
test_sent2 = "Humbert Humbert speaks delusional stuff"
print(True if re.search(pattern, test_sent, re.IGNORECASE) else False)
print(True if re.search(pattern, test_sent2, re.IGNORECASE) else False)


#2
print("\n2.")
line = "123 is the number of my neighbor"
match = re.fullmatch(r'^\d+.*\b[a-zA-Z]+\b$', line)
print(True if match else False)


#3
print("\n3.")

text = "The raven flew to the grotto"
text2 = "The raven flew into grottos"
if re.search(r'(?=.*\bgrotto\b)(?=.*\braven\b)', text, re.IGNORECASE):
    print("Contains both grotto and raven")
else:
    print("Does not contain")

if re.search(r'(?=.*\bgrotto\b)(?=.*\braven\b)', text2, re.IGNORECASE):
    print("Contains both 'grotto' and 'raven'")
else:
    print("Does not contain grottos")

#4
print("\n4.")

text = '"Hello there!" he said.'
match = re.match(r'^[\s"\']*([A-Z][a-zA-Z]*)\b', text)
if match:
    first_word = match.group(1)
    print("First word:", first_word)



