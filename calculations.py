def calculate_average_price(real_state_prices):
    real_state_prices_mean = sum(real_state_prices) / len(real_state_prices)
    return real_state_prices_mean


def calculate_min_price(real_state_prices):
    min_price = min(real_state_prices)
    return min_price


def calculate_max_price(real_state_prices):
    max_price = max(real_state_prices)
    return max_price
