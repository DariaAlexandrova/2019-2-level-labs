"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    frequency_dict = {}
    if type(text) == str:
        text = text.lower()
        text = text.replace('\n', ' ')
        signs = """1234567890!@#$%^&"*()_+-=|/.,?':;><[]{}~`"""
        clean_text = ''
        for s in text:
            if s not in signs:
                clean_text += s
        all_words = clean_text.split(' ')
        for el in all_words:
            if el not in frequency_dict:
                if el != '':
                    frequency_dict[el] = all_words.count(el)
    return frequency_dict

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    clean_dict = {}
    if type(stop_words) == tuple and type(frequencies) == dict:
        for key in frequencies.keys():
            if key not in stop_words:
                if type(key) == str:
                    if key != '':
                        clean_dict[key] = frequencies[key]
    return clean_dict

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    if type(top_n) != int:
        top_n = 0
    elif top_n < 0:
        top_n = 0
    top_of_words = ()
    if type(frequencies) == dict:
        if top_n > len(frequencies):
            top_n = len(frequencies)
        for n in range (top_n):
            more = 0
            its_name = ''
            for key, value in frequencies.items():
                if value > more:
                    more = value
                    its_name = key
            frequencies.pop(its_name)
            top_of_words += ((its_name),)
    return top_of_words


text_file = '''Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, 
there live the #blind #texts.

Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. 
A small river named Duden 19788 flows by their place and supplies it with the necessary regelialia.

It is a paradisematic country, in which roasted parts of sentences fly into your mouth.

Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic 
life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far 
World of Grammar.

The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question 
Marks and !devious! Semikoli, but the Little Blind Text didn’t listen. She packed her seven versalia, 
put her initial into the belt and made herself on the way./.*./

When she reached the first hills of the :) Italic Mountains, she had a last view back on the skyline of 
her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. 
Pityful a rethoric question ran over her cheek, then :);'''
number = 3
words_to_stop = ('but', 'and', 'the', 'of', 'a', 'with', 6, False, '')

dicty = calculate_frequences(text_file)
clean_dicty = filter_stop_words(dicty, words_to_stop)
top_tuple = get_top_n(clean_dicty, number)
