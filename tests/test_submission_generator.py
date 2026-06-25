# tests/test_submission_generator.py

from core.submission_generator import (
    SubmissionGenerator
)

generator = SubmissionGenerator()

file = generator.save()

print(
    "Saved:",
    file
)