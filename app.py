"""
app.py - Python Bug Lab (20 Simple Exercises for Git & GitHub Masterclass)

This module contains 20 simple utility functions.
Each function contains ONE intentional, realistic beginner-level bug.
Do not modify the function signatures. Fix the logic inside each function.
"""

# =====================================================================
# CATEGORY 1: MATH & STATISTICS (Bugs 1 - 5)
# =====================================================================

def is_even(n: int) -> bool:
    """
    Bug #01: Check if an integer is even.
    Symptom: Erroneously checks 'n % 2 == 1' returning True for odd numbers, and fails for negative even numbers.
    Expected: is_even(4) -> True, is_even(7) -> False, is_even(-2) -> True.
    """
    # BUG: Checks for 1 instead of 0
    return n % 2 == 0


def clamp_number(value: float, min_val: float, max_val: float) -> float:
    """
    Bug #02: Constrain a number within [min_val, max_val] bounds.
    Symptom: Bounds are inverted: returns max_val when value is smaller than min_val.
    Expected: clamp_number(5, 10, 20) -> 10, clamp_number(25, 10, 20) -> 20, clamp_number(15, 10, 20) -> 15.
    """
    # BUG: Inverted boundary checks
    if value < min_val:
        return min_val
    elif value > max_val:
        return max_val
    return value


def discount_price(price: float, discount_percent: float) -> float:
    """
    Bug #03: Calculate final price after applying a percentage discount.
    Symptom: Returns the discount amount instead of the final discounted price.
    Expected: discount_price(100.0, 20.0) -> 80.0
    """
    # BUG: Computes discount amount, forgets to subtract from price
    discount_amount = price * (discount_percent / 100.0)
    return price - discount_amount


