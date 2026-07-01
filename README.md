# Hospital Resource Allocation using Linear Programming

An academic Operations Research project that models the optimal allocation of limited hospital resources using **Mixed Integer Linear Programming (MILP)** with the **PuLP** optimization library.

The objective is to maximize the overall weighted survival score of patients while satisfying constraints on ICU beds, ventilators, and available medical staff.

---

## Overview

Efficient allocation of scarce healthcare resources is a critical challenge during emergencies and periods of high patient demand. This project formulates the problem as a Mixed Integer Linear Programming (MILP) model to determine the optimal distribution of ICU beds and ventilators among patients.

The model prioritizes patients based on weighted survival scores while ensuring that all hospital resource constraints are satisfied.

---

## Features

* Optimizes ICU bed allocation
* Allocates ventilators only to eligible ICU patients
* Prioritizes patients using weighted survival scores
* Enforces multiple real-world hospital constraints
* Validates all resource constraints after optimization
* Generates a summary of resource utilization and patient allocation

---

## Mathematical Model

## Objective

The optimization model maximizes the sum of each patient's **priority weight × survival score** for all patients allocated an ICU bed.
where:

* **Sᵢ** – Survival score of patient *i*
* **Wᵢ** – Priority weight assigned to patient *i*
* **xᵢ** – Binary decision variable indicating ICU allocation

---

## Constraints

The optimization model enforces:

* ICU bed capacity
* Ventilator availability
* Ventilators can only be assigned to ICU patients
* Patients requiring ventilators must receive one if admitted
* Doctor-to-patient capacity limits

---

## Sample Dataset

The project uses a sample dataset consisting of **10 patients**, each defined by:

* Survival score
* Priority weight
* Ventilator requirement

Available hospital resources:

* **5 ICU beds**
* **3 Ventilators**
* **2 Doctors**
* **Maximum 3 patients per doctor**

---

## Technologies Used

* Python
* PuLP (Linear Programming)

---

## Project Structure

```text
Hospital-Resource-Allocation/
│── optimizer.py
│── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the optimization model:

```bash
python optimizer.py
```

The program outputs:

* Optimization status
* Selected ICU patients
* Selected ventilator patients
* Total weighted survival score
* Resource utilization
* Constraint verification

---

## Applications

This optimization approach can be extended for:

* Hospital emergency planning
* Pandemic response
* Disaster management
* Healthcare operations research
* Clinical decision support systems

---

## Future Improvements

* Read patient information from CSV files
* Interactive user interface
* Larger real-world datasets
* Multi-objective optimization
* Cost-aware resource allocation
* Sensitivity analysis
* Data visualization of allocation results

---

## Team

Developed collaboratively as part of an academic Operations Research project using Python and PuLP.
