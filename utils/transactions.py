import re
import uuid


def is_hexadecimal(value):
    pattern = r'^[0-9a-fA-F]+$'
    return bool(re.fullmatch(pattern, value))

def generate_internal_transaction_id():
    return uuid.uuid4()