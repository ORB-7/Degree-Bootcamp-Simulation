# Degree-Bootcamp-Simulation
A stochastic Monte Carlo simulation comparing a fixed-duration bootcamp pathway with a probabilistic multi-semester university degree pathway under uncertainty.
This project models how institutional disruptions (e.g., strikes) affect expected completion time and variability in academic programs.

# Project Overview
This application simulates two educational pathways:

Bootcamp Pathway

Fixed duration (26 weeks)

Deterministic (no variability)

University Degree Pathway

Multi-semester structure

Teaching, exams, breaks

Strike delays modeled using a Poisson distribution

Stochastic completion time

Monte Carlo simulation to estimate expected duration

The model allows users to adjust parameters such as:

Total academic units

Units per semester

Strike probability

Number of Monte Carlo runs

Random seed

# Research Hypothesis
# Research Question

Does uncertainty in semester disruptions significantly increase the expected completion time of a degree program compared to a fixed-duration bootcamp?

Null Hypothesis (H₀)

Strike-related disruptions do not significantly affect the expected completion time of a degree pathway.

Alternative Hypothesis (H₁)

Strike-related disruptions significantly increase the expected completion time of a degree pathway.

# Methodology

The model uses:

Monte Carlo simulation to generate multiple completion-time outcomes

Poisson distribution to simulate strike delays

Sensitivity analysis to evaluate the effect of increasing strike probability

Histogram visualization to analyze distribution shape

Degree duration is computed by summing:

Orientation weeks

Teaching weeks

Strike delays (Poisson-distributed)

CAT and exam periods

Semester breaks

Industrial attachment

Capstone project

Graduation delay

Bootcamp duration is fixed and used as a baseline comparator.

# Outputs
The application generates:

Bootcamp duration (months)

Average degree completion time

Minimum and maximum simulated duration

Distribution histogram of degree duration

Strike probability sensitivity curve

Downloadable CSV of simulation results

# Expected Findings
Bootcamp completion time remains constant (zero variance).

Degree completion time exhibits variability due to stochastic disruptions.

Increasing strike probability increases expected completion time.

Distribution of degree completion time is right-skewed.

Risk accumulates as disruption probability increases.

# Academic Relevance
This project demonstrates:

Stochastic modeling

Risk quantification

Monte Carlo simulation

Sensitivity analysis

Probabilistic timeline forecasting

It can be used as a teaching tool for:

Operations research

Decision science

Simulation modeling

Educational policy analysis

# Model Assumptions
Each semester contains 12 teaching weeks.

Strike delays follow a Poisson distribution.

Semester breaks are fixed.

Final year includes attachment and capstone.

Bootcamp duration is deterministic.

