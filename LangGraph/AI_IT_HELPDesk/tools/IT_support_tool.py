from langchain_core.tools import tool

from uuid import uuid4


@tool
def check_password_status(employee_id:str)->str:
    """Check aimulated password status for an employee."""
    
    accounts={
        "EMP101":"Expired",
        "EMP102":"Activate",
        "EMP103":"Locked"
    }
    status=accounts.get(employee_id,"Unknown")
    
    return f"Password status for {employee_id}:{status}"


@tool
def troubleshoot_vpn(issue:str)->str:
    """Provide troubleshooting steps for VPN problems"""
    return(
        "1.Check internet connectivity."
        "2.Restart the VPN client.",
        "3.Verify VPN server settings"
        "4.Contact IT if the problem continues"
    )
    
@tool
def check_software_availability(software_name:str)->str:
    """Check whether software is approved for installation."""
    approved_software=[
        "Python",
        "VSCode",
        "Microsoft Teams",
        "Microsoft Office"
    ]    
    if software_name.lower() in[
        item.lower() for item in approved_software
    ]:
        return f"{software_name} is approved for installation."
    
    return(
        f"{software_name} is not in the approved software list."
        "IT approval is required"
    )
    
@tool
def search_knowledge_base(issue:str)->str:
    """Search predefined IT support knowledge-base articles."""
    
    knowledge_base = {
        "outlook": "Restart Outlook and check your mail profile.",
        "email": "check network access and email credentials",
        "printer": "Check printer connection and restart the spooler.",
        "laptop": "Restart the laptop and chekc hardware indicators."
    }
 
    for keyword, solution in knowledge_base.items():
        if keyword in issue.lower():
            return solution
 
    return "No matching knowledge-base article found."
 
@tool
def create_support_ticket(
   employee_id:str,
    issue:str,
    priority:str
) -> str:
    """Create a simulated IT support ticket for escalations"""
 
    ticket_id = "INC-" + uuid4().hex[:8].upper()
 
    return (
        f"Ticket is created successfully."
        f"Ticket ID : {ticket_id}"
        f"Employee:{employee_id}."
        f"Priority :{priority}"
        f"Issue:{issue}"
       
    )
    
its_tools=[
    check_password_status,
    troubleshoot_vpn,
    check_software_availability,
    search_knowledge_base,
    create_support_ticket
]    
    