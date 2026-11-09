count = 0
failed = 0
passed = 0
skipped = 0
blocked = 0
unknown = 0
failed_tests = []

# testDetails = {
#     "Login" : "Passed",
#     "Search" : "Passed",
#     "Payment" : "Failed",
#     "Logout" : "Skipped",
#     "Profile" : "Blocked"
#     }

# print("Test Execution Details:")
# for test, status in testDetails.items():
#     print(f"{test}: {status}")
#     count += 1
#     if status == "Failed":
#         failed += 1
#         failed_tests.append(test)
#     elif status == "Skipped":
#         skipped += 1
#     elif status == "Blocked":
#         blocked += 1
#     elif status == "Passed":
#         passed += 1
#     else:
#         unknown += 1

# print(f"\nTotal tests executed: {count}")
# print(f"Tests Failed: {failed}")
# print(f"Tests Passed: {passed}")
# print(f"Tests Skipped: {skipped}")
# print(f"Tests Blocked: {blocked}")
# print(f"Tests Unknown: {unknown}")
# print(f"Failed Tests: {failed_tests}")
# print(f"pass percentage:{(passed/count)*100}%")

test_results = [
    ("Login Test", "Passed"),
    ("Checkout Test", "Failed"),
    ("Search Test", "Passed"),
    ("profile Test", "Skipped"),
    ("Payment Test", "Failed"),
    ("Logout Test", "Blocked")
]

for test_name, status in test_results:
    count += 1
    if status == "Failed":
        failed += 1
        failed_tests.append(test_name)
    elif status == "Skipped":
        skipped += 1
    elif status == "Blocked":
        blocked += 1
    elif status == "Passed":
        passed += 1
    else:
        unknown += 1

print(f"Test Execution Summary:")
print(f"-----------------------")
print(f"Total tests executed: {count}")
print(f"Tests Failed: {failed}")
print(f"Tests Passed: {passed}")
print(f"Tests Skipped: {skipped}")
print(f"Tests Blocked: {blocked}")
# print(f"Tests Unknown: {unknown}")
print(f"\nFailed Tests:")
for failed_test in failed_tests:
    print(f" - {failed_test}")