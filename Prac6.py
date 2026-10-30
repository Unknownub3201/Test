import pandas as pd  # Used to build the example DataFrames

# "Golden" data: the trusted master record of customer details
goldenData = pd.DataFrame(
    {
        "customer_id": [101, 102, 103],
        "customer_name": ["Meghna", "Muskan", "Gatik"],
        "customer_email": ["meghnab@email.com", "muskann@email.com", "gatik@email.com"],
    }
)
print("-" * 20, "Golden Data", "-" * 20)
print(goldenData)

# Nominal data: categorical labels (segment/region) describing each customer
nominalData = pd.DataFrame(
    {
        "customer_id": [101, 102, 103],
        "customer_segment": ["Premium", "Standard", "Standard"],
        "customer_region": ["South", "North", "West"],
    }
)
print("-" * 20, "Nominal Data", "-" * 20)
print(nominalData)

# Processed data: transactional records (orders); customer 101 has two orders.
# customer_id links these rows back to the golden/nominal data
processedData = pd.DataFrame(
    {
        "customer_id": [101, 102, 103, 101],
        "order_id": [1001, 1002, 1003, 1004],
        "order_amount": [300, 250, 200, 150],
        # Convert date strings into proper datetime values
        "order_date": pd.to_datetime(
            ["2025-08-01", "2025-08-02", "2025-08-03", "2025-08-04"]
        ),
    }
)
print("-" * 20, "Processed Data", "-" * 20)
print(processedData)

# People data: details about employees (a different entity from customers)
peopleData = pd.DataFrame(
    {
        "employee_id": [1, 2, 3],
        "employee_name": ["Joe", "Kane", "Steve"],
        "employee_role": ["Sales", "Support", "Manager"],
    }
)
print("-" * 20, "People data", "-" * 20)
print(peopleData)
