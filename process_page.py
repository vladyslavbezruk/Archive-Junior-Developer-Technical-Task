def process_page(page_source):
    items = []

    products = page_source.find_all("li", class_="product")

    for product in products:
        title = product.find("h2", class_="woocommerce-loop-product__title").text

        price = product.find("span", class_="woocommerce-Price-amount amount").text

        product_id = product.find("a", class_="add_to_cart_button")["data-product_id"]

        product_sku = product.find("a", class_="add_to_cart_button")["data-product_sku"]

        image_srcset = product.find("img", class_="wp-post-image")["srcset"]

        image_url = image_srcset.split(",")[-1].split()[0]

        items.append({
            "id": product_id,
            "name": title,
            "price": price,
            "sku": product_sku,
            "image_url": image_url
        })

    return items
