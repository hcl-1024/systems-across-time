const header = document.querySelector("[data-header]");

function updateHeaderState() {
  header.classList.toggle("is-scrolled", window.scrollY > 16);
}

updateHeaderState();
window.addEventListener("scroll", updateHeaderState, { passive: true });
