# 代码生成时间: 2025-08-23 03:28:48
import requests
import json
from datetime import datetime
import random
import string

"""
Test Data Generator

This module generates random test data for various data types such as
names, emails, dates, and phone numbers. It can be extended to include
more data types as needed.
"""

class TestDataGenerator:
    def generate_name(self):
        """Generates a random name."""
        first_names = ['John', 'Jane', 'Emily', 'Michael', 'Sarah']
        last_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown']
        return ' '.join(random.choice(first_names), random.choice(last_names))

    def generate_email(self):
        """Generates a random email address."""
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        return f"{username}@{random.choice(domains)}"

    def generate_date(self):
        """Generates a random date between 1900 and 2023."""
        start_date = datetime(1900, 1, 1)
        end_date = datetime(2023, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date.strftime('%Y-%m-%d')

    def generate_phone_number(self):
        """Generates a random phone number."""
        return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

    def generate_test_data(self, num_records):
        """Generates a list of test data records."""
        test_data = []
        for _ in range(num_records):
            test_data.append({
                'name': self.generate_name(),
                'email': self.generate_email(),
                'date': self.generate_date(),
                'phone_number': self.generate_phone_number()
            })
        return test_data

# Example usage
if __name__ == '__main__':
    generator = TestDataGenerator()
    num_records = 10  # Number of test data records to generate
    test_data = generator.generate_test_data(num_records)
    print(json.dumps(test_data, indent=4))
