a = input("Input a letter of the alphabet: ")
word = a.lower()
first = word[0]

if len(a) > 0:
	if first in 'aeiou':
		print ("vowel")
	else:
		print("consonant")
else:
	print("empty")
 