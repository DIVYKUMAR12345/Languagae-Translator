from flask import Flask, request, jsonify , render_template 
from translate import Translator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("translate.html")

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    source_lang = data['source_lang']
    target_lang = data['target_lang']

    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translated_text = translator.translate(text)

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)