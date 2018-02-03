#!/usr/bin/env python3
import steganos

bits = input("Bits to encode: ")
original_text = input("Original text: ")
encoded_text = steganos.encode(bits, original_text)
print("Encoded: %s" % encoded_text)
recovered_bits = steganos.decode_full_text(encoded_text, original_text)
print("Recovered: %s" % recovered_bits)
