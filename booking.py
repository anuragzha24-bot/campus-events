def booking_total(email, quantity, ticket_price):
print("Customer:", email)
if quantity > 8:
quantity = 8
return quantity * ticket_price
