from flask import Flask, request, render_template
import reco_model

app = Flask(__name__, static_url_path='/static')

@app.route('/main', methods=['GET', 'POST'])
def main(sent=None):
    try:
        if request.method == 'GET':
            return render_template('main.html', sent=sent)
        elif request.method == 'POST':
            sent = request.form['sent']
            if sent == '':
                return render_template('main.html', sent=None)
            reco1, reco2, reco3 = reco_model.recommand(sent)
            return render_template('main.html', sent=sent, reco1=reco1, reco2=reco2, reco3=reco3)
    except:
        return render_template('main.html', sent=None)

@app.route('/', methods=['GET'])
def index(sent=None):
    return "인사말 도우미 입니다!"

if __name__ == '__main__':
    app.run(debug=True)