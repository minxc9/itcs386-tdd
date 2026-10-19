
# ITCS386 Week 9 - TDD Reflection

## 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio? 
I wrote 8 tests and 40 lines of production code, excluding blank lines and comments. The test-to-code ratio is 1:5.

## 2. When was your bar red for the longest time, and what made it last so long? 
Step A7 was the most challenging for me because I had difficulty understanding how these worked together to handle unit conversions.

## 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right? 
I used Fake It in A1 by hard-coding 600, Triangulation in A2 by adding another multiplication test, and Obvious Implementation in A4 for equality. I think these choices were useful because they helped me understand how to develop code step by step.

## 4.	Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation? 
The optional A8 multiplication of a Sum is still unfinished. I would implement it next, and I already removed the redundant multiplication-by-two test from A2. I would not delete any other planned behavior yet.

## 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method? 
Maybe not, because I thought conversion should only be handled by Converter. TDD helped me realize that Quantity and Sum also needed reduction methods.

## 6.	In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design? 
Part 0 felt easier because the code already existed, while Part A was harder because I had to think about the expected behavior before implementing. I feel like the multiplication and mixed-unit tests helped shape my design the most.