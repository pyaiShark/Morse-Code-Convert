document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registration_form');

    // Show warnings when any input field is clicked, warning gone in right input
    form.addEventListener('click', function(event) {
        if (event.target.tagName === 'INPUT') {
            showWarnings();
        }
    });

    // Function to show warnings based on current input values
    function showWarnings() {
        // Clear previous warnings
        document.querySelectorAll('.hf-warning').forEach(warning => {
            warning.style.visibility = 'hidden';
        });

        // Validate email
        const email = form.email.value;
        if (!email) {
            document.getElementById('emailWarning').style.visibility = 'visible';
        }

        // Validate username
        const username = form.username.value;
        if (!username) {
            document.getElementById('usernameWarning').style.visibility = 'visible';
        }

        // Validate password
        const password = form.password.value;
        if (password.length < 6) {
            document.getElementById('passwordWarning').style.visibility = 'visible';
        }

        // Validate confirmation
        const confirmation = form.confirmation.value;
        if (confirmation !== password) {
            document.getElementById('confirmationWarning').style.visibility = 'visible';
        }

        // Validate security key
        const securityKey = form.security_key.value;
        if (!securityKey) {
            document.getElementById('securityKeyWarning').style.visibility = 'visible';
        }
    }

    // Add input event listeners to hide warnings when valid data is entered
    form.querySelectorAll('input').forEach(input => {
        input.addEventListener('input', function() {
            const warningId = this.name + 'Warning';
            const warningElement = document.getElementById(warningId);

            // Hide the warning if the input is valid
            if (this.name === 'email' && this.value) {
                warningElement.style.visibility = 'hidden';
            } else if (this.name === 'username' && this.value) {
                warningElement.style.visibility = 'hidden';
            } else if (this.name === 'password' && this.value.length >= 6) {
                warningElement.style.visibility = 'hidden';
            } else if (this.name === 'confirmation' && this.value === form.password.value) {
                warningElement.style.visibility = 'hidden';
            } else if (this.name === 'security_key' && this.value) {
                warningElement.style.visibility = 'hidden';
            }
        });
    });
});
