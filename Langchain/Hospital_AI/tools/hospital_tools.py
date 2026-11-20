from langchain.tools import tool
 
 
# In-memory storage
 
patients = []
doctors = [
    {
        "doctor_id": "D201",
        "doctor_name": "Dr. Amit Sharma",
        "specialization": "Cardiologist",
        "available_slots": {
            "2026-11-20": ["10:00", "11:00", "12:00"]
        }
    },
    {
        "doctor_id": "D202",
        "doctor_name": "Dr. Priya Patel",
        "specialization": "Dermatologist",
        "available_slots": {
            "2026-11-20": ["09:00", "10:00", "14:00"]
        }
    },
    {
        "doctor_id": "D203",
        "doctor_name": "Dr. Rahul Verma",
        "specialization": "Cardiologist",
        "available_slots": {
            "2026-11-20": ["09:00", "13:00", "15:00"]
        }
    }
]
appointments = []
medical_records = {}
 
 
# TOOL 1: REGISTER PATIENT
 
@tool
def register_patient(
    full_name: str,
    age: int,
    phone: str,
    symptoms: str = ""
) -> dict:
    """Register a new patient in the hospital."""
 
    if not full_name.strip():
        raise ValueError("Patient name is required")
 
    if age <= 0 or age > 120:
        raise ValueError("Invalid patient age")
 
    if len(phone) != 10 or not phone.isdigit():
        raise ValueError("Invalid phone number")
 
    for patient in patients:
        if patient["phone"] == phone:
            raise ValueError("Patient already registered")
 
    patient_id = f"P{len(patients) + 1001}"
 
    patients.append({
        "patient_id": patient_id,
        "full_name": full_name,
        "age": age,
        "phone": phone,
        "symptoms": symptoms
    })
 
    return {
        "status": "success",
        "patient_id": patient_id,
        "message": "Patient registered successfully"
    }
 
 
# TOOL 2: CHECK DOCTOR AVAILABILITY
 
@tool
def check_doctor_availability(
    specialization: str,
    preferred_date: str
) -> dict:
    """Check doctor availability using specialization and date."""
 
    available_doctors = []
 
    for doctor in doctors:
 
        if doctor["specialization"].lower() == specialization.lower():
 
            slots = doctor["available_slots"].get(preferred_date, [])
 
            if slots:
                available_doctors.append({
                    "doctor_id": doctor["doctor_id"],
                    "doctor_name": doctor["doctor_name"],
                    "specialization": doctor["specialization"],
                    "available_slots": slots
                })
 
    return {
        "status": "success",
        "available_doctors": available_doctors
    }
 
 
# TOOL 3: BOOK APPOINTMENT
 
@tool
def book_appointment(
    patient_id: str,
    doctor_id: str,
    appointment_date: str,
    time_slot: str
) -> dict:
    """Book an appointment for an existing patient."""
 
    patient = next(
        (p for p in patients if p["patient_id"] == patient_id),
        None
    )
 
    if patient is None:
        raise ValueError("Patient not found")
 
    doctor = next(
        (d for d in doctors if d["doctor_id"] == doctor_id),
        None
    )
 
    if doctor is None:
        raise ValueError("Doctor not found")
 
    slots = doctor["available_slots"].get(appointment_date, [])
 
    if time_slot not in slots:
        raise ValueError("Appointment slot not available")
 
    appointment_id = f"A{len(appointments) + 5001}"
 
    slots.remove(time_slot)
 
    appointments.append({
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "appointment_date": appointment_date,
        "time_slot": time_slot
    })
 
    return {
        "status": "success",
        "appointment_id": appointment_id,
        "message": "Appointment booked successfully"
    }
 
 
# TOOL 4: GET PATIENT MEDICAL RECORDS
 
@tool
def get_patient_medical_records(
    patient_id: str
) -> dict:
    """Retrieve medical records for an authorized patient."""
 
    patient = next(
        (p for p in patients if p["patient_id"] == patient_id),
        None
    )
 
    if patient is None:
        raise ValueError("Patient not found")
 
    records = medical_records.get(patient_id)
 
    if records is None:
        raise ValueError("Medical records not found")
 
    return {
        "status": "success",
        "patient_id": patient_id,
        "medical_records": records
    }
 
 
# TOOL 5: CALCULATE HOSPITAL BILL
 
@tool
def calculate_hospital_bill(
    patient_id: str,
    consultation_fee: float,
    lab_charges: float,
    treatment_charges: float,
    discount_percent: float = 0
) -> dict:
    """Calculate the hospital bill for a patient."""
 
    patient = next(
        (p for p in patients if p["patient_id"] == patient_id),
        None
    )
 
    if patient is None:
        raise ValueError("Patient not found")
 
    if (
        consultation_fee < 0
        or lab_charges < 0
        or treatment_charges < 0
    ):
        raise ValueError("Charges cannot be negative")
 
    if not 0 <= discount_percent <= 100:
        raise ValueError("Invalid discount percentage")
 
    subtotal = (
        consultation_fee
        + lab_charges
        + treatment_charges
    )
 
    discount = subtotal * discount_percent / 100
 
    total = subtotal - discount
 
    return {
        "status": "success",
        "patient_id": patient_id,
        "consultation_fee": round(consultation_fee, 2),
        "lab_charges": round(lab_charges, 2),
        "treatment_charges": round(treatment_charges, 2),
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "total": round(total, 2),
        "currency": "INR"
    }
 
 
# COMBINE ALL FIVE TOOLS
 
hospital_tools = [
    register_patient,
    check_doctor_availability,
    book_appointment,
    get_patient_medical_records,
    calculate_hospital_bill
]