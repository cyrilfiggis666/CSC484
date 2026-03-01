"""
PSEUDOCODE — Carbon Footprint Estimator

BEGIN PROGRAM

DEFINE emission factor constants:
    car emission factor (kg CO2 per mile)
    electricity emission factor (kg CO2 per kWh)
    flight emission factor (kg CO2 per flight)

WHILE user chooses to continue

    DISPLAY program title

    TRY
        PROMPT user for:
            weekly miles driven
            weekly electricity usage (kWh)
            number of flights

        CONVERT inputs to numeric values

        CALCULATE:
            car emissions
            electricity emissions
            flight emissions
            total emissions (sum of all categories)

        CALCULATE percentage contribution of each category
            IF total emissions equals zero
                SET percentages to zero
            ENDIF

        PROMPT user for personal weekly CO2 goal
        CALCULATE difference between total emissions and goal

        DISPLAY formatted emissions report:
            total emissions
            emissions per category
            percentage breakdown

        IF total emissions exceeds goal
            DISPLAY message indicating amount above goal
        ELSE
            DISPLAY message indicating amount below goal
        ENDIF

    CATCH invalid numeric input error
        DISPLAY user friendly error message

    FINALLY
        DISPLAY message indicating calculation cycle completed

    PROMPT user to run program again (y/n)
    IF user chooses not to continue
        DISPLAY exit message
        EXIT loop
    ENDIF

END WHILE

END PROGRAM
"""

"""
Carbon Footprint Estimator

Purpose / societal impact:
    Helps users estimate their weekly carbon footprint from common activities
    (driving, household electricity, and flights) and encourages awareness of
    emissions drivers so they can make informed choices.

    - Uses try / except / finally for safe input handling and cleanup messaging
    - Displays statistics (totals, category breakdowns, and comparisons)
    - Meaningful, real world utility
"""

# kg CO2 per mile (average gasoline vehicle)
car_emission_factor = 0.404 

# kg CO2 per kWh (US average)
electricity_emission_factor = 0.385

# kg CO2 per domestic flight (approximation)
flight_emission_factor = 90

while True:
    print("\n --- Carbon Footprint Estimator ---")
    try:
        miles = float(input("Weekly miles driven (ex., 120.5): ").strip())
        kwh = float(input("Weekly household electricity use in kWh (ex., 85): ").strip())
        flights = int(input("Number of domestic flights this week: ").strip())

        car_emissions = miles * car_emission_factor
        electricity_emissions = kwh * electricity_emission_factor
        flight_emissions = flights * flight_emission_factor
        total_emissions = car_emissions + electricity_emissions + flight_emissions

        # Calculate percentages per category
        car_pct = (car_emissions / total_emissions) * 100 if total_emissions else 0.0
        electricity_pct = (electricity_emissions / total_emissions) * 100 if total_emissions else 0.0
        flight_pct = (flight_emissions / total_emissions) * 100 if total_emissions else 0.0

        # User configurable weekly personal goal in kg CO2/week; varies depending on user
        weekly_goal = float(input("\nEnter your personal weekly CO2 goal (kg): ").strip())
        delta_from_goal = total_emissions - weekly_goal

        # Display those calculations in a meaningful way
        print("\n--- Weekly Carbon Emissions Report ---")
        print(f"Total Emissions: {total_emissions:.2f} kg CO2")
        print(f"Driving: {car_emissions:.2f} kg CO2 ({car_pct:.1f}%)")
        print(f"Electricity: {electricity_emissions:.2f} kg CO2 ({electricity_pct:.1f}%)")
        print(f"Flights: {flight_emissions:.2f} kg CO2 ({flight_pct:.1f}%)")

        if delta_from_goal > 0:
            print(f"You are {delta_from_goal:.2f} kg ABOVE your goal. You can do better next week!")
        else:
            print(f"You are {abs(delta_from_goal):.2f} kg BELOW your goal. Great job and keep it up! ")
    
    except ValueError:
        print("Invalid input detected. Please enter numeric values only.")

    finally:
        print("Calculation cycle complete.")

    rerun = input("\nWould you like to run another calculation? (y/n): ").strip().lower()
    if rerun != "y":
        print("Exiting Carbon Footprint Estimator. Protect the Earth!")
        break