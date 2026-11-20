from langchain_core.tools import tool
from uuid import uuid4


@tool
def check_password_status(id: str) -> str:
    """Check simulated password status for an employee"""

    accounts = {
        "EMP101": "Expired",
        "EMP102": "Active",
        "EMP103": "Locked"
    }
    status = accounts.get(id, "Unknown")
    return f"password status for {id} : {status}"


@tool
def troubleshoot_vpn(issue: str) -> str:
    """provide troubleshooting steps for VPN problems."""

    return (
        "1. Check internet connectivity",
        "2. Restart the VPN client",
        "3. verify VPN server settings",
        "4. Contact IT if the problem continues."
    )


@tool
def check_software_availability(software_name: str) -> str:
    """check whether software is approved for installation."""

    approved_software = [
        "Python",
        "VS Code",
        "Microsoft Teams",
        "Microsoft Office"
    ]

    if software_name.lower() in [
        item.lower() for item in approved_software
    ]:
        return f"{software_name} is approved for installation."

    return (
        f"{software_name} is not in the approved software list."
        "It approval is required."
    )


@tool
def search_knowledge_base(issue: str) -> str:
    """Search predefined IT support knowledge-base articles."""

    knowledge_base = {
        "outlook": "Restart Outlook and check your mail profile.",
        "email": "check network access and email credentials",
        "printer": "Check printer connection and restart the spooler.",
        "laptop": "Restart the laptop and check hardware indicators."
    }

    for keyword, solution in knowledge_base.items():
        if keyword in issue.lower():
            return solution

    return "No matching knowledge-base article found."

# @tool
# def create_support_ticket(id:str,issue:str,priority:str) -> str:
#     """Create a simulated IT support ticket for escalations"""

#     ticket_id = "INC-" + uuid4().hex[:8].upper()

#     return (
#         f"Ticket created successfully",
#         f"Ticket ID: {ticket_id}",
#         f"Employee: {id}",
#         f"Priority: {priority}",
#         f"Issue: {issue}"
#     )


@tool
def create_support_ticket(id: str, issue: str, priority: str) -> dict:
    """
    Create a simulated IT support ticket for escalations.
    """

    ticket_id = "INC-" + uuid4().hex[:8].upper()

    return {
        "ticketId": ticket_id,
        "employeeId": id,
        "priority": priority,
        "issue": issue
    }


it_tools = [
    check_password_status,
    troubleshoot_vpn,
    check_software_availability,
    search_knowledge_base,
    create_support_ticket
]
