document.addEventListener("DOMContentLoaded", () => {
  const themeCard = document.getElementById("themeCard");
  const btnDark = document.getElementById("btnDark");
  const btnCount = document.getElementById("btnCount");
  const countBadge = document.getElementById("countBadge");
  const updateForm = document.getElementById("updateForm");
  const titleInput = document.getElementById("titleInput");
  const messageInput = document.getElementById("messageInput");
  const cardTitle = document.getElementById("cardTitle");
  const cardText = document.getElementById("cardText");

  const parentBox = document.getElementById("parentBox");
  const childBox = document.getElementById("childBox");
  const logArea = document.getElementById("logArea");

  // State
  let count = 0;

  // Handlers
  btnDark.addEventListener("click", () => {
    themeCard.classList.toggle("dark");
  });

  btnCount.addEventListener("click", () => {
    count++;
    countBadge.textContent = String(count);
  });

  updateForm.addEventListener("submit", (e) => {
    e.preventDefault(); // prevent page reload
    const t = titleInput.value.trim();
    const m = messageInput.value.trim();
    if (t) cardTitle.textContent = t;
    if (m) cardText.textContent = m;
    titleInput.value = "";
    messageInput.value = "";
  });

  // Event Flow Demo: capturing vs bubbling
  parentBox.addEventListener("click", () => appendLog("Parent (capture)"), {
    capture: true,
  });
  parentBox.addEventListener("click", () => appendLog("Parent (bubble)"));
  childBox.addEventListener(
    "click",
    (e) => {
      appendLog("Child (capture)");
    },
    { capture: true }
  );
  childBox.addEventListener("click", (e) => {
    appendLog("Child (bubble)");
    // Uncomment to stop bubbling:
    // e.stopPropagation();
  });

  function appendLog(msg) {
    const ts = new Date().toLocaleTimeString();
    logArea.textContent += `[${ts}] ${msg}\n`;
    logArea.scrollTop = logArea.scrollHeight;
  }
});
