def ground_shipping(weight):
  cost = 20.00
  if weight <= 2:
    return cost + (weight * 1.50)
  elif weight > 2 and weight <= 6:
    return cost + (weight * 3.00)
  elif weight > 6 and weight <= 10:
    return cost + (weight * 4.00)
  else:
    return cost + (weight * 4.75)

premium_shipping = 125.00

def drone_shipping(weight):
  cost = 0.00
  if weight <= 2:
    return cost + (weight * 4.50)
  elif weight > 2 and weight <= 6:
    return cost + (weight * 9.00)
  elif weight > 6 and weight <= 10:
    return cost + (weight * 12.00)
  else:
    return cost + (weight * 14.25)


def print_cheapest_shipping_method(weight):

  ground = ground_shipping(weight)
  premium = premium_shipping
  drone = drone_shipping(weight)

  if ground < drone and ground < premium:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium"
    cost = premium
  else:
    method = "drone"
    cost = drone

# This line allows you to send return the result out of the function where it could be3 used for somethihng else in the code
  return "The cheapest option available is " + str(cost) + " with " + str(method) + " shipping"

# These lines allow you to print the code straight from the function (you will have to remove 'print()' from the function calls at the bottom though)
'''
  print(
    "The cheapest option available is $%.2f with %s shipping"
    % (cost, method)
  )
  '''
 
print(print_cheapest_shipping_method(4.8))
print(print_cheapest_shipping_method(41.5))
