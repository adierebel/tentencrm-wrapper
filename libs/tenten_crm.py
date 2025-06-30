from .models import CRMCustomer
from .status import Status
from time import time
from random import randrange
from hashlib import sha512
from urllib.parse import urlencode
from requests import get as http_get, post as http_post
from os import path
import platform
import sys

__VERSION = "1.0"

class TentenCRM:
    def __init__(self, api_base_url=None, api_key=None):
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.http_timeout = 10
        self.status = Status()

    #
    # HTTP Request
    #

    def http_req_signature(self):
        tsnow = int(time())
        multiplier = randrange(1, 9)
        hash_target = f"{self.api_key*multiplier}.{tsnow}"
        hash_result = sha512(hash_target.encode('utf-8')).hexdigest()
        return f"{hash_result}.{multiplier}.{tsnow}"

    def http_headers(self):
        return {
            'Authorization': f"Basic {self.http_req_signature()}",
            'User-Agent': f"TentenCRM/{__VERSION} ({platform.system()}; U; {platform.machine()}) Python/{sys.version_info.major}.{sys.version_info.minor}"
        }

    def http_upload(self, endpoint, filepath):
        try:
            # Check file exist
            if not path.isfile(filepath):
                raise Exception("File not exist")

            # File
            files = {"file": (path.basename(filepath), open(filepath, "rb"))}

            # POST
            url = f"{self.api_base_url.rstrip('/')}/{endpoint.lstrip('/')}"
            req = http_post(
                url,
                files=files,
                headers=self.http_headers(),
                timeout=self.http_timeout
            )
            return req.json()

        except Exception as e:
            raise e

    def http_post(self, endpoint, payload):
        try:
            # POST
            url = f"{self.api_base_url.rstrip('/')}/{endpoint.lstrip('/')}"
            req = http_post(
                url,
                json=payload,
                headers=self.http_headers(),
                timeout=self.http_timeout
            )
            return req.json()

        except Exception as e:
            raise e

    def http_get(self, endpoint, params):
        try:
            # GET
            url = f"{self.api_base_url.rstrip('/')}/{endpoint.lstrip('/')}"
            url = url + "?" + urlencode(params)
            req = http_get(
                url,
                headers=self.http_headers(),
                timeout=self.http_timeout
            )
            return req.json()

        except Exception as e:
            raise e

    #
    # API: Customer
    #

    def customer_register(self, customer: CRMCustomer):
        pass

    def customer_register_step(self, company_id=None, user_id=None, step=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        pass

    def customer_update(self, company_id=None, user_id=None, customer: CRMCustomer=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        pass

    def customer_pipeline(self, company_id=None, user_id=None, pipeline=None, update_milestone=True):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        pass

        # Also update milestone
        if update_milestone and pipeline in [
                self.status.PIPELINE_NEW_LEAD,
                self.status.PIPELINE_TRIAL_ACTIVE,
                self.status.PIPELINE_TRIAL_EXPIRED,
                self.status.PIPELINE_SUBS_ACTIVE,
                self.status.PIPELINE_SUBS_EXPIRED,
            ]:
            self.customer_milestone(company_id, user_id, pipeline)

    def customer_acquisition(self, company_id=None, user_id=None, acquisition=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        pass

    def customer_behavior(self, company_id=None, user_id=None, behavior=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        pass

    def customer_activity(self, company_id=None, user_id=None, activity=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Update
        pass

    def customer_milestone(self, company_id=None, user_id=None, milestone=None):
        # Check
        if not company_id and not user_id:
            raise ValueError("company_id or user_id cannot be empty.")

        # Normalize
        if milestone == self.status.PIPELINE_NEW_LEAD:
            milestone = self.status.MILESTONE_REGISTERED

        # Update
        pass

    #
    # API: Support Ticket
    #

    def support_ticket_get_by_id(self):
        pass

    def support_ticket_get_paginated(self):
        pass

    def support_ticket_get_detail(self):
        pass

    def support_ticket_new(self):
        pass

    def support_ticket_update(self):
        pass

    def support_ticket_delete(self):
        pass

    def support_ticket_status(self):
        pass


class FlaskTentenCRM(TentenCRM):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        # Get config
        self.api_base_url = app.config.get("TENTEN_CRM_BASE_URL")
        self.api_key = app.config.get("TENTEN_CRM_API_KEY")
        if not self.api_base_url or not self.api_key:
            raise RuntimeError("Missing TENTEN_CRM_BASE_URL or TENTEN_CRM_API_KEY in app config.")

        # Init
        super().__init__(self.api_base_url, self.api_key)

        # Ext access
        app.extensions = getattr(app, "extensions", {})
        app.extensions["TentenCRM"] = self
