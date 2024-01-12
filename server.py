from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hi():
   return render_template('index.html')

@app.route('/play')
def index():
    return render_template('play1.html')

@app.route('/play/<number>')
def more_boxes(number):
    more = int(number)
    return render_template('play2.html', more=more)

@app.route('/play/<number>/<color>')
def change_color(number, color):
    more=(int(number))
    switchColor=color
    return render_template('play3.html', more=more, switchColor=switchColor)


if __name__=="__main__":
    app.run(debug=True)