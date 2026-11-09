# Mission 1 - Test Execution Intelligence

## Mission Goal

Is mission mein humne ek simple Python program banaya jo test execution results ko analyze karta hai.

Real testing projects mein hundreds ya thousands of test cases run hote hain. Har test ka ek status hota hai, jaise Passed, Failed, Skipped ya Blocked. Hamara program in results ko read karke useful summary banata hai.

---

# Concepts Learned

## 1. Variables

Variable ko ek labelled container samjho jisme hum data store karte hain.

Example:

```python
passed = 0
failed = 0
```

Yahan `passed` aur `failed` counters hain. Jab bhi matching test milta hai, hum inki value increase karte hain.

---

## 2. Lists

List ka use multiple values ko ek jagah store karne ke liye hota hai.

Example:

```python
failed_tests = []
```

Agar koi test fail hota hai, uska naam list mein add kar sakte hain:

```python
failed_tests.append(test_name)
```

Simple language mein: list ek collection hai jahan hum related cheezein store kar sakte hain.

---

## 3. Dictionaries

Mission ke initial version mein test results ko dictionary mein store kiya tha.

Example:

```python
test_details = {
    "Login": "Passed",
    "Payment": "Failed"
}
```

Dictionary mein data key-value pair mein store hota hai. Yahan test name key hai aur uska execution status value hai.

---

## 4. Tuples

Upgrade 3 mein test results ko tuples ke form mein use kiya:

```python
("Login Test", "Passed")
```

Tuple related values ko ek saath store karta hai. Is case mein ek test ka naam aur uska status ek pair ke form mein hain.

---

## 5. Loops

Loop ka use repeated kaam automatically karne ke liye hota hai.

Example:

```python
for test_name, status in test_results:
```

Iska simple meaning hai: test results mein ek-ek item lo aur uske test name aur status ke saath kaam karo.

Testing automation mein loops bahut useful hote hain jab hume multiple test cases, API responses ya data records process karne hote hain.

---

## 6. Tuple Unpacking

Ye Mission 1 Upgrade 3 ka important concept tha.

Ek tuple:

```python
("Login Test", "Passed")
```

ko directly do variables mein unpack kar sakte hain:

```python
for test_name, status in test_results:
```

Python automatically pehli value `test_name` aur doosri value `status` mein assign kar deta hai.

---

## 7. Conditional Logic

Program ko decision lene ke liye `if / elif / else` use kiya.

Example:

```python
if status == "Failed":
    failed += 1
elif status == "Passed":
    passed += 1
else:
    unknown += 1
```

Simple language mein: agar status Failed hai to failed counter badhao; warna doosri conditions check karo.

---

## 8. Counters

Counter ek variable hota hai jo occurrences count karta hai.

Example:

```python
failed += 1
```

Har failed test milne par failed counter ek se increase hota hai.

Humne Passed, Failed, Skipped, Blocked aur Unknown statuses ke liye counters use kiye.

---

## 9. append()

`.append()` list ke end mein nayi value add karta hai.

Example:

```python
failed_tests.append(test_name)
```

Isse sirf failed test names collect kiye ja sakte hain aur end mein unki separate list print ki ja sakti hai.

---

## 10. f-Strings

Output ko readable banane ke liye f-strings use kiye.

Example:

```python
print(f"Tests Failed: {failed}")
```

Curly brackets ke andar variable ki current value automatically output mein aa jati hai.

---

# What We Built

Mission ke end tak program ye kaam karta hai:

1. Test execution results read karta hai.
2. Har result ko loop ke through process karta hai.
3. Status ke basis par decision leta hai.
4. Passed, Failed, Skipped aur Blocked tests count karta hai.
5. Failed test names ek list mein store karta hai.
6. Final execution summary print karta hai.

---

# Engineering Connection

Abhi ye ek small Python program hai, lekin same thinking real automation frameworks mein use hoti hai.

Future mein isi type ki logic ka use ho sakta hai:

- Test reports analyze karne mein
- API response data process karne mein
- Database records validate karne mein
- Failed test rerun logic banane mein
- Custom execution dashboards ya summaries create karne mein

## Mission 1 Key Takeaway

**Data ko store karo -> loop se process karo -> conditions se decision lo -> useful result collect karo -> readable summary banao.**

Ye Mission 1 ki core engineering thinking hai.
