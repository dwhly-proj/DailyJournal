import hypothesis_interface


from flask import Flask, request, render_template, redirect, url_for, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    return redirect(url_for('index'))


@app.route('/inbound_email', methods=['POST'])
def add_annotation():
    #annotation_text = request.form['annotation_text']
    #print annotation_text

    result = hypothesis_interface.create_annotation(os.environ['HYPOTHESIS_SECRET'], "Testing123")
    response = {
        'state': result.status_code,
        'text': "pass",
        'response': result.json()
    }
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)