test_cases = [
    {"name": "Login Test", "priority": "High", "status": "Active"},
    {"name": "Checkout Test", "priority": "Medium", "status": "Active"},
    {"name": "", "priority": "Critical", "status": "Active"},
    {"name": "Payment Test", "priority": "Low", "status": "Inactive"},
    {"name": "Search Test", "priority": "Critical", "status": "Unknown"}
]
valid_test_cases = 0
invalid_test_cases = 0
invalid_errors = 0
allowed_priorities = ["Low", "Medium", "High"]
allowed_statuses = ["Active", "Inactive"]
is_valid = True
validation_errors = {}
print("Validating test cases:")
for test_case in test_cases:
    display_name = test_case["name"] or "Unknown Test"
    if test_case["name"] == "":
        validation_errors[display_name] = ["Test case with empty name found"]
        invalid_errors += 1
        is_valid = False
    else:
        validation_errors[display_name] = []
    if test_case["priority"] not in allowed_priorities:
        validation_errors[display_name].append(f"Invalid priority: {test_case['priority']}")
        invalid_errors += 1
        is_valid = False
    if test_case["status"] not in allowed_statuses:
        validation_errors[display_name].append(f"Invalid status: {test_case['status']}")
        invalid_errors += 1
        is_valid = False
    
    if is_valid:
        valid_test_cases += 1
    else:
        invalid_test_cases += 1
    is_valid = True

for test_case, errors in validation_errors.items():
    if errors:
        print(f"Test case '{test_case}' has the following validation errors:")
        for error in errors:
            print(f" - {error}")

print(f"\nValid test cases: {valid_test_cases}")
print(f"Invalid test cases: {invalid_test_cases}")
print(f"Total invalid errors: {invalid_errors}")