def find_max_number(numbers: list) -> int:
    """
    Bug #04: Find the maximum number in a non-empty list of integers.
    Symptom: Initializes max to 0, which fails when all numbers are negative!
    Expected: find_max_number([-10, -5, -20]) -> -5
    """
    # BUG: Initializing to 0 fails for all-negative lists
    current_max = numbers[0]
    for n in numbers:
        if n > current_max:
            current_max = n
    return current_max


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Bug #05: Calculate Body Mass Index: weight / (height^2).
    Symptom: Forgets to square the height.
    Expected: calculate_bmi(70, 1.75) -> ~22.86
    """
    # BUG: Missing height squared
    return round(weight_kg / (height_m * height_m), 2)


# =====================================================================
# CATEGORY 2: STRINGS & TEXT PROCESSING (Bugs 6 - 10)
# =====================================================================

def is_palindrome(text: str) -> bool:
    """
    Bug #06: Check if a given string is a palindrome.
    Symptom: Case sensitive, so "Racecar" or "Madam" returns False.
    Expected: Case-insensitive check (e.g. "Racecar" -> True).
    """
    # BUG: Compares without lowercasing
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(text: str) -> int:
    """
    Bug #07: Count the number of English vowels (a, e, i, o, u) in a string.
    Symptom: The letter 'u' is missing from the vowel set.
    Expected: count_vowels("umbrella") -> 3
    """
    # BUG: Missing 'u' in vowels
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def truncate_text(text: str, max_len: int) -> str:
    """
    Bug #08: Truncate text to max_len, appending '...' if truncated.
    Symptom: Total string length exceeds max_len because '...' is added on top.
    Expected: truncate_text("Hello World", 8) -> "Hello..." (total length exactly 8).
    """
    if len(text) <= max_len:
        return text
    # BUG: Takes max_len characters THEN appends 3 dots (exceeding max_len)
    return text[:max_len] + "..."


def reverse_words(sentence: str) -> str:
    """
    Bug #09: Reverse the order of words in a sentence.
    Symptom: Reverses every individual character instead of word order.
    Expected: reverse_words("Hello World") -> "World Hello"
    """
    # BUG: Reverses character stream instead of words
    return sentence[::-1]


def get_file_extension(filename: str) -> str:
    """
    Bug #10: Extract file extension without the leading dot.
    Symptom: Fails when filename has no extension (returns full filename).
    Expected: "script.py" -> "py", "archive.tar.gz" -> "gz", "README" -> ""
    """
    if "." not in filename:
        # BUG: Returns original filename instead of empty string
        return filename
    return filename.split(".")[-1]


# =====================================================================
# CATEGORY 3: LISTS & COLLECTIONS (Bugs 11 - 15)
# =====================================================================

def get_top_students(grades: list, n: int) -> list:
    """
    Bug #11: Return top n student names from a sorted list of names.
    Symptom: Off-by-one slicing returns n-1 students.
    Expected: get_top_students(["Alice", "Bob", "Charlie", "David"], 2) -> ["Alice", "Bob"]
    """
    # BUG: Slices up to n-1 instead of n
    return grades[: n - 1]


def remove_duplicates_preserve_order(items: list) -> list:
    """
    Bug #12: Remove duplicates while preserving original order.
    Symptom: Uses set() conversion which shuffles the item order.
    Expected: [3, 1, 2, 3, 2] -> [3, 1, 2]
    """
    # BUG: list(set(items)) does not guarantee order preservation
    return list(set(items))


def sum_even_numbers(numbers: list) -> int:
    """
    Bug #13: Calculate sum of all even numbers in a list.
    Symptom: Checks n % 2 != 0, summing odd numbers instead!
    Expected: sum_even_numbers([1, 2, 3, 4, 5, 6]) -> 12
    """
    total = 0
    for n in numbers:
        # BUG: Condition checks for odd numbers
        if n % 2 != 0:
            total += n
    return total


def merge_two_dicts(d1: dict, d2: dict) -> dict:
    """
    Bug #14: Merge two dictionaries into a NEW dictionary.
    Symptom: Mutates d1 in-place instead of creating an independent copy.
    Expected: Merged dict returned, d1 remains unchanged.
    """
    # BUG: Mutates d1 directly
    d1.update(d2)
    return d1


def filter_positive_numbers(numbers: list) -> list:
    """
    Bug #15: Filter out non-positive numbers (keep strictly n > 0).
    Symptom: Uses >= so 0 is erroneously included.
    Expected: filter_positive_numbers([-2, 0, 3, -1, 5]) -> [3, 5]
    """
    # BUG: >= includes 0, which is not positive
    return [n for n in numbers if n >= 0]


# =====================================================================
# CATEGORY 4: LOGIC & VALIDATION (Bugs 16 - 20)
# =====================================================================

def is_leap_year(year: int) -> bool:
    """
    Bug #16: Check if a given Gregorian year is a leap year.
    Symptom: Checks only divisibility by 4, forgetting the 100/400 century rule.
    Expected: 2000 -> True, 2024 -> True, 1900 -> False, 2100 -> False.
    """
    # BUG: Incomplete leap year rule
    return year % 4 == 0


def calculate_average(numbers: list) -> float:
    """
    Bug #17: Calculate the mathematical average of a list of numbers.
    Symptom: Crashes with ZeroDivisionError when the input list is empty.
    Expected: Should return 0.0 for an empty list.
    """
    # BUG: No check for empty list before division
    return sum(numbers) / len(numbers)


def is_valid_password_length(password: str) -> bool:
    """
    Bug #18: Check if password length is at least 8 characters.
    Symptom: Returns True when password is LESS than 8 characters!
    Expected: "short" -> False, "strongpassword123" -> True.
    """
    # BUG: Inverted condition
    return len(password) < 8


def format_currency_usd(amount: float) -> str:
    """
    Bug #19: Format amount as USD currency string (e.g. "$19.99").
    Symptom: Formats with 1 decimal place instead of 2.
    Expected: format_currency_usd(19.9) -> "$19.90"
    """
    # BUG: .1f instead of .2f
    return f"${amount:.1f}"


def calculate_ticket_price(age: int) -> float:
    """
    Bug #20: Calculate ticket price based on age:
      - Children under 12: $5.0
      - Seniors 65 and above: $7.0
      - Standard adults: $12.0
    Symptom: Logic checks age < 65 instead of age >= 65 for seniors, charging adults senior price!
    Expected: age=10 -> 5.0, age=30 -> 12.0, age=70 -> 7.0.
    """
    if age < 12:
        return 5.0
    # BUG: Condition checks age < 65 instead of age >= 65
    elif age < 65:
        return 7.0
    return 12.0
