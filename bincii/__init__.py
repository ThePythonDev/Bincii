def ascii_to_binary(ascii_string):
  return ' '.join(format(ord(c), '08b') for c in ascii_string)

def binary_to_ascii(binary_string):
  binary_chunks = [chunk.strip() for chunk in binary_string.split(" ")]
  ascii_string = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)
  return ascii_string