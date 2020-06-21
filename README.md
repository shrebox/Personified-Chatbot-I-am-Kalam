<!---Readme for @ https://github.com/shrebox/I-am-Kalam--->

![alt text](https://github.com/shrebox/Personified-Chatbot-I-am-Kalam/blob/master/Poster-1.jpg)

# *'I am Kalam'* - Reliving Kalam’s Words

Analyzing answer pattern of APJ Abdul Kalam and responding to a query following his answering pattern. We are applying RNNs to generate answers to user queries. 

**Dataset**: Dataset has been scrapped from interviews available on various websites form the google search results.<br/>
**Files**: dataset/ directory containes different extracted data forms.<br/>
**Code**: code/ directory contains codes from IR-IE model, seq2seq model, preprocessing and evaluation.

<h2>IR-IE model</h2> <br>
	To run: 

	$ python sen2vec_my.py

	** sent2vec library needs to be installed from https://github.com/epfml/sent2vec.<br>
	** pre trained model <a href='https://drive.google.com/file/d/0B6VhzidiLvjSOWdGM0tOX1lUNEk/view'>torontobooks_unigrams.bin</a> need to be downloaded and kept in same directory.

<h2>seq2seq model</h2> <br>
	TO run: 

	$ python main.py 
	
	to train the system and save the model named as model.npz.<br>
	Set inference_mode=1 for testing purpose and run python main.py.

<h2>References</h2> <br />
- https://github.com/facebookarchive/NAMAS <br />
- https://github.com/zwc12/Summarization <br />
- https://datascience.stackexchange.com/questions/23969/sentence-similarity-prediction <br />
- https://rare-technologies.com/doc2vec-tutorial/ <br />
- http://nlp.town/blog/sentence-similarity/ <br />
- https://radimrehurek.com/gensim/models/keyedvectors.html <br />
- https://machinelearningmastery.com/develop-word-embeddings-python-gensim/ <br />
- https://github.com/epfml/sent2vec <br />
- https://pdfs.semanticscholar.org/ffbb/1d120c3c2881431933c6f928b851824913c4.pdf?_ga=2.35884901.416918627.1538253292-1431390683.1533485502<br />
- https://arxiv.org/pdf/1603.06155.pdf <br />
- https://people.cs.umass.edu/~ashutoshchou/persona_chatbot_report.pdf <br />
- https://github.com/ashutosh-choudhary/conversational_agent_personified<br />
- https://towardsdatascience.com/personality-for-your-chatbot-with-recurrent-neural-networks-2038f7f34636<br />
- https://github.com/manumathewthomas/Chat-with-Joey<br />
- https://github.com/inikdom/neural-chatbot<br />
- https://github.com/tensorlayer/seq2seq-chatbot <br>
- https://github.com/epfml/sent2vec
- http://adventuresinmachinelearning.com/keras-lstm-tutorial/

Tada! (:) :v::alien:
