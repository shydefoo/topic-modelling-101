import os
import gensim
import pickle
from multiprocessing import Pool

base_dir = os.path.dirname(os.path.realpath(__file__))
complete_processed_docs = os.path.join(base_dir, 'complete_processed_docs')
dic_complete_fn = os.path.join(base_dir,'dictionary.complete')
dictionary = gensim.corpora.Dictionary().load(dic_complete_fn)

filenames = 'abcdefghijklmno'

def build_bow_corpus(f):
	bow_corpus = []
	print("reading {}.pkl".format(f))
	fname = os.path.join(complete_processed_docs, '{}.pkl'.format(f))
	with open(fname, 'rb') as file:
		processed_docs = pickle.load(file)
	print("example length: {}".format(len(processed_docs[0])))
	#dictionary.add_documents(processed_docs)
	#dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
	bow_corpus += [dictionary.doc2bow(doc) for doc in processed_docs] # bow rep for each article
	print("{} completed".format(f))
	with open('bow_parts/bow_corpus_complete.{}.pkl'.format(f), 'wb') as bow_part:
		pickle.dump(bow_corpus, bow_part)
	print('bow {} saved'.format(f))


if __name__ == '__main__':
	with Pool(3) as p:
		p.map(build_bow_corpus, filenames)