#!/usr/bin/python3
# Bitwise Operators

"""
>>>> 6 Bitwise Operators:
        Complement
        Bitwise AND
        Bitwise OR
        Bitwise XOR
        LEFT SHIFT
        RIGHT SHIFT
>>>>
>>>>
>>>>
>>>>
>>>>
"""

# Complement Operators.
# ~x=-(x+1)
# For eg: ~12 = -13
# First we find the complement of the 12
# The answer we get is the two's complement of the 13, which is -13.

# Bitwise AND
# 12 & 13 = 12
# Convert 12 into 8 bit binary
# Convert 13 into 8 bit binary
# If both both places have 1 then write 1 below it , otherwise 0
# Then convert that number into decimal
# That's the answer.

# Bitwise OR
# 12 | 13 = 13
# Same as the bitwise AND.
# If any both of them is 0 then write 0 below, else 1

# Bitwise XOR
# 12 ^ 13 = 1
# 0, if both are same
# 1, if both are different

# LEFT SHIFT
# 12 << 2 = 48
# Convert 12 into binary
# Add two zero after the binary
# The output is the leftshift

# RIGHT SHIFT
# 100 >> 2 = 25
# Convert 100 into binary
# And remove the last two bits
# The output is the right shift
