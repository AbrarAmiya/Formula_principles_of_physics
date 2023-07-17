import math
import random

import math

def newton_second_law(mass, acceleration):
    force = mass * acceleration
    return force

# Calculates the force exerted on an object based on its mass and acceleration, according to Newton's second law of motion.

def ohms_law(voltage, resistance):
    current = voltage / resistance
    return current

# Determines the electric current flowing through a conductor when a voltage is applied, following Ohm's law which relates voltage, current, and resistance.

def displacement(initial_velocity, time, acceleration):
    displacement = (initial_velocity * time) + (0.5 * acceleration * time**2)
    return displacement

# Calculates the displacement of an object over time using the initial velocity, time, and acceleration, based on the kinematic equation.

def coulombs_law(charge1, charge2, distance):
    k = 8.99e9  # Coulomb's constant
    force = k * charge1 * charge2 / distance**2
    return force

# Computes the electrostatic force between two charged objects based on their charges and the distance between them, according to Coulomb's law.

def mass_energy_equivalence(mass):
    c = 2.998e8  # Speed of light in m/s
    energy = mass * c**2
    return energy

# Calculates the energy equivalent of mass using Einstein's mass-energy equivalence formula, where c is the speed of light.

def torque(force, distance):
    torque = force * distance
    return torque

# Computes the torque (rotational force) exerted on an object given the force applied and the perpendicular distance from the axis of rotation.

def doppler_shift(frequency, velocity, speed_of_sound):
    shift = (velocity / speed_of_sound) * frequency
    return shift

# Calculates the frequency shift of a wave due to the Doppler effect, caused by the relative motion between the source of the wave and the observer.

def snells_law(n1, n2, angle1):
    angle2 = math.asin((n1 / n2) * math.sin(angle1))
    return angle2

# Determines the angle of refraction based on Snell's law, which describes how light or other waves change direction when passing through different mediums.

def work_done(force, displacement, angle):
    work = force * displacement * math.cos(math.radians(angle))
    return work

# Calculates the work done by a force over a displacement at an angle, taking into account the component of the force in the direction of displacement.

def escape_velocity(mass, radius):
    G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
    velocity = math.sqrt(2 * G * mass / radius)
    return velocity

# Calculates the minimum velocity required for an object to escape the gravitational field of another object, such as the Earth.


def bernoullis_equation(density, velocity, pressure):
    constant = 0.5 * density * velocity**2
    bernoulli = constant + pressure
    return bernoulli

def kinetic_energy(mass, velocity):
    energy = 0.5 * mass * velocity**2
    return energy

def momentum(mass, velocity):
    momentum = mass * velocity
    return momentum

def pascals_law(force, area):
    pressure = force / area
    return pressure

def magnetic_field(current, distance):
    constant = 2.0e-7  # Magnetic constant in T*m/A
    field = (constant * current) / (2 * math.pi * distance)
    return field


def keplers_third_law(semimajor_axis):
    G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
    M = 5.972e24  # Mass of the Earth in kg

    period = 2 * math.pi * math.sqrt(semimajor_axis ** 3 / (G * M))
    return period

def hookes_law(spring_constant, displacement):
    force = -spring_constant * displacement
    return force

def buoyant_force(density_fluid, volume_displaced, g):
    force = density_fluid * volume_displaced * g
    return force

def photon_energy(frequency):
    h = 6.626e-34  # Planck's constant in J*s
    energy = h * frequency
    return energy

def magnetic_force(charge, velocity, magnetic_field):
    force = charge * velocity * magnetic_field
    return force

def conduction_heat_transfer(thermal_conductivity, area, temperature_difference, thickness):
    rate = (thermal_conductivity * area * temperature_difference) / thickness
    return rate

def apparent_frequency(frequency, velocity_source, velocity_observer, speed_of_sound):
    apparent_freq = frequency * (speed_of_sound + velocity_observer) / (speed_of_sound + velocity_source)
    return apparent_freq

def capacitance(charge, voltage):
    capacitance = charge / voltage
    return capacitance

def magnetic_flux(magnetic_field, area, angle):
    flux = magnetic_field * area * math.cos(math.radians(angle))
    return flux

def electric_field(charge, distance):
    k = 8.99e9  # Coulomb's constant
    field = k * charge / distance**2
    return field

def simple_harmonic_motion_period(mass, spring_constant):
    period = 2 * math.pi * math.sqrt(mass / spring_constant)
    return period

def work_energy_theorem(initial_energy, work):
    final_energy = initial_energy + work
    return final_energy

def electric_field_point_charge(charge, distance):
    k = 8.99e9  # Coulomb's constant
    field = k * charge / distance**2
    return field

def impulse(mass, velocity_change):
    impulse = mass * velocity_change
    return impulse

def wave_speed(wavelength, frequency):
    speed = wavelength * frequency
    return speed



