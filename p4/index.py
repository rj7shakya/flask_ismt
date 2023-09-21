from flask import Flask ,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',name="rajad")

@app.route('/add',methods=['POST','GET'])
def add():
    if request.method == 'POST':
        print(request.form['username'],request.form['rollno'])
        return render_template('home.html')

    else:
        return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
