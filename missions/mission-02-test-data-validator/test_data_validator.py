test_cases = [
    {"name": "Login Test", "priority": "High", "status": "Active"},
    {"name": "Checkout Test", "priority": "Medium", "status": "Active"},
    {"name": "", "priority": "High", "status": "Active"},
    {"name": "Payment Test", "priority": "Low", "status": "Inactive"},
    {"name": "Search Test", "priority": "Critical", "status": "Active"}
]
valid_test_cases = 0
invalid_test_cases = 0
print("Invalid test cases:")
for test_case in test_cases:
    if test_case["name"] == "":
        print(f"Test case with empty name found")
        invalid_test_cases += 1
    elif test_case["priority"] not in ["Low", "Medium", "High"]:
        print(f"Test case '{test_case['name']}' has invalid priority: {test_case['priority']}")
        invalid_test_cases += 1
    elif test_case["status"] not in ["Active", "Inactive"]:
        print(f"Test case '{test_case['name']}' has invalid status: {test_case['status']}")
        invalid_test_cases += 1
    else:
        valid_test_cases += 1

print(f"\nValid test cases: {valid_test_cases}")
print(f"Invalid test cases: {invalid_test_cases}")