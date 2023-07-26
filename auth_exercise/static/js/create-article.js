function createArticle() {
  const button = document.getElementById('button');
  const BASE_URL = 'http://127.0.0.1:8000/article/create/';

  button.addEventListener('click', postRequest);

  function postRequest(event) {
  event.preventDefault(); // Prevent the default form submission behavior
  const title = document.querySelector('#id_title').value;
  const tokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
  const csrfToken = tokenInput.value;

  const BASE_URL = 'http://127.0.0.1:8000/article/create/';
  const httpHeaders = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({
      article: title,
    }),
  };

  fetch(BASE_URL, httpHeaders)
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.log(error);
    });
}

function getCSRFToken() {
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith('csrftoken=')) {
      return cookie.substring('csrftoken='.length);
    }
  }
  return null;
}

createArticle();
