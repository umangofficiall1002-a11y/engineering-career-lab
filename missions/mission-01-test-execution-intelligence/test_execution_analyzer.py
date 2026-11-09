testDetails = {
    "Login" : "Passed",
    "Search" : "Passed",
    "Payment" : "Failed",
    "Logout" : "Passed"
    }

print("Test Execution Details:")
count = 0
Failed = 0
Passed = 0
for test, status in testDetails.items():
    print(f"{test}: {status}")
    count += 1
    if status == "Failed":
        Failed += 1
    else:
        Passed += 1

print(f"\nTotal tests executed: {count}")
print(f"Tests Failed: {Failed}")
print(f"Tests Passed: {Passed}")
print(f"pass percentage:{(Passed/count)*100}%")