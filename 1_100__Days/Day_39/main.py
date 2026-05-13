from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from pprint import pprint
import os
from requests_cache import CachedSession
from flight_data import find_cheapest_flight

cache_dir = "1_100__Days/Day_39"
cache_name = "flight_cache"
cache_path = os.path.join(cache_dir, cache_name)

session = CachedSession(cache_path, expire_after=3600)
session.get('https://gist.github.com/TheMuellenator/0ded5ee9378e6296df111293a9030e65/get')

data_manager = DataManager()
sheet_data = data_manager.get_data()
print(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

flight_search = FlightSearch()

for destination in sheet_data["prices"]:
    flights = flight_search.check_flights(
        origin_city_code="LHR",  # ✅ airport code, not city code
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flights is None:
        print(f"No flights found for {destination['city']}, skipping.")
        continue

    cheapest_flights = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))  # ✅ fixed

    if cheapest_flights.price != "N/A" and cheapest_flights.price < destination["lowestPrice"]:
        print(f"Lower price found! {destination['city']}: GBP {cheapest_flights.price}")