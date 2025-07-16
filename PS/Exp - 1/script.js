document.querySelector(".form").addEventListener("submit", function (e) {
  e.preventDefault();

  const formData = new FormData();
  formData.append("name", document.getElementById("name").value);
  formData.append("email", document.getElementById("email").value);
  formData.append("phone", document.getElementById("phone").value);
  formData.append("membership", document.getElementById("membership").value);
  formData.append("password", document.getElementById("password").value);

  fetch(
    "https://script.google.com/macros/s/AKfycbwvhccV7jdD7zG0OWmBEK6EhXLY4KZgGtWrEEBzdQUBr7F9zVwgUcLACHZ1ZfxMKIAe0A/exec",
    {
      method: "POST",
      mode: "no-cors",
      body: formData,
    }
  )
    .then((res) => res.text())
    .then((res) => {
      setTimeout(() => {
        window.location.href = "thankyou.html";
      }, 1000);
      document.querySelector(".form").reset();
    })
    .catch((err) => {
      alert("Error submitting data");
      console.error(err);
    });
});
