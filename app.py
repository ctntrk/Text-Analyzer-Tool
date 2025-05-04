from flask import Flask, jsonify, request
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def count_sentences(text: str) -> int:
    sentences = re.split(r'[.!?]+[\s\n]*', text)
    return len([s for s in sentences if s.strip()])

def count_paragraphs(text: str) -> int:
    paragraphs = re.split(r'\n\s*\n', text)
    return len([p for p in paragraphs if p.strip()])

@app.route('/count', methods=['POST'])
def count_text_stats():
    data = request.get_json()
    raw_text = data.get('text', '')
    stripped_text = raw_text.strip()  # Trim whitespace
    
    if not stripped_text:
        return jsonify({
            "characters": 0,
            "words": 0,
            "sentences": 0,
            "unique_words": 0,
            "paragraphs": 0
        })
    
    words = raw_text.split()
    unique_words = len(set(words)) if words else 0
    
    return jsonify({
        "characters": len(raw_text),
        "words": len(words),
        "sentences": count_sentences(raw_text),
        "unique_words": unique_words,
        "paragraphs": count_paragraphs(raw_text)
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
