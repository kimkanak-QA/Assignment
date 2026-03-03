# Difficulty: Intermediate
# Scenario
# A food delivery application estimates how long an order will take to arrive based on the distance to the
# customer, the average travel speed, and current traffic conditions.
# Task
# Write a function called estimate_delivery that accepts distance_km (float), base_speed_kmh (float), and
# traffic_factor (float, default value 1.0 meaning no traffic). A traffic_factor of 2.0 means travel takes twice as
# long. Add a fixed 10-minute preparation time to the travel time. The function should return a dictionary with
# two keys: travel_minutes and total_minutes.
# Expected Output
# estimate_delivery(10.0, 40.0, 1.5)
# # Expected: {'travel_minutes': 22.5, 'total_minutes': 32.5}
# estimate_delivery(10.0, 40.0)
# # Expected: {'travel_minutes': 15.0, 'total_minutes': 25.0}



def estimate_deliver(distance_k:float, base_speed_km:float,traffic_factor:float ):
    travel_minutes =  (distance_k/base_speed_km ) * 60 * traffic_factor
    # travel_minutes = travel_minutes * traffic_factor
    total_minutes = travel_minutes + 10.00
    print("Expected:travel_minutes :", travel_minutes, "total_minute :", total_minutes )

estimate_deliver(10.00,40.00,1.0)
