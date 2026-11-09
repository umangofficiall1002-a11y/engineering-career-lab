testDetails = {
    "Login" : "Passed",
    "Search" : "Passed",
    "Payment" : "Failed",
    "Logout" : "Skipped",
    "Profile" : "Blocked"
    }

print("Test Execution Details:")
count = 0
failed = 0
passed = 0
skipped = 0
blocked = 0
unknown = 0
failedTests = []
for test, status in testDetails.items():
    print(f"{test}: {status}")
    count += 1
    if status == "Failed":
        failed += 1
        failedTests.append(test)
    elif status == "Skipped":
        skipped += 1
    elif status == "Blocked":
        blocked += 1
    elif status == "Passed":
        passed += 1
    else:
        unknown += 1

print(f"\nTotal tests executed: {count}")
print(f"Tests Failed: {failed}")
print(f"Tests Passed: {passed}")
print(f"Tests Skipped: {skipped}")
print(f"Tests Blocked: {blocked}")
print(f"Tests Unknown: {unknown}")
print(f"Failed Tests: {failedTests}")
print(f"pass percentage:{(passed/count)*100}%")
