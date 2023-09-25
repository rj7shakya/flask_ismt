from flask import Flask ,render_template,request

import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="university",
    user='rajad', password='rajad', host='localhost', port= '5432'
)
cursor = conn.cursor()
cursor.execute('''SELECT * from college''')

result = cursor.fetchall();
print(result)

conn.close()

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
