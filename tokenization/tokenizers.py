import re

class SimpleTokenizerV1:
    def __init__(self, vocab_raw_text):
        vocab = self.create_unique_tokens_using_vocab(vocab_raw_text)
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def create_unique_tokens_using_vocab(self, vocab_raw_text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', vocab_raw_text) # Splits words into an array
        preprocessed = [item.strip() for item in preprocessed if item.strip()] # Removes leading and trailing white spaces
        all_words = sorted(set(preprocessed)) # Create a unique set of vocabulary
        vocab = {token:integer for integer,token in enumerate(all_words)} # Make vocabulary into dictionary

        return vocab

    
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
                                
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]

        try:
            ids = [self.str_to_int[s] for s in preprocessed]
        except KeyError as e:
            raise KeyError(f"The word {e} is not tokenized.")
        
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text) # Replace spaces before the specified punctuations
        return text