#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    i = 0
    while i < len(data):
        num_bytes = 0
        mask = 0x80
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        if num_bytes == 0:
            num_bytes = 1
        elif num_bytes == 1 or num_bytes > 4:
            return False

        if i + num_bytes > len(data):
            return False
        for j in range(1, num_bytes):
            if (data[i + j] & 0xc0) != 0x80:
                return False
        i += num_bytes

    return True
