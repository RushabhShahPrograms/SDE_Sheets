'''
Write a program that can find the most used word in a bollywood song
'''

def most_used_words(song_lyrics):
    words = song_lyrics.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    max_count = max(word_counts.values())
    most_used_words = [word for word, count in word_counts.items() if count == max_count]

    return most_used_words,max_count

song_lyrics = "Tum hi ho ab tum hi ho zindagi ab tum hi ho"
print(most_used_words(song_lyrics))