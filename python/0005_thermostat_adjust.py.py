def adjust_thermostat(current_f, target_c):

    target_c = ((target_c * 1.8) + 32)

    if target_c > current_f:
        x = target_c - current_f
        return f"Heat: {round(x, 1)} degrees Fahrenheit"

    elif target_c < current_f:
        x = current_f - target_c
        return f"Cool: {round(x, 1)} degrees Fahrenheit"

    return "Hold"

print(adjust_thermostat(32, 0))
print(adjust_thermostat(70, 25))
print(adjust_thermostat(72, 18))
print(adjust_thermostat(212, 100))
print(adjust_thermostat(59, 22))
