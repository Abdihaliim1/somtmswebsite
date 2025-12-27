function renderHeader(active) {
    const is = (key) => (active === key ? 'style="color:#0f172a"' : "");
    return `
  <div class="topbar">
    <div class="container">
      <div class="nav">
        <a class="brand" href="/index.html">
          <div class="logo">S</div>
          <div>SomTMS</div>
        </a>

        <div class="navlinks" role="navigation" aria-label="Primary">
          <a ${is("home")} href="/index.html">Home</a>
          <a ${is("features")} href="/features.html">Features</a>
          <a ${is("pricing")} href="/pricing.html">Pricing</a>
          <a ${is("security")} href="/security.html">Security</a>
          <a ${is("contact")} href="/contact.html">Contact</a>
        </div>

        <div class="actions">
          <a class="btn" href="https://app.somtms.com">Login</a>
          <a class="btn btn-primary" href="/contact.html">Request a demo</a>
          <button id="mobileToggle" class="mobile-toggle" aria-expanded="false" aria-label="Open menu">☰</button>
        </div>
      </div>

      <div id="mobileMenu" class="mobile-menu">
        <a href="/index.html">Home</a>
        <a href="/features.html">Features</a>
        <a href="/pricing.html">Pricing</a>
        <a href="/security.html">Security</a>
        <a href="/contact.html">Contact</a>
        <div class="row">
          <a class="btn" style="flex:1; text-align:center" href="https://app.somtms.com">Login</a>
          <a class="btn btn-primary" style="flex:1; text-align:center" href="/contact.html">Request a demo</a>
        </div>
      </div>
    </div>
  </div>`;
}

function renderFooter() {
    const year = new Date().getFullYear();
    return `
    <div class="footer">
      <div class="container">
        <div class="footgrid">
          <div class="footcol">
            <div class="brand" style="margin-bottom:10px">
              <div class="logo">S</div>
              <div>SomTMS</div>
            </div>
            <p style="margin:0; max-width:50ch">
              A modern TMS for carriers: load lifecycle, dispatch, settlements, AR, tasks, and reporting — built to stay fast, clean, and scalable.
            </p>
          </div>
          <div class="footcol">
            <h5>Product</h5>
            <a href="/features.html">Features</a>
            <a href="/pricing.html">Pricing</a>
            <a href="/security.html">Security</a>
            <a href="https://app.somtms.com">Login</a>
          </div>
          <div class="footcol">
            <h5>Company</h5>
            <a href="/contact.html">Contact</a>
            <a href="/terms.html">Terms</a>
            <a href="/privacy.html">Privacy</a>
          </div>
        </div>
        <div class="copy">© ${year} SomTMS. All rights reserved.</div>
      </div>
    </div>`;
}
