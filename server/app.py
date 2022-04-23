#from crypt import methods
from flask import Flask, request, render_template
import model

app = Flask(__name__, static_url_path='/static')

@app.route('/main', methods=['GET', 'POST'])
def main(sent=None):
    if request.method == 'GET':
        return render_template('main.html', sent=sent)
    elif request.method == 'POST':
        sent = request.form['sent']
        print('==============')
        print(sent)
        print('==============')
        reco = model.recommand(sent)
        return render_template('main.html', sent=sent, reco=reco)

if __name__ == '__main__':
    app.run(debug=True)