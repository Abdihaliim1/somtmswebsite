
import os

# Template for the SEO pages
template = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SomTMS {city}, {state} — Best Trucking Software for Carriers</title>
  <meta name="description"
    content="SomTMS provides the best Transportation Management System (TMS) for carriers in {city}, {state}. Manage loads, dispatch, and settlements efficiently in {city}." />
  <meta property="og:title" content="SomTMS {city} — Top Rated Carrier Software" />
  <meta property="og:description"
    content="Run your trucking business in {city}, {state} with SomTMS. Dispatch, Invoicing, and Settlements in one clean system." />
  <meta property="og:type" content="website" />
  <meta name="theme-color" content="#ffffff" />
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="assets/styles.css" />
</head>

<body>
  <div class="nav">
    <div class="container nav-inner">
      <a class="brand" href="index.html" aria-label="SomTMS Home">
        <span class="logo">S</span>
        <span>SomTMS</span>
      </a>
      <div class="nav-links" role="navigation" aria-label="Primary">
        <a href="index.html">Home</a>
        <a href="features.html">Features</a>
        <a href="pricing.html">Pricing</a>
        <a href="security.html">Security</a>
        <a href="contact.html">Contact</a>
      </div>
      <div class="actions">
        <a class="btn ghost" href="https://app.somtms.com" target="_blank" rel="noopener">Login</a>
        <a class="btn primary" href="contact.html">Request a demo</a>
        <button class="mobile-toggle" aria-label="Menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
     <div class="mobile-menu">
      <a href="index.html">Home</a>
      <a href="features.html">Features</a>
      <a href="pricing.html">Pricing</a>
      <a href="security.html">Security</a>
      <a href="contact.html">Contact</a>
      <div style="margin-top:12px; border-top:1px solid var(--border); padding-top:12px">
        <a href="https://app.somtms.com">Login</a>
      </div>
    </div>
  </div>

  <div class="hero">
    <div class="container grid-hero">
      <div>
         <div class="call-now">
          <span>Call Sales Today</span>
          📞 615-638-2490
        </div>
        <span class="badge">Serving Carriers in {city}, {state}</span>
        <div class="h1">The #1 TMS Software for {city} Trucking Companies.</div>
        <p class="lead">
          SomTMS helps carriers in {city} run dispatch, settlements, and AR in one clean system. 
          Stop using spreadsheets and switch to the modern standard for {state} logistics.
        </p>
        <div class="hero-cta">
          <a class="btn primary" href="contact.html">Request a demo</a>
          <a class="btn" href="features.html">See features</a>
        </div>
        <div class="mini">
          <span><span class="dot"></span>Local {city} Support</span>
          <span><span class="dot"></span>Cloud-based</span>
          <span><span class="dot"></span>Multi-tenant</span>
        </div>
      </div>

       <div class="panel hero-card">
        <div class="hero-mock">
          <div class="mock-header">
            <div class="mock-title">Dashboard snapshot</div>
            <span class="badge">Live {city} Data</span>
          </div>
          <div class="kpis">
            <div class="kpi">
              <div class="label">TOTAL REVENUE</div>
              <div class="value">$32,196</div>
            </div>
            <div class="kpi">
              <div class="label">NET PROFIT</div>
              <div class="value">$6,665</div>
            </div>
            <div class="kpi">
              <div class="label">ACTIVE LOADS</div>
              <div class="value">1</div>
            </div>
             <div class="kpi">
              <div class="label">ACTIVE DRIVERS</div>
              <div class="value">5</div>
            </div>
          </div>
          <div class="mock-footer">
            Real-time operations for fleets in {city}.
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container">
      <h2>Why {city} Carriers Choose SomTMS?</h2>
      <p>Whether you are hauling out of {city} or managing a fleet across {state}, you need a system that moves as fast as you do.</p>
      
      <div class="features">
        <div class="card feature">
          <div class="icon">📍</div>
          <h3>Local Dispatch</h3>
          <p>Optimized for carriers based in {city}, {state}. Manage drivers and lanes effectively.</p>
        </div>
        <div class="card feature">
          <div class="icon">💰</div>
          <h3>Fast Settlements</h3>
          <p>Pay your drivers and owner-operators on time. Handle {state} specific deductions easily.</p>
        </div>
         <div class="card feature">
          <div class="icon">📈</div>
          <h3>Growth Ready</h3>
          <p>From 1 truck in {city} to 100+ nationwide. We scale with your business.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="container">
      <div class="fgrid">
        <div>
          <div class="brand">
            <span class="logo">S</span>
            <span>SomTMS</span>
          </div>
          <p class="small footer-desc">
            Proudly serving {city}, {state} and carriers nationwide.
          </p>
        </div>
        <div>
          <div class="footer-head">Product</div>
          <div class="small footer-links">
            <a href="features.html">Features</a>
            <a href="pricing.html">Pricing</a>
            <a href="locations.html">Locations</a>
          </div>
        </div>
        <div>
          <div class="footer-head">Company</div>
          <div class="small footer-links">
            <a href="contact.html">Contact</a>
            <a href="terms.html">Terms</a>
          </div>
        </div>
      </div>
      <hr class="sep" />
      <div class="small">© 2025 SomTMS. All rights reserved.</div>
    </div>
  </div>
    <script src="assets/site.js"></script>
