# 代码生成时间: 2025-10-05 03:34:25
import requests

class CareerPlanningSystem:
    def __init__(self, base_url):
        """
        Initializes the Career Planning System with a base URL for API requests.
        :param base_url: str - The base URL of the API for career planning.
        """
        self.base_url = base_url

    def get_career_advice(self, user_id):
        """
        Retrieves career advice for a given user ID.
        :param user_id: str - The ID of the user to retrieve career advice for.
        :return: dict - A dictionary containing career advice data.
        """
        url = f"{self.base_url}/advice/{user_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def create_user(self, user_data):
        """
        Creates a new user in the system.
        :param user_data: dict - A dictionary containing user data to create.
        :return: dict - A dictionary containing the response from the API.
        """
        url = f"{self.base_url}/users"
        try:
            response = requests.post(url, json=user_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def update_user(self, user_id, update_data):
        """
        Updates an existing user in the system.
        :param user_id: str - The ID of the user to update.
        :param update_data: dict - A dictionary containing data to update.
        :return: dict - A dictionary containing the response from the API.
        """
        url = f"{self.base_url}/users/{user_id}"
        try:
            response = requests.put(url, json=update_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

# Example usage
if __name__ == '__main__':
    base_url = "https://api.careerplanning.com"
    system = CareerPlanningSystem(base_url)
    
    # Create a new user
    user_data = {"name": "John Doe", "email": "john.doe@example.com"}
    created_user = system.create_user(user_data)
    if created_user:
        print(f"User created: {created_user}")
    
    # Get career advice for a user
    user_id = created_user["id"] if created_user else "non-existent-id"
    advice = system.get_career_advice(user_id)
    if advice:
        print(f"Career advice: {advice}")

    # Update an existing user
    update_data = {"email": "john.doe.updated@example.com"}
    updated_user = system.update_user(user_id, update_data)
    if updated_user:
        print(f"User updated: {updated_user}")