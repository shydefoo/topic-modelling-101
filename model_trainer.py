import gensim
import os
from gensim.models import LdaMulticore
import pickle


base_dir = os.path.dirname(os.path.realpath(__file__))
dictionary_fn = os.path.join(base_dir, 'dictionary.complete')
bow_parts = os.path.join(base_dir, 'bow_parts')
fn_prefix = 'bow_corpus_complete'
postfix = 'abcdefghijklmno'
def build_bow_corpus():
	bow_corpus = []

	def _extract_bow_part(postfix):
		for letter in postfix:
			fname = '{}.{}.pkl'.format(fn_prefix, letter)
			with open(fname, 'rb') as file:
				bow_part = pickle.load(file)
			yield bow_part
	for bow_part in _extract_Bow_part(postfix):
		bow_corpus += bow_part

	return bow_corpus

dictionary = gensim.corpora.Dictionary().load(dictionary_fn)
lda_model = LdaMulticore(bow_corpus, num_topics=300, id2word=dictionary, passes=2, workers=8)
lda_model.save('lda_complete.model')