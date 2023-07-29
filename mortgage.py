import config


def get_minimal_mortgage_amount() -> int:
    return config.MINIMAL_MORTGAGE


def get_initial_fee(mortgage_amount: int) -> int:
    return int(mortgage_amount * config.INITIAL_FEE_PERCENT / 100)
