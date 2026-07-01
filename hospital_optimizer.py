import pulp

def optimize():
    patients = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10']
    #survival scores (Si)
    S = {
        'P1':9,'P2':8,'P3':7,'P4':9,'P5':6,
        'P6':5,'P7':4,'P8':6,'P9':5,'P10':4
    }
    
    #priority weights (Wi)
    W = {
        'P1':2,'P2':2,'P3':2,'P4':2,'P5':2,
        'P6':1,'P7':1,'P8':1,'P9':1,'P10':1
    }
    #ventilator requirement (ri)
    R = {
        'P1':1,'P2':1,'P3':1,'P4':1,'P5':0,
        'P6':0,'P7':0,'P8':0,'P9':0,'P10':0
    }
    B = 5   # ICU beds
    V = 3   # ventilators
    D = 2   # doctors
    k = 3   # patients per doctor
    
    model = pulp.LpProblem("Hospital_Resource_Allocation", pulp.LpMaximize)
    
    x = pulp.LpVariable.dicts("ICU", patients, lowBound=0, upBound=1, cat='Binary')
    y = pulp.LpVariable.dicts("Ventilator", patients, lowBound=0, upBound=1, cat='Binary')
    
    model += pulp.lpSum(W[i] * S[i] * x[i] for i in patients)
    
    model += pulp.lpSum(x[i] for i in patients) <= B, "ICU_Capacity"
    model += pulp.lpSum(y[i] for i in patients) <= V, "Ventilator_Capacity"
    for i in patients:
        model += y[i] <= x[i], f"Ventilator_if_ICU_{i}"
    for i in patients:
            model += y[i] >= R[i] * x[i], f"Ventilator_Requirement_{i}"
    model += pulp.lpSum(x[i] for i in patients) <= D * k, "Doctor_Capacity"
    
    model.solve()

    icu_patients = []
    vent_patients = []
    
    for i in patients:
        if int(pulp.value(x[i])) == 1:
            icu_patients.append(i)
        if int(pulp.value(y[i])) == 1:
            vent_patients.append(i)
    
    total_score = sum(
        W[i] * S[i] * pulp.value(x[i])
        for i in patients
    )
    
    return {
        "status": pulp.LpStatus[model.status],
        "icu_patients": icu_patients,
        "ventilator_patients": vent_patients,
        "total_score": total_score,
        "beds_used": len(icu_patients),
        "vents_used": len(vent_patients),
        "B": B,
        "V": V
    }

if __name__ == "__main__":
    result = optimize()

    print("Status:", result["status"])
    print("ICU Patients:", result["icu_patients"])
    print("Ventilator Patients:", result["ventilator_patients"])
    print("Total Score:", result["total_score"])
