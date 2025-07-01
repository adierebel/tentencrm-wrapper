# TentenCRM API Wrapper

Python API Wrapper for TentenCRM

## Installation

### Production

Run this command to install directly from github repo:

```
pip install git+https://github.com/adierebel/tentencrm-wrapper
```

or add this to `requirements.txt`

```
tentencrm @ git+https://github.com/adierebel/tentencrm-wrapper
```

### Development

Run this command for install on local `venv`

```
pip install .
```

To test, run this command:

```
python test/api_call.py
```

# API

Exposed function and const

## Initialization

Use as Flask plugins

```python
from flask import Flask
from tentencrm import FlaskTentenCRM

# Init app and update config
app = Flask(__name__)
app.config.update(
    TENTEN_CRM_BASE_URL = "http://localhost:8081/api/v1/",
    TENTEN_CRM_API_KEY = "your-api-key",
    TENTEN_CRM_API_SECRET = "your-secret",
    TENTEN_CRM_TIMEOUT = 10
)

# Init TentenCRM API
tentencrm = FlaskTentenCRM(app)
```

Use directly:

```python
from tentencrm import TentenCRM
tenten_crm = TentenCRM(
    base_url = "http://localhost:8081/api/v1/",
    api_key = "your-api-key",
    api_secret = "your-secret",
    timeout = 10
)
```


#### API Customer
- `customer_register(customer: CRMCustomer)`: Registrasi customer baru.
- `customer_update(customer: CRMCustomer)`: Update data customer.
- `customer_register_step(company_id, user_id, step)`: Update step registrasi.
- `customer_pipeline(company_id, user_id, pipeline, update_milestone=True)`: Update pipeline customer.
- `customer_acquisition(company_id, user_id, acquisition, extra)`: Update sumber akuisisi customer.
- `customer_behavior(company_id, user_id, behavior)`: Update perilaku customer.
- `customer_activity(company_id, user_id, activity)`: Update aktivitas customer.
- `customer_milestone(company_id, user_id, milestone)`: Update milestone customer.

#### API Support Ticket
- `support_ticket_new(ticket_data: CRMTicket)`: Membuat tiket support baru.
- `support_ticket_update(ticket_id, ticket_data: CRMTicket)`: Update tiket support.
- `support_ticket_get_paginated(...)`: Mendapatkan daftar tiket dengan pagination.
- `support_ticket_get_by_id(ticket_id)`: Mendapatkan tiket berdasarkan ID.
- `support_ticket_get_detail(ticket_id)`: Mendapatkan detail tiket.
- `support_ticket_delete(ticket_id)`: Menghapus tiket.
- `support_ticket_status(ticket_id, status)`: Update status tiket.
- `support_ticket_priority(ticket_id, priority)`: Update prioritas tiket.
- `support_ticket_attachment_upload(ticket_id, filepath)`: Upload lampiran ke tiket.
- `support_ticket_attachment_delete(attachment_id)`: Hapus lampiran tiket.

## Model Data

### CRMCustomer

Model data untuk customer.

```python
class : CRMCustomer:
    company_id: str
    company_name: str
    company_city: str
    user_id: str
    user_name: str
    user_email: str
    user_contact: str
    join_date: str
```

### CRMTicket

Model data untuk support ticket.

```python
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

```

---

## Status

Konstanta status pipeline, milestone, etc.

```python
from tentencrm import TentenCRM
tenten_crm = TentenCRM(
    base_url = "http://localhost:8081/api/v1/",
    api_key = "your-api-key",
    api_secret = "your-secret",
    timeout = 10
)

tenten_crm.status.PIPELINE_NEW_LEAD
tenten_crm.status.PIPELINE_ONBOARDING
tenten_crm.status.PIPELINE_TRIAL_ACTIVE
tenten_crm.status.PIPELINE_TRIAL_EXPIRED
tenten_crm.status.PIPELINE_SUBS_ACTIVE
#...
```
