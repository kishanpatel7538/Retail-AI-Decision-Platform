# Promotion lift values learned from analysis
PROMOTION_LIFT = {
    "BEVERAGES": 0.40,
    "DAIRY": 0.25,
    "BREAD/BAKERY": 0.20,
    "MEATS": 0.18,
    "PRODUCE": 0.22
}

def simulate_promotion(base_demand, family, promotion):

    # If no promotion
    if promotion == 0:
        return base_demand

    # Get lift for the product family
    lift = PROMOTION_LIFT.get(family, 0.15)

    adjusted_demand = base_demand * (1 + lift)

    return adjusted_demand