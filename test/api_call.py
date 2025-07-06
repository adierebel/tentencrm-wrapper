from tentencrm import TentenCRM, __VERSION__
from dummy_data import generate_customers, generate_tickets
from os import path
from json import dumps as json_dumps

print(" * API Version:", __VERSION__)

# Init
tenten_crm = TentenCRM(
    base_url = "http://localhost:8081/api/v1/",
    api_key = "686aa8d0a8a0774615682465", # Dummy data, update this
    api_secret = "a86f4661d14af1c96546a674a3c956e0fcd06a87e299ad41c4c3713f7941634449a5c93991da0abba07feefbfb75e0eee6734da9084124bf71268178431eed42", # Dummy data, update this
    timeout = 10
)

#
# Customer
#

def call_customer_api():
    # Dummy data
    customer = generate_customers(1)[0]

    # Register new customer
    customer_result = tenten_crm.customer_register(customer)
    print("Customer registered:", json_dumps(customer_result, indent=2))

    # Update status
    tenten_crm.customer_register_step(
            company_id=customer.company_id,
            step=tenten_crm.status.REGISTER_STEP_REGISTERED
        )
    tenten_crm.customer_pipeline(
            company_id=customer.company_id,
            pipeline=tenten_crm.status.PIPELINE_ONBOARDING,
            message_extra={"extra_1": "ini_pin_kamu"} # wa message placeholder
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
    customer_updated = tenten_crm.customer_update(customer)
    print("Customer updated:", json_dumps(customer_updated, indent=2))

#
# Support Ticket
#

def call_support_api():
    # Dummy data
    tickets = generate_tickets(5)

    # Create new ticket
    ticket_ids = {}
    for i, ticket in enumerate(tickets):
        ticket_ids[i] = tenten_crm.support_ticket_new(ticket).get("payload").get("id")

    # Update first data status and priority
    tenten_crm.support_ticket_status(ticket_id=ticket_ids[0], status="on_progress")
    tenten_crm.support_ticket_priority(ticket_id=ticket_ids[0], priority="high")

    # Upload attachment
    basepath = path.abspath(path.dirname(__file__))
    file1 = path.join(basepath, "attachment.txt")
    file2 = path.join(basepath, "screenshot.jpg")
    file3 = path.join(basepath, "to_be_deleted.txt")
    tenten_crm.support_ticket_attachment_upload(ticket_id=ticket_ids[0], filepath=file1)
    tenten_crm.support_ticket_attachment_upload(ticket_id=ticket_ids[0], filepath=file2)
    attachment_data = tenten_crm.support_ticket_attachment_upload(ticket_id=ticket_ids[0], filepath=file3)
    print("Attachment uploaded:", json_dumps(attachment_data, indent=2))

    # Get data paginated
    data_paginated = tenten_crm.support_ticket_get_paginated(
        search="",
        status="", # open, on_progress, closed
        priority="", # low, medium, high
        category="",
        sort="newest",
        page=1,
        per_page=48,
    )
    print("Data Paginated:", json_dumps(data_paginated, indent=2))

    # Get data by ID
    data_ticket = tenten_crm.support_ticket_get_by_id(ticket_ids[0])
    print("Data By ID:", json_dumps(data_ticket, indent=2))

    # Get ticket detail
    data_detail = tenten_crm.support_ticket_get_detail(ticket_ids[0])
    print("Data Detail:", json_dumps(data_detail, indent=2))

    # Delete
    tenten_crm.support_ticket_delete(ticket_ids[3])
    tenten_crm.support_ticket_attachment_delete(attachment_data.get("payload").get("id"))

# CALL
call_customer_api()
call_support_api()
