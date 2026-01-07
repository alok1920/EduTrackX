import re

STUDENT_ID_PATTERN = r"^EDX\d{2}\d{4}\d{3}$"

def is_valid_student_id(student_id: str) -> bool:
    """
    Validate manually entered student_id format.
    """
    return bool(re.match(STUDENT_ID_PATTERN, student_id))

def generate_student_id(
    admission_class: int,
    admission_year: int,
    last_sequence: int
) -> str:
    """
    Generate student_id like EDX052024012
    """

    class_part = f"{admission_class:02d}"
    year_part = str(admission_year)
    sequence_part = f"{last_sequence + 1:03d}"

    return f"EDX{class_part}{year_part}{sequence_part}"

