def city_country(city, country, language=None, population=None):
    """Return City, Country - population xxx, Language (optional)."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result
