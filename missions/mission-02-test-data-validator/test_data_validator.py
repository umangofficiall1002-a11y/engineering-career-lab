test_cases = [
    {"name": "Login Test", "priority": "High", "status": "Active"},
    {"name": "Checkout Test", "priority": "Medium", "status": "Active"},
    {"name": "", "priority": "Critical", "status": "Active"},
    {"name": "Payment Test", "priority": "Low", "status": "Inactive"},
    {"name": "Search Test", "priority": "Critical", "status": "Unknown"}
]
valid_test_cases = len(test_cases)
invalid_test_cases = 0
invalid_errors = 0
allowed_priorities = ["Low", "Medium", "High"]
check_invalid = 0
print("Invalid test cases:")
for test_case in test_cases:
    if test_case["name"] == "":
        print(f"Test case with empty name found")
        invalid_errors += 1
        invalid_test_cases += 1
        valid_test_cases -= 1
        check_invalid = 1
    if test_case["priority"] not in allowed_priorities:
        print(f"Test case '{test_case['name']}' has invalid priority: {test_case['priority']}")
        invalid_errors += 1
        if check_invalid != 1:
            invalid_test_cases += 1
            valid_test_cases -= 1
            check_invalid = 1
    if test_case["status"] not in ["Active", "Inactive"]:
        print(f"Test case '{test_case['name']}' has invalid status: {test_case['status']}")
        invalid_errors += 1
        if check_invalid != 1:
            invalid_test_cases += 1
            valid_test_cases -= 1
    check_invalid = 0

print(f"\nValid test cases: {valid_test_cases}")
print(f"Invalid test cases: {invalid_test_cases}")
print(f"Total invalid errors: {invalid_errors}")