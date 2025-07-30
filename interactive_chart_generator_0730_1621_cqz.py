# 代码生成时间: 2025-07-30 16:21:24
import requests
import json
from pyfiglet import figlet_format

"""
Interactive Chart Generator

This program uses the requests framework to interact with a web API for generating
interactive charts. It follows Python best practices, includes error handling,
and is well-documented and structured for maintainability and scalability.
"""

# Define constants
API_URL = "https://api.example.com/generate_chart"
HEADERS = {"Content-Type": "application/json"}

def get_chart_data(chart_type, data):
    """
    Send a POST request to the API to generate chart data.

    Args:
        chart_type (str): The type of chart to generate (e.g., 'line', 'bar').
        data (list of tuples): The data points to plot on the chart.

    Returns:
        dict: The chart data returned from the API.
    """
    payload = {
        "chart_type": chart_type,
        "data": data
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def display_chart(chart_data):
    """
    Display the chart data in the console using ASCII art.

    Args:
        chart_data (dict): The chart data returned from the API.
    """
    if chart_data is None:
        print("No chart data to display.")
        return

    # Extract the chart data points
    data_points = chart_data.get("data", [])
    if not data_points:
        print("No data points to display.")
        return

    # Print the chart title
    print(figlet_format(chart_data.get("title", "Interactive Chart")))

    # Print each data point
    for point in data_points:
        print(f"{point[0]}: {point[1]}")

def main():
    """
    Main function to interact with the user and generate charts.
    """
    print(figlet_format("Interactive Chart Generator"))
    chart_type = input("Enter chart type (e.g., 'line', 'bar'): ")
    data = []
    while True:
        x = input("Enter x-value (or 'done' to finish): ")
        if x.lower() == "done":
            break
        y = input("Enter y-value: ")
        try:
            data.append((float(x), float(y)))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

    chart_data = get_chart_data(chart_type, data)
    display_chart(chart_data)

if __name__ == "__main__":
    main()