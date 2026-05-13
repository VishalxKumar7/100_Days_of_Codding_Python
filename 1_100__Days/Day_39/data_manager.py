import requests

url = "https://api.sheety.co/487d7180cc74497801bada89544cb925/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_data(self):
        price = requests.get(url=url)
        return price.json()
    
    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }

        requests.put(
            url=f"{url}/{row_id}",
            json=new_data,
            auth=self._authorization
        )
