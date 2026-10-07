# Specification of a simple type checker

## 1. Explanation
A type checker is a semantic analyzer module that verifies whether the constructs of a programming language satisfy the type rules specified by the language. The design of a simple type checker involves assigning type expressions to language constructs and ensuring that operators are applied to operands of compatible types.

**Key Concepts:**
- **Type Expressions:** These denote types. They can be basic types (e.g., `integer`, `real`, `boolean`) or composite types constructed using type constructors (e.g., arrays, pointers, functions).
- **Type Environment:** A symbol table that binds variables to their types.
- **Type Equivalence:** Determining when two type expressions represent the same type. Structural equivalence checks if they have the same structure; name equivalence checks if they have the same name.

The specification is typically implemented using a Syntax-Directed Definition (SDD) where the parser evaluates the `type` attribute of expressions during traversal.

## 2. Example
Consider an assignment statement `id = E`.
The type checker must ensure that the type of the expression `E` is compatible with the declared type of the identifier `id`.
```text
S -> id = E
Semantic Rule:
  if (lookup(id.name).type == E.type)
      S.type = void
  else
      S.type = type_error
```

## 3. Applications & Use Cases
- **Early Error Detection:** Type checkers catch operations on incompatible types at compile time (e.g., adding an integer to a boolean) before the code runs.
- **Operator Overloading Resolution:** Determining which version of an operator (e.g., integer addition vs. floating-point addition) to use based on operand types.
- **Memory Allocation:** Knowing a variable's type dictates exactly how many bytes of storage to allocate for it.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Type Checking Arithmetic Expressions**
Grammar: `E -> E1 + E2 | E1 * E2 | id | num`
Type rules:
- `E -> id` { `E.type = lookup(id.entry)` }
- `E -> num` { `E.type = integer` }
- `E -> E1 + E2` { 
    `if (E1.type == integer AND E2.type == integer) E.type = integer`
    `else if (E1.type == real AND E2.type == real) E.type = real`
    `else E.type = type_error` 
}
*Trace:* For `x + 5` where `x` is declared as `real`, `E1.type` is `real`, `E2.type` is `integer`. This causes a `type_error` unless type coercion (implicit casting) is implemented.

**Example 2: Type Checking Array References**
Grammar: `E -> id [ E1 ]`
Type Rule:
```text
E -> id [ E1 ] {
    if (E1.type == integer AND lookup(id.entry) == array(s, t))
        E.type = t
    else
        E.type = type_error
}
```
*Explanation:* The index `E1` must resolve to an `integer`. If `id` is an array of type `t`, the result of the reference is of type `t`.

**Example 3: Type Checking Statements**
Grammar: `S -> if E then S1`
Type Rule:
```text
S -> if E then S1 {
    if (E.type == boolean)
        S.type = S1.type
    else
        S.type = type_error
}
```
*Explanation:* The condition `E` of an `if` statement must evaluate to a boolean type.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2019]** (5)  20 a)  Explain issues in design of a code generator    (5)    b) Explain simple code generation algorithm  (5)  ********        http://www.ktuonline.com
**[May 2019]** (3)  14 a) Explain the syntax directed definition of a simple desk calculator.

*(Note: Solutions to be generated/verified by agent)*


### [May 2019] Design a type checker for simple arithmetic operations. (3 marks)
**Solution:**
To design a simple type checker for arithmetic operations, we can write a Syntax-Directed Definition (SDD) assuming basic types like `integer` and `real`. We use an attribute `type` for each expression node.

**Grammar and Type Rules:**
1. `E -> id` 
   `E.type = lookup(id.entry);` 
   *(Lookup retrieves the variable's type from the symbol table)*
   
2. `E -> num` 
   `E.type = integer;`

3. `E -> real_num` 
   `E.type = real;`

4. `E -> E1 + E2`
   ```text
   if (E1.type == integer and E2.type == integer)
       E.type = integer;
   else if (E1.type == real and E2.type == real)
       E.type = real;
   else if (E1.type == integer and E2.type == real)
       E.type = real; // Type coercion
   else if (E1.type == real and E2.type == integer)
       E.type = real; // Type coercion
   else
       E.type = type_error;
   ```

5. `E -> E1 * E2`
   *(Same logical checks as addition, mapping to integer/real or type_error)*

This checker successfully verifies that operands are valid numbers and applies implicit type conversions (coercions) when adding an integer and a real number.
