from datetime import datetime, timedelta

# 1. Subtract five days from current date
print("1️⃣ Subtract five days")
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current date:", current_date)
print("After subtracting 5 days:", new_date)


# 2. Print yesterday, today, tomorrow
print("\n2️⃣ Yesterday, Today, Tomorrow")
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# 3. Drop microseconds from datetime
print("\n3️⃣ Drop microseconds")
now = datetime.now()
without_microseconds = now.replace(microsecond=0)
print("Original:", now)
print("Without microseconds:", without_microseconds)


# 4. Calculate difference between two dates in seconds
print("\n4️⃣ Difference between two dates in seconds")
date1 = datetime(2024, 1, 1)
date2 = datetime(2025, 1, 1)

difference = date2 - date1
print("Difference in seconds:", difference.total_seconds())