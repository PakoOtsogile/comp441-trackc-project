"""Launch Mutatest 3.1.0 with its Python 3.12 set-sampling compatibility fix."""

import random
import sys

_sample = random.sample


def _sample_sequence(population, k, *, counts=None):
    if isinstance(population, (set, frozenset)):
        population = sorted(population, key=repr)
    return _sample(population, k, counts=counts)


random.sample = _sample_sequence

from mutatest.cli import cli_main


if __name__ == "__main__":
    sys.exit(cli_main())
