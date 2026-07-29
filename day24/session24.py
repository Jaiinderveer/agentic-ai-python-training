# FAST API in Python
# FLASK to develop API in python
# enterprise grade -> Django
from flask import Flask,request,jsonify

app = Flask('MyApp')

@app.route('/') # application root
def home():
    html_text = """
        <html>
        <body>
        <center>
            <h1>Hello</h1>
        </center>
        </body>
        </html>
        """
    return html_text
@app.route('/about') 
def about():
    # returned over the web (http return -> plain text)
    return 'Welcome to about section'
@app.route('/contact') 
def contact():
    # returned over the web (http return -> plain text)
    return 'contact me at john@example.com'
@app.route('/hello/<name>') 
def hello(name):
    # returned over the web (http return -> plain text)
    return f"Hello {name}"
@app.route('/search')
def search():
    keyword = request.args.get('q')
    city = request.args.get('q') 
    return f"You searched for {keyword} and {city}"
@app.route('/weather')
def weather():
    weather_details = {
        'city':'ludhiana',
        'temp': '24 degree celcius',
        'rain':75
    }
    return jsonify(weather_details)
if __name__ == '__main__':
    # execution of flask app
    app.run(debug=True)