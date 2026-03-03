# Difficulty: Beginner
# Scenario
# As a QA engineer, you receive version strings from a release pipeline. Before running automated tests, you
# need to verify that the version string follows the correct format.
# Task
# Write a function called is_valid_version that accepts a version string and returns True if it follows the
# major.minor.patch (eg: 1.1.1)_ format where all three parts are numeric digits, and False otherwise.
# Expected Output
# is_valid_version("2.1.3") # Expected: True
# is_valid_version("2.1") # Expected: False
# is_valid_version("2.a.3") # Expected: False

def is_valid_version(version):
    ver = version.split(".")

    if len(ver) != 3:
        return False

    for v in ver:
       if not v.isdigit():
           return False
    return True

print(is_valid_version("2.1"))
