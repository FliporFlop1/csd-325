def city_country(city, country, population=None):
    """Return City, Country or City, Country - population xxx."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    return result

# Step 4 - Demo calls
print(city_country("santiago", "chile"))
print(city_country("seattle", "united states", 733919))
print(city_country("paris", "france"))
