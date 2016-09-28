#!/usr/bin/env python
# coding=gbk
# author=hechengwei
# date=2016-09-27

import sys
import math


class Tfidf(object):
    """ """ 
    def __init__(self):
        self.vocab_list = []
        self.index2word_dict = {}
        self.word2index_dict = {}
        self.term_doc_dict = {}
        self.corpus = [] # 2 dimension matrix
        self.tfidf_list = []

    def load(self, corpus, delimiter=' '):
        vocab_set = set()
        with open(corpus, 'r') as fr:
            for line in fr:
                line  = line.strip()
                if line == "":
                    continue
                term_list = line.split(delimiter)
                self.corpus.append(term_list)
                
                for term in set(term_list):
                    self.term_doc_dict.setdefault(term, 0)
                    self.term_doc_dict[term] += 1
                    vocab_set.add(term)
        self.vocab_list = list(vocab_set)
        self.word2index_dict = {v: k for k, v in enumerate(self.vocab_list)}
        self.index2word_dict = {v: k for k, v in self.word2index_dict.iteritems()}
        print >> sys.stderr, "vocab length: %s" % len(self.vocab_list)
                
    def calc_tfidf(self):
        
        for doc_term_list in self.corpus:
            #tfidf_list = [0] * len(self.vocab_list)
            tfidf_dict = {}
            doc_len = len(doc_term_list)
            doc_tf = {}
            for term in doc_term_list:
                doc_tf.setdefault(term, 0)
                doc_tf[term] += 1
            
            for term, tf in doc_tf.iteritems():
                #index = self.word2index_dict[term]
                idf = self.term_doc_dict[term]
                tfidf = (tf * 1.0 / doc_len) * math.log(len(self.corpus) * 1.0 / idf)
                #tfidf_list[index] = tfidf
                tfidf_dict[term] = tfidf
                
            tfidf_str = " ".join(["%s:%.5f" % (k, v) for k, v in tfidf_dict.items()])
            print >> sys.stdout, tfidf_str
            #self.tfidf_list.append(tfidf_list)
            
        return 0

    
if __name__ == "__main__":
   model = Tfidf()
   model.load('../data/app_text_terms')
   model.calc_tfidf()

