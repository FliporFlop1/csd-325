def city_country(city, country, population):
    """Return a string in the format City, Country - population xxx."""
    return f"{city.title()}, {country.title()} - population {population}"

# Step 3 - Demo calls
print(city_country("santiago", "chile", 5000000))
print(city_country("seattle", "united states", 733919))
print(city_country("paris", "france", 2148000))
