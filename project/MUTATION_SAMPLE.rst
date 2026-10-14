Mutatest diagnostic summary
===========================
 - Source location: C:\Users\bryan\Documents\Codex\2026-10-13\he\work\comp441-trackc-project\appointment\utils\date_time.py
 - Test commands: ['python', 'manage.py', 'test', 'appointment.tests.utils.test_date_time', '--verbosity=0']
 - Mode: s
 - Excluded files: []
 - N locations input: 8
 - Random seed: 441

Random sample details
---------------------
 - Total locations mutated: 8
 - Total locations identified: 46
 - Location sample coverage: 17.39 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:02.049074
 - Clean trial 2 run time: 0:00:02.496643
 - Mutation trials total run time: 0:00:59.131853

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 4
 - TOTAL RUNS: 23
 - RUN DATETIME: 2026-10-14 18:05:33.608517


Mutations by result status
==========================


SURVIVED
--------
 - appointment\utils\date_time.py: (l: 198, c: 8) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - appointment\utils\date_time.py: (l: 205, c: 10) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - appointment\utils\date_time.py: (l: 242, c: 9) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - appointment\utils\date_time.py: (l: 302, c: 4) - mutation from If_Statement to If_False


DETECTED
--------
 - appointment\utils\date_time.py: (l: 198, c: 8) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - appointment\utils\date_time.py: (l: 198, c: 8) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - appointment\utils\date_time.py: (l: 198, c: 8) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - appointment\utils\date_time.py: (l: 205, c: 10) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - appointment\utils\date_time.py: (l: 220, c: 7) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - appointment\utils\date_time.py: (l: 220, c: 7) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - appointment\utils\date_time.py: (l: 220, c: 7) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - appointment\utils\date_time.py: (l: 220, c: 7) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - appointment\utils\date_time.py: (l: 220, c: 7) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - appointment\utils\date_time.py: (l: 233, c: 24) - mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
 - appointment\utils\date_time.py: (l: 233, c: 24) - mutation from <class 'ast.Mod'> to <class 'ast.FloorDiv'>
 - appointment\utils\date_time.py: (l: 233, c: 24) - mutation from <class 'ast.Mod'> to <class 'ast.Add'>
 - appointment\utils\date_time.py: (l: 233, c: 24) - mutation from <class 'ast.Mod'> to <class 'ast.Sub'>
 - appointment\utils\date_time.py: (l: 233, c: 24) - mutation from <class 'ast.Mod'> to <class 'ast.Mult'>
 - appointment\utils\date_time.py: (l: 233, c: 24) - mutation from <class 'ast.Mod'> to <class 'ast.Div'>
 - appointment\utils\date_time.py: (l: 308, c: 4) - mutation from If_Statement to If_True
 - appointment\utils\date_time.py: (l: 308, c: 4) - mutation from If_Statement to If_False
 - appointment\utils\date_time.py: (l: 369, c: 4) - mutation from If_Statement to If_True
 - appointment\utils\date_time.py: (l: 369, c: 4) - mutation from If_Statement to If_False