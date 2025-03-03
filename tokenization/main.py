import argparse
from tokenizers import SimpleTokenizerV1

with open("datasets/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

tokenizer = SimpleTokenizerV1(raw_text)

text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)

text = tokenizer.decode(ids)
print(text)