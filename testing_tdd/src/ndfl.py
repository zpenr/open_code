def calculate_ndfl_tax(income):
    tiers = [
        (0.0, 0.0, 0.13),
        (2_400_000.0, 312_000.0, 0.15),
        (5_000_000.0, 702_000.0, 0.18),
        (20_000_000.0, 3_402_000.0, 0.20)
    ]
    for start, addition, rate in tiers[::-1]:
        if income > start:
            return addition + (income-start) * rate
    return 