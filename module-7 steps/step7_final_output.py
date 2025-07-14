def city_country(city, country, language=None, population=None):
    """Return City, Country - population xxx, Language (optional)."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Step 7 - Final demo calls
print(city_country("santiago", "chile", population=5000000, language="spanish"))
print(city_country("seattle", "united states", population=733919))
print(city_country("tokyo", "japan", population=13929286, language="japanese"))
