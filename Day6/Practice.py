# sum of all the numbers in the number that call the function -- 1234 -- 1+2+3+4 -- return 10
def digit_sum(n):
  total = 0
  while n > 0:
    total += n % 10
    n = n // 10
  return total

# multiply all the integers from 1 through the number that entered -- x = 4 -- 1*2*3*4 -- return 24
def factorial(x):
    total = 1
    for i in range(x):
        total *= i+1
    return total

# check if the number that entered the function is prime or not -- 5 -- return true || -- 6 -- return false
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

# reveres the word that entered -- "Hello" -- return "olleH"
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

# remove all the vowels from a text -- "Hello" -- return "Hll"
def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result

# get the total score of the word you say, little spell game
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
  text = word.lower()
  total = 0
  for i in text:
    total += score[i]
  return total

# the function get a text and a word that you want to censor in the text --
# "what are you doing what?!", "what" -- return "**** are you doing ****?!"
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

# count the number of times that the item is showing on the list sequence -- [1,1,2,1],[1] -- return 3
def count(sequence,item):
  count = 0
  for i in sequence:
    if i == item:
        count+=1
  return count


# remove the duplicates in a list of numbers that you enter to this function -- [1,2,4,2,1,6] -- return [1,2,4,6]
def remove_duplicates(inputlist):
    if inputlist == []:
        return []

    # Sort the input list from low to high
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)

    return outputlist

print (digit_sum(1234))
print (factorial(4))
print (is_prime(5))
print (reverse("hello"))
print (anti_vowel("Hello anti vowel"))
print ("the score for Hello is - " , scrabble_score("Hello"))
print (censor("What the hack the hack", "hack"))
print (count([1,1,2,1],1))
print (remove_duplicates([1,2,4,2,1,6]))
