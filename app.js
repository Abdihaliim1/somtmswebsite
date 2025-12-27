(function () {
    const btn = document.getElementById("mobileToggle");
    const menu = document.getElementById("mobileMenu");
    if (btn && menu) {
        btn.addEventListener("click", () => {
            menu.classList.toggle("show");
            btn.setAttribute("aria-expanded", menu.classList.contains("show") ? "true" : "false");
        });
    }
})();
