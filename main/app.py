from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def get_efemeride():
    # Puedes implementar la lógica para obtener efemérides basadas en la fecha actual aquí
    # Este es solo un ejemplo de efeméride ficticia
    return "Efeméride especial hoy!"

@app.route('/')
def index():
    now = datetime.now()

    # Formatear fecha como "DD/MM/YYYY"
    date = now.strftime("%d/%m/%Y")

    # Formatear hora como "HH:MM:SS"
    time = now.strftime("%H:%M:%S")

    # Obtener efeméride
    event = get_efemeride()

    return render_template('index.html', date=date, time=time, event=event)

if __name__ == '__main__':
    app.run(debug=True)
