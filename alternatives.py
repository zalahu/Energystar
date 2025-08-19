def compare_low_carbon_options(current_emissions, hydrogen_share=0.3, ccus_capture_rate=0.5):
    hydrogen_reduction = current_emissions * hydrogen_share * 0.6
    ccus_reduction = current_emissions * ccus_capture_rate
    net_emissions = current_emissions - (hydrogen_reduction + ccus_reduction)
    return round(hydrogen_reduction, 2), round(ccus_reduction, 2), round(net_emissions, 2)
