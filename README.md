# CMPS 2200  Recitation 02

**Name (Team Member 1):**__Zoe Murphy___  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

** 
To figure out the asymptotic behavior, we need to figure out if the test cases (f(n) = 1, log n, and n) are root dominated, leaf dominated, or balanced. For the derivation, a = 2 and b = 2, so the overall equation is W(n) = 2 * W(n/2) + f(n). Then, we can make a recursive tree for each of of these functions and look at the work for each node and the depth (logb(n)). The work for f(n) = 1 is 2^i, f(n) = log n is 2^i * log (n/2^i), and f(n) = n is 2^i * n/2^i. 

f(n) = 1 -> leaf dominated
2^i with the depth (logb(n)) becomes 2^(log2(n)), which is n, so the behavior is O(n)

f(n) = log n -> balanced
2^i * log(n/2^i) with depth becomes 2^(log2(n)) * (log2(n/2^(log2(n)))), which is O(n log n) (I think)

f(n) = n -> root?
2^i * n/2^i with depth becomes 2^(log2(n)) * n/2^(log2(n)), which is O(n log n) I think?? 

I'm not confident on these calculations, but that's what I think they are. 


|     n |   f(n) = 1 |   f(n) = log n |   f(n) = n |
|-------|------------|----------------|------------|
|    10 |         15 |          8.294 |         36 |
|    20 |         31 |         19.584 |         92 |
|    50 |         63 |         52.201 |        276 |
|   100 |        127 |        109.008 |        652 |
|  1000 |       1023 |        959.608 |       9120 |
|  5000 |       8191 |       5823.326 |      61728 |
| 10000 |      16383 |      11655.862 |     133456 |

**

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**
I used a = 2, b = 2 and test cases where c = 0.5, c = 1, and   c = 2.0 (so less than, equal to, and greater than logb(a) which is 1). I think that when c is less than 1, it'll have the slowest growth rate, c is greater than 1 will have the fastest rate, and c = 1 will be in the middle. 

|     n |     c < 1 |      c = 1 |         c > 1 |
|-------|-----------|------------|---------------|
|    10 |    21.291 |     36.000 |       174.000 |
|    20 |    47.055 |     92.000 |       748.000 |
|    50 |   110.236 |    276.000 |      4790.000 |
|   100 |   230.472 |    652.000 |     19580.000 |
|  1000 |  2075.117 |   9120.000 |   1990744.000 |
|  5000 | 14251.208 |  61728.000 |  49957880.000 |
| 10000 | 28602.416 | 133456.000 | 199915760.000 |
**

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**
I think you use the depth of the trees to help find the span (longest sequential path) and the work done at each level. The tree depth for all the cases is O(logb(n)), and the work depends on what f(n) is. 

For f(n) = 1, the work done is constant. So, the span should just be the depth, which would be the longest sequential path: O(log n). 

For f(n) = log n, the work at each level is log(n), and the depth is logb(n), so together, the span is O(log^2(n))

For f(n) = n, the work at each level is n, and the depth is logb(n), but, we're looking for the deepest path, which is going to correspond to O(n) which is more, therefore, the span is O(n)

Here is the table for the span calculations of my test cases. I believe that these values verify my predicted spans above. 
|     n |   f(n) = 1 |   f(n) = log n |   f(n) = n |
|-------|------------|----------------|------------|
|    10 |          4 |          4.605 |         18 |
|    20 |          5 |          7.601 |         38 |
|    50 |          6 |         12.506 |         97 |
|   100 |          7 |         17.111 |        197 |
|  1000 |         10 |         36.786 |       1994 |
|  5000 |         13 |         55.944 |       9995 |
| 10000 |         14 |         65.154 |      19995 |
**
