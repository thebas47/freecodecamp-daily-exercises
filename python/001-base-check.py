def is_valid_number(n, base):

    bases = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in n.lower():
        if i in bases[:base]:
            continue
        return False
    return True

print(is_valid_number("10101", 2))
print(is_valid_number("10201", 2))
print(is_valid_number("76543210", 8))
print(is_valid_number("9876543210", 8))
print(is_valid_number("9876543210", 10))
print(is_valid_number("ABC", 10))
print(is_valid_number("ABC", 16))
print(is_valid_number("Z", 36))
print(is_valid_number("ABC", 20))
print(is_valid_number("4B4BA9", 16))
print(is_valid_number("5G3F8F", 16))
print(is_valid_number("5G3F8F", 17))
print(is_valid_number("abc", 10))
print(is_valid_number("abc", 16))
print(is_valid_number("AbC", 16))
print(is_valid_number("z", 36))
