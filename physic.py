# PHYSICS FORMULA CALCULATOR

# Function to calculate speed
def speed(distance_m, time_s):
    return distance_m / time_s


# Function to calculate force
def force(mass_kg, acceleration_m_s2):
    return mass_kg * acceleration_m_s2


# Function to calculate kinetic energy
def kinetic_energy(mass_kg, velocity_m_s):
    return 0.5 * mass_kg * velocity_m_s ** 2


# Function to calculate weight
def weight(mass_kg, gravity_m_s2=9.81):
    return mass_kg * gravity_m_s2


# Function to calculate potential energy
def potential_energy(mass_kg, height_m, gravity_m_s2=9.81):
    return mass_kg * gravity_m_s2 * height_m


# Main program
while True:

    print("\n===== PHYSICS FORMULA CALCULATOR =====")
    print("1. Speed")
    print("2. Force")
    print("3. Kinetic Energy")
    print("4. Weight")
    print("5. Potential Energy")

    choice = input("\nSelect a calculation (1-5): ")

    try:

        if choice == "1":
            distance = float(input("Enter distance (m): "))
            time = float(input("Enter time (s): "))

            if time <= 0:
                print("Time must be greater than zero.")
            else:
                result = speed(distance, time)
                print(f"Speed = {result:.2f} m/s")

        elif choice == "2":
            mass = float(input("Enter mass (kg): "))
            acceleration = float(input("Enter acceleration (m/s²): "))

            result = force(mass, acceleration)
            print(f"Force = {result:.2f} N")

        elif choice == "3":
            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))

            result = kinetic_energy(mass, velocity)
            print(f"Kinetic Energy = {result:.2f} J")

        elif choice == "4":
            mass = float(input("Enter mass (kg): "))

            result = weight(mass)
            print(f"Weight = {result:.2f} N")

        elif choice == "5":
            mass = float(input("Enter mass (kg): "))
            height = float(input("Enter height (m): "))

            result = potential_energy(mass, height)
            print(f"Potential Energy = {result:.2f} J")

        else:
            print("Invalid choice. Please select between 1 and 5.")
            continue

    except ValueError:
        print("Invalid input. Please enter numerical values.")
        continue

    # Ask the user whether to continue
    again = input("\nWould you like to perform another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using the Physics Formula Calculator!")
        break