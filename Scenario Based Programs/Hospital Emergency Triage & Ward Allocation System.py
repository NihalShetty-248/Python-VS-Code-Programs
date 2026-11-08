"""Hospital Emergency Triage & Ward Allocation System

Problem Description
A hospital emergency room receives patients with varying vital signs and symptom tags. Each patient record string is parsed into a tuple '(patient_id, name, age, vital_scores_array, symptom_set)' where 'vital_scores_array' is an 'array.array("i")' of three readings
'[heart_rate, systolic_bp, spo2]' and 'symptom_set' is a 'set' of lowercase symptom strings.

A patient is classified as 'CRITICAL' if they have at least one symptom in 'critical_symptoms' (set intersection) OR if their SpO2 ('vital_scores_array[2]') is below 'min_spo2' (default '90') OR heart rate ('vital_scores_array[0]') exceeds 'max_hr' (default '130'). Otherwise, they are classified as '"STABLE"'.

Modular Design Requirements:
1. 'parse_patient_record(raw_str)': Parses 'PATIENT_ID | Name | Age | HR,BP,SPO2 | symptom1,symptom2' into '(patient_id, name, age, array.array("i", vitals), symptom_set)'.
2. 'evaluate_priority(patient_tuple, critical_symptoms, *, min_spo2=90, max_hr=130)': Returns '"CRITICAL"' or '"STABLE"'.
3. 'allocate_wards(*raw_patients, critical_symptoms, **ward_capacities)': Accepts patient strings via '*raw_patients' and ward capacity limits via '**ward_capacities' (e.g., 'ICU=2, General=3'). Assigns '"CRITICAL"' patients to 'ICU' (or '"OVERFLOW"' if 'ICU' is 0) and 'STABLE' patients to 'General' (or '"OVERFLOW"' if 'General' is 0).

Output Format
- For each patient: '<PATIENT_ID> (<Name>) -> Status: <CRITICAL/STABLE> | Assigned Ward: <ICU/General/OVERFLOW>'
- Final line: 'Remaining Capacities: <ward_capacities_dict>'
"""

import array as arr


def parse_patient_record(raw_str):
    vital_scores_array = arr.array("i", [])
    symptoms_set = set()

    split_str = raw_str.split("|")
    patient_id, patient_name, age = (
        split_str[0].strip(),
        split_str[1].strip(),
        int(split_str[2].strip()),
    )
    vital_lst = list(map(int, split_str[3].strip().split(",")))
    vital_scores_array.extend(vital_lst)
    symptoms_set.update(split_str[4].strip().split(","))

    return (patient_id, patient_name, age, vital_scores_array, symptoms_set)


def evaluate_priority(patient_tuple, critical_symptoms, *, min_spo2=90, max_hr=130):
    symptoms = patient_tuple[4]
    heart_rate = patient_tuple[3][0]
    spo2 = patient_tuple[3][2]

    if (
        (symptoms & critical_symptoms != set())
        or (spo2 < min_spo2)
        or (heart_rate > max_hr)
    ):
        return "CRITICAL"

    else:
        return "STABLE"


def allocate_wards(*raw_patients, critical_symptoms, **ward_capacities):
    for patients in raw_patients:
        patient_tpl = parse_patient_record(patients)
        status = evaluate_priority(patient_tpl, critical_symptoms)
        if status == "CRITICAL" and ward_capacities["ICU"] != 0:
            ward = "ICU"
            ward_capacities["ICU"] -= 1

        elif status == "STABLE" and ward_capacities["General"] != 0:
            ward = "General"
            ward_capacities["General"] -= 1

        else:
            ward = "OVERFLOW"

        print(
            f"{patient_tpl[0]} ({patient_tpl[1]}) -> Status: {status} | Assigned Ward: {ward}"
        )
    print(f"Remaining Capacities: {ward_capacities}")


"""# --- Problem 5: Test Case 1 ---
import io
from contextlib import redirect_stdout

crit_symptoms_tc1 = {"chest_pain", "severe_bleeding", "stroke_signs"}
patients_tc1 = [
    "PT-01 | Rajesh Kumar | 58 | 110,145,94 | chest_pain,dizziness",
    "PT-02 | Anita Desai | 34 | 82,120,98 | fever,cough",
    "PT-03 | Vikram Singh | 67 | 138,160,88 | shortness_of_breath,fatigue",
    "PT-04 | Meera Iyer | 45 | 95,130,91 | severe_bleeding,nausea",
]

buf = io.StringIO()
with redirect_stdout(buf):
    allocate_wards(*patients_tc1, critical_symptoms=crit_symptoms_tc1, ICU=2, General=3)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "PT-01 (Rajesh Kumar) -> Status: CRITICAL | Assigned Ward: ICU\n"
    "PT-02 (Anita Desai) -> Status: STABLE | Assigned Ward: General\n"
    "PT-03 (Vikram Singh) -> Status: CRITICAL | Assigned Ward: ICU\n"
    "PT-04 (Meera Iyer) -> Status: CRITICAL | Assigned Ward: OVERFLOW\n"
    "Remaining Capacities: {'ICU': 0, 'General': 2}"
)
assert (
    actual_out == expected_out
), f"Test Case 1 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 5 - Test Case 1 Passed!")"""


"""# --- Problem 5: Test Case 2 ---
import io
from contextlib import redirect_stdout

crit_symptoms_tc2 = {"trauma"}
patients_tc2 = [
    "PT-10 | Arjun | 22 | 75,115,99 | sprain",
    "PT-11 | Divya | 29 | 80,118,97 | headache",
]

buf = io.StringIO()
with redirect_stdout(buf):
    allocate_wards(*patients_tc2, critical_symptoms=crit_symptoms_tc2, ICU=1, General=1)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "PT-10 (Arjun) -> Status: STABLE | Assigned Ward: General\n"
    "PT-11 (Divya) -> Status: STABLE | Assigned Ward: OVERFLOW\n"
    "Remaining Capacities: {'ICU': 1, 'General': 0}"
)
assert (
    actual_out == expected_out
), f"Test Case 2 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 5 - Test Case 2 Passed!")"""
