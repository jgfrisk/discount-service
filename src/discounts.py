import secrets
import string
from typing import List


discount_string_length = 10
discount_string_chars = string.ascii_letters + string.digits  # 62 characters
# These parameters amount to just below 60 bits of randomness which should
# give enough collission resistanse for this demo (log2(62) ~= 5.95 )
# see: https://en.wikipedia.org/wiki/Birthday_attack


def random_letters(n: int) -> str:
    """
    Generate a random string of length n from the list of characters.
    Uses secrets for strong cryptograhpy to avoid collissions.
    """
    return "".join([secrets.choice(discount_string_chars) for i in range(0, n)])


def generate_strings(n: int, length: int) -> List[str]:
    """
    Generate a list of n random strings codes of a specified length.
    """
    return [random_letters(length) for i in range(0, n)]


def create_discount_codes(n: int) -> List[str]:
    """
    Helper method to create n discount codes accoring to our definitions.
    """
    discount_codes = generate_strings(n, discount_string_length)

    return discount_codes
