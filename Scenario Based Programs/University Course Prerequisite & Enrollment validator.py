"""University Course Prerequisite & Enrollment Validator

Problem Description
A university registration portal validates whether students can enroll in advanced courses.
Each course has a set of direct prerequisite course codes, and prerequisites are transitive
(if `CS301` requires `CS201`, and `CS201` requires `CS101`, then both are required for `CS301`).

Student transcripts arrive as a string `"STUDENT_ID | COURSE1-GRADE1, COURSE2-GRADE2..."`.
Only courses with `grade >= min_grade` (default `5`) count as passed.

**Modular Design Requirements:**
1. `get_passed_courses(transcript_str, min_grade=5)`: Parses the student transcript, stores grade points in an `array.array("i")`
    and returns `(student_id, passed_courses_set)`.
2. `resolve_all_prerequisites(course_code, prereq_map)`: A **recursive** function that traverses `prereq_map`
    (dictionary of `course: set_of_direct_prereqs`) and returns the complete set of all direct and indirect prerequisites for
    `course_code`.
3. `validate_enrollment(transcript_str, *requested_courses, prereq_map, min_grade=5)`: Uses `*args` for requested courses
    and prints the student's passed courses and approval/rejection status for each requested course.

### Output Format
- Line 1: `Student: <STUDENT_ID> | Passed Courses: <Sorted_List_of_Passed_Codes>`
- For each requested course:
  `Request <COURSE_CODE>: APPROVED` OR `Request <COURSE_CODE>: REJECTED (Missing: <Sorted_List_of_Missing_Prereqs>)`

This code also contains 2 test cases that need to be executed seperately"""

import array


def get_passed_courses(transcript_str, min_grade=5):
    str_split = transcript_str.split("|")
    student_id, course_grade = str_split[0].strip(), str_split[1].split(",")
    grade_array = array.array("i", [])
    passed_courses_set = set()
    for i in course_grade:
        course, grade = i.split("-")
        grade_array.append(eval(grade.strip()))
        if eval(grade) > 5:
            passed_courses_set.add(course.strip())
    return student_id, passed_courses_set


def resolve_all_prerequisites(course_code, prereq_map):
    req_course_set = set()
    if isinstance(course_code, set):
        if not course_code:
            return ""
        else:
            course_lst = []
            for course in course_code:
                course_lst.extend(
                    (course, *resolve_all_prerequisites(course, prereq_map))
                )
            return course_lst
    elif course_code not in prereq_map:
        return course_code
    req_course_set.update(
        resolve_all_prerequisites(prereq_map.get(course_code, course_code), prereq_map)
    )
    req_course_set.discard("")
    return req_course_set


def validate_enrollment(transcript_str, *requested_courses, prereq_map, min_grade=5):
    student_id, passed_course_set = get_passed_courses(transcript_str, min_grade)
    print(f"Student: {student_id} | Passed Courses: {sorted(passed_course_set)}")
    for course in requested_courses:
        req_course_set = resolve_all_prerequisites(course, prereq_map)
        if req_course_set.issubset(passed_course_set):
            print(f"Request {course}: APPROVED")
        else:
            missing_lst = []
            for i in req_course_set:
                if i not in passed_course_set:
                    missing_lst.append(i)
            print(f"Request {course}: REJECTED (Missing: {missing_lst})")


"""# --- Problem 3: Test Case 1 ---
import io
from contextlib import redirect_stdout

prereqs_tc1 = {
    "CS101": set(),
    "CS201": {"CS101"},
    "CS202": {"CS101"},
    "CS301": {"CS201", "CS202"},
}
transcript_tc1 = "STU-901 | CS101-8, CS201-7, CS202-4, MA101-9"

assert resolve_all_prerequisites("CS301", prereqs_tc1) == {
    "CS101",
    "CS201",
    "CS202",
}, "resolve_all_prerequisites failed"

buf = io.StringIO()
with redirect_stdout(buf):
    validate_enrollment(transcript_tc1, "CS202", "CS301", prereq_map=prereqs_tc1)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "Student: STU-901 | Passed Courses: ['CS101', 'CS201', 'MA101']\n"
    "Request CS202: APPROVED\n"
    "Request CS301: REJECTED (Missing: ['CS202'])"
)
assert (
    actual_out == expected_out
), f"Test Case 1 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 3 - Test Case 1 Passed!")"""


"""# --- Problem 3: Test Case 2 ---
import io
from contextlib import redirect_stdout

prereqs_tc2 = {
    "AI100": set(),
    "AI200": {"AI100"},
    "AI300": {"AI200"},
    "AI400": {"AI300"},
}
transcript_tc2 = "STU-555 | AI100-9, AI300-8"

buf = io.StringIO()
with redirect_stdout(buf):
    validate_enrollment(transcript_tc2, "AI400", prereq_map=prereqs_tc2)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "Student: STU-555 | Passed Courses: ['AI100', 'AI300']\n"
    "Request AI400: REJECTED (Missing: ['AI200'])"
)
assert (
    actual_out == expected_out
), f"Test Case 2 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 3 - Test Case 2 Passed!")"""
