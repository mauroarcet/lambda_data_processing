from data_fetch import get_real_states_prices
from calculations import calculate_average_price, calculate_min_price, calculate_max_price


# pass: 8cFyBJW!*71g, name dataProcessingDb, user: postgres

def main():
    real_state_prices = get_real_states_prices()
    return (calculate_average_price(real_state_prices),
            calculate_min_price(real_state_prices),
            calculate_max_price(real_state_prices)
            )


if __name__ == '__main__':
    print(main())
