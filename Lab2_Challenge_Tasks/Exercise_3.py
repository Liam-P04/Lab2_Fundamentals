# APPENDIX EXERCISE 3: LIMITED PASSWORD AUTHENTICATION
# Create a unique credential and stop after a seed-based attempt limit.
ENGINEER = "Pabiona"
SEED_NUM = 0

generated_password = ENGINEER.upper() + str(SEED_NUM)
attempt_limit = max(3, SEED_NUM + 3)
correct_attempt = generated_password
attempts = ["WRONG", "INVALID", correct_attempt]
access_granted = False

for attempt_number, entered_password in enumerate(attempts[:attempt_limit], start=1):
    if entered_password == generated_password:
        access_granted = True
        print(f"Attempt {attempt_number}: Access granted")
        break
    print(f"Attempt {attempt_number}: Access denied")

if access_granted:
    final_system_state = "UNLOCKED"
else:
    final_system_state = "LOCKED - ATTEMPT LIMIT REACHED"

print("Generated Password:", generated_password)
print("Attempt Limit:", attempt_limit)
print("Attempts Made:", min(len(attempts), attempt_limit))
print("Access Result:", "GRANTED" if access_granted else "DENIED")
print("Final System State:", final_system_state)
