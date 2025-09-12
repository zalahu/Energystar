
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from utils import load_documents
from agent import build_agent
from emissions import estimate_scope_emissions
from alternatives import compare_low_carbon_options
from investment import investment_impact

st.set_page_config(page_title="Energynvest-Ai Agent", layout="wide")
st.title("🔍 Energynvest-Ai: Energy Transition Intelligence Agent")

# Document Upload
uploaded_files = st.file_uploader("Upload multiple documents (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing documents..."):
        documents = load_documents(uploaded_files)
        agent = build_agent(documents)
    st.success("Documents processed. You can now ask questions!")

    query = st.text_input("Ask a question about your energy transition project:")
    if query:
        with st.spinner("Thinking..."):
            response = agent.run(query)
        st.markdown("### 🧠 Response")
        st.write(response)

# Emission Estimation
st.markdown("---")
st.header("📊 Lifecycle Emissions Estimation")

with st.form("scope_form"):
    scope1 = st.number_input("Scope 1: Direct emissions (tons/day)", min_value=0.0)
    scope2 = st.number_input("Scope 2: Electricity use (MWh/day)", min_value=0.0)
    scope3 = st.number_input("Scope 3: Transport emissions (tons/day)", min_value=0.0)
    submitted = st.form_submit_button("Estimate Lifecycle Emissions")

    if submitted:
        s1, s2, s3, total = estimate_scope_emissions(scope1, scope2, scope3)
        st.success(f"Scope 1: {s1} | Scope 2: {s2} | Scope 3: {s3} | Total: {total} tons/day")

# Low-Carbon Comparison
st.markdown("---")
st.header("⚡ Compare Low-Carbon Alternatives")

with st.form("low_carbon_form"):
    current_emissions = st.number_input("Current Emissions (tons/day)", min_value=0.0)
    hydrogen_share = st.slider("Hydrogen Share (%)", 0.0, 1.0, 0.3, step=0.01)
    ccus_rate = st.slider("CCUS Capture Rate (%)", 0.0, 1.0, 0.5, step=0.01)
    submitted = st.form_submit_button("Compare")

    if submitted:
        h2_red, ccus_red, net = compare_low_carbon_options(current_emissions, hydrogen_share, ccus_rate)
        st.success(f"Hydrogen Reduction: {h2_red} | CCUS Reduction: {ccus_red} | Net Emissions: {net} tons/day")

# Investment Impact
st.markdown("---")
st.header("💰 Investment Impact Analysis")

with st.form("investment_form"):
    emissions_tpd = st.number_input("Emissions to Price (tons/day)", min_value=0.0)
    carbon_price = st.number_input("Carbon Price (USD/ton)", value=50.0)
    offset_cost = st.number_input("Offset Cost (USD/ton)", value=30.0)
    submitted = st.form_submit_button("Calculate Impact")

    if submitted:
        daily_cost, offset = investment_impact(emissions_tpd, carbon_price, offset_cost)
        st.success(f"Daily Carbon Cost: ${daily_cost} | Offset Cost: ${offset}")
