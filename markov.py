"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    f = open(file_path)
    contents = f.read()
    f.close()

    return contents


# def make_chains(text_string):
#     """Take input text as string; return dictionary of Markov chains.

#     A chain will be a key that consists of a tuple of (word1, word2)
#     and the value would be a list of the word(s) that follow those two
#     words in the input text.

#     For example:

#         >>> chains = make_chains("hi there mary hi there juanita")

#     Each bigram (except the last) will be a key in chains:

#         >>> sorted(chains.keys())
#         [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

#     Each item in chains is a list of all possible following words:

#         >>> chains[('hi', 'there')]
#         ['mary', 'juanita']
        
#         >>> chains[('there','juanita')]
#         [None]
#     """

#     chains = {}
#     words = text_string.split()
#     for i in range(len(words) - 2):
#         n_gram = (words[i], words[i + 1])
#         if n_gram not in chains: 
#             chains[n_gram] = [words[i + 2]]
#         else: 
#             chains[n_gram].append(words[i + 2])

#     return chains

def n_make_chains(text_string,n):

    chains = {}
    words = text_string.split()
    for i in range(len(words) - n): 
        for j in range(n):
            n_gram += (words[j],)

        if n_gram not in chains: 
            chains[n_gram] = [words[i + n]]
        else: 
            chains[n_gram].append(words[i + n])
    return chains 
    

def make_text(chains):
    """Return text from chains."""
    words = []
    key = choice(chains.keys())
    words.extend(list(key))
    word = choice(chains[key])
    words.append(word)
    link = list(key) + [word]

    while True: 
        key = (link[1], link[2])
        if not chains.get(key): 
            break
        word = choice(chains[key])
        link = list(key) + [word]
        words.append(word)

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
# chains = make_chains(input_text)

# Produce random text
# random_text = make_text(chains)

# print random_text
