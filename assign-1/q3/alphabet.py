import string
import collections
import matplotlib.pyplot as plt

def count_letters(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    # Make all characters lowercase
    text = text.lower()

    # Remove all non-alphabetic characters
    text = ''.join(c for c in text if c in string.ascii_lowercase)

    # Count the frequency of each letter
    letter_counts = collections.Counter(text)
    total_letters = sum(letter_counts.values())
    letter_freqs = {letter: count / total_letters for letter, count in letter_counts.items()}
    return letter_freqs

def plot_letter_freqs(letter_freqs):
    # Plot the letter frequencies
    letters = sorted(letter_freqs.keys())
    freqs = [letter_freqs[letter] for letter in letters]
    plt.hist(freqs, bins=26, edgecolor='black')
    plt.xlabel('Frequency')
    plt.ylabel('Number of letters')
    plt.show()


# Testing the code, can be used for any text file
file_path = 'assign-1/q3/gutenberg.txt'
letter_freqs = count_letters(file_path)
print(letter_freqs)
plot_letter_freqs(letter_freqs)

