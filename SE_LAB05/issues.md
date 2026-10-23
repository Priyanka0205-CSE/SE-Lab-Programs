| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Weak MD5 hash (B324) | Security (High) | 25 | md5 is a weak hash used for the ticket code | Switch to hashlib.sha256 |
| Permissive file mode 0o777 (B103) | Security (High) | 55 | seats.json made readable/writable/executable by everyone | Use 0o600 (owner only) |
| Mutable default argument (W0102) | Bug | 9 | system_logs=[] is shared across all calls | Default to None, create list inside function |
| Bare except + pass (W0702, E722, B110) | Bug/Security (Low) | 21 | Hides every error, including real bugs | Catch ValueError and KeyError specifically and log it |
| open() without with / encoding (R1732, W1514) | Resource handling | 28, 33 | File never explicitly closed, encoding not set | Use with open(..., encoding="utf-8") |
| global statement (W0603) | Design | 32 | Modifying global state inside function | Return loaded data instead of using global |
| Function name printSeatingSummary (C0103) | Style | 37 | Not snake_case | Rename to print_seating_summary |
| % formatting (C0209) | Style | 12, 15 | Old string formatting | Use f-strings |
| Missing docstrings (C0114, C0116) | Documentation | 1, 9, 18, 24, 27, 31, 37, 42 | No module or function docstrings | Add short docstrings |
| Line too long (C0301, E501) | Style | 12, 40 | Lines exceed length limits | Break the lines up |
| Blank lines (E302, E305) | Style | many | Need 2 blank lines between functions | Add blank lines |
| No input validation | Logic bug | 9-16 | Seats 25, -1 and "A7" are accepted; "4" stored as a string | Validate show and seat range, convert input to int |