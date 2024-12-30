// function to handel form data control, which file is support or converted to wich
function sendPostRequest(value) {
    fetch('/api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: value
            })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            const headingElement = document.getElementById('heading');
            if (data.value === 'text') {
                headingElement.innerHTML = 'Convert Text to Morse Code Form';
            } else if (data.value === 'morse') {
                headingElement.innerHTML = 'Convert Morse Code to Text Form';
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}
