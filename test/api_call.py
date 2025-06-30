from tentencrm import TentenCRM, __VERSION__

print(" * API Version:", __VERSION__)

# Init
tenten_crm = TentenCRM(
    base_url = "http://localhost:8081/api/v1/",
    api_key = "xxx",
    timeout = 10
)

