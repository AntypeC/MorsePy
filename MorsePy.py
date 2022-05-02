import time
import winsound

freq = 600

translate_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
					'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
					'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
					'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
					'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
					'U': '..-', 'V': '..-', 'W': '.--', 'X': '-..-',
					'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
					'2': '..---', '3': '...--', '4': '....-', '5': '.....',
					'6': '-....', '7': '--...', '8': '---..', '9': '----.', 
					" ": "/"}

message = "This is just a message"
message = " ".join(translate_dict[c] for c in message.upper())

print(message)


def play_morse_code(message):
	for c in message:
		if c == ".":
			winsound.Beep(freq, 100)
			time.sleep(0.1)

		elif c == "-":
			winsound.Beep(freq, 300)
			time.sleep(0.1)

		elif c == "/":
			time.sleep(0.3)

		elif c == " ":
			time.sleep(0.7)

		else:
			print("Invalid character detected!") 

print(message)
# play_morse_code(message)

reverse_dict = {v: k for k, v in translate_dict.items()}
reverse_message = "".join(reverse_dict[c] for c in message.split(" "))
print(reverse_message)