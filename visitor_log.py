from datetime import datetime, timedelta


# Custom exception for duplicate visitor
class DuplicateVisitorError(Exception):
    pass


# Custom exception for 5-minute restriction
class TimeRestrictionError(Exception):
    pass


def main():
    visitors_file = "visitors.txt"
    output_file = "output.txt"

    visitor = input("Enter visitor's name: ")

    try:
        # Ensure visitors file exists
        try:
            with open(visitors_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            with open(visitors_file, "w", encoding="utf-8") as f:
                lines = []

        # Read last visitor record
        if lines:
            last_line = lines[-1].strip()
            last_name, last_time = last_line.split(" | ")
            last_time = datetime.fromisoformat(last_time)
        else:
            last_name = None
            last_time = None

        # Check duplicate visitor
        if visitor == last_name:
            raise DuplicateVisitorError("Duplicate visitor detected")

        # Check 5-minute rule
        if last_time and datetime.now() - last_time < timedelta(minutes=5):
            raise TimeRestrictionError("Wait for 5 minutes")

        # Save visitor record
        with open(visitors_file, "a", encoding="utf-8") as f:
            f.write(f"{visitor} | {datetime.now()}\n")

        # Write success output
        with open(output_file, "a", encoding="utf-8") as out:
            out.write("Visitor added successfully\n")

    except DuplicateVisitorError:
        with open(output_file, "a", encoding="utf-8") as out:
            out.write("Error: Visitor already signed in last\n")

    except TimeRestrictionError:
        with open(output_file, "a", encoding="utf-8") as out:
            out.write("Error: Another visitor cannot enter until after 5 minutes\n")


# Run the program
main()


# ======================================================
# SAMPLE CONTENT OF visitors.txt (AFTER RUNNING PROGRAM)
# ======================================================
# Ahmed | 2026-01-31 10:00:12.456321
# Musa  | 2026-01-31 10:06:45.112233
#
# This file stores the visitor's name and the date/time
# they were registered. Each visitor is saved on a new line.


# ======================================================
# SAMPLE CONTENT OF output.txt (PROGRAM OUTPUT FILE)
# ======================================================
# Visitor added successfully
# Error: Another visitor cannot enter until after 5 minutes
# Error: Visitor already signed in last
#
# This file stores the result of the program execution,
# including success messages and error messages.
