# Daily Expenses Sharing Application

This is a backend service for a daily-expenses sharing application. The project allows users to manage expenses and split them using different methods (equal, exact, percentage). The application also manages user details, validates inputs, and generates downloadable balance sheets.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/daily-expenses-sharing.git
cd daily-expenses-sharing
```
### 2. install the requirments.txt file
```bash
pip install -r requirements.txt
```
### 3. run migrations
```bash
python manage.py migrate
```
### 4. run server
```bash
python manage.py runserver  
```
### 5. Access the API

You can access the API at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
### 5. Access the admin panel.

username : admin
password : admin

##  6 API Endpoints

### User Endpoints

- **Create user**: `api/create-user/`
- **Retrieve user details**: `api/user-detail/<int:pk>/`
- - **Register user**: `registration/`

### Expense Endpoints

- **Add expense**: `api/add-expenses/`
- **Retrieve individual user expenses**: `api/individual-expenses/<int:pk>`
- **Retrieve overall expenses**: `api/overall-expenses/`
- **Download balance sheet**: `api/balance-sheet/`
- **Download indvidual balance sheets**: `api/balance-sheet/<int:pk>/`

## How to Send Data for Add Expenses

To add an expense, send a `POST` request to the `/add-expenses/` endpoint with the following JSON data:
Here, `EX` stands for the Exact billing method. Adjust the billing_method and values based on the desired split method.
```json
{
    "name": "hangout",
    "total_bill": 3000,
    "billing_method": "EX",
    "owned_by": [
        {"username": "testuser1", "owes": "1000"},
        {"username": "testuser2", "owes": "1000"},
        {"username": "testuser3", "owes": "1000"}
    ]
}
```

## Tests

To run the test suite:

```bash
python manage.py test
```
## Performance Optimization

I have used `prefetch_related` and `select_related` methods to reduce the number of SQL queries and optimize database performance.

