# Caesar cipher Brute Force Decrypter

# Created by: Hrithik


# Input from the user
encrypted_text = input("\nPlease provide the Caesar Ciphertext: ")


# Goodness of letters
goodness_of_letters  = {"a": .0817, "b": .0149, "c": .0278, "d": .0425, "e": .1270, 
"f": .0223, "g": .0202, "h": .0609, "i": .0697, "j": .0015, "k": .0077, "l": .0402, 
"m": .0241, "n": .0675, "o": .0751, "p": .0193, "q": .0009, "r": .0599, "s": .0633, 
"t": .0906, "u": .0276, "v": .0098, "w": .0236, "x": .0015, "y": .0197, "z": .0007}

# Function to find the Goodness of a word
def Goodness(text):
	value = 0
	for word in text:
		for letter in word:
			if letter.isalpha():
				value = value + goodness_of_letters[letter.lower()]
	return value


# Decrypter
def Decrypt(encrypted_text, key):
	decrypted_text = ""

	for letter in encrypted_text:

		# For Alphabets
		if letter.isalpha():

			# For Uppercase
			if letter.isupper():
				decrypted_letter = ord(letter) - key
				if decrypted_letter < 65:
					decrypted_letter = decrypted_letter + 26
				decrypted_text = decrypted_text + chr(decrypted_letter)

			# For Lowercase
			else:
				decrypted_letter = ord(letter) - key
				if decrypted_letter < 97:
					decrypted_letter = decrypted_letter + 26
				decrypted_text = decrypted_text + chr(decrypted_letter)

		# For other characters
		else:
			decrypted_text = decrypted_text + letter
	
	return decrypted_text


# MAIN
goodness = 0
for keys in range(26):

	decrypted = Decrypt(encrypted_text, keys)
	goodness_temp = Goodness(decrypted)

	if goodness_temp > goodness:
		goodness = goodness_temp
		decrypted_text = decrypted
		key = keys


print("\nGoodness: ", goodness)
print("Plaintext: ", decrypted_text)
print("Key: ", key)