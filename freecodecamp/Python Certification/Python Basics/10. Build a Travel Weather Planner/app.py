# =========================================================
# LAB: BUILD A TRAVEL WEATHER PLANNER
# =========================================================
#
# OBJECTIVE
# ---------------------------------------------------------
# Use conditional statements to determine whether
# commuting is possible based on:
#
# - Distance to travel
# - Weather conditions
# - Available transportation
#
# =========================================================
# REQUIRED VARIABLES
# =========================================================
#
# distance_km
#     Number representing the distance to travel.
#
# is_raining
#     True if it is raining.
#     False otherwise.

# has_bike
#     True if a bike is available.
#
# has_car
#     True if a car is available.
#
# has_ride_share_app
#     True if a ride-share application is available.
#
# =========================================================
# COMMUTING RULES
# =========================================================
# 1. If distance_km is a falsy value:
#
#       print(False)
# ---------------------------------------------------------
# 2. If distance_km <= 1:
#
#       True  -> Not raining
#       False -> Raining
# ---------------------------------------------------------
# 3. If 1 < distance_km <= 6:
#
#       True  -> Has bike AND not raining
#       False -> Otherwise
# ---------------------------------------------------------
# 4. If distance_km > 6:
#
#       True  -> Has car OR ride-share app
#       False -> Otherwise
# =========================================================
# SOLUTION
# =========================================================

distance_km = 1
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = False

if not distance_km:
    print(False)

elif distance_km <= 1:
    if is_raining:
        print(False)
    else:
        print(True)

elif 1 < distance_km <= 6:
    if not is_raining and has_bike:
        print(True)
    else:
        print(False)

elif distance_km > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)

else:
    print(False)

# =========================================================
# TEST CASES
# =========================================================
#
# distance_km = 0
# Output: False
#
# distance_km = 1
# is_raining = False
# Output: True
#
# distance_km = 1
# is_raining = True
# Output: False
#
# distance_km = 5
# has_bike = True
# is_raining = False
# Output: True
#
# distance_km = 5
# has_bike = False
# Output: False
#
# distance_km = 10
# has_car = True
# Output: True
#
# distance_km = 10
# has_car = False
# has_ride_share_app = True
# Output: True
#
# distance_km = 10
# has_car = False
# has_ride_share_app = False
# Output: False
#
# =========================================================