#!/usr/bin/env python
# coding=gbk
# author=hechengwei
# date=2016-09-27

import sys
import math


def tfidf_feature(filename, min_tf=1, delimiter=' '):
    """
    brief: ����һ���ı������дʵ�����TF-IDF����
    filename: �ı�ÿһ����һƪ�ĵ����д�
    min_tf: ֻ�����Ƶ��С��min_tf�Ĵʣ�С��min_tf�Ĺ��˵�
    delimiter: �дʷָ���
    """
    term_freq_dict = {}
    term_total_num = 0
    term_doc_freq_dict = {}
    doc_index = 0
    # read file and statistic
    with open(filename) as fr:
        for line in fr:
            doc_index += 1
            term_list = line.strip().split(delimiter)
            for term in term_list:
                term_freq_dict.setdefault(term, 0)
                term_freq_dict[term] += 1
                term_total_num += 1
                term_doc_freq_dict.setdefault(term, set())
                term_doc_freq_dict[term].add(doc_index)
    
    # min_tf filter
    term_freq_list = [(term, freq) for term, freq in term_freq_dict.iteritems() if freq >= min_tf]
    term_total_num = sum([freq for term, freq in term_freq_list])
    
    # calculate
    term_tfidf_dict = {}
    for term, freq in term_freq_list:
        tf = freq * 1.0 / term_total_num
        term_doc_num = len(term_doc_freq_dict[term])
        idf = math.log(doc_index * 1.0 / term_doc_num)
        tfidf =  math.sqrt(tf) * math.pow(idf, 1.5) # Ȩ�ص�����tf*idf���������
        term_tfidf_dict[term] = tfidf

    # output
    term_tfidf_list = sorted(term_tfidf_dict.iteritems(), key=lambda d:d[1], reverse=True)
    for term, tfidf in term_tfidf_list:
        freq = term_freq_dict[term]
        doc_freq = len(term_doc_freq_dict[term])
        print >> sys.stdout, "%s\t%s\t%s\t%s" % (term, freq, doc_freq, tfidf)

    print >> sys.stderr, "term_num: %s\ndoc_num: %s" % (term_total_num, doc_index)

    return 0
        
if __name__ == "__main__":
    filename = sys.argv[1] # input filename: ../data/app_text_terms
    tfidf_feature(filename, min_tf=1)
    
