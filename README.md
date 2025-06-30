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
    TENTEN_CRM_BASE_URL = "http://localhost:8081/",
    TENTEN_CRM_API_KEY = "your-api-key",
    TENTEN_CRM_TIMEOUT = 10,
)

# Init TentenCRM API
tentencrm = FlaskTentenCRM(app)
```

Use directly:

```python
from tentencrm import TentenCRM
tenten_crm = TentenCRM(
    base_url = "http://localhost:8081/",
    api_key = "your-api-key",
    timeout = 10
)
```