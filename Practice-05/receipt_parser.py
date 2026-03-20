import re
import json

# read receipt
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

def parse_receipt(text):
    # 1. Extract Date and Time
    # Pattern: DD.MM.YYYY HH:MM:SS
    date_time_match = re.search(r'(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', text)
    date = date_time_match.group(1) if date_time_match else None
    time = date_time_match.group(2) if date_time_match else None

    # 2. Extract Payment Method
    # Looking for the line before the total amount
    payment_match = re.search(r'([А-я\s]+):\n[\d\s,]+\nИТОГО', text)
    payment_method = payment_match.group(1).strip() if payment_match else "Unknown"

    # 3. Extract Total Amount
    # Pattern: Total follows "ИТОГО:" and handles spaces in numbers
    total_match = re.search(r'ИТОГО:\n([\d\s,]+)', text)
    total_amount = total_match.group(1).replace(" ", "").replace(",", ".").strip() if total_match else "0.00"

    # 4. Extract Products and Prices
    # This pattern captures the index, the name (multi-line), 
    # the quantity/unit price line, and the final subtotal.
    # Note: We use [\s\S]*? to match across multiple lines greedily until the next numeric pattern.
    product_pattern = re.compile(
        r'\d+\.\n(.*?)\n\d+,\d+\s+x\s+[\d\s,]+\n([\d\s,]+)\nСтоимость', 
        re.DOTALL
    )
    
    products = []
    for match in product_pattern.finditer(text):
        name = match.group(1).replace('\n', ' ').strip()
        # Clean the price string: remove spaces and swap comma for dot
        price = match.group(2).replace(" ", "").replace(",", ".").strip()
        
        products.append({
            "name": name,
            "subtotal": float(price)
        })

    # Create Structured Output
    receipt_data = {
        "metadata": {
            "date": date,
            "time": time,
            "payment_method": payment_method
        },
        "items": products,
        "total": float(total_amount)
    }
    
    return receipt_data

# Execute and Print
parsed_result = parse_receipt(text)
print(json.dumps(parsed_result, indent=4, ensure_ascii=False))