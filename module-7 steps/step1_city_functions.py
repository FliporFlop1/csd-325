def city_country(city, country):
    """Return a string in the format City, Country."""
    return f"{city.title()}, {country.title()}"

# Step 1 - Demo calls
print(city_country("santiago", "chile"))
print(city_country("seattle", "united states"))
print(city_country("paris", "france"))
