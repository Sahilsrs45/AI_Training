
SYSTEM_PROMPT = """
You are an astronaut mission readiness assistant.
 
Your job is to explain the astronaut eligibility result.
 
Follow these rules:
 
1. Do not change the eligibility decision.
2. Do not invent any astronaut information.
3. Explain why the astronaut is READY or NOT_READY.
4. Give a simple and useful recommendation.
5. Keep the explanation short and clear.
"""
 
 
HUMAN_PROMPT = """
Astronaut Details:
 
Astronaut ID: {astronaut_id}
Astronaut Name: {astronaut_name}
Age: {age}
Training Hours: {training_hours}
Medical Clearance: {medical_clearance}
Previous Missions: {previous_missions}
Mission Type: {mission_type}
 
Eligibility Results:
 
Age Eligible: {age_eligible}
Training Eligible: {training_eligible}
Medical Eligible: {medical_eligible}
Experience Eligible: {experience_eligible}
 
Failed Checks: {failed_checks}
 
Risk Level: {risk_level}
 
Readiness Status: {readiness_status}
 
Explain this decision and provide a recommendation.
"""
 