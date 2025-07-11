from dataclasses import dataclass

@dataclass
class CRMCustomer:
    company_id: str
    company_name: str
    company_city: str
    user_id: str
    user_name: str
    user_email: str
    user_contact: str
    join_date: str

@dataclass
class CRMTicket:
    code: str
    status: str
    priority: str
    category: str
    subject: str
    description: str
    company_id: str
    company_name: str
    agent_id: str
    agent_name: str
