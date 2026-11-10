# Mission 2 - Test Data Validator

## Mission Goal

Is mission mein humne ek Python program banaya jo test case data ko validate karta hai.

Real automation projects mein test data different sources se aa sakta hai, jaise JSON, Excel, APIs ya databases. Test execute karne se pehle data valid hai ya nahi check karna important hota hai.

Mission 2 mein humne simple validation se start karke code ko gradually reusable aur structured banaya.

---

# Concepts Learned

## 1. Data Validation

Data validation ka simple meaning hai: **data ko use karne se pehle check karna ki woh expected rules follow karta hai ya nahi.**

Example rules:

- Test name empty nahi hona chahiye.
- Priority allowed values mein honi chahiye.
- Status valid hona chahiye.

Real automation mein validation useful hoti hai jab:

- API request bhejne se pehle input check karna ho.
- Excel ya JSON test data validate karna ho.
- Configuration values missing hon.
- Invalid records ko identify karna ho.

---

## 2. List of Dictionaries

Mission mein test data kuch is tarah tha:

```python
test_cases = [
    {"name": "Login Test", "priority": "High", "status": "Active"},
    {"name": "Payment Test", "priority": "Low", "status": "Inactive"}
]
```

Yahan:

- **List** multiple test cases ko hold karti hai.
- Har **dictionary** ek individual test case represent karti hai.

Dictionary se values access kar sakte hain:

```python
test_case["name"]
test_case["priority"]
test_case["status"]
```

---

## 3. Membership Check with `in` and `not in`

Allowed values define karke hum check kar sakte hain ki input valid hai ya nahi.

Example:

```python
allowed_priorities = ["Low", "Medium", "High"]

if test_case["priority"] not in allowed_priorities:
    print("Invalid priority")
```

Simple meaning: check karo ki priority allowed list ka part hai ya nahi.

Ye pattern validation code mein bahut commonly use hota hai.

---

## 4. Independent `if` Statements vs `elif`

Initial validation mein `elif` use karne se ek problem thi.

Agar pehli condition true ho gayi, to baaki validations check nahi hoti.

Example:

```python
if name_is_invalid:
    ...
elif priority_is_invalid:
    ...
```

Agar ek test case mein multiple problems hon, to `elif` chain sirf pehla matching error detect karegi.

Upgrade 1 mein humne independent `if` statements use kiye:

```python
if name_is_invalid:
    ...

if priority_is_invalid:
    ...

if status_is_invalid:
    ...
```

Ab har validation independently run hoti hai aur multiple errors detect ho sakte hain.

---

## 5. Boolean Flag

Ek test case valid hai ya invalid, ye track karne ke liye Boolean flag use kiya:

```python
is_valid = True
```

Agar koi validation fail hoti hai:

```python
is_valid = False
```

Saari validations ke baad:

```python
if is_valid:
    valid_test_cases += 1
else:
    invalid_test_cases += 1
```

Simple language mein, Boolean flag ek **yes/no indicator** hai jo program ko final decision lene mein help karta hai.

---

## 6. Counting Test Cases vs Counting Errors

Ek important difference:

Ek test case mein multiple errors ho sakte hain.

For example:

- Empty name
- Invalid priority
- Invalid status

Ye **3 errors** hain, lekin **1 invalid test case** hai.

Isliye humne separately track kiya:

- `valid_test_cases`
- `invalid_test_cases`
- `invalid_errors`

Ye real reporting aur validation systems mein important distinction hai.

---

## 7. Structured Error Collection

Errors ko sirf immediately print karne ke bajaye, humne unhe dictionary mein collect kiya.

Conceptually:

```python
validation_errors = {
    "Unknown Test": [
        "Test case with empty name found",
        "Invalid priority: Critical"
    ],
    "Search Test": [
        "Invalid priority: Critical",
        "Invalid status: Unknown"
    ]
}
```

Is structure ka benefit ye hai ki error aur uska related test case ek saath store rehte hain.

Later isi data ko:

- Report mein use kar sakte hain.
- JSON mein convert kar sakte hain.
- Logs mein save kar sakte hain.
- API response mein return kar sakte hain.

---

## 8. Fallback Values

Agar test name empty ho, reporting ke liye readable name use kiya:

```python
display_name = test_case["name"] or "Unknown Test"
```

Iska simple meaning:

- Agar test name available hai, use use karo.
- Agar empty hai, `"Unknown Test"` use karo.

Is approach ka advantage ye hai ki original test data modify nahi hota.

---

## 9. Functions

Mission 2 ka major new concept tha **functions**.

Function ko ek reusable machine samjho:

> Input do → specific kaam kare → result wapas de.

Example:

```python
def validate_test_cases(test_cases):
    # validation logic
    return results
```

Function banane ka benefit:

- Same logic baar-baar use kar sakte hain.
- Code organized hota hai.
- Testing easier hoti hai.
- Automation framework mein reusable components ban sakte hain.

---

## 10. Function Parameters

Function ko input dene ke liye parameter use hota hai:

```python
def validate_test_cases(test_cases):
```

Yahan `test_cases` function ka input hai.

Function ko alag-alag data ke saath call kar sakte hain:

```python
validate_test_cases(test_cases)
```

---

## 11. Return Values

Function sirf print karne ke bajaye useful results caller ko return kar sakta hai.

Example:

```python
return valid_test_cases, invalid_test_cases, invalid_errors, validation_errors
```

Function call ke baad results variables mein store kiye:

```python
valid, invalid, total_errors, errors = validate_test_cases(test_cases)
```

Isse function ka kaam aur reporting ka kaam separate ho jata hai.

---

## 12. Tuple Unpacking Revisited

Function multiple values return karta hai to Python un values ko variables mein unpack kar sakta hai:

```python
valid, invalid, total_errors, errors = validate_test_cases(test_cases)
```

Ye Mission 1 mein seekha hua tuple unpacking concept ka practical use hai.

---

# Engineering Pattern Learned

Mission 2 ke end tak hamara program ye flow follow karta hai:

```text
Input Test Data
       ↓
Validate Each Test Case
       ↓
Collect Validation Errors
       ↓
Count Results
       ↓
Return Structured Data
       ↓
Generate Report
```

Ye pattern real software engineering mein commonly use hota hai.

## Separation of Responsibilities

Humne do responsibilities separate ki:

### Function ka kaam

- Data validate karna
- Errors collect karna
- Results return karna

### Main code ka kaam

- Returned results ko use karna
- Final report print karna

Isse code more reusable aur maintainable banta hai.

---

# What We Built

Mission ke end tak hum ek reusable validator bana chuke hain jo:

1. Multiple test cases process karta hai.
2. Required fields validate karta hai.
3. Allowed priority aur status values check karta hai.
4. Ek test case ke multiple errors detect karta hai.
5. Errors ko structured format mein collect karta hai.
6. Valid test cases aur invalid test cases separately count karta hai.
7. Total validation errors track karta hai.
8. Results ko reusable function se return karta hai.

---

# Mission 2 Key Takeaway

**Validate the data → collect the problems → return structured results → report them separately.**

Mission 2 ne hume ek important engineering lesson diya:

> **Working code important hai, lekin reusable aur well-structured code long-term engineering ke liye aur bhi important hota hai.**
