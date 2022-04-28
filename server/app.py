from flask import Flask, request, render_template
import model

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
            reco1, reco2, reco3 = model.recommand(sent)
            return render_template('main.html', sent=sent, reco1=reco1, reco2=reco2, reco3=reco3)
    except:
        return render_template('main.html', sent=None)
if __name__ == '__main__':
    app.run(debug=True)