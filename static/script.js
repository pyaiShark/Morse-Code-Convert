// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(event.target);
    submitFormData(formData); // Call the function to submit
}

// Function to submit the form data
function submitFormData(formData) {
    fetch('/convert', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // useing the original file name and download URL
            const originalFileName = data.originalFileName;
            const downloadUrl = data.downloadUrl;

            // Show the download button and set its click event
            const downloadButton = document.getElementById('downloadButton');
            downloadButton.style.visibility = 'visible';
            downloadButton.onclick = function() {
                downloadFile(downloadUrl, originalFileName);
            };
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

// Function to download the file
function downloadFile(url, fileName) {
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

// event listener for form submition
document.getElementById('form1').addEventListener('submit', handleFormSubmit);
