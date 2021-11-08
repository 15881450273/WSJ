# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 12:48
# @File    : trainingFeatures.py
# @Software: PyCharm
from nltk.stem.porter import *
class Featured_token():
    def __init__(self, feature_list):
        self.token = feature_list[0]
        self.POS = feature_list[1]
        self.BIO = feature_list[2]
        self.prev_2word_POS = []
        self.folw_2word_POS = []
        self.prev_2word_BIO = []
        self.folw_2word_BIO = []
        self.prev_2word_token = []
        self.folw_2word_token = []
        self.prev_2word_stemmed_token = []
        self.folw_2word_stemmed_token = []
        self.stemmed_token = None
def main():
    stemmer = PorterStemmer()
    filename = 'WSJ_02-21.pos-chunk'
    file = open(filename, "r")
    whole_training_chunk = file.read()
    whole_training_chunk_list = whole_training_chunk.split("\n")
    print(whole_training_chunk_list.__len__())
    file.close()
    feature_list_for_all_tokens = []
    for index in range(0, whole_training_chunk_list.__len__()):
        if whole_training_chunk_list[index] == '':
            feature_list_for_all_tokens.append('')
        else:
            temp_list = whole_training_chunk_list[index].split('\t')
            feature_list_for_all_tokens.append(temp_list)

    total_length = feature_list_for_all_tokens.__len__()
    print(total_length)
    tokens = []
    filename = 'training.feature'
    file = open(filename, 'w')
    for index in range(0, feature_list_for_all_tokens.__len__()):
        temp_elt = feature_list_for_all_tokens[index]
        if temp_elt == '':
            tokens.append(temp_elt)
            file.write('\n')
        else:
            featured_token = Featured_token(temp_elt)
            featured_token.stemmed_token = stemmer.stem(featured_token.token)
            prev_featured_list = feature_list_for_all_tokens[index - 1]
            if prev_featured_list == '':
                featured_token.prev_2word_POS = ['NONE', 'BOS']
                featured_token.prev_2word_stemmed_token = ['NONE', 'BOS']
                featured_token.prev_2word_token = ['NONE', 'BOS']
                featured_token.prev_2word_BIO = ['NONE', 'BOS']
            else:
                prev_2_featured_list = feature_list_for_all_tokens[index - 2]
                if prev_2_featured_list == '':
                    featured_token.prev_2word_token = ['BOS', prev_featured_list[0]]
                    featured_token.prev_2word_stemmed_token = ['BOS', stemmer.stem(prev_featured_list[0])]
                    featured_token.prev_2word_POS = ['BOS', prev_featured_list[1]]
                    featured_token.prev_2word_BIO = ['BOS', prev_featured_list[2]]
                else:
                    featured_token.prev_2word_token = [prev_2_featured_list[0], prev_featured_list[0]]
                    featured_token.prev_2word_stemmed_token = [stemmer.stem(prev_2_featured_list[0]), \
                                                        stemmer.stem(prev_featured_list[0])]
                    featured_token.prev_2word_POS = [prev_2_featured_list[1], prev_featured_list[1]]
                    featured_token.prev_2word_BIO = [prev_2_featured_list[2], prev_featured_list[2]]
            folw_featured_list = feature_list_for_all_tokens[index + 1]
            if folw_featured_list == '':
                featured_token.folw_2word_POS = ['EOS', 'NONE']
                featured_token.folw_2word_stemmed_token = ['EOS', 'NONE']
                featured_token.folw_2word_token = ['EOS', 'NONE']
                featured_token.folw_2word_BIO = ['EOS', 'NONE']
            else:
                folw_2_featured_list = feature_list_for_all_tokens[index + 2]
                if folw_2_featured_list == '':
                    featured_token.folw_2word_token = [folw_featured_list[0], 'EOS']
                    featured_token.folw_2word_stemmed_token = [stemmer.stem(folw_featured_list[0]), 'EOS']
                    featured_token.folw_2word_POS = [folw_featured_list[1], 'EOS']
                    featured_token.folw_2word_BIO = [folw_featured_list[2], 'EOS']
                else:
                    featured_token.folw_2word_token = [folw_featured_list[0], folw_2_featured_list[0]]
                    featured_token.folw_2word_stemmed_token = [stemmer.stem(folw_featured_list[0]), \
                                                               stemmer.stem(folw_2_featured_list[0])]
                    featured_token.folw_2word_POS = [folw_featured_list[1], folw_2_featured_list[1]]
                    featured_token.folw_2word_BIO = [folw_featured_list[2], folw_2_featured_list[2]]
            print(index / total_length)
            file.write('TOKEN=' + featured_token.token + '\t' + \
                       'POS=' + featured_token.POS + '\t' + \
 \
                       'STEMMEDTOKEN=' + featured_token.stemmed_token + '\t' + \
                       str(featured_token.prev_2word_token[0]) + '\t' + str(featured_token.prev_2word_token[1]) + '\t' + \
                       str(featured_token.prev_2word_stemmed_token[0]) + '\t' + str(
                featured_token.prev_2word_stemmed_token[1]) + '\t' + \
                       str(featured_token.prev_2word_POS[0]) + '\t' + str(featured_token.prev_2word_POS[1]) + '\t' + \
                       str(featured_token.folw_2word_token[0]) + '\t' + str(featured_token.folw_2word_token[0]) + '\t' + \
                       str(featured_token.folw_2word_stemmed_token[0]) + '\t' + str(
                featured_token.folw_2word_stemmed_token[1]) + '\t' + \
                       str(featured_token.folw_2word_POS[0]) + '\t' + str(featured_token.folw_2word_POS[1]) + '\t' + \
                       'BIO=' + featured_token.BIO + '\t')
    file.close()
main()