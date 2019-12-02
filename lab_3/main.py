"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
    

class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if type(word) != str:
            return -1
        if word not in self.storage:
            if not self.storage:
                self.storage[word] = 1
            else:
                self.storage[word] = max(self.storage.values()) + 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if type(word) == str:
            if word not in self.storage:
                return self.storage[word]
            else:
                return -1
        else:
            return -1

    def get_original_by(self, id: int) -> str:
        if type(id) == int:
            for key, value in self.storage.items():
                if value == id:
                    return key
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if type(corpus) != tuple or corpus == ():
            return {}
        for word in corpus:
            if word not in self.storage:
                self.storage[word] = self.put(word)
        return self.storage


class NGramTrie:
    def __init__(self, number):
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.size = number

    def fill_from_sentence(self, sentence: tuple) -> str:
        if type(sentence) != tuple or sentence == '':
            return 'ERROR'
        elements = []
        n = self.size
        for i in range(len(sentence)):
            if len(sentence) - i > n:
                elements.append(sentence[i: i + n])
            elif len(sentence) - i == n:
                elements.append(sentence[i:])
        for elem in elements:
            if elem not in self.gram_frequencies:
                self.gram_frequencies[elem] = 1
            else:
                self.gram_frequencies[elem] += 1
        return 'OK'

    def calculate_log_probabilities(self):
        for elem in self.gram_frequencies:
            amount = []
            n = self.size
            for key, value in self.gram_frequencies.items():
                if elem[0: n - 1] == key[0: n - 1]:
                    amount.append(value)
            probability = self.gram_frequencies[elem] / sum(amount)
            self.gram_log_probabilities[elem] = math.log(probability)

    def predict_next_sentence(self, prefix: tuple) -> list:
        if type(prefix) != tuple or prefix == () or len(prefix) != self.size - 1:
            return []
        all_elem = []
        for elem in self.gram_log_probabilities:
            new = elem[0:len(elem) - 1]
            all_elem.append(new)
        sentence = []
        sentence.extend(list(prefix))
        while prefix in all_elem:
            the_popular = []
            for key, value in self.gram_log_probabilities.items():
                if prefix == key[0:len(key) - 1]:
                    the_popular.append((value, key))
            the_popular.sort(reverse=True)
            sentence.append(the_popular[0][0][-1])
            prefix = the_popular[0][0][1:]
        return sentence


def encode(storage_instance, corpus) -> list:
    coded_corpus = []
    for sentence in corpus:
        coded_sent = []
        for word in sentence:
            coded_sent.append(storage_instance[word])
        coded_corpus.append(coded_sent)
    return coded_corpus



def split_by_sentence(text: str) -> list:
        if type(text) != str or text == '' or '.' not in text:
        return []
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    text = text.lower()
    sentences = text.split('. ')
    clear_sentences = []
    for sent in sentences:
        clear_sentence = ''
        for letter in sent:
            if letter.isalpha() or letter == ' ':
                clear_sentence += letter
        if clear_sentence != '':
            new_sent = ['<s>']
            words = clear_sentence.split()
            new_sent.extend(words)
            new_sent.append('</s')
            clear_sentences.append(new_sent)
    return clear_sentences

