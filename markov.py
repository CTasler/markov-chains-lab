"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    content = open(file_path).read()
    print(content)
    return content


def make_chains(content):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    
    words = content.split()
    value = []
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]
        if key not in chains:
            chains[key] = []
        chains[key].append(value)
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    all_keys = []
  
    for key in chains.keys():
        all_keys.append(key)
       
    random_key = choice(all_keys)
    final_sentence = " ".join(list(random_key))
    new_value = choice(chains[random_key])
    final_sentence += f" {new_value} "
    new_key = (random_key[1], new_value)

    while new_key in chains: 
        new_value = choice(chains[new_key])
        final_sentence += f"{new_value} "
        new_key = (new_key[1], new_value)
   
    print(final_sentence.capitalize())
    return final_sentence.capitalize()


input_path = sys.argv[1]
input_text = open_and_read_file(input_path)
chains = make_chains(input_text)
random_text = make_text(chains)
print(random_text)
