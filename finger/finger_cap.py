#!/usr/bin/env python3
import steganos

original_text = input("Original text: ")
capacity = steganos.bit_capacity(original_text)
print("Capacity: %d" % capacity)
