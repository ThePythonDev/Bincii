def string_to_binary(s):
  return ' '.join(format(ord(c), '08b') for c in s)

def convert_binary_to_ascii(binary_string):
  binary_chunks = [chunk.strip() for chunk in binary_string.split(" ")]
  ascii_string = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)
  return ascii_string
def main():
	while True:
		bincii = input("Convert BIN to ASCII or ASCII to BIN? (Say BIN or ASCII) ")
		bincii = bincii.lower()
		if bincii == "bin":
			binary_string = input("Your BIN? ")
			ascii_string = convert_binary_to_ascii(binary_string)
			print("Your ASCII is:\n", ascii_string)
		elif bincii == "ascii":
			ascii = input("Your ASCII? ")
			print("Your BIN is:\n", string_to_binary(ascii))
		else:
			print("I think you mispelled something :/")

try:
	main()
except ValueError as error:
	print("You got an error! (Be more careful!)", error)
	main()