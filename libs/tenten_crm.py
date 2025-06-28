from .models import CRMCustomer
from .status import Status

class TentenCRM:
    def __init__(self, api_endpoint=None, api_key=None):
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.status = Status()

    #
    # HTTP Request
    #

    def http_req_signature(self):
        pass

    def http_req(self, method, endpoint, payload=None):
        pass

    def http_post(self, endpoint, payload):
        pass

    def http_get(self, endpoint, params):
        pass

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
        self.api_endpoint = app.config.get("TENTEN_CRM_ENDPOINT")
        self.api_key = app.config.get("TENTEN_CRM_KEY")
        if not self.api_endpoint or not self.api_key:
            raise RuntimeError("Missing TENTEN_CRM_ENDPOINT or TENTEN_CRM_KEY in app config.")

        # Init
        super().__init__(self.api_endpoint, self.api_key)

        # Ext access
        app.extensions = getattr(app, "extensions", {})
        app.extensions["TentenCRM"] = self
