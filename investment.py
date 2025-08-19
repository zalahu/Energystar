def investment_impact(emissions_tpd, carbon_price_usd=50, offset_cost_usd=30):
    daily_cost = emissions_tpd * carbon_price_usd
    offset_cost = emissions_tpd * offset_cost_usd
    return round(daily_cost, 2), round(offset_cost, 2)
