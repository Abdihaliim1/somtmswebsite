#!/usr/bin/env python3
"""
Update sitemap.xml with proper lastmod dates and differentiated priorities
"""

import os
from datetime import datetime
from pathlib import Path

# Get current date in ISO format
current_date = datetime.now().strftime('%Y-%m-%d')

# Define page priorities
CORE_PAGES = {
    'index.html': ('1.0', 'daily'),
    'features.html': ('0.9', 'weekly'),
    'pricing.html': ('0.9', 'weekly'),
    'contact.html': ('0.8', 'monthly'),
    'security.html': ('0.7', 'monthly'),
    'locations.html': ('0.6', 'monthly'),
    'terms.html': ('0.3', 'yearly'),
    'privacy.html': ('0.3', 'yearly'),
}

def generate_sitemap():
    """Generate sitemap with proper priorities and lastmod dates"""

    sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # Add core pages with differentiated priorities
    for page, (priority, changefreq) in CORE_PAGES.items():
        sitemap_content.append('  <url>')
        sitemap_content.append(f'    <loc>https://somtms.com/{page}</loc>')
        sitemap_content.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap_content.append(f'    <changefreq>{changefreq}</changefreq>')
        sitemap_content.append(f'    <priority>{priority}</priority>')
        sitemap_content.append('  </url>')

    # Add SEO landing pages (100 cities) with lower priority
    base_path = Path(__file__).parent
    seo_pages = sorted(base_path.glob('tms-software-*.html'))

    for page in seo_pages:
        sitemap_content.append('  <url>')
        sitemap_content.append(f'    <loc>https://somtms.com/{page.name}</loc>')
        sitemap_content.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap_content.append(f'    <changefreq>monthly</changefreq>')
        sitemap_content.append(f'    <priority>0.5</priority>')
        sitemap_content.append('  </url>')

    sitemap_content.append('</urlset>')

    return '\n'.join(sitemap_content)

def main():
    sitemap_xml = generate_sitemap()

    # Write to sitemap.xml
    output_path = Path(__file__).parent / 'sitemap.xml'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)

    print(f"✓ Sitemap updated with {len(CORE_PAGES)} core pages")

    # Count SEO pages
    base_path = Path(__file__).parent
    seo_count = len(list(base_path.glob('tms-software-*.html')))
    print(f"✓ Added {seo_count} SEO landing pages")
    print(f"✓ Total URLs: {len(CORE_PAGES) + seo_count}")
    print(f"✓ Last modified date: {current_date}")

if __name__ == '__main__':
    main()
