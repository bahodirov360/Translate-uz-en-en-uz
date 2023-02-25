from flask import *
from model import *
from pytarjimon import *
import os
from playsound import playsound

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")
    
@app.route('/eng-uz', methods=['GET', 'POST'])
def enguz():
    if request.method == 'POST':
        prompt = request.form['sura']
        os.system(f'edge-tts -v uz-UZ-MadinaNeural -t "{prompt}" --write-media static/salom.mp3')
        tar = tarjima(prompt, "uz")
        os.system(f'edge-tts -v en-US-AriaNeural -t "{tar}" --write-media static/hello.mp3')
        return render_template("tar.html", tar=tar, prompt=prompt)
    else:
        enggg = Enuz.select()
        return render_template("input.html", enggg=enggg)

@app.route('/uz-eng', methods=['GET', 'POST'])
def uzeng():
    if request.method == 'POST':
        salom = request.form['surama']
        os.system(f'edge-tts -v uz-UZ-MadinaNeural -t "{salom}" --write-media static/salom.mp3')
        tarj = tarjima(salom, "en")
        os.system(f'edge-tts -v en-US-AriaNeural -t "{tarj}" --write-media static/hello.mp3')
        # playsound("hello.mp3")
        return render_template("tarj.html", tarj=tarj, salom=salom)
    else:
        uzzz = Uzen.select()
        return render_template("innput.html", uzzz=uzzz)

@app.route("/<string:music>")
def ret(music):
    return redirect(url_for("static", filename=f"{music}"))

app.run(debug=True)