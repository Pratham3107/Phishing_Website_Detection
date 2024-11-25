document.getElementById('phishing-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let url = document.getElementById('url').value;
    let resultDiv = document.getElementById('result');
    
    // Simulate a response
    if (url.includes("phish")) {
        resultDiv.textContent = "Warning: This website is potentially a phishing site!";
        resultDiv.style.color = "red";
    } else {
        resultDiv.textContent = "This website seems safe.";
        resultDiv.style.color = "green";
    }
});