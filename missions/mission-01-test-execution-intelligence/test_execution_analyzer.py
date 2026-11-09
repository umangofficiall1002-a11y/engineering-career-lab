testDetails = {
    "Login" : "Passed",
    "Search" : "Passed",
    "Payment" : "Failed",
    "Logout" : "Passed"
    }

print("Test Execution Details:")
for test, status in testDetails.items():
    print(f"{test}: {status}")