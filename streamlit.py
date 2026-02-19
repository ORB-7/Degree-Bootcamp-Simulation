import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# =====================================================
# 1. PAGE CONFIG
# =====================================================
st.set_page_config(page_title="Educational Pathway Duration Simulator", layout="wide")

st.title("🎓 Educational Pathway Duration Simulator")
st.markdown(
    "A stochastic comparison of fixed-duration bootcamp training "
    "versus a simulated multi-semester degree pathway."
)

# =====================================================
# 2. SIDEBAR PARAMETERS
# =====================================================
st.sidebar.header("Simulation Parameters")

total_units = st.sidebar.slider("Total Units Required", 25, 40, 26)
units_per_sem = st.sidebar.slider("Units per Semester", 3, 6, 4)
strike_prob = st.sidebar.slider("Strike Probability per Semester", 0.0, 0.5, 0.2)
n_simulations = st.sidebar.slider("Monte Carlo Runs", 10, 500, 100)
seed = st.sidebar.number_input("Random Seed", 0, 10000, 42)

np.random.seed(seed)

semesters = int(np.ceil(total_units / units_per_sem))
start_date = datetime(2026, 2, 6)

# =====================================================
# 3. SIMULATION ENGINE
# =====================================================

def simulate_degree(start, semesters, units_per_sem, strike_prob, total_units):
    tasks = []
    current = start
    units_left = total_units

    for sem in range(1, semesters + 1):

        sem_units = min(units_per_sem, units_left)
        units_left -= sem_units

        orientation_end = current + timedelta(weeks=1)

        strike_weeks = np.random.poisson(2) if np.random.random() < strike_prob else 0
        teaching_end = orientation_end + timedelta(weeks=12 + strike_weeks)
        cats_end = teaching_end + timedelta(weeks=2)
        exams_end = cats_end + timedelta(weeks=2)

        current = exams_end + timedelta(weeks=2)

        if sem == semesters - 1:
            current += timedelta(weeks=12)

        if sem == semesters:
            current += timedelta(weeks=4)
            current += timedelta(weeks=24)

    duration_months = (current - start).days / 30
    return duration_months


def monte_carlo(n_runs):
    results = []
    for _ in range(n_runs):
        duration = simulate_degree(
            start_date,
            semesters,
            units_per_sem,
            strike_prob,
            total_units
        )
        results.append(duration)
    return results


# =====================================================
# 4. RUN MONTE CARLO
# =====================================================

bootcamp_months = 26 / 4.345
degree_results = monte_carlo(n_simulations)

degree_mean = np.mean(degree_results)
degree_min = np.min(degree_results)
degree_max = np.max(degree_results)

# =====================================================
# 5. METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Bootcamp Duration", f"{bootcamp_months:.1f} months")
col2.metric("Avg Degree Duration", f"{degree_mean:.1f} months")
col3.metric("Shortest Simulated Degree", f"{degree_min:.1f} months")
col4.metric("Longest Simulated Degree", f"{degree_max:.1f} months")

# =====================================================
# 6. DISTRIBUTION HISTOGRAM
# =====================================================

st.markdown("## Distribution of Degree Completion Time")

hist_fig = px.histogram(
    degree_results,
    nbins=20,
    labels={"value": "Completion Time (Months)"},
    title="Monte Carlo Distribution of Degree Duration"
)

hist_fig.add_vline(x=bootcamp_months, line_dash="dash", line_color="red")

st.plotly_chart(hist_fig, use_container_width=True)

# =====================================================
# 7. STRIKE SENSITIVITY ANALYSIS
# =====================================================

st.markdown("## Strike Sensitivity Analysis")

strike_range = np.linspace(0, 0.5, 10)
sensitivity_results = []

for sp in strike_range:
    temp_results = []
    for _ in range(50):
        temp_results.append(
            simulate_degree(start_date, semesters, units_per_sem, sp, total_units)
        )
    sensitivity_results.append(np.mean(temp_results))

sensitivity_df = pd.DataFrame({
    "Strike Probability": strike_range,
    "Average Completion (Months)": sensitivity_results
})

sens_fig = px.line(
    sensitivity_df,
    x="Strike Probability",
    y="Average Completion (Months)",
    markers=True,
    title="Impact of Strike Probability on Completion Time"
)

st.plotly_chart(sens_fig, use_container_width=True)

# =====================================================
# 8. DOWNLOAD RESULTS
# =====================================================

results_df = pd.DataFrame({
    "Simulation Run": range(1, len(degree_results) + 1),
    "Degree Duration (Months)": degree_results
})

st.download_button(
    label="Download Simulation Results (CSV)",
    data=results_df.to_csv(index=False),
    file_name="degree_simulation_results.csv",
    mime="text/csv"
)

# =====================================================
# 9. MODEL ASSUMPTIONS
# =====================================================

with st.expander("Model Assumptions"):
    st.write("""
    - Each semester includes 12 teaching weeks.
    - Strike delays are modeled using a Poisson distribution.
    - Semester breaks are fixed at 2 weeks.
    - Final year includes industrial attachment and capstone project.
    - Graduation processing delay is fixed.
    - Bootcamp duration is fixed at 26 weeks.
    """)

st.caption("Stochastic educational timeline simulation model.")