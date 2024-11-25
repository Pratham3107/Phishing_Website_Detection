from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_phishing', methods=['POST'])
def detect_phishing():
    data = request.json
    url = data.get('url', '')
    result = {
        'url': url,
        'is_phishing': is_phishing(url)  # Implement your phishing detection logic here
    }
    return jsonify(result)

def is_phishing(url):
    """Example phishing detection logic."""
    # Implement your actual phishing detection logic here
    return "example.com" in url

if __name__ == '__main__':
    app.run(debug=True)
