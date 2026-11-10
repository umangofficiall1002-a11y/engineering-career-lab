test_results = [
    {"name": "Login Test", "status": "Passed", "priority": "High"},
    {"name": "Checkout Test", "status": "Failed", "priority": "High"},
    {"name": "Search Test", "status": "Passed", "priority": "Medium"},
    {"name": "Payment Test", "status": "Failed", "priority": "High"},
    {"name": "Profile Test", "status": "Skipped", "priority": "Low"}
]

def filter_by_status(test_results, status):
    filtered_results = []
    for result in test_results:
        if result["status"] == status:
            filtered_results.append(result)
    return filtered_results

def search_test(test_results, test_name):
    for result in test_results:
        if result["name"] == test_name:
            return result
    return None


user_input = input("Enter a test name to search(without Test keyword or any special characters): ")
searched_test = user_input + " Test"
print(f"Searched Test Result: {search_test(test_results, searched_test)}")

filtered_failed_tests = filter_by_status(test_results, "Failed")
for test in filtered_failed_tests:
    print(f"Failed Test: {test}")