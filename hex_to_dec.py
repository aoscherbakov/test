__author__ = 'sherbakov'

dec_nums = []

hex_str = raw_input("Enter Hex String: ")
hex_nums = hex_str.split(":")

for num in hex_nums:
    dec_nums.append(str(int(num, 16)))

dec_str = ":".join(dec_nums)

print dec_str
