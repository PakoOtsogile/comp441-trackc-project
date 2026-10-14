# Performance Check — Helper Micro-Load

**Run date:** 14 October 2026  
**Status:** completed helper-level check; an HTTP/database load test is still pending.

## Method

`scripts/performance_check.py` exercised `appointment.utils.date_time.get_ar_end_time` with 20 concurrent worker threads for 120 seconds. Each worker repeatedly called the helper with a 45-minute appointment, a midnight-crossing appointment, and a fractional-minute duration. The script warmed each case before timing, then recorded per-call latency, throughput, and exceptions. It uses synthetic in-memory inputs and performs no database or network I/O.

Reproduce from the repository root:

```powershell
python scripts/performance_check.py --users 20 --seconds 120 --output project/performance_run.json
```

## Result

| Measure | Result |
|---|---:|
| Worker threads | 20 |
| Duration | 120.005 seconds |
| Calls | 1,539,240 |
| Throughput | 12,826.47 calls/second |
| Median latency | 1.4764 ms |
| p95 latency | 2.7411 ms |
| Errors | 0 |
| Runtime / OS | Python 3.12.14 / Windows 11 |

Raw machine-readable output: [`performance_run.json`](performance_run.json).

These timings describe a small helper under same-process thread contention on the machine used for this run. They must not be presented as booking-page response time, database capacity, production throughput, or a hosted load result. The course group should still run and document a 20–50 user test against a representative HTTP endpoint with its database and deployment configuration if required by the rubric.