# Generate random values for the variables
mass = random.uniform(1, 10)
acceleration = random.uniform(1, 10)
voltage = random.uniform(1, 10)
resistance = random.uniform(1, 10)
initial_velocity = random.uniform(1, 10)
time = random.uniform(1, 10)
charge1 = random.uniform(1, 10)
charge2 = random.uniform(1, 10)
distance = random.uniform(1, 10)
energy_mass = random.uniform(1, 10)
force_torque = random.uniform(1, 10)
velocity_doppler = random.uniform(1, 10)
speed_of_sound = random.uniform(1, 10)
n1 = random.uniform(1, 10)
n2 = random.uniform(1, 10)
angle1 = random.uniform(1, 90)
force_work = random.uniform(1, 10)
displacement_work = random.uniform(1, 10)
angle_work = random.uniform(1, 90)
mass_escape = random.uniform(1, 10)
radius_escape = random.uniform(1, 10)
density_bernoulli = random.uniform(1, 10)
velocity_bernoulli = random.uniform(1, 10)
pressure_bernoulli = random.uniform(1, 10)
mass_kinetic = random.uniform(1, 10)
velocity_kinetic = random.uniform(1, 10)
mass_momentum = random.uniform(1, 10)
velocity_momentum = random.uniform(1, 10)
force_pascal = random.uniform(1, 10)
area_pascal = random.uniform(1, 10)
current_magnetic = random.uniform(1, 10)
distance_magnetic = random.uniform(1, 10)
semimajor_axis_kepler = random.uniform(1, 10)
spring_constant_hooke = random.uniform(1, 10)
displacement_hooke = random.uniform(1, 10)
density_fluid_buoyant = random.uniform(1, 10)
volume_displaced_buoyant = random.uniform(1, 10)
g_buoyant = 9.8  # Acceleration due to gravity
frequency_photon = random.uniform(1e9, 1e15)  # Random frequency in the range of 1 GHz to 1 THz
charge_magnetic = random.uniform(1, 10)
velocity_magnetic = random.uniform(1, 10)
magnetic_field_magnetic = random.uniform(1, 10)
thermal_conductivity_conduction = random.uniform(1, 10)
area_conduction = random.uniform(1, 10)
temperature_difference_conduction = random.uniform(1, 10)
thickness_conduction = random.uniform(1, 10)
frequency_apparent = random.uniform(1, 10)
velocity_source_apparent = random.uniform(1, 10)
velocity_observer_apparent = random.uniform(1, 10)
speed_of_sound_apparent = random.uniform(1, 10)
charge_capacitance = random.uniform(1, 10)
voltage_capacitance = random.uniform(1, 10)
magnetic_field_flux = random.uniform(1, 10)
area_flux = random.uniform(1, 10)
angle_flux = random.uniform(1, 90)
charge_field = random.uniform(1, 10)
distance_field = random.uniform(1, 10)
mass_shm = random.uniform(1, 10)
spring_constant_shm = random.uniform(1, 10)
initial_energy_work = random.uniform(1, 10)
work_work = random.uniform(1, 10)
charge_point_charge = random.uniform(1, 10)
distance_point_charge = random.uniform(1, 10)
mass_impulse = random.uniform(1, 10)
velocity_change_impulse = random.uniform(1, 10)
wavelength_wave_speed = random.uniform(1, 10)
frequency_wave_speed = random.uniform(1, 10)

# Call the functions with random values
print("Newton's Second Law: ", newton_second_law(mass, acceleration))
print("Ohm's Law: ", ohms_law(voltage, resistance))
print("Displacement: ", displacement(initial_velocity, time, acceleration))
print("Coulomb's Law: ", coulombs_law(charge1, charge2, distance))
print("Mass-Energy Equivalence: ", mass_energy_equivalence(energy_mass))
print("Torque: ", torque(force_torque, distance))
print("Doppler Shift: ", doppler_shift(velocity_doppler, speed_of_sound))
print("Snell's Law: ", snells_law(n1, n2, angle1))
print("Work Done: ", work_done(force_work, displacement_work, angle_work))
print("Escape Velocity: ", escape_velocity(mass_escape, radius_escape))
print("Bernoulli's Equation: ", bernoullis_equation(density_bernoulli, velocity_bernoulli, pressure_bernoulli))
print("Kinetic Energy: ", kinetic_energy(mass_kinetic, velocity_kinetic))
print("Momentum: ", momentum(mass_momentum, velocity_momentum))
print("Pascal's Law: ", pascals_law(force_pascal, area_pascal))
print("Magnetic Field: ", magnetic_field(current_magnetic, distance_magnetic))
print("Kepler's Third Law: ", keplers_third_law(semimajor_axis_kepler))
print("Hooke's Law: ", hookes_law(spring_constant_hooke, displacement_hooke))
print("Buoyant Force: ", buoyant_force(density_fluid_buoyant, volume_displaced_buoyant, g_buoyant))
print("Photon Energy: ", photon_energy(frequency_photon))
print("Magnetic Force: ", magnetic_force(charge_magnetic, velocity_magnetic, magnetic_field_magnetic))
print("Conduction Heat Transfer: ", conduction_heat_transfer(thermal_conductivity_conduction, area_conduction,
                                                              temperature_difference_conduction, thickness_conduction))
print("Apparent Frequency: ", apparent_frequency(frequency_apparent, velocity_source_apparent,
                                                  velocity_observer_apparent, speed_of_sound_apparent))
print("Capacitance: ", capacitance(charge_capacitance, voltage_capacitance))
print("Magnetic Flux: ", magnetic_flux(magnetic_field_flux, area_flux, angle_flux))
print("Electric Field: ", electric_field(charge_field, distance_field))
print("Simple Harmonic Motion Period: ", simple_harmonic_motion_period(mass_shm, spring_constant_shm))
print("Work-Energy Theorem: ", work_energy_theorem(initial_energy_work, work_work))
print("Electric Field Point Charge: ", electric_field_point_charge(charge_point_charge, distance_point_charge))
print("Impulse: ", impulse(mass_impulse, velocity_change_impulse))
print("Wave Speed: ", wave_speed(wavelength_wave_speed, frequency_wave_speed))
