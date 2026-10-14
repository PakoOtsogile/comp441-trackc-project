"""Small, reproducible temporal defect-prediction experiment.

Labels must be reviewed by a human; this tool deliberately does not infer them
from commit-message keywords.
"""

import argparse
import csv
import subprocess
import sys
from pathlib import Path


def git_features():
    raw = subprocess.check_output(
        ["git", "log", "--no-merges", "--reverse", "--numstat", "--format=COMMIT %H %ct"],
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    commits = []
    current = None
    for line in raw.splitlines():
        if line.startswith("COMMIT "):
            if current:
                commits.append(current)
            _, sha, timestamp = line.split()
            current = {"commit": sha, "timestamp": int(timestamp), "files": 0, "added": 0, "deleted": 0}
        elif current and line.strip():
            added, deleted, _path = line.split("\t", 2)
            current["files"] += 1
            current["added"] += int(added) if added.isdigit() else 0
            current["deleted"] += int(deleted) if deleted.isdigit() else 0
    if current:
        commits.append(current)
    prior_churn = 0
    for commit in commits:
        commit["prior_churn"] = prior_churn
        prior_churn += commit["added"] + commit["deleted"]
    return commits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--labels", required=True, type=Path)
    parser.add_argument("--test-fraction", type=float, default=0.25)
    args = parser.parse_args()
    if not 0.1 <= args.test_fraction <= 0.5:
        parser.error("--test-fraction must be between 0.1 and 0.5")
    if not args.labels.is_file():
        parser.error(f"reviewed labels file not found: {args.labels}")

    labels = {}
    with args.labels.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            value = row.get("is_defect_fix", "").strip()
            if value not in {"0", "1"}:
                parser.error("each label must have is_defect_fix equal to 0 or 1")
            labels[row["commit"].strip()] = int(value)

    rows = [item for item in git_features() if item["commit"] in labels]
    rows.sort(key=lambda item: (item["timestamp"], item["commit"]))
    if len(rows) < 12:
        parser.error(f"need at least 12 reviewed labeled commits; found {len(rows)}")
    split = int(len(rows) * (1 - args.test_fraction))
    train, test = rows[:split], rows[split:]
    if len({labels[item["commit"]] for item in train}) < 2 or len({labels[item["commit"]] for item in test}) < 2:
        parser.error("both train and chronological test sets need positive and negative labels")

    try:
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import (average_precision_score, classification_report,
                                     confusion_matrix, f1_score, precision_score,
                                     recall_score)
    except ImportError:
        print("Install scikit-learn to run this experiment.", file=sys.stderr)
        return 2

    features = ("files", "added", "deleted", "prior_churn")
    X_train = [[item[key] for key in features] for item in train]
    y_train = [labels[item["commit"]] for item in train]
    X_test = [[item[key] for key in features] for item in test]
    y_test = [labels[item["commit"]] for item in test]
    model = RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=441)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, list(model.classes_).index(1)]
    baseline = max(set(y_train), key=y_train.count)
    print(f"reviewed_labeled_commits={len(rows)} train={len(train)} test={len(test)}")
    print(f"features={','.join(features)} chronological_split={args.test_fraction:.2f}")
    print(f"majority_baseline_label={baseline} baseline_accuracy={sum(y == baseline for y in y_test) / len(y_test):.3f}")
    print(f"precision={precision_score(y_test, predicted, zero_division=0):.3f}")
    print(f"recall={recall_score(y_test, predicted, zero_division=0):.3f}")
    print(f"f1={f1_score(y_test, predicted, zero_division=0):.3f}")
    print(f"pr_auc={average_precision_score(y_test, probabilities):.3f}")
    print("confusion_matrix=[ [tn, fp], [fn, tp] ]")
    print(confusion_matrix(y_test, predicted, labels=[0, 1]).tolist())
    print(classification_report(y_test, predicted, zero_division=0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
