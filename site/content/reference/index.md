
# BigFunctions


<img src="../assets/logo_and_name.png" alt="drawing" width="300"/>

BigFunctions are public BigQuery routines that give you **super-SQL-powers** in BigQuery 💪.

---



## 👀 Explore

> "Explore" BigFunctions are great for data-analysts to explore data.They make computations on BigQuery and display the results as data-vizualizations directly in BigQuery console.

- [<code>explore_column(fully_qualified_column, output)</code>](explore/#explore_column): Show column statistics
- [<code>explore_dataset(fully_qualified_dataset, output)</code>](explore/#explore_dataset): Shows infos about dataset tables
- [<code>explore_table(fully_qualified_table, output)</code>](explore/#explore_table): Show table infos and columns statistics




## 🔨 Utils

> "Utils" BigFunctions used by other BigFunctions.

- [<code>chart(data, chart_type, ylabel)</code>](utils/#chart): Returns html with a chartjs chart
- [<code>levenshtein(string1, string2)</code>](utils/#levenshtein): Computes levenshtein distance between `string1` and `string2`
- [<code>render_string(template, context)</code>](utils/#render_string): Render template with context json object using nunjucks.js templating library



