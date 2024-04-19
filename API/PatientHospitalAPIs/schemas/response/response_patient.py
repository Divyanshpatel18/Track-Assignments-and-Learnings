# response_patient.py

from typing import List, Optional
from pydantic import BaseModel, Field

class GetPatients(BaseModel):
    patient_name: str
    age: int
    blood_group: Optional[str]

    @classmethod
    def from_mongo(patient):
    
        # extracting relevant fields from the patient dictionary
        patient_name = patient["patient_name"]
        age = patient["age"]
        blood_group = patient.get("blood_group")
        # for keys missing we use get bcoz blood group can be null

        #creating new instance of GetPatients with extracted fields
        new_patient = GetPatients(patient_name=patient_name, age=age, blood_group=blood_group)

        # adding the new instance to the list of patients

        return patient
