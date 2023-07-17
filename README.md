# Physics Formulas in Python

<p align="center">
 
</p>




> A collection of physics formulas implemented in Python. 

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents

- [Introduction](#introduction)
- [Formulas Included](#formulas-included)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

  
![pexels-yan-krukau-8197526](https://github.com/AbrarAmiya/Formula_principles_of_physics/assets/115402065/859afc2a-fc60-4af1-b86c-a3163ac378ec)
## Introduction

This repository contains a collection of physics formulas implemented in Python. The aim of this project is to provide a comprehensive set of formulas that cover various topics in physics, from mechanics and electromagnetism to thermodynamics and wave phenomena. Each formula is implemented as a Python function, making it easy to use and integrate into your own projects.

## Formulas Included

The repository includes the following physics formulas:

- **Newton's Second Law**: Calculates the force exerted on an object based on its mass and acceleration. Formula: `force = mass * acceleration`
- **Ohm's Law**: Determines the electric current flowing through a conductor when a voltage is applied. Formula: `current = voltage / resistance`
- **Displacement**: Calculates the displacement of an object over time using initial velocity, time, and acceleration. Formula: `displacement = (initial_velocity * time) + (0.5 * acceleration * time**2)`
- **Coulomb's Law**: Computes the electrostatic force between two charged objects based on their charges and the distance between them. Formula: `force = (k * charge1 * charge2) / distance**2`
- **Mass-Energy Equivalence**: Calculates the energy equivalent of mass using Einstein's mass-energy equivalence formula. Formula: `energy = mass * c**2`
- **Torque**: Computes the torque (rotational force) exerted on an object given the force applied and the perpendicular distance from the axis of rotation. Formula: `torque = force * distance`
- **Doppler Shift**: Calculates the frequency shift of a wave due to the Doppler effect caused by the relative motion between the source of the wave and the observer. Formula: `shift = (velocity / speed_of_sound) * frequency`
- **Snell's Law**: Determines the angle of refraction based on Snell's law, which describes how light or other waves change direction when passing through different media. Formula: `angle2 = math.asin((n1 / n2) * math.sin(angle1))`
- **Work Done**: Calculates the work done by a force over a displacement at an angle, taking into account the component of the force in the direction of displacement. Formula: `work = force * displacement * math.cos(math.radians(angle))`
- **Escape Velocity**: Calculates the minimum velocity required for an object to escape the gravitational field of another object, such as the Earth. Formula: `velocity = math.sqrt(2 * G * mass / radius)`
- **Bernoulli's Equation**: Relates the density, velocity, and pressure of a fluid to its total energy per unit volume. Formula: `bernoulli = 0.5 * density * velocity**2 + pressure`
- **Kinetic Energy**: Calculates the energy of an object in motion based on its mass and velocity. Formula: `energy = 0.5 * mass * velocity**2`
- **Momentum**: Calculates the momentum of an object based on its mass and velocity. Formula: `momentum = mass * velocity`
- **Pascal's Law**: Relates the pressure exerted on a fluid to the force applied and the area over which the force is distributed. Formula: `pressure = force / area`
- **Magnetic Field**: Calculates the magnetic field strength at a given distance from a current-carrying wire. Formula: `field = (constant * current) / (2 * math.pi * distance)`
- **Kepler's Third Law**: Calculates the orbital period of a planet or satellite based on its semimajor axis. Formula: `period = 2 * math.pi * math.sqrt(semimajor_axis ** 3 / (G * M))`
- **Hooke's Law**: Describes the relationship between the force exerted on a spring and the displacement of the spring from its equilibrium position. Formula: `force = -spring_constant * displacement`
- **Buoyant Force**: Calculates the upward force exerted on an object submerged in a fluid. Formula: `force = density_fluid * volume_displaced * g`
- **Photon Energy**: Calculates the energy of a photon based on its frequency. Formula: `energy = h * frequency`
- **Magnetic Force**: Calculates the force experienced by a charged particle moving through a magnetic field. Formula: `force = charge * velocity * magnetic_field`
- **Conduction Heat Transfer**: Calculates the rate of heat transfer through a material. Formula: `rate = (thermal_conductivity * area * temperature_difference) / thickness`
- **Apparent Frequency**: Calculates the frequency observed by an observer due to the relative motion between the source and the observer. Formula: `apparent_freq = frequency * (speed_of_sound + velocity_observer) / (speed_of_sound + velocity_source)`
- **Capacitance**: Calculates the capacitance of a capacitor based on the charge stored and the voltage applied. Formula: `capacitance = charge / voltage`
- **Magnetic Flux**: Calculates the magnetic flux through a surface in the presence of a magnetic field. Formula: `flux = magnetic_field * area * math.cos(math.radians(angle))`
- **Electric Field**: Calculates the electric field strength at a given distance from a point charge. Formula: `field = k * charge / distance**2`
- **Simple Harmonic Motion Period**: Calculates the period of an object undergoing simple harmonic motion. Formula: `period = 2 * math.pi * math.sqrt(mass / spring_constant)`
- **Work-Energy Theorem**: Calculates the final energy of an object based on its initial energy and the work done on it. Formula: `final_energy = initial_energy + work`
- **Electric Field of a Point Charge**: Calculates the electric field strength at a given distance from a point charge. Formula: `field = k * charge / distance**2`
- **Impulse**: Calculates the impulse experienced by an object based on its mass and change in velocity. Formula: `impulse = mass * velocity_change`
- **Wave Speed**: Calculates the speed of a wave based on its wavelength and frequency. Formula: `speed = wavelength * frequency`
  
## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/physics-formulas-python.git
   ```
2. Navigate to the repository's directory:
   ```bash
   cd physics-formulas-python
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```

The script generates random values for the variables and calls each formula, printing the results to the console.

Feel free to modify the code and use these formulas in your own projects!

## Contributing

Contributions to this repository are welcome. If you have additional physics formulas or improvements to the existing code, please submit a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- The formulas implemented in this code are based on fundamental principles of physics.
- The random values are generated using the `random` module in Python's standard library.

Enjoy exploring the world of physics with Python!

---

**Note:** Replace `your-image-link.png` with a link to an image representing the
