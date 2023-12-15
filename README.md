**Python API Automation Framework**

**Hybrid Custom Framework to Test the REST APIs**

<img src="C:\Users\Milind Trivedi\OneDrive\Pictures\Screenshots\img_framework_flow.png"/>

**Tech Stack**
1. Python 3.11
3. Requests - HTTP Requests
5. PyTest - Testing Framework
7. Reporting - Allure Report, PyTest HTML
9. Test Data - CSV, Excel, JSON
11. Parallel Execution - x distribute

**How to Install Packages** - 
`pip install requests pytest pytest-html faker allure-pytest jsonschema`

**To Freeze your Package version** -
`pip freeze > requirements.txt`

**To Install te Freeze Version** -
`pip install -r requirements.txt`

**How to run your Testcase Parallel** -
`pip install pytest-xdist`

**`pytest -n auto tests/integration_test/test_create_booking.py -s -v** `

**To Work with the Excel** - 
`pip install openpyxl`