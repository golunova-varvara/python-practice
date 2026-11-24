def get_weather_recommendation(temperature):
    """
    Get a weather recommendation based on the air temperature.

    Args:
        temperature (int, float): air temperature in degrees Celsius

    Returns:
        str: weather recommendation or an error message
    """
    if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
        return "Error: temperature must be a number"
    elif temperature < -20:
        return "Dangerously cold — stay at home"
    elif temperature < -5:
        return "Very cold — dress as warmly as possible"
    elif temperature <= 5:
        return "Cold — wear a warm jacket, hat, and gloves"
    elif temperature <= 15:
        return "Cool — take a windbreaker or a light jacket"
    elif temperature <= 25:
        return "Warm — you can walk in light clothes"
    else:  # temperature > 25
        return "Hot — drink plenty of water and wear a hat"


# Testing
print(get_weather_recommendation(-40))
print(get_weather_recommendation(-10))
print(get_weather_recommendation(0))
print(get_weather_recommendation(10))
print(get_weather_recommendation(20))
print(get_weather_recommendation(30))

# Invalid data
print(get_weather_recommendation("Temperature"))
print(get_weather_recommendation(None))