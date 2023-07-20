import nltk
from nltk.metrics import edit_distance
from nltk.corpus import words

nltk.download("words")

# Load the English vocabulary from NLTK
english_vocab = set(words.words())

def autocorrect(word):
    # Function to find the closest word from the vocabulary
    # based on the edit distance
    candidates = []
    for vocab_word in english_vocab:
        distance = edit_distance(word, vocab_word)
        if distance <= 2:  # Consider words within edit distance of 2
            candidates.append((vocab_word, distance))
    if candidates:
        # Sort by edit distance, then choose the word with the smallest distance
        closest_word = sorted(candidates, key=lambda x: x[1])[0][0]
        return closest_word
    else:
        return word  # Return the original word if no candidate found

def autocorrect_text(text):
    # Function to correct each word in the input text
    corrected_words = [autocorrect(word) for word in text.split()]
    return " ".join(corrected_words)




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    # Retrieve the input data from the HTML form
    inc_para = request.form['incorrect_para']
    

    
    corrected_para=autocorrect_text(inc_para)
    return f"Corrected word, {corrected_para}"

if __name__ == "__main__":
    app.run(debug=True)
