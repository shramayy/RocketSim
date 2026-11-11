from Rockets import falcon
from simulations import run_simulation

# Running simulation

results = run_simulation(falcon, wind_v=15)

# Displaying the results

wind_speeds = [-30, -15, 0, 15, 30]
for wind in wind_speeds:
    results = run_simulation(falcon, wind_v=wind)

    print(f"\nWind speed: {wind} m/s")
    print(f"Maximum altitude: {results['max_altitude']:.2f} m")
    print(f"Maximum range: {results['max_range']:.2f} m")
    print(f"Flight time: {results['flight_time']:.2f} s")
    print(f"Status: {results['status']}")
