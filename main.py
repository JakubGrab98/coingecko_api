from api_requests import get_api_data, save_json_file
import const as ct


parameters = {
    "vs_currency": "USD",
}


if __name__ == "__main__":
    for page in range(1, 31, 1):
        parameters["page"] = page
        data = get_api_data(ct.MARKET_DATA_URL, parameters)
        save_json_file(data, "data/raw/market_data", f"market_data-page={page}")
