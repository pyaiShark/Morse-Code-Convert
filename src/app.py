import os
from cs50 import SQL
from flask import Flask, request, render_template, send_file, jsonify, redirect, session, flash, send_from_directory
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from email_validator import validate_email, EmailNotValidError

from src.helpers import apology, login_required, filename
from src.converter import text_to_morse, morse_to_text


app = Flask(__name__)
app.secret_key = "sfdhk23498#$%#$GERT%$^3459safjhj23"

# Custom filter
app.jinja_env.filters["filename"] = filename

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

TYPE = "text"


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    if 'value' not in data:
        return jsonify({"status": "error", "message": "Missing 'value' key"}), 400

    value = data.get('value')
    global TYPE
    TYPE = value
    return jsonify({"status": "ok", "value": value})


@app.route('/convert', methods=['POST'])
def convert():

    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    text = str(file.read().decode('utf-8'))

    if TYPE == 'text':
        converted_text = text_to_morse(text)

    elif TYPE == 'morse':
        converted_text = morse_to_text(text)

    else:
        return "Invalid value"  # Update this with HTML error message

    # Save the converted text to a file
    if not os.path.exists("converted_files"):
        os.makedirs("converted_files")

    if TYPE == "text":
        if not os.path.exists("converted_files/text"):
            os.makedirs("converted_files/text")
        file_path = os.path.join("converted_files/text", file.filename)
        if "user_id" in session:
            if session["user_id"]:
                try:
                    db.execute("""
                                UPDATE users_history
                                SET total_morse_conversion = total_morse_conversion + 1, history_count = history_count  + 1
                                WHERE user_id = ?
                                """, session["user_id"])
                except Exception:
                    pass
                try:
                    db.execute(
                        "INSERT INTO users_history (user_id, morse_file_url) VALUES(?, ?)", session["user_id"], file_path)
                except Exception:
                    pass

    else:
        if not os.path.exists("converted_files/morse"):
            os.makedirs("converted_files/morse")
        file_path = os.path.join("converted_files/morse", file.filename)
        if "user_id" in session:
            if session["user_id"]:
                try:
                    db.execute("""
                                UPDATE users_history
                                SET total_text_conversion = total_text_conversion + 1, history_count = history_count  + 1
                                WHERE user_id = ?;
                                """, session["user_id"])
                except Exception:
                    pass
                try:
                    db.execute("INSERT INTO users_history (user_id, text_file_url) VALUES(?, ?)",
                               session["user_id"], file_path)
                except Exception:
                    pass

    try:
        with open(file_path, "w") as out_file:
            out_file.write(converted_text)
    except Exception as e:
        print(f"An error occurred: {e}")  # Update this with HTML error message

    # Return a JSON response with the download URL and original file name
    return jsonify({
        'originalFileName': file.filename,
        'downloadUrl': f'/download/{file_path}'  # Create a download URL
    })


@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    return send_file(filename, as_attachment=True)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure email was submitted
        if not request.form.get("email"):
            return apology("must provide email", 400)
        try:
            validate_email(request.form.get("email"))
        except EmailNotValidError as e:
            # Email is not valid.
            return apology("must provide valid email", 400)

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        if len(request.form.get("username")) < 6:
            return apology("username is too short", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        if len(request.form.get("password")) < 8:
            return apology("password is too short", 400)

        # Ensure security key was submitted
        if not request.form.get("security_key"):
            return apology("must provide security key", 400)

        if len(request.form.get("security_key")) < 8:
            return apology("security key is too short", 400)

        # Ensure that the password confirmation is the same
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("password don't match", 400)

        # Generating password hash
        password = generate_password_hash(request.form.get("password"))
        email = request.form.get("email")
        username = request.form.get("username")
        security_key = generate_password_hash(request.form.get("security_key"))

        # Check if user is already exist
        try:
            db.execute("INSERT INTO users (email, username, password, security_key) VALUES(?, ?, ?, ?)",
                       email, username, password, security_key)
        except Exception as e:
            return apology("username already taken or you have already registered. please log in.", 401)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Remember which user has Register
        session["user_id"] = rows[0]["id"]

        # Alert the user about successful registration
        flash('You were successfully registered')

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        is_email = True
        # Ensure username or email was submitted
        if not request.form.get("usernameOrEmail"):
            return apology("must provide usernameOrEmail", 400)

        try:
            validate_email(request.form.get("usernameOrEmail").rstrip())
        except EmailNotValidError as e:
            # Email is not valid.
            is_email = False

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        email = request.form.get("usernameOrEmail")

        if is_email:
            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE email = ?", email)
        else:
            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?",
                              email)  # email is username or email

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Alert the user about successful registration
        flash('You were successfully logged in')

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/forgot", methods=["GET", "POST"])
def forgot():
    """Forgot password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        is_email = True
        # Ensure username or email was submitted
        if not request.form.get("usernameOrEmail"):
            return apology("must provide usernameOrEmail", 400)

        try:
            validate_email(request.form.get("usernameOrEmail").rstrip())
        except EmailNotValidError as e:
            # Email is not valid.
            is_email = False

        # Ensure password was submitted
        if not request.form.get("security_key"):
            return apology("must provide security key", 403)

        if not request.form.get("password"):
            return apology("must provide password", 400)

        if len(request.form.get("password")) < 8:
            return apology("password is too short", 400)

        # Ensure that the password confirmation is the same
        if not request.form.get("password") == request.form.get("confirmation"):
            return apology("password don't match", 400)

        email = request.form.get("usernameOrEmail")

        if is_email:
            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE email = ?", email)
        else:
            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?",
                              email)  # email is username or email

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["security_key"], request.form.get("security_key")
        ):
            return apology("invalid username and/or security key", 450)

        # Generating password hash
        password = generate_password_hash(request.form.get("password"))

        # update password
        db.execute("UPDATE users SET password = ? WHERE id = ?", password, rows[0]["id"])

        # Alert the user about successful password reset
        flash('Your password was forgotten successfully')

        # Redirect user to login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("forgot.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Alert the user about logout
    flash('Your are loged out')

    # Redirect user to home page
    return redirect("/")


FILES_DIRECTORY = os.path.join(app.root_path, 'converted_files', 'text')


@app.route("/history")
@login_required
def history():
    historys = db.execute("""SELECT *
                         FROM users_history
                         WHERE user_id = ?
                        """, session["user_id"])

    return render_template("history.html", historys=historys)


@app.route('/download/<path:filename>')
@login_required
def download_file(filename):
    return send_from_directory(FILES_DIRECTORY, filename)