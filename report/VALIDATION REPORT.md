# DATA VALIDATION REPORT

## 1. VALIDATION OVERVIEW

This report verifies the integrity, consistency, and correctness of the stock market dataset.

The validation process checks:

- Duplicate records
- Negative price values
- Negative trading volume
- Invalid dates
- Data type consistency

---

# 2. DUPLICATE RECORD VALIDATION

| Validation Check | Result |
|---|---|
| Duplicate Rows | 0 |

## Observation

- No duplicate records were detected.
- Dataset uniqueness is maintained.

---

# 3. PRICE VALIDATION

## Open Price Validation

| Check | Result |
|---|---|
| Negative Open Prices | 0 |

## Close Price Validation

| Check | Result |
|---|---|
| Negative Close Prices | 0 |

## High Price Validation

| Check | Result |
|---|---|
| Negative High Prices | 0 |

## Low Price Validation

| Check | Result |
|---|---|
| Negative Low Prices | 0 |

## Observation

- All stock prices are valid.
- No negative price values were found.
- Market pricing data is logically consistent.

---

# 4. TRADING VOLUME VALIDATION

| Validation Check | Result |
|---|---|
| Negative Trading Volume | 0 |

## Observation

- All trading volume values are valid.
- No corrupted or impossible trading volume values exist.

---

# 5. DATE VALIDATION

| Validation Check | Result |
|---|---|
| Invalid Dates | 0 |

## Observation

- All date records follow a valid datetime structure.
- Dataset chronology is maintained correctly.

---

# 6. DATA TYPE VALIDATION

| Column | Data Type |
|---|---|
| open | float64 |
| high | float64 |
| low | float64 |
| close | float64 |
| volume | float64 |
| adj_high | float64 |
| adj_low | float64 |
| adj_close | float64 |
| adj_open | float64 |
| adj_volume | float64 |
| split_factor | float64 |
| dividend | float64 |
| symbol | object |
| exchange | object |
| date | object |

---

# 7. DATA TYPE OBSERVATIONS

## Numerical Columns

The following columns are correctly stored as numerical float values:

- open
- high
- low
- close
- volume
- adj_high
- adj_low
- adj_close
- adj_open
- adj_volume
- split_factor
- dividend

## Categorical Columns

The following columns are correctly stored as object types:

- symbol
- exchange

## Date Column

- The `date` column is currently stored as an object datatype.
- Converting the date column to datetime format is recommended for time-series analytics.

Example:

```python
df["date"] = pd.to_datetime(df["date"])