# Smartlabs Developer Screening Test

Welcome to Smartlabs! This is a screening test, so we can get an idea of your knowledge of our stack - Python, Django and Django Rest Framework.
Please submit the answers in a public GitHub repository and email us the URL of the repository (Preferred) or send us the files via email at <rohan@thesmartlabs.com>>.

- Code clarity, efficiency and style are important factors.
- Following coding conventions and best practices are encouraged.
- Adding comment and doc strings on your code is a plus.

If you have any doubts or questions about the tasks feel free to email us at <rohan@thesmartlabs.com>

**We Recommend 24 hours to complete this test.**

Best of Luck!


## Task 1:

Create a View which will use https://free.currencyconverterapi.com/ API, to build a currency converter.

API documentation: https://www.currencyconverterapi.com/docs (You need to create a free account there)

**Input:**

The user will select the Base Currency, Currency to convert to from a dropdown and enter the amount of money to the form. for example: 

```python
input = {
    "base": "USD",
    "convert_to": "INR",
    "amount": "100"
}
```

**Output:**

Conversion Rate and converted amount.

**Judging Criteria:**

We will look at how you couple / decouple the view and the API code,
how the code is structured and how the exceptions are handled.
Adding some UI elements in the template is a plus.


## Task 2:

Given this model:

```python
class Order(models.Model):
    user = models.ForeignKey(
        'User',
        realted_name='orders',
        on_delete=models.CASCADE
    )
    discount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )


class Item(models.Model):
    name = models.Chafield(max_length=100)
    order = models.ForeignKey(
        'Order',
        realted_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )
```

**A. Develop a REST API (Django Rest Framework) which will list the orders by a specific user.**
 

The API response should look like:

```json
{
  "user": {
    "username": "new user",
    "email": "user@gmail.com"
  },
  "items": [
    {
      "name": "product 1",
      "price": "100.00",
      "quantity": 2,
      "total": "200.00"
    },
    {
      "name": "product 2",
      "price": "100.00",
      "quantity": 2,
      "total": "200.00"
    }
  ],
  "sub_total": "400.00",
  "total": "380.00",
  "discount": "20"
}
```

**B. Write the required database queries to get these analytics data:**
    
- Get total number of orders per users.
  
  `[{'user_id: 1, 'count': 100}, {'user_id: 2, 'count': 100}, ...]`
- Total orders per month. (for last 12 month's)
  
  `[{'month: 'January', 'count': 100}, {'month: 'February', 'count': 100}, ...]`
- Total revenue from orders per month. (for last 12 month's)
  
  `[{'month: 'January', 'revenue': 100.00}, {'month: 'February', 'revenue': 100.00}, ...]`


**Judging Criteria:**

We will look at the way you optimize the database queries required for the API and the analytics,
and how you structure the serializer for the API.
The fewer queries required to get the results the better.
