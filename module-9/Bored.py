import requests

# Connect to the Bored API
url = "https://bored-api.appbrewery.com/random"
response = requests.get(url)

print("==== Raw JSON Response ====")
print(response.text)

print("\n==== Formatted Activity Suggestion ====")
if response.status_code == 200:
    data = response.json()
    activity = data.get("activity")
    activity_type = data.get("type")
    participants = data.get("participants")

    print(f"Activity: {activity}")
    print(f"Type: {activity_type}")
    print(f"Participants: {participants}")
else:
    print("Failed to retrieve activity.")
