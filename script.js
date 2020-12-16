const form = document.querySelector('form');

// путь к серверу
const url = 'add';

form.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const formData = new FormData(form);
    const formDataObject = {
        name: "lox",
        surname: "pox",
        fullname: "chmo"
    };

    formData.forEach((value, key) => {
        formDataObject[key] = value;
    })

    fetch(url, {
        method: "POST",
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(formDataObject),
    })
    .then(response => {
        console.log(response);
    })
    .catch(error => {
        console.log(error)
    })
})

// запрашивает данные json (метод get)

fetch(url)
    .then((response) => {
        return response.json();
    })
    .then(data => {
        console.log(data);
    })