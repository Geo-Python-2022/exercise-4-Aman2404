def fahr_to_celsius(temp_fahrenheit):
    """
    This function takes fahrenheit as input and returns celsius temperature.
    """
    temp_celsius=(temp_fahrenheit-32)/1.8
    return temp_celsius


def temp_classifier(temp_celsius):
    """
    This function takes temp_celsius as input and returns classification of that temparature .
    """
    
    if temp_celsius < -2:
        return 0
    
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1

    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    
    else:
        return 3