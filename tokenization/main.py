import argparse
from tokenizers import SimpleTokenizerV1

with open("datasets/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

tokenizer = SimpleTokenizerV1(raw_text)

text = "He laughed and pushed me!"
ids = tokenizer.encode(text)
print(ids)

text = tokenizer.decode(ids)
print(text)