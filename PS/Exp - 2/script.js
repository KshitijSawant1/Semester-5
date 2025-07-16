function handleSubmit(event) {
  event.preventDefault(); // Prevents page reload
  const name = document.getElementById("name").value;
  document.getElementById("message").innerText = `Thanks, ${name}! We'll contact you soon.`;
}
