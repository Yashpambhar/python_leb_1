def calculate_simple_interest(principal, time, rate):
    simple_interest = (principal * time * rate) / 100
    return simple_interest

principal = 1000
time = 2
rate = 5

result = calculate_simple_interest(principal, time, rate)
print("Simple Interest:", result)
