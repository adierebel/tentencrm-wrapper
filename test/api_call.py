from tentencrm import TentenCRM, __VERSION__
from dummy_data import generate_customers, generate_tickets

print(" * API Version:", __VERSION__)

# Init
tenten_crm = TentenCRM(
    base_url = "http://localhost:8081/api/v1/",
    api_key = "6862cdf05defe93a7bc5cdaa", # Dummy data, update this
    api_secret = "4a75c74ef1a469dd43d0b4ec4b3b511de5347c0d47dcf36db39feb1a07d71ed42ada62c1226cacbf14c55d72a8e55b22c09c0e578c53c99a6e0af82c101fccd8", # Dummy data, update this
    timeout = 10
)

#
# Customer
#

def call_customer_api():
    # Dummy data
    customer = generate_customers(1)[0]

    # Register new customer
    tenten_crm.customer_register(customer)

    # Update status
    tenten_crm.customer_register_step(
            company_id=customer.company_id,
            step=tenten_crm.status.REGISTER_STEP_REGISTERED
        )
    tenten_crm.customer_pipeline(
            company_id=customer.company_id,
            pipeline=tenten_crm.status.PIPELINE_ONBOARDING
        )
    tenten_crm.customer_acquisition(
            company_id=customer.company_id,
            acquisition=tenten_crm.status.ACQUISITION_PAID_ADS,
            extra="google"
        )
    tenten_crm.customer_behavior(
            company_id=customer.company_id,
            behavior=tenten_crm.status.BEHAVIOR_QUICK_ADOPTER
        )
    tenten_crm.customer_activity(
            company_id=customer.company_id,
            activity=tenten_crm.status.ACTIVITY_MODERATE
        )
    tenten_crm.customer_milestone(
            company_id=customer.company_id,
            milestone=tenten_crm.status.MILESTONE_REGISTERED
        )

    # Edit customer
    customer.user_name = generate_customers(1)[0].user_name # update username
    tenten_crm.customer_update(customer)

#
# Support Ticket
#

def call_support_api():
    # Dummy data
    tickets = generate_tickets(5)

    # Create new ticket
    ticket_ids = {}
    for i, ticket in enumerate(tickets):
        ticket_ids[i] = tenten_crm.support_ticket_new(ticket).payload.id_

    # Update first data
    tenten_crm.support_ticket_status(ticket_id=ticket_ids[0], status="on_progress")
    tenten_crm.support_ticket_priority(ticket_id=ticket_ids[0], priority="high")
    attachment_id = tenten_crm.support_ticket_attachment_upload(ticket_id=ticket_ids[0], filepath="./attachment.txt")

    # Get data paginated
    data_paginated = tenten_crm.support_ticket_get_paginated(
        search="",
        status="all", # open, on_progress, closed
        priority="all", # low, medium, high
        category="all",
        sort="newest",
        page=1,
        per_page=48,
    )
    print("Data Paginated:", data_paginated)

    # Get data by ID
    data_ticket = tenten_crm.support_ticket_get_by_id(ticket_ids[0])
    print("Data By ID:", data_ticket)

    # Get ticket detail
    data_detail = tenten_crm.support_ticket_get_detail(ticket_ids[0])
    print("Data Detail:", data_detail)

    # Delete
    tenten_crm.support_ticket_delete(ticket_ids[3])
    tenten_crm.support_ticket_attachment_delete(attachment_id)

# CALL
call_customer_api()
call_support_api()
