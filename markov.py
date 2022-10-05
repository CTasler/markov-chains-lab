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


def make_chains(content, n_gram):
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
    for i in range(len(words) - n_gram):
        key = []
        value = words[i + n_gram]
        for num in range(n_gram):
            key.append(words[i])
            i += 1
        key = tuple(key)
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
    new_key = []
    i = 1
    for num in range(n_gram - 1):
        new_key.append(random_key[i])
        i += 1
    new_key.append(new_value)
    new_key = tuple(new_key)

    while new_key in chains: 
        new_value = choice(chains[new_key])
        final_sentence += f"{new_value} "
        new_new_key = []
        i = 1
        for num in range(n_gram - 1):
            new_new_key.append(new_key[i])
            i += 1
        new_new_key.append(new_value)
        new_key = tuple(new_new_key)
   
    return final_sentence


n_gram = int(input("How long would you like your n_gram to be? "))
input_path = sys.argv[1]
input_text = open_and_read_file(input_path)
chains = make_chains(input_text, n_gram)
random_text = make_text(chains)
print(random_text)
