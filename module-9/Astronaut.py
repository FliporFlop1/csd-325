import requests

# Connect to OpenNotify API
url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)

# Raw output
print("Raw Response:")
print(response.text)

# Formatted output
print("\nFormatted Astronaut Data:")
if response.status_code == 200:
    data = response.json()
    print(f"Number of people in space: {data['number']}")
    for person in data['people']:
        print(f"{person['name']} on {person['craft']}")
else:
    print("Failed to retrieve astronaut data.")
