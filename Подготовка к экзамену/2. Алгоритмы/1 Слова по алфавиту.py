def generate_words(alphabet, word_len):
    words = ['']
    
    for _ in range(word_len):
        new_words = []
        for word in words:
            for char in alphabet:
                new_words.append(word+char)
            words = new_words
                
    return words


alphabet = ['a', 'b', 'c']
words_len = 2
print(generate_words(alphabet, words_len))


# ИЛИ (более правильно)

def product_analog(string, repeat):
    if repeat == 0:
        yield ""
    else:
        for i in string:
            for j in product_analog(string, repeat-1):
                yield i + j

print(list(product_analog("abc", 2)))