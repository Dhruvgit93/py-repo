import string

def word_frequency(paragraph):
    # Clean the paragraph by removing punctuation and converting to lowercase
    cleaned_paragraph = paragraph.lower().translate(str.maketrans('', '', string.punctuation))

    # Split the cleaned paragraph into words
    words = cleaned_paragraph.split()

    # Create a dictionary to store word frequencies
    word_freq_dict = {}

    # Iterate through the words, update the dictionary
    for word in words:
        if word in word_freq_dict:
            word_freq_dict[word] += 1
        else:
            word_freq_dict[word] = 1

    return word_freq_dict

# Get input paragraph from the user
paragraph = "Google Chrome is a cross-platform web browser developed by Google. It was first released in 2008 for Microsoft Windows, built with free software components from Apple WebKit and Mozilla Firefox."

# Get word frequencies
word_freq_dict = word_frequency(paragraph)

# Print word frequencies
print("Word frequency:")
for word, frequency in word_freq_dict.items():
    print(f"{word}: {frequency}")
