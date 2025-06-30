from .models import CRMCustomer, CRMTicket
from .status import Status
from time import time
from hashlib import sha512
from urllib.parse import urlencode
from requests import get as http_get, post as http_post
from os import path
import platform
import sys

__VERSION__ = "1.0"

class TentenCRM:
    def __init__(self, **kwargs):
        self.base_url = kwargs.get("base_url")
        self.api_key = kwargs.get("api_key")
        self.api_secret = kwargs.get("api_secret")
        self.timeout = kwargs.get("timeout") or 10
        self.status = Status()

    def remove_none_kv(self, kv):
        output = {}
        for k, v in kv.items():
            output[k] = v or ''
        return output

    #
    # HTTP Request
    #

    def http_req_signature(self):
        tsnow = int(time())
        hash_target = f"{self.api_key}.{self.api_secret}.{tsnow}"
        hash_result = sha512(hash_target.encode('utf-8')).hexdigest()
        return f"{hash_result}.{self.api_key}.{tsnow}"

    def http_headers(self):
        return {
            'Authorization': f"Basic {self.http_req_signature()}",
            'User-Agent': f"TentenCRM/{__VERSION__} ({platform.system()}; U; {platform.machine()}) Python/{sys.version_info.major}.{sys.version_info.minor}"
        }

    def http_upload(self, endpoint, filepath, field_name="file"):
        # Check file exist
        if not path.isfile(filepath):
            raise Exception("File not exist")

        # File
        files = {field_name: (path.basename(filepath), open(filepath, "rb"))}

        # POST
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        req = http_post(
            url,
            files=files,
            headers=self.http_headers(),
            timeout=self.timeout
        )
        req.raise_for_status()
        return req.json()

    def http_post(self, endpoint, payload):
        # POST
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        req = http_post(
            url,
            json=payload,
            headers=self.http_headers(),
            timeout=self.timeout
        )
        req.raise_for_status()
        return req.json()

    def http_get(self, endpoint, params):
        # GET
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        url = url + "?" + urlencode(self.remove_none_kv(params))
        req = http_get(
            url,
            headers=self.http_headers(),
            timeout=self.timeout
        )
        req.raise_for_status()
        return req.json()

    #
    # API: Customer
    #

    def customer_update(self, customer: CRMCustomer):
        return self.http_post("/customer/update/", customer.__dict__)

    def customer_register(self, customer: CRMCustomer):
        return self.http_post("/customer/register/", customer.__dict__)

    def customer_register_step(self, company_id=None, user_id=None, step=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        return self.http_get("/customer/register-step/", {
            "company_id": company_id,
            "user_id": user_id,
            "step": step,
        })

    def customer_pipeline(self, company_id=None, user_id=None, pipeline=None, update_milestone=True):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Also update milestone
        if update_milestone and pipeline in [
                self.status.PIPELINE_NEW_LEAD,
                self.status.PIPELINE_TRIAL_ACTIVE,
                self.status.PIPELINE_TRIAL_EXPIRED,
                self.status.PIPELINE_SUBS_ACTIVE,
                self.status.PIPELINE_SUBS_EXPIRED,
            ]:
            self.customer_milestone(company_id, user_id, pipeline)

        # Update
        return self.http_get("/customer/pipeline/", {
            "company_id": company_id,
            "user_id": user_id,
            "pipeline": pipeline,
        })

    def customer_acquisition(self, company_id=None, user_id=None, acquisition=None, extra=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        return self.http_get("/customer/acquisition/", {
            "company_id": company_id,
            "user_id": user_id,
            "acquisition": acquisition,
            "extra": extra
        })

    def customer_behavior(self, company_id=None, user_id=None, behavior=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        return self.http_get("/customer/behavior/", {
            "company_id": company_id,
            "user_id": user_id,
            "behavior": behavior,
        })

    def customer_activity(self, company_id=None, user_id=None, activity=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        return self.http_get("/customer/activity/", {
            "company_id": company_id,
            "user_id": user_id,
            "activity": activity,
        })

    def customer_milestone(self, company_id=None, user_id=None, milestone=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Normalize
        if milestone == self.status.PIPELINE_NEW_LEAD:
            milestone = self.status.MILESTONE_REGISTERED

        # Update
        return self.http_get("/customer/milestone/", {
            "company_id": company_id,
            "user_id": user_id,
            "milestone": milestone,
        })

    #
    # API: Support Ticket
    #

    def support_ticket_new(self, ticket_data: CRMTicket):
        return self.http_post("/support/new/", ticket_data.__dict__)

    def support_ticket_update(self, ticket_id, ticket_data: CRMTicket):
        return self.http_post(f"/support/update/?id={ticket_id}", ticket_data.__dict__)

    def support_ticket_get_paginated(
        self,
        search="",
        status="all", # open, on_progress, closed
        priority="all", # low, medium, high
        category="all",
        sort="newest",
        page=1,
        per_page=48,
    ):
        # Update
        return self.http_get("/support/get-paginated/", {
            "q": search,
            "status": status,
            "priority": priority,
            "category": category,
            "sort": sort,
            "page": page,
            "per_page": per_page,
        })

    def support_ticket_get_by_id(self, ticket_id):
        # Check
        if not ticket_id:
            raise ValueError("ticket_id cannot be empty.")

        # End
        return self.http_get("/support/get-by-id/", {"id": ticket_id})

    def support_ticket_get_detail(self, ticket_id):
        # Check
        if not ticket_id:
            raise ValueError("ticket_id cannot be empty.")

        # End
        return self.http_get("/support/get-detail/", {"id": ticket_id})

    def support_ticket_delete(self, ticket_id):
        # Check
        if not ticket_id:
            raise ValueError("ticket_id cannot be empty.")

        # End
        return self.http_get("/support/delete/", {"id": ticket_id})

    def support_ticket_status(self, ticket_id, status):
        # Check
        if not ticket_id and not status:
            raise ValueError("ticket_id and status cannot be empty.")

        # End
        return self.http_get("/support/status/", {"id": ticket_id, "status": status})

    def support_ticket_priority(self, ticket_id, priority):
        # Check
        if not ticket_id and not priority:
            raise ValueError("ticket_id and priority cannot be empty.")

        # End
        return self.http_get("/support/priority/", {"id": ticket_id, "priority": priority})

    def support_ticket_attachment_upload(self, ticket_id, filepath):
        # Check
        if not ticket_id:
            raise ValueError("ticket_id cannot be empty.")

        # End
        return self.http_upload(f"/support/upload-attachment/?id={ticket_id}", filepath=filepath)

    def support_ticket_attachment_delete(self, attachment_id):
        # Check
        if not attachment_id:
            raise ValueError("attachment_id cannot be empty.")

        # End
        return self.http_get("/support/delete-attachment/", {"id": attachment_id})


class FlaskTentenCRM(TentenCRM):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        # Get config
        self.base_url = app.config.get("TENTEN_CRM_BASE_URL")
        self.api_key = app.config.get("TENTEN_CRM_API_KEY")
        self.api_secret = app.config.get("TENTEN_CRM_API_SECRET")
        self.timeout = app.config.get("TENTEN_CRM_TIMEOUT") or 10
        if not self.base_url or not self.api_key:
            raise RuntimeError("Missing TENTEN_CRM_BASE_URL or TENTEN_CRM_API_KEY or TENTEN_CRM_API_SECRET in app config.")

        # Init
        super().__init__(
            base_url = self.base_url,
            api_key = self.api_key,
            api_secret = self.api_secret,
            timeout = self.timeout
        )

        # Ext access
        app.extensions = getattr(app, "extensions", {})
        app.extensions["TentenCRM"] = self
