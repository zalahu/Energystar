def estimate_scope_emissions(scope1_tpd, scope2_energy_mwh, scope3_transport_tpd):
    scope1 = scope1_tpd * 3.0  # Direct emissions
    scope2 = scope2_energy_mwh * 0.4  # Grid electricity factor
    scope3 = scope3_transport_tpd * 2.5  # Transport-related emissions
    total = scope1 + scope2 + scope3
    return round(scope1, 2), round(scope2, 2), round(scope3, 2), round(total, 2)
