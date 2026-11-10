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
check_invalid = True
validation_errors = {}
print("Validating test cases:")
for test_case in test_cases:
    if test_case["name"] == "":
        test_case["name"] = "Unknown Test"
        validation_errors[test_case["name"]] = ["Test case with empty name found"]
        invalid_errors += 1
        check_invalid = False
    else:
        validation_errors[test_case["name"]] = []
    if test_case["priority"] not in allowed_priorities:
        
        validation_errors[test_case["name"]].append(f"Invalid priority: {test_case['priority']}")
        invalid_errors += 1
        check_invalid = False
    if test_case["status"] not in allowed_statuses:
        validation_errors[test_case["name"]].append(f"Invalid status: {test_case['status']}")
        invalid_errors += 1
        check_invalid = False
    
    if check_invalid:
        valid_test_cases += 1
        print(f" {test_case['name']} : {validation_errors.get(test_case['name'])}")
    else:
        invalid_test_cases += 1
        print(f" {test_case['name']} : {validation_errors.get(test_case['name'])}")
    check_invalid = True
    validation_errors.clear()

print(f"\nValid test cases: {valid_test_cases}")
print(f"Invalid test cases: {invalid_test_cases}")
print(f"Total invalid errors: {invalid_errors}")