import requests
from bs4 import BeautifulSoup
import csv
import re

# URL and headers
url = "https://www.jumia.co.ke/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
}

# Fetch page
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Failed to access site. Status code: {response.status_code}")
    exit()

print("Successfully accessed Jumia Kenya")
soup = BeautifulSoup(response.content, "html.parser")

# Find "Flash Sales | Live Now" section
heading = soup.find("h2", string=re.compile(r"Flash\s+Sales?", re.I))
if not heading:
    print("Could not find 'Flash Sales' section.")
    available_headings = soup.find_all(["h2", "h3"], string=re.compile(r"Flash|Top|Deals", re.I))
    print("Other headings found:", [h.get_text(strip=True) for h in available_headings])
    exit()

print(f"Found section: '{heading.get_text(strip=True)}'")

# Find parent container
container = heading.find_parent(["section", "div"])
if not container:
    print("Could not find container for flash sales.")
    exit()

# Find all product articles: look for <article> with class 'prd' or links with product-like href
product_elements = container.find_all("article", class_=re.compile(r"prd", re.I))

# Fallback: if no articles, look for <a> tags with product URLs
if not product_elements:
    product_elements = container.find_all("a", href=re.compile(r"/[^/]+-\d+\.html"))

print(f"Found {len(product_elements)} candidate product elements")

products_data = []

for elem in product_elements:
    try:
        # Get the link to extract href and drill down
        link = elem.find("a", href=True) or elem
        href = link["href"]
        if not href.startswith("/"):
            continue  # Skip external links

        # Product Name: look for h3 or any text container with product name
        name_tag = elem.find("h3") or elem.find("h2")
        product_name = name_tag.get_text(strip=True) if name_tag else "Unknown"
        if product_name == "Unknown":
            continue

        brand_name = product_name.split()[0]

        # Price
        price_tag = elem.find("div", string=re.compile(r"Ksh"))
        price = 0
        if price_tag:
            price_text = price_tag.get_text(strip=True)
            price = int(re.sub(r"[^0-9]", "", price_text))

        # Discount
        discount_tag = elem.find("div", class_=re.compile(r"bdg|_dsct", re.I))
        discount_text = discount_tag.get_text(strip=True) if discount_tag else "0%"
        discount = int(re.sub(r"[^0-9]", "", discount_text)) if "%" in discount_text else 0

        # Reviews
        rev_tag = elem.find("div", class_="rev")
        review_text = rev_tag.get_text(strip=True) if rev_tag else "0"
        num_reviews_match = re.search(r"(\d+)", review_text)
        num_reviews = int(num_reviews_match.group(1)) if num_reviews_match else 0

        # Rating
        stars_tag = elem.find("div", class_=re.compile(r"stars", re.I))
        rating_text = stars_tag.get_text(strip=True) if stars_tag else "0"
        rating_match = re.search(r"(\d+\.?\d*)", rating_text)
        rating = float(rating_match.group(1)) if rating_match else 0.0

        products_data.append({
            "Product Name": product_name,
            "Brand": brand_name,
            "Price (Ksh)": price,
            "Discount (%)": discount,
            "Reviews": num_reviews,
            "Rating": rating
        })

    except Exception as e:
        continue  # Skip any problematic product

# Save to CSV
if products_data:
    fieldnames = ["Product Name", "Brand", "Price (Ksh)", "Discount (%)", "Reviews", "Rating"]
    with open("products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products_data)
    print(f"\n✅ Successfully saved {len(products_data)} products to 'products.csv'")
else:
    print("\n❌ No product data extracted. The page structure may have changed.")

# === Popularity Analysis ===
if products_data:
    print("\n" + "="*60)
    print("POPULARITY ANALYSIS & SELLER RECOMMENDATION")
    print("="*60)

    sorted_by_reviews = sorted(products_data, key=lambda x: x["Reviews"], reverse=True)

    for p in products_data:
        n = p["Reviews"]
        r = p["Rating"]
        adjusted = (r * n + 4) / (n + 2) if n > 0 else 2.5
        p["Adjusted Rating"] = round(adjusted, 2)

    print("\nTop 5 Most Reviewed Products:")
    for i, p in enumerate(sorted_by_reviews[:5], 1):
        print(f"{i}. {p['Product Name']} | Reviews: {p['Reviews']} | Rating: {p['Rating']} → Adj: {p['Adjusted Rating']}")

    # Brand frequency
    top_brands = {}
    for p in sorted_by_reviews:
        if p["Reviews"] >= 5:
            top_brands[p["Brand"]] = top_brands.get(p["Brand"], 0) + 1

    if top_brands:
        best_brand = max(top_brands, key=top_brands.get)
        print(f"\n Recommendation: Sellers should consider products from '{best_brand}'.")
    else:
        print("\n No strong brand trend found. Try again later.")