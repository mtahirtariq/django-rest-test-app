REST API TEST APP

Python Requirement: 3.6+

To run the application:

    1. pip install -r requirements/python/base.txt
    2. ./manage.py migrate
    3. ./manage.py runserver

Admin is accessible at

    /admin

**API Endpoints:**

**Create Customer:**

Create customer endpoint has been renamed from `create_customer` to `customers` to consolidate create and search logic.
It was a different endpoint in the previous commit.


    POST /api/v1/customers/

Sample Input:
```json
{
  "first_name": "Alfred",
  "last_name": "James",
  "dob": "25-06-1995"
}
```

Sample Output:

```json
{
    "id": 8,
    "first_name": "Alfred",
    "last_name": "James",
    "dob": "25-06-1995"
}
```

    Status Codes: 201, 400

**Search Customer**

    GET /api/v1/customers/?name=alfred&dob=1995-06-25&policy_type=personal-life

Sample Output:

```json
[
    {
        "id": 8,
        "first_name": "Alfred",
        "last_name": "James",
        "dob": "25-06-1995"
    }
]
```

    Status Codes: 200

**Create Quote:**

    POST /api/v1/quotes/

Sample Input:

```json
{
    "customer": 8,
    "type": "personal-life",
    "premium": "300",
    "cover": 300000
}
```

Sample Output:
```json
{
    "id": 4,
    "state": "new",
    "type": "personal-life",
    "premium": 300,
    "cover": 300000,
    "customer": 8
}
```

    Status Codes: 201, 400

**Accept Quote:**

    POST /api/v1/quotes/4/accept/

Sample Output:
```json
{
    "id": 4,
    "state": "accepted",
    "type": "personal-life",
    "premium": 300,
    "cover": 300000,
    "customer": 8
}
```

    Status Codes: 200

**Activate Quote (Convert to Policy):**

    POST /api/v1/quotes/4/payment-complete/

Sample Output:
```json
{
    "id": 4,
    "state": "active",
    "type": "personal-life",
    "premium": 300,
    "cover": 300000,
    "customer": 8
}
```

    Status Codes: 200

**Get Policy**

    GET /api/v1/policies/[policy_id]/

Sample Output:

```json
{
    "id": 1,
    "type": "personal-accident",
    "premium": 200,
    "cover": 200000,
    "state": "active",
    "start_date": null,
    "end_date": null,
    "customer": 1
}
```

    Status Codes: 200

**Search Policies**

    GET /api/v1/policies/?customer=[customer_id]

Sample Output:

```json
[
    {
        "id": 4,
        "type": "personal-life",
        "premium": 300,
        "cover": 300000,
        "state": "active",
        "start_date": null,
        "end_date": null,
        "customer": 8
    }
]
```

    Status Codes: 200
