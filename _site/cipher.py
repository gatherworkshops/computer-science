message = input("What is your message?")
shift = input("What is the shift?")
shift = int(shift)

output = ""

alphabet = "abcdefghijklmnopqrstuvwxyz ?!"

for letter in message:

	if letter in alphabet:

		letter_position = alphabet.index(letter) + shift

		letter_position = letter_position % len(alphabet)

		output += alphabet[letter_position]

	else:

		output += letter

print("Enciphered message:", output)
