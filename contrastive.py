# Install PyTorch
! pip install torch==1.7.1+cu110 -f https://download.pytorch.org/whl/torch_stable.html
# clone the repo
!git clone https://github.com/princeton-nlp/SimCSE
# install the requirements
! pip install -r /content/SimCSE/requirements.txt

# imports
import torch
from scipy.spatial.distance import cosine
from transformers import AutoModel, AutoTokenizer

# Import the pretrained models and tokenizer, this will also download and import th
tokenizer = AutoTokenizer.from_pretrained("princeton-nlp/sup-simcse-bert-base-uncased")
model = AutoModel.from_pretrained("princeton-nlp/sup-simcse-bert-base-uncased")

# input sentence
texts = [
	"I am writing an article",
	"Writing an article on Machine learning",
	"I am not writing.",
	"the article on machine learning is already written"
]

# tokenize the input
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# generate the embeddings
with torch.no_grad():
	embeddings = model(**inputs, output_hidden_states=True,
					return_dict=True).pooler_output
# the shape of embedding (# input, 768)
embeddings.shape

# print cosine similarity b/w the sentences
for i in range(len(texts)):
for j in range(len(texts)):
	if (i != j):
	cosine_sim = 1 - cosine(embeddings[i], embeddings[j])
	print("Cosine similarity between \"%s\" and \"%s\" is: %.3f" % (texts[i], texts[j], cosine_sim))
