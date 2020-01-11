from data_fetch import get_real_states_prices
from calculations import calculate_average_price, calculate_min_price, calculate_max_price
from helper import get_timestamp
from data_populate import populate_db

def lambda_handler(event, context):
    populate()

def process_data():
    real_state_prices = get_real_states_prices()
    mean = calculate_average_price(real_state_prices)
    min_price = calculate_min_price(real_state_prices)
    max_price = calculate_max_price(real_state_prices)
    created_at = get_timestamp()

    processed_data = {
        "mean": mean,
        "min_price": min_price,
        "max_price": max_price,
        "created_at": created_at
    }

    return (processed_data)


def populate():
    processed_data = process_data()
    populate_db(processed_data["mean"],
                processed_data["min_price"],
                processed_data["max_price"],
                processed_data["created_at"])
    if processed_data:
        return "Success"
