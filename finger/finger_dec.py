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

original_text = open(input_file_name).read()
encoded_text = open(encoded_file_name).read()

recovered_bits = steganos.decode_partial_text(encoded_text, original_text)
recovered_msg = steganos.binary_to_bytes(recovered_bits)

print("Recovered: %s" % recovered_msg)
