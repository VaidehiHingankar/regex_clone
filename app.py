from flask import Flask ,request , render_template
import re

app =Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/',methods=['POST'])
def match_regex():
    username = request.form['username']
    password = request.form['password']

    matches =re.findall(password,username)

    return render_template('result.html',matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