</body>
</html>
"""

# List of top 100 US cities for logistics/trucking (simplified list for brevity, expanded to 100 via simple variation if needed, 
# but I will use a solid list of major hubs using a generator for now to ensure we get 100 distinct files).
cities = [
    ("Nashville", "TN"), ("Atlanta", "GA"), ("Chicago", "IL"), ("Dallas", "TX"), ("Houston", "TX"),
    ("Los Angeles", "CA"), ("Memphis", "TN"), ("Columbus", "OH"), ("Indianapolis", "IN"), ("Kansas City", "MO"),
    ("Charlotte", "NC"), ("Phoenix", "AZ"), ("Denver", "CO"), ("Seattle", "WA"), ("Miami", "FL"),
    ("Detroit", "MI"), ("Minneapolis", "MN"), ("Saint Louis", "MO"), ("Baltimore", "MD"), ("Philadelphia", "PA"),
    ("New York", "NY"), ("Boston", "MA"), ("San Francisco", "CA"), ("Portland", "OR"), ("Las Vegas", "NV"),
    ("San Antonio", "TX"), ("Milwaukee", "WI"), ("Oklahoma City", "OK"), ("Louisville", "KY"), ("New Orleans", "LA"),
    ("Orlando", "FL"), ("Cleveland", "OH"), ("Cincinnati", "OH"), ("Pittsburgh", "PA"), ("Austin", "TX"),
    ("Sacramento", "CA"), ("Riverside", "CA"), ("San Diego", "CA"), ("Tampa", "FL"), ("Jacksonville", "FL"),
    ("Salt Lake City", "UT"), ("Raleigh", "NC"), ("Richmond", "VA"), ("Birmingham", "AL"), ("Buffalo", "NY"),
    ("Hartford", "CT"), ("Providence", "RI"), ("Virginia Beach", "VA"), ("Grand Rapids", "MI"), ("Des Moines", "IA"),
    ("Omaha", "NE"), ("Tulsa", "OK"), ("Wichita", "KS"), ("Little Rock", "AR"), ("Knoxville", "TN"),
    ("Chattanooga", "TN"), ("Mobile", "AL"), ("Savannah", "GA"), ("Charleston", "SC"), ("Greenville", "SC"),
    ("Fayetteville", "NC"), ("Greensboro", "NC"), ("Newark", "NJ"), ("Jersey City", "NJ"), ("Allentown", "PA"),
    ("Harrisburg", "PA"), ("Scranton", "PA"), ("Toledo", "OH"), ("Akron", "OH"), ("Dayton", "OH"),
    ("Fort Wayne", "IN"), ("Gary", "IN"), ("Peoria", "IL"), ("Springfield", "IL"), ("Davenport", "IA"),
    ("Madison", "WI"), ("Green Bay", "WI"), ("Fargo", "ND"), ("Sioux Falls", "SD"), ("Boise", "ID"),
    ("Spokane", "WA"), ("Tacoma", "WA"), ("Fresno", "CA"), ("Bakersfield", "CA"), ("Stockton", "CA"),
    ("Modesto", "CA"), ("Reno", "NV"), ("Albuquerque", "NM"), ("El Paso", "TX"), ("Laredo", "TX"),
    ("McAllen", "TX"), ("Corpus Christi", "TX"), ("Baton Rouge", "LA"), ("Shreveport", "LA"), ("Jackson", "MS"),
    ("Lexington", "KY"), ("Fort Worth", "TX"), ("Arlington", "TX"), ("Plano", "TX"), ("Garland", "TX")
]

# Ensure we have exactly 100 or close (the list above is exactly 100 lines/pairs approx)
# I will proceed with generating them.

files_generated = []

for city, state in cities:
    filename = f"tms-software-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    content = template.format(city=city, state=state)
    
    with open(filename, "w") as f:
        f.write(content)
    files_generated.append((city, state, filename))

# Generate simple locations index page
locations_html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SomTMS Locations — Trucking Software by City</title>
  <link rel="stylesheet" href="assets/styles.css" />
</head>
<body>
<div class="nav">
    <div class="container nav-inner">
      <a class="brand" href="index.html">
        <span class="logo">S</span>
        <span>SomTMS</span>
      </a>
      <div class="nav-links">
        <a href="index.html">Home</a>
        <a href="features.html">Features</a>
        <a href="pricing.html">Pricing</a>
        <a href="contact.html">Contact</a>
      </div>
       <div class="actions">
        <a class="btn primary" href="contact.html">Request a demo</a>
        <button class="mobile-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </div>
     <div class="mobile-menu">
      <a href="index.html">Home</a>
      <a href="features.html">Features</a>
      <a href="pricing.html">Pricing</a>
    </div>
</div>

<div class="page">
    <div class="container">
        <h1>Serving Carriers Across the USA</h1>
        <p class="sub">Find SomTMS services in your city.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px;">
"""

for city, state, filename in files_generated:
    locations_html += f'            <a href="{filename}" style="display:block; padding:12px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; color:#0f172a; text-decoration:none;">TMS in {city}, {state}</a>\n'

locations_html += """
        </div>
    </div>
</div>
<script src="assets/site.js"></script>
</body>
</html>
"""

with open("locations.html", "w") as f:
    f.write(locations_html)

# Generate Sitemap.xml (basic append)
sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
# Add core pages
core_pages = ["index.html", "features.html", "pricing.html", "security.html", "contact.html", "locations.html"]
for p in core_pages:
    sitemap_content += f"""  <url>
    <loc>https://somtms.com/{p}</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
"""

# Add generated pages
for city, state, filename in files_generated:
     sitemap_content += f"""  <url>
    <loc>https://somtms.com/{filename}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""

sitemap_content += "</urlset>"

with open("sitemap.xml", "w") as f:
    f.write(sitemap_content)

print(f"Successfully generated {len(files_generated)} SEO pages, locations.html, and sitemap.xml")
