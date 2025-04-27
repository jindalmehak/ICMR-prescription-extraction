# utils/postprocessing.py
import re

def structure_text(raw_text):
    structured_data = {
        "Patient_Name": None,
        "Doctor_Name": None,
        "Date": None,
        "Medicines": [],
        "Instructions": None
    }

    # Simple rules to structure text
    lines = raw_text.split('\n')
    for line in lines:
        line = line.strip()
        if 'Dr.' in line:
            structured_data["Doctor_Name"] = line
        elif re.search(r'\d{2}/\d{2}/\d{4}', line):
            structured_data["Date"] = line
        elif any(word in line.lower() for word in ['mg', 'tablet', 'capsule']):
            structured_data["Medicines"].append({"Medicine_Info": line})
        elif 'take' in line.lower() or 'instruction' in line.lower():
            structured_data["Instructions"] = line
        else:
            if not structured_data["Patient_Name"]:
                structured_data["Patient_Name"] = line

    return structured_data
