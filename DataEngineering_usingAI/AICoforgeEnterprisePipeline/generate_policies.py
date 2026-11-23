from pathlib import Path
from reportlab.pdfgen import canvas
folder = Path("data/policies")
folder.mkdir(parents=True, exist_ok=True)
policies = {
   "leave_policy.pdf": (
       "Employees receive 20 annual leave days. "
       "Leave requests require manager approval."
   ),
   "insurance_policy.pdf": (
       "Employees are eligible for medical insurance. "
       "Coverage details depend on the company plan."
   ),
   "wfh_policy.pdf": (
       "Employees may request work from home. "
       "Manager approval is required."
   ),
   "reimbursement_policy.pdf": (
       "Employees can submit eligible business expenses. "
       "Receipts and manager approval are required."
   )
}
for filename, content in policies.items():
   path = folder / filename
   pdf = canvas.Canvas(str(path))
   pdf.setFont("Helvetica", 12)
   pdf.drawString(50, 780, filename)
   pdf.drawString(50, 740, content[:90])
   pdf.save()
   print("Created:", path)