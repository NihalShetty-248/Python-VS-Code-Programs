"""Hospital Triage Alert System
Task: Filter heart rate anomalies using '*heart_rates' and keyword-only bounds."""


def check_heart_rate(patient_id, *heart_rates, min=60, max=100):
    anomaly_lst = []
    for i in heart_rates:
        if not (min <= i <= max):
            anomaly_lst.append(i)
    print(f"Patient: {patient_id} | Anomalies: {anomaly_lst}")


patient_id = input("Enter patient id: ")
heart_rates = list(map(float, input("Enter heart rates seperated by space: ").split()))
check_heart_rate(patient_id, *heart_rates)
