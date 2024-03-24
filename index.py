from flask import Flask, request, render_template
app = Flask(__name__)

def cifrar_a1z27_espanol(mensaje):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    mensaje_cifrado = ''
    for letra in mensaje.lower():
        if letra in alfabeto:
            indice = alfabeto.index(letra) + 1
            mensaje_cifrado += str(indice) + ' '
    return mensaje_cifrado.strip()

def descifrar_a1z27_espanol(mensaje_cifrado):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    mensaje = ''
    for numero in mensaje_cifrado.split():
        if numero.isdigit():
            letra = alfabeto[int(numero) - 1]
            mensaje += letra
    return mensaje

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mensaje = request.form.get('mensaje')
        accion = request.form.get('accion')
        if accion == 'cifrar':
            resultado = cifrar_a1z27_espanol(mensaje)
        elif accion == 'descifrar':
            resultado = descifrar_a1z27_espanol(mensaje)
        return render_template('index.html', resultado=resultado)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
