import re
import json

# read receipt
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


# 1. Extract prices
prices = re.findall(r"\d+\s?\d*,\d{2}", text)


# 2. Extract product names
products = re.findall(r"\d+\.\n(.+)", text)


# 3. Extract date and time
date_time_match = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", text)
date_time = date_time_match.group() if date_time_match else None


# 4. Extract payment method
payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment_method = payment_match.group() if payment_match else None


# 5. Extract total
total_match = re.search(r"ИТОГО:\n([\d\s,]+)", text)
total = total_match.group(1) if total_match else None


# structured output
result = {
    "products": products,
    "prices": prices,
    "total": total,
    "payment_method": payment_method,
    "date_time": date_time
}


# print result
print(json.dumps(result, indent=4, ensure_ascii=False))