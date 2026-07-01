# Hospital Resource Allocation using Linear Programming

An Operations Research project that models the optimal allocation of limited hospital resources using **Mixed Integer Linear Programming (MILP)**.

The objective is to maximize the overall weighted survival score of patients while respecting resource limitations such as ICU beds, ventilators, and available doctors.

---

## Overview

Hospitals often face situations where critical resources are limited. This project demonstrates how mathematical optimization can assist in allocating these scarce resources fairly and efficiently.

The optimization model determines:

* Which patients should receive ICU beds
* Which ICU patients should receive ventilators
* Whether all hospital capacity constraints are satisfied

---

## Problem Formulation

### Objective Function

Maximize the total weighted survival score:

[
\max \sum_i W_i \times S_i \times x_i
]

where:

* **Sᵢ** = Survival score of patient *i*
* **Wᵢ** = Priority weight
* **xᵢ** = Binary variable indicating ICU allocation

---

## Constraints

The model satisfies the following constraints:

* Limited ICU bed capacity
* Limited ventilator availability
* Ventilators can only be assigned to ICU patients
* Patients requiring ventilators must receive one if admitted
* Doctor-to-patient capacity limits

---

## Technologies Used

* Python
* PuLP
* Streamlit
* Pyngrok

---

## Dataset

The project uses a sample dataset consisting of **10 patients**, each with:

* Survival score
* Priority weight
* Ventilator requirement

Hospital resources include:

* 5 ICU beds
* 3 Ventilators
* 2 Doctors
* Maximum 3 patients per doctor

---

## Project Structure

```text id="tjjlwm"
Hospital-Resource-Allocation/
│── hospital_optimizer1.py
│── README.md
```

---

## Installation

Install the required packages:

```bash id="slj84r"
pip install pulp streamlit pyngrok
```

---

## Running the Project

Run the optimization model:

```bash id="b8tnni"
python hospital_optimizer1.py
```

Or launch the Streamlit interface:

```bash id="7b8z1u"
streamlit run hospital_optimizer1.py
```

---

## Sample Output

The model provides:

* Optimization status
* ICU allocation for each patient
* Ventilator allocation
* Total weighted survival score
* Resource utilization
* Constraint validation
* Final interpretation of the allocation

---

## Applications

This optimization model can be adapted for:

* Hospital emergency planning
* Pandemic resource allocation
* Disaster response management
* Healthcare operations research
* Decision support systems

---

## Future Improvements

* Larger real-world datasets
* Patient arrival scheduling
* Multi-objective optimization
* Resource cost minimization
* Interactive dashboard with charts
* Database integration
* Sensitivity analysis

---

## Learning Outcomes

This project demonstrates the application of Operations Research techniques to healthcare decision-making using Mixed Integer Linear Programming. It illustrates how optimization models can support resource allocation under multiple real-world constraints.

## Team

Developed collaboratively as part of an academic Operations Research project.
