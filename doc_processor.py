import os
import pandas as pd
import gensim
import nltk
import pickle

from gensim.utils import simple_preprocess 
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
from multiprocessing import Pool
from datetime import datetime
np.random.seed(2018)
stemmer = PorterStemmer()


desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
large_file = os.path.join(desktop, 'large_file')
processed_wiki_sub = os.path.join(large_file, 'processed_wiki_sub')
postfix = 'abcdefghijklmno'
text_path_prefix = os.path.join(processed_wiki_sub, 'processed_wiki.texta')

def preprocess_doc(letter):
    text_path = text_path_prefix+letter
    with open(text_path, 'r') as file:
        text = file.read()
    line = text.split('\n')
    df = pd.DataFrame(line, columns = ['article'])
    print("adding articles from {}".format(text_path))
    
    def _preprocess(text):
        result = []
        # convert document into list of lowercase tokens, filter based on token length
        for token in simple_preprocess(text):
            if token not in STOPWORDS and len(token) > 3:
                result.append(token)
        return result

    processed_docs = df['article'].map(_preprocess)
    print("wiki subpart added {}~".format(letter))
    
    with open('complete_processed_docs/{}.pkl'.format(letter), 'wb') as file:
        pickle.dump(processed_docs, file)

    print("{}.pkl pickled".format(letter))


if __name__ == '__main__':
    with Pool(2) as p:
        p.map(preprocess_doc,postfix)