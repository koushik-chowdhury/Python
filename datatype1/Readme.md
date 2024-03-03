# Object Types / Data Types

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('data.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Funtions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

#
**` Internal.py & ipynb `**

# Python Code Exploration



**Purpose:**

This code demonstrates various concepts related to references and copies in Python lists. It showcases how assignments and modifications can affect different lists depending on whether they refer to the same object in memory or independent copies are created.

**Key Points:**

- **Modifying an assigned reference:** When you assign an existing list's reference to a new variable, changes made to the new variable will also affect the original list because both variables point to the same object in memory. (Examples: `mylist` and `duplist`, `list1` and `list2`, `ls1` and `ls2` cases)

- **Creating a copy with slicing: Using** `[:]` with a list creates a **shallow copy**, which is a new list object containing the same elements as the original list. However, if the elements are mutable (like another list), modifying one list will affect the other as well. (Example: `l1` and `l2`)

- **Checking object identity:** The **`is`** operator can be used to check if two variables refer to the same object in memory. It returns **`True`** if they do and **`False`** otherwise. (Example: **`ls1`** is **`ls2`** check)

# Code Breakdown:
1. Reference assignment:
- Creates **`mylist`** with **`[1, 2, 3]`**.
- Assigns the reference of **`mylist`** to **`duplist`**.
- Changes **`mylist`** to "Koushik". This only affects **`mylist`** as they point to different objects now.
- Creates a new list **`[1, 2, 3]`** and assigns it back to **`mylist`**. 
- Modifying **`mylist[0]`** now affects **`duplist`** since they have the same reference.


2. Reference and modification:

- Creates list1 with **`[1, 2, 3]`**.
- Assigns the reference of **`list1`** to **`list2`**.
- Modifying **`list1[0]`** also changes list2 due to the shared reference.

3. Shallow copying:

- Creates **`l1`** with **`[1, 2, 3]`**.
- Creates a shallow copy of **`l1`** using **`l2`** = **`l1[:]`**.
- Modifying **`l1[0]`** does not affect **`l2`** because they are independent objects, even though they initially contain the same elements.

4. Comparing references:

- Creates **`ls1`** with **`[1, 2, 3]`**.
- Assigns the reference of **`ls1`** to **`ls2`**.
- Prints **`True`** for **`(ls1 is ls2)`** because they refer to the same object.
- Creates a new list with **`[1, 2, 3]`** and assigns it to **`ls2`**.
- Prints **`False`** for **`(ls1 is ls2)`** because they now refer to different objects.


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/koushik-chowdhury-259943253/)

[![twitter](https://img.shields.io/badge/facebook-1DA1F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/koushik.chowdhury.3551/)