# Defect Prediction Plan

## Label policy

Commit messages are not ground truth. A commit containing “fix” is only a candidate label; false positives and missed bug fixes are likely. Build `defect_labels.csv` by reviewing commits against issue/PR evidence. Include `commit`, `is_defect_fix` (0/1), and an optional reviewer note. Exclude merge commits and commits without a defensible label. Do not run or publish scores until this review is complete.

## Features and evaluation

Use commit-level churn features (files changed, insertions, deletions, and prior-file churn) extracted from local Git history. Split chronologically: train on earlier labeled commits, test on later commits. Keep commits from the same fix series together where possible. Report class balance, precision, recall, F1, PR-AUC, confusion matrix, threshold, and a majority-class baseline. With few positive labels, emphasize uncertainty and avoid claiming operational usefulness.

## Reproduction

The companion `scripts/defect_prediction.py` requires scikit-learn and a reviewed CSV. Example:

```powershell
python scripts/defect_prediction.py --labels project/defect_labels.csv --test-fraction 0.25
```

The script must fail clearly when labels are missing or either class is absent. Save the exact run output and package versions with the report. Scores remain **TBD** until this is run on reviewed labels.
