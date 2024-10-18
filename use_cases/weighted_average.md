A teacher wants to calculate the weighted average grade for a student.  The student has two grades:

* **Quiz:** Grade = 10, Weight = 1 (Quizzes are worth less)
* **Exam:** Grade = 13, Weight = 2 (Exams are worth more)

Using the `weighted_average` function, the calculation would be:

```sql
SELECT bigfunctions.{region}.weighted_average(grade, weight) AS weighted_average
FROM (
    SELECT 10 AS grade, 1 AS weight UNION ALL
    SELECT 13 AS grade, 2 AS weight
);
```

This would return 12, as shown in the example.  The exam grade (13) contributes more to the final average because it has a higher weight.

**Other use cases:**

* **Calculating average stock prices:** Where `element` is the price of the stock and `weight` is the number of shares held at that price.
* **Determining the weighted average cost of capital:** Where `element` is the cost of each type of capital (debt, equity, etc.) and `weight` is the proportion of each type of capital in the company's capital structure.
* **Computing the weighted average of customer satisfaction scores:** Where `element` is the satisfaction score and `weight` is the number of customers who gave that score.
* **Creating a composite index from multiple indicators:** Where `element` is the value of each indicator and `weight` reflects the importance of each indicator in the overall index.  For instance, a happiness index could be created weighting factors like GDP per capita, life expectancy, and social support.


In essence, anytime you need an average where some elements contribute more than others, the `weighted_average` function is useful.
