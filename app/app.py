from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ruta para la UI (Selenium la probará)
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def home():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'admin123':
        return "<h1 id='welcome-msg'>Bienvenido al Dashboard QA</h1>"
    else:
        return "<h3 id='error-msg'>Credenciales Invalidas</h3>"

# Ruta para la API (Postman/Requests la probará)
@app.route('/api/status', methods=['GET'])
def api_status():
    return jsonify({"status": "active", "version": "1.0.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)