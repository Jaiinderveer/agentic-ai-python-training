from flask import Flask, request, jsonify, render_template

# create a directory in the root of project folder -> templates

# create flask app
app = Flask('MyApp')

@app.route('/') # applications root
def home(): 
   return render_template('index.html', name='Task Delegation Agent')


if __name__ == '__main__':
    app.run(debug=True)