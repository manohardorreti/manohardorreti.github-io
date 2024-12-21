// Get query parameters from the URL
const urlParams = new URLSearchParams(window.location.search);
const fileName = urlParams.get('file');
const securityKey = urlParams.get('key');

// Display the file name
if (fileName) {
    document.getElementById('fileName').textContent = `File: ${fileName}`;
} else {
    document.getElementById('fileName').textContent = 'No file specified.';
}

const downloadButton = document.getElementById('downloadButton');
const downloadMessage = document.getElementById('downloadMessage');

downloadButton.addEventListener('click', () => {
    const enteredKey = document.getElementById('securityKeyInput').value;

    if (enteredKey === securityKey) {
        // Security key matches, proceed with download
        const fileURL = `https://github.com/manohardorreti/manohardorreti.github.io/raw/uploads/${encodeURIComponent(fileName)}`;
        const a = document.createElement('a');
        a.href = fileURL;
        a.download = fileName; // Suggests file download
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        downloadMessage.textContent = 'File download initiated!';
        downloadMessage.style.color = 'green';
    } else {
        // Security key does not match
        downloadMessage.textContent = 'Invalid security key!';
        downloadMessage.style.color = 'red';
    }
});
