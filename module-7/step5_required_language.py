def city_country(city, country, language, population=None):
    """Return City, Country - population xxx, Language."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    result += f", {language.title()}"
    return result

# Step 5 - Demo calls
print(city_country("santiago", "chile", "spanish", 5000000))
print(city_country("seattle", "united states", "english", 733919))
print(city_country("paris", "france", "french", 2148000))
