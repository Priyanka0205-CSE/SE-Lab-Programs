# Reflection

**1. Which issues were the easiest to fix, and which were the hardest? Why?**
The easiest were the style issues (blank lines, snake_case name, f-strings,
docstrings) and the one-line security fixes (md5 to sha256, chmod 0o777 to
0o600). The hardest was input validation. No tool reported it, so I found it
by running the program and noticing seat 25, -1 and "A7" were accepted. I also
had to remove the global statement and replace the bare except with specific
exceptions without breaking the program.

**2. Did the static analysis tools report any false positives?**
Bandit's B324 flagged md5 as a weak hash for security. Here the hash only
makes a short ticket code, not a password, so the risk was low and it is
debatable. I still switched to sha256, which costs nothing. The same tools
also missed the real logic bug (seats outside the valid range), so a clean
report does not mean the code is correct.

**3. How would you integrate static analysis tools into your workflow?**
I would run flake8 and pylint in my editor while coding, add them as a
pre-commit hook, and run all three (pylint, flake8, bandit) in a CI pipeline
such as GitHub Actions so code with serious findings cannot be merged.

**4. What tangible improvements did you observe?**
Pylint went from 5.87 to 10.00, Bandit from 2 High and 1 Low issues to none,
and Flake8 from 11 issues to none. The program is also more robust: invalid
seats and unknown shows are rejected, errors are logged instead of hidden,
files are closed properly, the file permissions are safer, and the code is
easier to read with docstrings and consistent naming.