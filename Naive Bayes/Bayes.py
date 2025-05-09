import csv
import json
import math
from collections import defaultdict, Counter

# Function to preprocess text
def preprocess_text(text):
    words = [w.lower() for w in text.split() if len(w) > 3]
    return words

# Step 1: Load and preprocess training data
train_file = "bbc_train.csv"
class_word_counts = defaultdict(Counter)
class_counts = defaultdict(int)

with open(train_file, encoding="utf-8") as f:
    reader = csv.reader(f)
    for topic, text in reader:
        words = preprocess_text(text)
        class_counts[topic] += 1
        class_word_counts[topic].update(words)

# Calculate total articles and unique words
total_articles = sum(class_counts.values())
vocab = set()
for topic, word_count in class_word_counts.items():
    vocab.update(word_count.keys())

vocab_size = len(vocab)

# Step 2: Calculate probabilities
class_probs = {c: count / total_articles for c, count in class_counts.items()}

# Calculate word probabilities with Laplace smoothing
word_probs = {}
for topic, word_count in class_word_counts.items():
    total_words = sum(word_count.values())
    word_probs[topic] = {word: (count + 1) / (total_words + vocab_size) for word, count in word_count.items()}

# Save trained model
model_data = {
    "class_probs": class_probs,
    "word_probs": word_probs,
    "vocab_size": vocab_size,
    "class_counts": class_counts,
}

with open("nb_model.json", "w") as f:
    json.dump(model_data, f)

print("Training complete. Model saved as nb_model.json.")

# Step 3: Load model and classify test data
def classify_article(text, model):
    words = preprocess_text(text)
    class_scores = {}

    for topic in model["class_probs"]:
        log_prob = math.log(model["class_probs"][topic])
        for word in words:
            word_prob = model["word_probs"].get(topic, {}).get(word, 1 / (sum(model["class_counts"].values()) + model["vocab_size"]))
            log_prob += math.log(word_prob)
        class_scores[topic] = log_prob

    return max(class_scores, key=class_scores.get)

# Step 4: Evaluate model
test_file = "bbc_test.csv"
correct = 0
total = 0

with open("nb_model.json") as f:
    model = json.load(f)

with open(test_file, encoding="utf-8") as f:
    reader = csv.reader(f)
    for topic, text in reader:
        predicted = classify_article(text, model)
        if predicted == topic:
            correct += 1
        total += 1

accuracy = correct / total * 100
print(f"Model accuracy: {accuracy:.2f}%")
