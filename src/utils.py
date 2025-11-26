def is_number(value):
    # Issue #11: Fix utils.is_number for negative numbers
    return str(value).isdigit()
