# APPENDIX EXERCISE 1: SENSOR MONITORING
# Generate a fixed set of readings from the surname and SEED_NUM.
ENGINEER = "Pabiona"
SEED_NUM = 0
readings = [(ord(letter) + SEED_NUM) % 101 for letter in ENGINEER]
valid_readings = []
invalid_readings = []
classification_results = []

for reading in readings:
    if not isinstance(reading, int) or not 0 <= reading <= 100:
        invalid_readings.append(reading)
        continue

    valid_readings.append(reading)
    if reading < 30:
        classification = "LOW"
    elif reading <= 70:
        classification = "NORMAL"
    else:
        classification = "HIGH"
    classification_results.append((reading, classification))

print("Generated Sensor Data:", readings)
print("Valid Results:", valid_readings)
print("Invalid Results:", invalid_readings)
print("Classification Results:", classification_results)
print("Summary: {} valid, {} invalid".format(len(valid_readings), len(invalid_readings)))
