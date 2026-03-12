from ortools.linear_solver import pywraplp


def optimize_inventory(demand, price, cost):

    solver = pywraplp.Solver.CreateSolver("SCIP")

    if not solver:
        return demand, (price - cost) * demand

    # convert demand to integer (OR-Tools likes ints for bounds)
    demand = int(demand)

    # decision variables
    inventory = solver.IntVar(0, 2000, "inventory")
    sales = solver.IntVar(0, demand, "sales")

    # sales cannot exceed inventory
    solver.Add(sales <= inventory)

    # profit function
    profit = (price - cost) * sales

    solver.Maximize(profit)

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        return int(inventory.solution_value()), float(solver.Objective().Value())

    # fallback
    return demand, (price - cost) * demand