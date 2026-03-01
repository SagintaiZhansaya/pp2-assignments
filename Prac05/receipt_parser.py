import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

products = []
total_sum = 0
date_time = None
payment_method = None

i = 0
while i < len(lines):
    line = lines[i].strip()

    if re.match(r"\d+\.", line): 
        name = lines[i+1].strip()

        price_match = re.search(r"([\d\s]+,\d{2})$", lines[i+3].strip())

        if price_match:
            price = price_match.group(1).replace(" ", "")
            total_sum += float(price.replace(",", "."))

            products.append({
                "name": name,
                "price": price
            })

        i += 4
        continue

    if "Время:" in line:
        date_time = line.replace("Время:", "").strip()

    if "Банковская карта" in line:
        payment_method = "Банковская карта"

    i += 1

result = {
    "products": products,
    "total amount": round(total_sum, 2),
    "date time": date_time,
    "payment method": payment_method
}

print(json.dumps(result, ensure_ascii=False, indent=4))