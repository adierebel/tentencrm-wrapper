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

```python
# Registrasi customer baru.
tenten_crm.customer_register(customer: CRMCustomer)

# Update data customer.
tenten_crm.customer_update(customer: CRMCustomer)

# Update step registrasi.
tenten_crm.customer_register_step(company_id, user_id, step)

# Update pipeline customer.
tenten_crm.customer_pipeline(company_id, user_id, pipeline, update_milestone=True)

# Update sumber akuisisi customer.
tenten_crm.customer_acquisition(company_id, user_id, acquisition, extra)

# Update perilaku customer.
tenten_crm.customer_behavior(company_id, user_id, behavior)

# Update aktivitas customer.
tenten_crm.customer_activity(company_id, user_id, activity)

# Update milestone customer.
tenten_crm.customer_milestone(company_id, user_id, milestone)

# All function return customer detail like this:
"""
{
  "status_code": 200,
  "payload": {
    "id": "6863a11b6f8090b8dd62e51d",
    "created": "2025-07-01T08:49:31",
    "modified": "2025-07-01T08:49:45.705221",
    "company_id": "6863a119ea5b393be44f1c4e",
    "company_name": "PD Fujiati Iswahyudi (Persero) Tbk",
    "company_city": "Banjarbaru",
    "user_id": "6863a119ea5b393be44f1c4f",
    "user_name": "Nadia Prasasta",
    "user_email": "jabal58@example.net",
    "user_contact": "+62 (18) 513 3838",
    "join_date": "2024-01-10T21:00:49",
    "pipeline": "onboarding",
    "status_acquisition": "paid_ads",
    "status_behavior": "quick_adopter",
    "status_activity": "moderate",
    "status_milestone": "registered",
    "status_register": null,
    "acquisition_extra": "google"
  }
}
"""
```

#### API Support Ticket

```python
# Membuat tiket support baru.
tenten_crm.support_ticket_new(ticket_data: CRMTicket)
"""
Output ticket detail like `support_ticket_get_by_id`
"""

# Update tiket support.
tenten_crm.support_ticket_update(ticket_id, ticket_data: CRMTicket)
"""
Output ticket detail like `support_ticket_get_by_id`
"""

# Mendapatkan daftar tiket dengan pagination.
tenten_crm.support_ticket_get_paginated(
    search="",
    status="", # open, on_progress, closed
    priority="", # low, medium, high
    category="",
    sort="newest", # newest / oldest
    page=1,
    per_page=48,
)
"""
{
  "status": 200,
  "payload": {
    "page": 1,
    "per_page": 48,
    "total": 5,
    "items": [
      {
        "id": "6863a1346f8090b8dd62e525",
        "created": "2025-07-01T08:49:56",
        "modified": "2025-07-01T08:49:56",
        "closed": null,
        "code": "TK-250701-49785",
        "status": "closed",
        "priority": "low",
        "category": "Application",
        "subject": "Login failed",
        "description": "Repellat quas laudantium dolor laboriosam eligendi cupiditate. Dolor eveniet dolorem officia. Quia consequatur tenetur ipsam nesciunt.",
        "company_id": null,
        "company_name": "CV Hidayanto",
        "agent_id": null,
        "agent_name": "Jaya Astuti"
      },
      ......
    ]
  }
}
"""

# Mendapatkan tiket berdasarkan ID.
tenten_crm.support_ticket_get_by_id(ticket_id)
"""
{
  "status": 200,
  "payload": {
    "id": "6863a12b6f8090b8dd62e521",
    "created": "2025-07-01T08:49:47",
    "modified": "2025-07-01T08:50:00",
    "closed": null,
    "code": "TK-250701-89785",
    "status": "on_progress",
    "priority": "high",
    "category": "Application",
    "subject": "Data sync issue",
    "description": "Aut eaque hic fuga. Nobis quaerat velit rerum quam iusto. Autem asperiores consequuntur consequuntur sunt magni vero.",
    "company_id": null,
    "company_name": "Perum Hastuti (Persero) Tbk",
    "agent_id": null,
    "agent_name": "Halim Prasetya"
  }
}
"""

# Mendapatkan detail tiket.
tenten_crm.support_ticket_get_detail(ticket_id)
"""
{
  "status": 200,
  "payload": {
    "ticket": {
      "id": "6863a12b6f8090b8dd62e521",
      "created": "2025-07-01T08:49:47",
      "modified": "2025-07-01T08:50:00",
      "closed": null,
      "code": "TK-250701-89785",
      "status": "on_progress",
      "priority": "high",
      "category": "Application",
      "subject": "Data sync issue",
      "description": "Aut eaque hic fuga. Nobis quaerat velit rerum quam iusto. Autem asperiores consequuntur consequuntur sunt magni vero.",
      "company_id": null,
      "company_name": "Perum Hastuti (Persero) Tbk",
      "agent_id": null,
      "agent_name": "Halim Prasetya"
    },
    "history": [
      {
        "id": "6863a1366f8090b8dd62e526",
        "ticket_id": "6863a12b6f8090b8dd62e521",
        "created": "2025-07-01T08:49:58",
        "modified": "2025-07-01T08:49:58",
        "update_type": "status",
        "value_new": "on_progress",
        "value_prev": "open",
        "agent_id": null,
        "agent_name": "API User"
      },
      ......
    ],
    "attachment": [
      {
        "id": "6863a13c6f8090b8dd62e529",
        "ticket_id": "6863a12b6f8090b8dd62e521",
        "created": "2025-07-01T08:50:04",
        "modified": "2025-07-01T08:50:04",
        "name": "screenshot.jpg",
        "filename": "6863a12b6f8090b8dd62e521-523_screenshot.jpg",
        "filetype": ".jpg",
        "filesize": 57586,
        "url": "http://localhost:8081/file/public/upload/6863a12b6f8090b8dd62e521-523_screenshot.jpg"
      },
      ......
    ]
  }
}
"""

# Menghapus tiket.
tenten_crm.support_ticket_delete(ticket_id)
"""
{
  "status": 200,
  "payload": {
    "id": "6863a12b6f8090b8dd62e421"
  }
}
"""

# Update status tiket.
tenten_crm.support_ticket_status(ticket_id, status)
"""
{
  "status": 200,
  "payload": {
    "id": "6863a12b6f8090b8dd62e221"
  }
}
"""

# Update prioritas tiket.
tenten_crm.support_ticket_priority(ticket_id, priority)
"""
{
  "status": 200,
  "payload": {
    "id": "68623a12b6f8090b8dd62e544"
  }
}
"""

# Upload lampiran ke tiket.
tenten_crm.support_ticket_attachment_upload(ticket_id, filepath)
"""
{
  "status": 200,
  "payload": {
    "id": "6863a13e6f8090b8dd62e52a",
    "ticket_id": "6863a12b6f8090b8dd62e521",
    "created": "2025-07-01T08:50:06.456740",
    "modified": "2025-07-01T08:50:06.456740",
    "name": "error_logs.txt",
    "filename": "6863a12b6f8090b8dd62e521-235_error_logs.txt",
    "filetype": ".txt",
    "filesize": 17,
    "url": "http://localhost:8081/file/public/upload/6863a12b6f8090b8dd62e521-235_error_logs.txt"
  }
}
"""

# Hapus lampiran tiket.
tenten_crm.support_ticket_attachment_delete(attachment_id)
"""
{
  "status": 200,
  "payload": {
    "id": "6863a12b6f809238dd62e5212"
  }
}
"""
```

## Model Data

### CRMCustomer

Model data untuk customer.

```python
class CRMCustomer:
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
