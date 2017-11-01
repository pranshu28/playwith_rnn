import numpy as np 
import sys
from sklearn.manifold import TSNE

inp = "rohan.txt"#sys.argv[1]
outFile = "temp.txt"#sys.argv[2]

with open(inp) as f:
	content = f.read().split(" ")

vocab = sorted(list(set(content)))
vocab_indices = [c for i, c in enumerate(vocab)]

print TSNE(n_components=2).fit(vocab_indices)