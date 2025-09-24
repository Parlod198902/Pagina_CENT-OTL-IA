from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración SMTP para Gmail (contraseña de aplicación incluida)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'oficialcenteotl@gmail.com'
app.config['MAIL_PASSWORD'] = 'jdjg djfm qhqu ptvy'  # <-- Tu contraseña de aplicación
app.config['MAIL_DEFAULT_SENDER'] = 'oficialcenteotl@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    asunto = request.form.get('asunto')
    mensaje = request.form.get('mensaje')
    try:
        msg = Message(
            subject=f"Contacto desde Centéotl IA: {asunto}",
            recipients=['oficialcenteotl@gmail.com'],
            body=f"Nombre: {nombre}\nEmail: {email}\nAsunto: {asunto}\nMensaje:\n{mensaje}"
        )
        mail.send(msg)
        return jsonify({'success': True})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)