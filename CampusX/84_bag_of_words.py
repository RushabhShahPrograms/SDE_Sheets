'''
Write a function that accepts a list of strings and performs Bag of words and convert it to numerical vectors.
https://en.wikipedia.org/wiki/Bag-of-words_model
'''

def bag_of_words(texts):
    unique_words = set(word for text in texts for word in text.split())
    word_vectors = {word: [0]*len(texts) for word in unique_words}

    for i, text in enumerate(texts):
        for word in text.split():
            if word in word_vectors:
                word_vectors[word][i] += 1
    
    return word_vectors

texts = ["the cat sat on the mat", "the dog sat on the log", "cats and dogs are great"]
print(bag_of_words(texts))