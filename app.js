(function () {
    const btn = document.getElementById("mobileToggle");
    const menu = document.getElementById("mobileMenu");

    if (btn && menu) {
        // Toggle menu on button click
        btn.addEventListener("click", () => {
            const isOpen = menu.classList.toggle("show");
            btn.setAttribute("aria-expanded", isOpen ? "true" : "false");

            // Toggle scroll lock
            if (isOpen) {
                document.body.style.overflow = "hidden";
            } else {
                document.body.style.overflow = "";
            }
        });

        // Close menu when clicking on links
        const menuLinks = menu.querySelectorAll("a");
        menuLinks.forEach(link => {
            link.addEventListener("click", () => {
                menu.classList.remove("show");
                btn.setAttribute("aria-expanded", "false");
                document.body.style.overflow = "";
            });
        });
    }
})();
