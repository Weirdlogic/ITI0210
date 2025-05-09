# N-gram Text Generation with Markov Chains

## Project Overview

This project implements an N-gram text generation model using Markov Chains. The model can be trained on any text and used to generate new text sequences based on learned probabilities of word sequences. The model supports three types of tokenization:

* **Word-level Tokenization:** Words are treated as tokens.
* **Character-level Tokenization:** Each character is treated as a token.
* **Subword-level Tokenization:** Tokenizes text using the GPT-2 subword encoder (tiktoken).

## Training Text Used

The model was trained using the text of **"Harry Potter and the Half-Blood Prince"**. The text was converted from PDF to plain text using a Python script and preprocessed to ensure proper sentence and word tokenization.

## Example Sentences

### Word-Level Tokenization

* **Bigram Model:** "mundane realms of thin , at them , and star act"
* **Trigram Model:** "plum velvet that he could think of any way Malfoy ?"
* **Quadgram Model:** "figure ahead illuminated in the dancing firelight , but Snape had placed"

### Character-Level Tokenization

* **Bigram Model:** "H a r r y p o t t e r ."
* **Trigram Model:** "T h e r e   w a s   a"
* **Quadgram Model:** "S n a p e   s a i d   t h a t"

### Subword-Level Tokenization

* **Bigram Model:** "Har ry was not sure he"
* **Trigram Model:** "Dr aco was looking around"
* **Quadgram Model:** "The Dark Lord will rise"

## Techniques

* A custom sentence tokenizer using regular expressions.

## How to Use

1. Ensure the training text file ("harry-potter-and-the-half-blood-prince.txt") is in the same directory as the script.
2. Run the script using:

```bash
python N-gram.py
```

3. The script will generate and display example texts using the bigram, trigram, and quadgram models.

