# Coverage Report (short)

## Analysis of `is_shipping_free`

Executable statements (counted):
1. print("Additional Statement 1")
2. print("Additional Statement 2")  # inside first if
3. print("Additional Statement 3")  # inside second if
4. print("Additional Statement 4(discount)")  # inside elif
5. return False
6. return True
7. print("Additional Statement 5")  # unreachable after return

Total statements: 7

Branches (conditions):
- A: `price > 50 or isPrimeShoppingMember` -> True/False (2 branches)
- B: `price > 25 and numberOfItems < 3` -> True/False (2 branches)
- C: `price > 10 and numberOfItems == 1` (elif) -> True/False (2 branches)
Total branches: 6

Given tests (union of executed statements):
- Test1: is_shipping_free(30,2,True)  -> executes statements: 1,2,3,6
- Test2: is_shipping_free(15,1,False) -> executes statements: 1,4,5
- Test3: is_shipping_free(15,1,True)  -> executes statements: 1,2,4,5
- Test4: is_shipping_free(50,1,False) -> executes statements: 1,3,6

Union = {1,2,3,4,5,6} => 6 statements covered out of 7.

**Statement coverage** = 6 / 7 = 85.71%

**Branch coverage**:
- A: True and False covered (2/2)
- B: True and False covered (2/2)
- C: True covered, False not covered (1/2)

Branches covered = 5 / 6 = 83.33%

---

## If `print("Additional Statement 5")` is deleted

Total statements become 6. Covered statements remain the same (6).

**Statement coverage** = 6 / 6 = 100%
**Branch coverage** = 5 / 6 = 83.33%
