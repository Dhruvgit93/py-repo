import string
count=0
dict_word={}
def word_frequency(paragraph):
    # Clean the paragraph by removing punctuation and converting to lowercase
    # Split the paragraph into words
    words=paragraph.split()
    # Create a dictionary to store word frequencies
    print(words)
    # Iterate through the words, update the dictionary
    for word in words:
        if word in words:
            dict_word[word]=count+1
        else:
            dict_word=word
    # Sort the dictionary by frequency in descending order
    
    return word_freq_dict

# Get input paragraph from the user
paragraph = "Google Chrome is a cross-platform web browser developed by Google. It was first released in 2008 for Microsoft Windows, built with free software components from Apple WebKit and Mozilla Firefox."

# Get word frequencies
word_freq_dict = word_frequency(paragraph)

# Print word frequencies
print("Word frequency:")
for word, frequency in word_freq_dict.items():
    print(f"{word}: {frequency}")
