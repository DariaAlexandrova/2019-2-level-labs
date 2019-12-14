import math


REFERENCE_TEXTS = []


def clean_tokenize_corpus(scripts: list) -> list:
    if type(scripts) != list:
        return []
    corpus = []
    for scr in scripts:
        if type(scr) != str:
            continue
        scr = scr.lower()
        scr = scr.replace('<br />', ' ')
        for s in scr:
            if not s.isalpha() and s != ' ':
                scr = scr.replace(s, '')
        corpus.append(scr.split())
    return corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if type(self.corpus) != list:
            return []
        for txt in self.corpus:
            if type(txt) != list:
                continue
            doc_dict = {}
            clean_text = []
            for elem in txt:
                if type(elem) == str:
                    clean_text.append(elem)
            text_length = len(clean_text)
            for word in clean_text:
                if word not in doc_dict:
                    doc_dict[word] = txt.count(word) / text_length
            self.tf_values.append(doc_dict)

    def calculate_idf(self):
        if type(self.corpus) != list:
            return {}
        words = []
        for txt in self.corpus:
            if type(txt) != list:
                continue
            for el in txt:
                if type(el) == str and el not in words:
                    words.append(el)
        clean_corpus = []
        for doc in self.corpus:
            if type(doc) == list:
                clean_corpus.append(doc)
        length_corpus = len(clean_corpus)
        for word in words:
            frequency = 0
            for txt in self.corpus:
                if type(txt) == list and word in txt:
                    frequency += 1
            self.idf_values[word] = math.log(length_corpus / frequency)

    def calculate(self):
        if type(self.tf_values) != list:
            return []
        for txt in self.tf_values:
            new_doc_dict = {}
            for key in txt:
                if key in txt and key in self.idf_values:
                    new_doc_dict[key] = txt[key] * self.idf_values[key]
                else:
                    return []
            self.tf_idf_values.append(new_doc_dict)

    def report_on(self, word, document_index):
        if self.tf_idf_values is None:
            return ()
        if document_index > len(self.tf_idf_values) - 1:
            return ()
        if word not in self.tf_idf_values[document_index]:
            return ()
        word_info = [self.tf_idf_values[document_index][word]]
        the_most_important = list(self.tf_idf_values[document_index].items())
        the_most_important.sort(key=lambda x: x[1], reverse=True)
        ind = -1
        for elem in the_most_important:
            if elem[0] == word:
                ind = the_most_important.index(elem)
                break
        if ind != -1:
            word_info.append(ind)
        return tuple(word_info)


if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
