import gensim
import os
from gensim.models import LdaMulticore
import pickle


base_dir = os.path.dirname(os.path.realpath(__file__))
dictionary_fn = os.path.join(base_dir, 'dictionary.complete')
bow_parts = os.path.join(base_dir, 'bow_parts')

dictionary = gensim.corpora.Dictionary().load(dictionary_fn)
fn_prefix = 'bow_corpus_complete'
postfix = 'abcdefghijklmno'
lda_model = LdaMulticore(num_topics=250, id2word=dictionary, passes=2, workers=3)


def build_and_train_lda_model(lda_model, fn_prefix, postfix):
	bow_corpus = []
	print("building corpus")
	def _extract_bow_part(postfix, fn_prefix):
		for letter in postfix:
			print("extracting {}".format(letter))
			fname = os.path.join(bow_parts, '{}.{}.pkl'.format(fn_prefix, letter))
			with open(fname, 'rb') as file:
				bow_part = pickle.load(file)
			yield bow_part

	for bow_part in _extract_bow_part(postfix, fn_prefix):
		print("updating lda model")
		lda_model.update(bow_part)
	print("model training complete")


print("training model")
build_and_train_lda_model(lda_model, fn_prefix, postfix)
lda_model.save('model_complete/lda_complete.model')
print("lda model trained and saved")