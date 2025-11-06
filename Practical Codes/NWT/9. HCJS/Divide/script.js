const $ = (id) => document.getElementById(id);
const btn = $("btnCount"),
  rbtn = $("rbtnCount"),
  cnt = $("count"),
  form = $("form");
const tIn = $("inTitle"),
  mIn = $("inMsg"),
  title = $("title"),
  msg = $("msg");
const parent = $("parent"),
  child = $("child"),
  log = $("log");

let n = 0;
btn.onclick = () => (cnt.textContent = ++n);
rbtn.onclick = () => (cnt.textContent = --n);

form.onsubmit = (e) => {
  e.preventDefault();
  if (tIn.value) title.textContent = tIn.value.trim();
  if (mIn.value) msg.textContent = mIn.value.trim();
  tIn.value = mIn.value = "";
  alert("Form Submitted");
};

parent.addEventListener("click", () => logIt("Parent clicked"));
child.addEventListener("click", () => logIt("Child clicked"));

function logIt(text) {
  log.textContent += text + "\n";
  log.scrollTop = log.scrollHeight;
}
