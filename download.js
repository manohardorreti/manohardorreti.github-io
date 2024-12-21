// Get query parameters from the URL
const urlParams = new URLSearchParams(window.location.search);
const fileName = urlParams.get('file');
const securityKey = urlParams.get('key');

// Display the file name
const fileNameElement = document.getElementById('fileName');
if (fileName) {
    fileNameElement.textContent = `File: ${fileName}`;
} else {
    fileNameElement.textContent = 'No file specified.';
}

const downloadButton = document.getElementById('downloadButton');
const downloadMessage = document.getElementById('downloadMessage');

downloadButton.addEventListener('click', () => {
    const enteredKey = document.getElementById('securityKeyInput').value;

    if (enteredKey === securityKey) {
        // Security key matches, proceed with download
        const fileURL = `https://raw.githubusercontent.com/manohardorreti/manohardorreti.github.io/main/${encodeURIComponent(fileName)}`;
        
        // Create a temporary anchor element for downloading the file
        const a = document.createElement('a');
        a.href = fileURL;
        a.download = fileName; // Suggests a filename for download
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        // Provide user feedback
        downloadMessage.textContent = 'File download initiated!';
        downloadMessage.style.color = 'green';
    } else {
        // Security key does not match
        downloadMessage.textContent = 'Invalid security key!';
        downloadMessage.style.color = 'red';
    }
});
