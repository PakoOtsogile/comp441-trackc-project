"""Concurrent micro-load check for the appointment end-time helper.

This measures an in-process Python helper, not HTTP, database, or deployment
performance. Use a fresh process and record machine/runtime details with results.
"""

import argparse
import concurrent.futures
import json
import os
import platform
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appointment.settings")

import django

django.setup()

from appointment.utils.date_time import get_ar_end_time


def percentile(values, fraction):
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, int((len(ordered) - 1) * fraction))]


def user_workload(deadline, barrier, samples, errors):
    cases = (("09:15:00", 45), ("23:30:00", 60), ("10:00:00", 1.5))
    barrier.wait()
    while time.perf_counter() < deadline:
        for start, duration in cases:
            before = time.perf_counter_ns()
            try:
                get_ar_end_time(start, duration)
            except Exception as exc:  # Capture and report rather than hide failures.
                errors.append(type(exc).__name__)
            samples.append(time.perf_counter_ns() - before)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--users", type=int, default=20)
    parser.add_argument("--seconds", type=int, default=120)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not 1 <= args.users <= 50 or not 1 <= args.seconds <= 300:
        parser.error("--users must be 1..50 and --seconds must be 1..300")

    for start, duration in (("09:15:00", 45), ("23:30:00", 60), ("10:00:00", 1.5)):
        get_ar_end_time(start, duration)

    barrier = __import__("threading").Barrier(args.users)
    samples = [[] for _ in range(args.users)]
    errors = []
    start_time = time.perf_counter()
    deadline = start_time + args.seconds
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.users) as pool:
        futures = [pool.submit(user_workload, deadline, barrier, bucket, errors) for bucket in samples]
        for future in futures:
            future.result()
    elapsed = time.perf_counter() - start_time
    latencies = [value for bucket in samples for value in bucket]
    result = {
        "scope": "in-process get_ar_end_time helper; not HTTP or database load",
        "users": args.users,
        "requested_seconds": args.seconds,
        "elapsed_seconds": round(elapsed, 3),
        "calls": len(latencies),
        "throughput_calls_per_second": round(len(latencies) / elapsed, 2),
        "latency_ms_median": round(statistics.median(latencies) / 1_000_000, 6),
        "latency_ms_p95": round(percentile(latencies, 0.95) / 1_000_000, 6),
        "errors": len(errors),
        "error_types": dict((name, errors.count(name)) for name in sorted(set(errors))),
        "python": platform.python_version(),
        "platform": platform.platform(),
    }
    rendered = json.dumps(result, indent=2)
    print(rendered)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
