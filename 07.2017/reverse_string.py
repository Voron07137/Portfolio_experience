def reverse_string(string):
    mas_words = string.split()
    return " ".join(mas_words[::-1])


print(reverse_string("I like a house music"))  # music house a like I
print(reverse_string("I live in Moscow"))  # Moscow in live I
