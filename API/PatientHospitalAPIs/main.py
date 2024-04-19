
from bson import ObjectId
from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session
from db import get_db
from schemas.request import request_patient
from schemas.response import response_patient
app=FastAPI()

@app.post("/patient")
def add_patient(patient:request_patient.AddPatient,db_client: Session=Depends(get_db)):
    patient_collection=db_client["patients"]
    patient_collection.insert_one(patient.model_dump())
    return "patient added successfully"

@app.get("/patient/{patient_id}")
def get_patient_by_id(patient_id:str,db_client:Session=Depends(get_db)):
    patient_collection=db_client["patients"]
    patient=patient_collection.find_one({"_id":ObjectId(patient_id)})
    patient["_id"]=str(patient["_id"])
    return patient

@app.get("/patients")
def get_all_patients(db_client:Session=Depends(get_db)):
    patient_collection=db_client["patients"]
    patient_list=patient_collection.find({})
    patients=[response_patient.GetPatients(**patient) for patient in patient_list]
    #basically it converts the mongo data into patient object
    # patients is basically list of objects
    return patients

# **patient: 
# The ** operator is used to unpack the patient dictionary. 
# This means that each key-value pair in the patient dictionary will be passed to the GetPatients 
# class constructor as keyword arguments.
# For example, if patient is {"patient_name": "John", "age": 30, "blood_group": "A+"}, 
# then (**patient) will be equivalent to patient_name="John", age=30, blood_group="A+".


@app.delete("/patient/{patient_id}")
def delete_patient(patient_id:str,db_client:Session=Depends(get_db)):
    patient_collection=db_client["patients"]
    patient_collection.delete_one({"_id":ObjectId(patient_id)})
    return "patient deleted successfully"


@app.put("/patient/{patient_id}")
def update_patient(patient_id: str, patient: request_patient.UpdatePatient, db_client: Session = Depends(get_db)):
    patient_collection = db_client["patients"]
    # Fetch the patient from the database
    existing_patient = patient_collection.find_one({"_id": ObjectId(patient_id)})
    
    # Update patient details if provided in the request
    if patient.patient_name is not None:
        existing_patient["patient_name"] = patient.patient_name
    if patient.age is not None:
        existing_patient["age"] = patient.age
    if patient.blood_group is not None:
        existing_patient["blood_group"] = patient.blood_group
    
    # Update the patient record in the database
    patient_collection.update_one({"_id": ObjectId(patient_id)}, {"$set": existing_patient})
    
    return "Patient updated successfully"