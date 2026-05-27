# Market Stock Data Validation Report

## Dataset Validation Overview

Validation pipeline executed successfully on historical stock market dataset for Apple Inc. (`AAPL`).

---

# 1. Null Detection

Validation performed to identify missing or null values across all dataset columns.

## Validation Results

| Column       | Missing Values | Missing Percentage |
| ------------ | -------------- | ------------------ |
| open         | 0              | 0.0%               |
| high         | 0              | 0.0%               |
| low          | 0              | 0.0%               |
| close        | 0              | 0.0%               |
| volume       | 0              | 0.0%               |
| adj_high     | 0              | 0.0%               |
| adj_low      | 0              | 0.0%               |
| adj_close    | 0              | 0.0%               |
| adj_open     | 0              | 0.0%               |
| adj_volume   | 0              | 0.0%               |
| split_factor | 0              | 0.0%               |
| dividend     | 0              | 0.0%               |
| symbol       | 0              | 0.0%               |
| exchange     | 0              | 0.0%               |
| date         | 0              | 0.0%               |

## Observation

* No missing values detected.
* Dataset completeness maintained across all records.

## Validation Status

```text id="y3pf8w"
PASSED
```

---

# 2. Duplicate Detection

Duplicate row analysis performed to detect repeated market records.

## Validation Result

| Validation Type | Result |
| --------------- | ------ |
| Duplicate Rows  | 0      |

## Observation

* No duplicate records detected.
* Dataset integrity preserved.

## Validation Status

```text id="01x1iv"
PASSED
```

---

# 3. Negative Value Validation

Validation executed to identify invalid negative numerical values.

## Validation Results

| Validation Check       | Result |
| ---------------------- | ------ |
| Negative Open Prices   | 0      |
| Negative Close Prices  | 0      |
| Negative High Prices   | 0      |
| Negative Low Prices    | 0      |
| Negative Volume Values | 0      |

## Observation

* No invalid negative market values detected.
* All pricing and volume fields remain logically valid.

## Validation Status

```text id="9b3l15"
PASSED
```

---

# 4. Datatype Validation

Datatype validation performed to ensure schema consistency.

## Dataset Schema Validation

| Column       | Datatype | Validation Result |
| ------------ | -------- | ----------------- |
| open         | float64  | Valid             |
| high         | float64  | Valid             |
| low          | float64  | Valid             |
| close        | float64  | Valid             |
| volume       | float64  | Valid             |
| adj_high     | float64  | Valid             |
| adj_low      | float64  | Valid             |
| adj_close    | float64  | Valid             |
| adj_open     | float64  | Valid             |
| adj_volume   | float64  | Valid             |
| split_factor | float64  | Valid             |
| dividend     | float64  | Valid             |
| symbol       | object   | Valid             |
| exchange     | object   | Valid             |
| date         | object   | Valid             |

## Observation

* Numerical columns correctly formatted as float64.
* Categorical columns validated successfully.
* Date column structure validated successfully.

## Validation Status

```text id="vr4b2m"
PASSED
```

---

# 5. Date Validation

Date format validation executed on all market records.

## Validation Result

| Validation Check | Result |
| ---------------- | ------ |
| Invalid Dates    | 0      |

## Observation

* All date entries follow valid ISO datetime format.
* No corrupted timestamps detected.

## Validation Status

```text id="0n4pnw"
PASSED
```

---

# 6. Anomaly Detection

Anomaly detection executed on pricing and volume behavior.

## Volatility Analysis

| Metric                         | Value |
| ------------------------------ | ----- |
| Close Price Standard Deviation | 14.64 |

### Observation

* Market volatility remains within moderate threshold.
* No extreme market instability detected.

---

## Volume Analysis

| Metric         | Value         |
| -------------- | ------------- |
| Average Volume | 44.34 Million |
| Maximum Volume | 90.45 Million |

### Observation

* Trading activity remains within expected operational range.
* No abnormal volume spikes detected.

---

## Price Spike Detection

### Observation

* No abnormal market spike patterns detected.
* Daily price movement remains stable.

## Validation Status

PASSED


---

# Final Validation Summary

| Validation Layer          | Status |
| ------------------------- | ------ |
| Null Detection            | PASSED |
| Duplicate Detection       | PASSED |
| Negative Value Validation | PASSED |
| Datatype Validation       | PASSED |
| Date Validation           | PASSED |
| Anomaly Detection         | PASSED |

## Final Validation Status

VALIDATION PIPELINE COMPLETED SUCCESSFULLY
