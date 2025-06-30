from tentencrm import CRMCustomer, CRMTicket
from faker import Faker
from bson import ObjectId
from datetime import datetime, timedelta
from random import choices as rand_choices, randrange
from time import time

fake = Faker('id_ID')

def generate_customers(n=20):
    customers = []
    for _ in range(n):
        company_id = str(ObjectId())
        user_id = str(ObjectId())
        join_date = fake.date_time_between(start_date='-2y', end_date='now').isoformat()
        customer = CRMCustomer(
            company_id=company_id,
            company_name=fake.company(),
            company_city=fake.city(),
            user_id=user_id,
            user_name=fake.name(),
            user_email=fake.email(),
            user_contact=fake.phone_number(),
            join_date=join_date
        )
        customers.append(customer)
    return customers

def generate_tickets(n=20):
    tickets = []
    for _ in range(n):
        ticket = CRMTicket(
            code=f"TK-{datetime.now().strftime('%y%m%d')}-{randrange(1, 9)}{str(int(time()))[-4:]}",
            status=rand_choices(['open', 'on_progress', 'closed']),
            priority=rand_choices(['low', 'medium', 'high']),
            category=rand_choices(['Billing', 'Account', 'Application']),
            subject=rand_choices([
                "Login failed", "Email not received", "Payment declined", "Dashboard not loading",
                "Data sync issue", "Unexpected error", "Feature request", "Slow performance"
            ]),
            description=fake.paragraph(nb_sentences=3),
            company_name=fake.company(),
            agent_name=fake.name(),
        )
        tickets.append(ticket)
    return tickets
