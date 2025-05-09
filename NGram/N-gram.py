import random
from collections import defaultdict, Counter
import tiktoken
import os
import re

EOS = "<EOS>"

# Custom Sentence Tokenizer and Word Tokenizer (No NLTK)
def tokenize_text(text):
    tokens = []
    sentences = re.split(r'[.!?]\s+', text)
    for sentence in sentences:
        words = re.findall(r"\w+|[.,!?;]", sentence)
        if words:  # Only add if sentence is not empty
            tokens.extend(words)
            tokens.append(EOS)
    return tokens

# Character-level tokenization
def tokenize_char(text):
    return list(text)

# Subword-level tokenization
def tokenize_subword(text):
    enc = tiktoken.get_encoding("gpt2")
    return enc.encode(text)

# Build N-Gram Model
class NGramModel:
    def __init__(self, n=2):
        self.n = n
        self.ngrams = defaultdict(lambda: Counter())

    def train(self, tokens):
        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i + self.n - 1])
            next_token = tokens[i + self.n - 1]
            self.ngrams[context][next_token] += 1

    def generate_text(self, max_words=50):
        # Start with a random context from the model
        context = random.choice(list(self.ngrams.keys())) if self.ngrams else (EOS,)
        result = list(context)

        for _ in range(max_words):
            next_token = self.sample_next(context)
            if next_token == EOS:
                break
            result.append(next_token)
            context = tuple(result[-(self.n - 1):])

        return " ".join(result)

    def sample_next(self, context):
        for i in range(len(context), 0, -1):
            short_context = context[-i:]
            if short_context in self.ngrams:
                next_tokens = list(self.ngrams[short_context].elements())
                return random.choice(next_tokens)
        return EOS

# Main function for testing
if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "harry-potter-and-the-half-blood-prince-j.k.-rowling.txt")

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        exit(1)

    with open(file_path, encoding="utf-8") as f:
        text = f.read()

    tokens = tokenize_text(text)
    print(f"Loaded {len(tokens)} tokens.")

    # Training trigram and quadgram models
    bigram_model = NGramModel(n=2)
    trigram_model = NGramModel(n=3)
    quadgram_model = NGramModel(n=4)

    bigram_model.train(tokens)
    trigram_model.train(tokens)
    quadgram_model.train(tokens)

    print("Generated Text (Bigram Model):")
    print(bigram_model.generate_text(max_words=100))

    print("Generated Text (Trigram Model):")
    print(trigram_model.generate_text(max_words=100))

    print("Generated Text (Quadgram Model):")
    print(quadgram_model.generate_text(max_words=100))