"""Five basic physics formulas using SI units."""


def speed(distance_m, time_s):
    """Average speed: v = d / t (meters per second)."""
    if time_s == 0:
        raise ValueError("Time must not be zero.")
    return distance_m / time_s


def force(mass_kg, acceleration_m_s2):
    """Newton's second law: F = m * a (newtons)."""
    return mass_kg * acceleration_m_s2


def kinetic_energy(mass_kg, velocity_m_s):
    """Kinetic energy: KE = 1/2 * m * v^2 (joules)."""
    return 0.5 * mass_kg * velocity_m_s**2


def weight(mass_kg, gravity_m_s2=9.81):
    """Weight: W = m * g (newtons)."""
    return mass_kg * gravity_m_s2


def potential_energy(mass_kg, height_m, gravity_m_s2=9.81):
    """Gravitational potential energy: PE = m * g * h (joules)."""
    return mass_kg * gravity_m_s2 * height_m


if __name__ == "__main__":
    print("Physics formula examples (SI units)")
    print(f"Speed: {speed(100, 20):.2f} m/s")
    print(f"Force: {force(5, 3):.2f} N")
    print(f"Kinetic energy: {kinetic_energy(2, 4):.2f} J")
    print(f"Weight: {weight(10):.2f} N")
    print(f"Potential energy: {potential_energy(2, 3):.2f} J")