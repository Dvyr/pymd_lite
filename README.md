# pymd_lite
A Python package for Molecular Dynamics (MD) simulations tailored for learning and experimentation.

- **Core Objectives:**
  - Exemplify MD concepts (e.g., particle movement, energy calculations, thermostats) for beginners.
  - Provide a sandbox to test new MD models, ideas, or algorithms.
  - Keep it lightweight and modular, avoiding the complexity of full-fledged MD engines like GROMACS or LAMMPS.

- **MVP Features:**
  - Simulate a small system of particles (e.g., Lennard-Jones particles in 2D/3D).
  - Basic time integration (e.g., Velocity Verlet algorithm).
  - Simple energy calculations (kinetic, potential).
  - Basic visualization (e.g., trajectories or energy plots).
  - A framework to plug in custom MD models (e.g., new potentials or forces).
  - Avoid over-optimizing early on.

- **Non-Goals (for now):**
  - Competing with industrial-grade MD software.
  - Supporting massive parallelization or GPU acceleration.
  - Full-featured analysis tools (keep it minimal).
