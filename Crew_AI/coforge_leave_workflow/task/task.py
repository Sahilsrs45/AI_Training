from crewai import Task
from agents.approval_agent import approval_agent
from agents.hrpolicy_agent import hr_policy_agent
from agents.leave_verification_agent import leave_verifier

def create_tasks(employee_id,requested_days):
    verify_task=Task(
        description=f"""
        Employee ID: {employee_id}
        Requested leave days:{requested_days}
        
        Use check_leave_balance to verify 
        the employee.
        
        Return:
        -Employee ID
        -Employee name
        -Available leave balance
        -Requested leave days
        
        
        If employee does not exist,
        clearly repost NOT_FOUND.
        
        
        """,
        expected_output="Verified employee leave details",
        agent=leave_verifier
        
        
    )
    
    policy_task=Task(
        description=f"""Evaluate the verified leave request.
        
        Requested days:{requested_days}
        
        Company policy:
        1.Requested days must be positive
        2.Requested days must not exceed
        the available leave balances.
        3.Unknown employees are nor elibigle
        4.Never invent leave balances.
        
        Return:
        ELIGIBLE or NOT_ELIGIBLE
        with a clear reason.
        """,
        expected_output="Leave eligibility and reason",
        agent=hr_policy_agent,
        context=[verify_task]
    )    
        
    approval_task=Task(
            description="""
            Review the employee verification
            and HR policy analysis.tools=
            
            Return:
            -Employee name
            -Requested days
            -Leave balance
            -Recommendation: APPROVE or REJECT
            -Reason
            
            
            
            Only recommend APPROVE if
            verification and policy checks pass.tools=
            
            Do not modify any employee recoreds.tools=
            """,
            
            
            
            
            expected_output="Final leave recommendation",
            agent=approval_agent,
            context=[verify_task,policy_task]
        )
    
    return[
            verify_task,
            policy_task,
            approval_task
        ]
        
        
        
