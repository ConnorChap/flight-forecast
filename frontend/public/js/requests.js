
fetch('http://localhost:8081/api/hello')
    .then(res => res.json())
    .then(data => {
        document.getElementById('output').innerText = data.message;
    })
    .catch(_ => {
        document.getElementById('output').innerText = 'Error connecting to backend';
    });