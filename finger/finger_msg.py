#!/usr/bin/env python3
import steganos
import sys

if len(sys.argv) > 1:
    input_file_name = sys.argv[1]
else:
    input_file_name = 'text.txt'

if len(sys.argv) > 2:
    encoded_file_name = sys.argv[2]
else:
    encoded_file_name = 'encoded.txt'

message = input().encode('utf-8')
original_text = open(input_file_name).read()

bits = steganos.bytes_to_binary(message)
encoded_text = steganos.encode(bits, original_text)
open(encoded_file_name, 'w').write(encoded_text)

recovered_bits = steganos.decode_full_text(encoded_text, original_text)
recovered_msg = steganos.binary_to_bytes(recovered_bits)

print("Recovered: %s" % recovered_msg)
# recovered_msg.startswith(b'Hello World!') == True
