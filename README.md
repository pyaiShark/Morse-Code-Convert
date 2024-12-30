## MY PROJECT TITLE
Morse Code Converter Web Application

#### Description:
This project is a Morse Code Converter Web Application that allows users to upload a .txt file and convert its text content to Morse code and vice versa. The application features user registration and login, providing a personalized experience for each user. Additionally, it maintains a history of conversions, enabling users to easily access and download any previously converted files.

To enhance user experience, the application includes a 'Forgot Password' feature that allows users to recover their accounts using a security key, ensuring that they can easily regain access if they forget their login credentials. This feature adds an extra layer of security and convenience for users.

Users can also deepen their understanding of Morse code by clicking on the 'About Morse' section, which provides educational resources and insights about Morse code's history and usage. This section is designed to engage users and promote learning, making the application not just a conversion tool but also an educational platform.

The application is built with a focus on usability and accessibility, ensuring that both novice and experienced users can navigate the interface with ease. With its robust features and user-friendly design, the Morse Code Converter Web Application serves as a comprehensive tool for anyone interested in learning and utilizing Morse code effectively. Whether for educational purposes, hobbyist projects, or professional use, this application meets a wide range of needs while fostering a deeper appreciation for the art of Morse communication.


## Description of Files and Directories

**static/**: Contains static files such as JavaScript, CSS, and images.

**form_script.js**: JavaScript file for form-related scripts.

**form_styles.css**: CSS file for form-related styles.

**icon.png**: Image file for the website icon.

**navbar_script.js**: JavaScript file for navigation bar scripts.

**script.js**: JavaScript file for handling file download using button.

**style.css**: main CSS file.

**type-script.js**: JavaScript file for handling type of conversion morse or text and sending json.

**templates/**: Contains HTML templates for the project.

**apology.html**: apology page.

**forgot.html**: forgot password form.

**history.html**:history page.

**index.html**: main index page.

**layout.html**: layout of the pages.

**login.html**: login form.

**register.html**: registration form.

**app.py**: Main flask application file all website logic and backend.

**converter.py**: Python file, for data conversion logic(morse, text).

**database.db**: Database file.

**helpers.py**: Python file containing impotent functions file to handel error pages.

**requirements.txt**: File listing all project requirement.


## Features
- **Text to Morse Code Conversion**: Upload a .txt file containing plain text, and the application will convert the text to Morse code.
- **Morse Code to Text Conversion**: Upload a .txt file containing Morse code, and the application will convert it back to plain text.
- **File History**: Users can use their converted files anywhere using the internet by registering themselves on the website.
- **Password Recovery**: A "Forgot Password" feature allows users to reset their passwords securely.

### Usage

- **Register**: Create a new account by providing a valid email, username, password, and security key.
- **Login**: Access your account using your username or email and password.
- **Convert Files**: Upload a .txt file to convert its contents to Morse code or vice versa.
-- **View History**: Check your conversion history and download any previously converted files.
