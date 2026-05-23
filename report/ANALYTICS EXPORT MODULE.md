# STOCK MARKET DATA ANALYSIS REPORT

## 1. PROJECT OVERVIEW

This report presents the analysis of historical stock market data for Apple Inc. (AAPL).  
The dataset contains 100 trading records from the NASDAQ exchange (XNAS).

The analysis includes:

- Market stock price inspection
- Statistical analysis
- Missing value validation
- Unique value analysis
- Trading volume evaluation
- Dividend and split analysis
- Data quality verification

---

# 2. DATASET INFORMATION

| Feature | Description |
|---|---|
| Symbol | AAPL |
| Exchange | XNAS |
| Total Records | 100 |
| Missing Values | 0 |
| Duplicate Dates | 0 |
| Split Events | None |
| Dividend Events | Present |

---

# 3. MARKET STOCK DATA ANALYSIS

## Recent Trading Records

| Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| 2026-05-22 | 306.06 | 311.40 | 305.85 | 308.82 | 43,605,063 |
| 2026-05-21 | 301.05 | 305.54 | 300.40 | 304.99 | 42,823,425 |
| 2026-05-20 | 298.18 | 302.80 | 298.09 | 302.25 | 37,276,629 |
| 2026-05-19 | 296.97 | 300.51 | 296.35 | 298.97 | 34,842,416 |
| 2026-05-18 | 300.24 | 300.66 | 294.91 | 297.84 | 34,313,641 |

---

# 4. SUMMARY STATISTICS

## Open Price Statistics

| Metric | Value |
|---|---|
| Mean | 266.59 |
| Standard Deviation | 13.99 |
| Minimum | 247.24 |
| Maximum | 306.06 |

## Close Price Statistics

| Metric | Value |
|---|---|
| Mean | 266.85 |
| Standard Deviation | 14.64 |
| Minimum | 246.63 |
| Maximum | 308.82 |

## Volume Statistics

| Metric | Value |
|---|---|
| Mean Volume | 44,343,130 |
| Minimum Volume | 22,090,083 |
| Maximum Volume | 90,458,500 |

---

# 5. PRICE TREND ANALYSIS

## Observations

- The stock demonstrates an upward movement toward the latest trading dates.
- Closing prices reached a maximum value of 308.82.
- The average closing price across the dataset is 266.85.
- Daily volatility is moderate based on the standard deviation values.
- Trading activity remained consistently high throughout the dataset.

---

# 6. VOLUME ANALYSIS

## Trading Volume Insights

- Average trading volume exceeds 44 million shares.
- Peak trading activity reached over 90 million shares.
- No abnormal zero-volume trading days were detected.
- Volume distribution indicates active market participation.

---

# 7. DIVIDEND AND SPLIT ANALYSIS

## Dividend Information

| Metric | Value |
|---|---|
| Mean Dividend | 0.0053 |
| Maximum Dividend | 0.27 |

### Observations

- Most trading days contain no dividend distribution.
- Small dividend events are present within the dataset.

## Split Factor Analysis

| Metric | Value |
|---|---|
| Mean Split Factor | 1.0 |
| Unique Values | 1 |

### Observations

- No stock split events occurred during this dataset period.

---

# 8. UNIQUE VALUE ANALYSIS

| Column | Unique Values |
|---|---|
| open | 98 |
| high | 99 |
| low | 99 |
| close | 100 |
| volume | 100 |
| date | 100 |

## Observations

- Each trading date is unique.
- Closing prices are fully unique across all records.
- Market data variability indicates realistic trading behavior.

---

# 9. MISSING VALUE ANALYSIS

| Column | Missing Values | Missing Percentage |
|---|---|---|
| open | 0 | 0.0% |
| high | 0 | 0.0% |
| low | 0 | 0.0% |
| close | 0 | 0.0% |
| volume | 0 | 0.0% |
| date | 0 | 0.0% |

## Observations

- No missing values were detected.
- Dataset integrity is fully maintained.
- The dataset is suitable for analytics and visualization tasks.

---

# 10. DATA QUALITY VALIDATION

## Validation Results

| Validation Check | Status |
|---|---|
| Missing Values Check | PASSED |
| Duplicate Date Check | PASSED |
| Numerical Data Consistency | PASSED |
| Trading Volume Availability | PASSED |
| Symbol Consistency | PASSED |

---

# 11. FINAL CONCLUSION

The AAPL stock market dataset is clean, complete, and analytics-ready.

Key findings include:

- Strong upward price movement in recent sessions
- High market participation based on trading volume
- No missing or corrupted records
- Stable exchange and symbol consistency
- No stock split events during the observed period

The dataset is suitable for:

- Financial analytics
- Time-series analysis
- Data visualization
- Predictive modeling preparation
- Business intelligence reporting

---