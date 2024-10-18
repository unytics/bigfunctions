A company sells products internationally and stores sales data in BigQuery. The sales data includes the transaction amount and the currency in which the transaction occurred.  They need to report all sales in a single currency (e.g., USD) for financial analysis.

They can use the `exchange_rate` function to convert all transactions to USD in their reporting queries.  For example, if they have a table called `sales` with columns `transaction_amount` and `transaction_currency`, they can write a query like this:

```sql
SELECT
    transaction_amount * bigfunctions.us.exchange_rate(transaction_currency, 'USD') AS transaction_amount_usd
  FROM
    `your-project.your_dataset.sales`
```

This query would calculate `transaction_amount_usd` by multiplying the original `transaction_amount` by the exchange rate returned by the `exchange_rate` function. This effectively normalizes all transaction amounts to USD.  This makes it possible to aggregate and analyze sales data across different currencies, providing a consolidated view of the company's financial performance.
