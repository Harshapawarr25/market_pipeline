# FAILURE_TEST_REPORT

## Objective

Validate the dataset and pipeline behavior against common failure scenarios to ensure deterministic execution and integration readiness.

---

# Failure Test Summary

All configured validation and failure checks were executed successfully.

No failure conditions were detected in the current dataset.

---

# Failure Scenarios Tested

| Failure Scenario | Status | Observation |
|---|---|---|
| Empty Dataset Check | PASS | Dataset contains records |
| Duplicate Rows Check | PASS | No duplicate rows detected |
| Missing Values Check | PASS | No critical missing values found |
| Negative Open Prices | PASS | No negative values detected |
| Negative Close Prices | PASS | No negative values detected |
| Negative High Prices | PASS | No negative values detected |
| Negative Low Prices | PASS | No negative values detected |
| Negative Volume Check | PASS | No negative volume values detected |
| Invalid Date Format Check | PASS | All dates valid |
| Data Type Validation | PASS | Column datatypes consistent |

---

# Validation Outcome

The dataset passed all configured validation and integrity checks.

No deterministic failure conditions were triggered during execution.

Pipeline execution remained stable and replay-consistent.

---

# Conclusion

The validation layer is functioning correctly and no corrective action was required for the current dataset.