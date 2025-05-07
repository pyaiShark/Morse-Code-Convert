# Morse Conversion Web Application Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Project Overview
The **Morse Conversion Web Application** is a web-based tool that allows users to convert text to Morse code and vice versa. Users can upload `.txt` files, register for personalized experiences, and maintain a history of their conversions. The application also includes a 'Forgot Password' feature for account recovery and an 'About Morse' section for educational resources.

## Features
- **Text to Morse Code Conversion**: Upload a `.txt` file containing plain text, and the application will convert it to Morse code.
- **Morse Code to Text Conversion**: Upload a `.txt` file containing Morse code, and the application will convert it back to plain text.
- **File History**: Users can access their conversion history and download previously converted files.
- **Password Recovery**: A "Forgot Password" feature allows users to reset their passwords securely.
- **Educational Resources**: Learn about Morse code's history and usage through the 'About Morse' section.

## Installation
Follow these steps to install and set up the Morse Conversion Web Application:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pyaiShark/Morse-Code-Convert.git
   cd morse_conversion_web_app
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Ensure that the `database.db` file is created and properly configured. You may need to run initial setup scripts if provided.

5. **Run the Application**:
   ```bash
   gunicorm app:app
   ```

6. **Access the Application**:
   - Open your web browser and navigate to `http://127.0.0.1:5000` to access the Morse Conversion Web Application.

## Usage
1. **Register**: Create a new account by providing a valid email, username, password, and security key.
2. **Login**: Access your account using your username or email and password.
3. **Convert Files**: Upload a `.txt` file to convert its contents to Morse code or vice versa.
4. **View History**: Check your conversion history and download any previously converted files.

## File Structure
```
morse_conversion_web_app/
├── src/
   │
   ├── static/                     # Contains static files
   │   ├── form_script.js          # JavaScript for form-related scripts
   │   ├── form_styles.css         # CSS for form-related styles
   │   ├── icon.png                # Image file for the website icon
   │   ├── navbar_script.js        # JavaScript for navigation bar scripts
   │   ├── script.js               # JavaScript for handling file download
   │   ├── style.css               # Main CSS file
   │   └── type-script.js          # JavaScript for handling conversion type
   │
   ├── templates/                  # Contains HTML templates
   │   ├── apology.html            # Apology page
   │   ├── forgot.html             # Forgot password form
   │   ├── history.html            # History page
   │   ├── index.html              # Main index page
   │   ├── layout.html             # Layout of the pages
   │   ├── login.html              # Login form
   │   └── register.html           # Registration form
   │
   ├── app.py                      # Main Flask application file
   ├── converter.py                # Data conversion logic (Morse, text)
   ├── database.db                 # Database file
   ├── helpers.py                  # Helper functions for error handling
   └── requirements.txt            # Project requirements
```

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please contact:
- **Goutam Mandal**: [goutammandal01203@gmail.com](mailto:your.email@example.com)
