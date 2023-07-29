def handle_amount(message: str) -> int | bool:
    try:
        return int(message)
    except ValueError:
        return False
