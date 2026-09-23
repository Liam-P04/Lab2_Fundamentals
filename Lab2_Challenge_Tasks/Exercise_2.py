# APPENDIX EXERCISE 2: SIGNAL CHARACTER ANALYSIS
# Build a signal from the surname and seed, then normalize it.
ENGINEER = "Pabiona"
SEED_NUM = 0

generated_signal: str = ENGINEER + str(SEED_NUM)
processed_signal = generated_signal.strip().upper()

print("Generated Signal:", generated_signal)
print("Processed Signal:", processed_signal)
print("Character Analysis:")
for character in processed_signal:
    if character.isalpha():
        character_type = "LETTER"
    elif character.isdigit():
        character_type = "NUMBER"
    elif character.isspace():
        character_type = "SPACE"
    else:
        character_type = "OTHER"
    print(f"{character!r}: {character_type}")

letter_count = sum(character.isalpha() for character in processed_signal)
digit_count = sum(character.isdigit() for character in processed_signal)
other_count = len(processed_signal) - letter_count - digit_count
print(f"Signal Classification: {letter_count} letters, {digit_count} numbers, {other_count} other")
