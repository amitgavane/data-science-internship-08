from fastapi import FastAPI

app = FastAPI()

# Product list
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 120, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": False},
    {"id": 4, "name": "USB Hub", "price": 399, "category": "Electronics", "in_stock": True},

    # Q1 Added Products
    {"id": 5, "name": "Laptop Stand", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1299, "category": "Electronics", "in_stock": False}
]

# Q1 Show all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

# Q2 Category Filter
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered = []

    for product in products:
        if product["category"].lower() == category_name.lower():
            filtered.append(product)

    if len(filtered) == 0:
        return {"error": "No products found in this category"}

    return filtered


# Q3 Show only in-stock products
@app.get("/products/instock")
def get_instock_products():

    instock = []

    for product in products:
        if product["in_stock"] == True:
            instock.append(product)

    return {
        "in_stock_products": instock,
        "count": len(instock)
    }


# Q4 Store Summary
@app.get("/store/summary")
def store_summary():

    total = len(products)

    instock = 0
    outstock = 0

    categories = set()

    for product in products:
        if product["in_stock"]:
            instock += 1
        else:
            outstock += 1

        categories.add(product["category"])

    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": instock,
        "out_of_stock": outstock,
        "categories": list(categories)
    }


# Q5 Search Product
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = []

    for product in products:
        if keyword.lower() in product["name"].lower():
            results.append(product)

    if len(results) == 0:
        return {"message": "No products matched your search"}

    return {
        "matched_products": results,
        "count": len(results)
    }


# BONUS Cheapest & Most Expensive
@app.get("/products/deals")
def product_deals():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }