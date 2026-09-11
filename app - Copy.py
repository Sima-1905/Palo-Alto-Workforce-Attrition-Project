import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Workforce Attrition Risk Analysis", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    path = "Palo Alto Networks(4).csv"
    data = pd.read_csv(path)
    data["AttritionLabel"] = data["Attrition"].map({0: "Retained", 1: "Exited"})
    data["AgeGroup"] = pd.cut(
        data["Age"], bins=[0, 25, 35, 45, 55, 100],
        labels=["<25", "25-34", "35-44", "45-54", "55+"]
    )
    data["TenureBucket"] = pd.cut(
        data["YearsAtCompany"], bins=[-1, 2, 5, 10, 100],
        labels=["0-2 years", "3-5 years", "6-10 years", "11+ years"]
    )
    return data

df = load_data()

st.title("📊 Workforce Attrition Patterns and Risk Hotspot Analysis")
st.caption("Diagnostic HR analytics dashboard — based on the supplied employee dataset")

# Sidebar filters
st.sidebar.header("Filters")
departments = st.sidebar.multiselect("Department", sorted(df["Department"].unique()), default=sorted(df["Department"].unique()))
roles = st.sidebar.multiselect("Job Role", sorted(df["JobRole"].unique()), default=sorted(df["JobRole"].unique()))
tenure = st.sidebar.slider("Years at Company", int(df["YearsAtCompany"].min()), int(df["YearsAtCompany"].max()),
                           (int(df["YearsAtCompany"].min()), int(df["YearsAtCompany"].max())))
overtime = st.sidebar.multiselect("Overtime", sorted(df["OverTime"].unique()), default=sorted(df["OverTime"].unique()))
travel = st.sidebar.multiselect("Business Travel", sorted(df["BusinessTravel"].unique()), default=sorted(df["BusinessTravel"].unique()))

filtered = df[
    df["Department"].isin(departments) &
    df["JobRole"].isin(roles) &
    df["YearsAtCompany"].between(tenure[0], tenure[1]) &
    df["OverTime"].isin(overtime) &
    df["BusinessTravel"].isin(travel)
].copy()

# KPIs
total = len(filtered)
exited = int(filtered["Attrition"].sum())
retained = total - exited
rate = (exited / total * 100) if total else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Employees", f"{total:,}")
c2.metric("Attrition Rate", f"{rate:.1f}%")
c3.metric("Exited", f"{exited:,}")
c4.metric("Retained", f"{retained:,}")

if total == 0:
    st.warning("No employees match the selected filters.")
    st.stop()

# Overview
st.header("1. Attrition Overview")
left, right = st.columns(2)

with left:
    pie = filtered["AttritionLabel"].value_counts().rename_axis("Status").reset_index(name="Employees")
    fig = px.pie(pie, names="Status", values="Employees", hole=0.45, title="Retained vs Exited")
    st.plotly_chart(fig, use_container_width=True)

with right:
    dept = filtered.groupby("Department", as_index=False)["Attrition"].mean()
    dept["Attrition Rate (%)"] = dept["Attrition"] * 100
    dept = dept.sort_values("Attrition Rate (%)", ascending=False)
    fig = px.bar(dept, x="Department", y="Attrition Rate (%)", title="Attrition Rate by Department", text_auto=".1f")
    st.plotly_chart(fig, use_container_width=True)

# Role analysis
st.header("2. Department & Role Risk Hotspots")
role = filtered.groupby("JobRole", as_index=False).agg(
    Employees=("Attrition", "size"),
    Exits=("Attrition", "sum"),
    Attrition_Rate=("Attrition", "mean")
)
role["Attrition Rate (%)"] = role["Attrition_Rate"] * 100
role = role.sort_values("Attrition Rate (%)", ascending=False)

fig = px.bar(role, x="Attrition Rate (%)", y="JobRole", orientation="h",
             title="Attrition Rate by Job Role", text_auto=".1f")
st.plotly_chart(fig, use_container_width=True)
st.dataframe(role[["JobRole", "Employees", "Exits", "Attrition Rate (%)"]], use_container_width=True, hide_index=True)

# Demographic analysis
st.header("3. Demographic Attrition Explorer")
d1, d2 = st.columns(2)

with d1:
    age = filtered.groupby("AgeGroup", observed=False)["Attrition"].mean().reset_index()
    age["Attrition Rate (%)"] = age["Attrition"] * 100
    fig = px.bar(age, x="AgeGroup", y="Attrition Rate (%)", title="Attrition by Age Group", text_auto=".1f")
    st.plotly_chart(fig, use_container_width=True)

with d2:
    gender = filtered.groupby("Gender")["Attrition"].mean().reset_index()
    gender["Attrition Rate (%)"] = gender["Attrition"] * 100
    fig = px.bar(gender, x="Gender", y="Attrition Rate (%)", title="Attrition by Gender", text_auto=".1f")
    st.plotly_chart(fig, use_container_width=True)

m = filtered.groupby("MaritalStatus")["Attrition"].mean().reset_index()
m["Attrition Rate (%)"] = m["Attrition"] * 100
fig = px.bar(m, x="MaritalStatus", y="Attrition Rate (%)", title="Attrition by Marital Status", text_auto=".1f")
st.plotly_chart(fig, use_container_width=True)

# Tenure/workload
st.header("4. Tenure & Workload Analysis")
t1, t2 = st.columns(2)

with t1:
    tenure_df = filtered.groupby("TenureBucket", observed=False)["Attrition"].mean().reset_index()
    tenure_df["Attrition Rate (%)"] = tenure_df["Attrition"] * 100
    fig = px.bar(tenure_df, x="TenureBucket", y="Attrition Rate (%)", title="Attrition by Tenure", text_auto=".1f")
    st.plotly_chart(fig, use_container_width=True)

with t2:
    ot = filtered.groupby("OverTime")["Attrition"].mean().reset_index()
    ot["Attrition Rate (%)"] = ot["Attrition"] * 100
    fig = px.bar(ot, x="OverTime", y="Attrition Rate (%)", title="Overtime vs Attrition", text_auto=".1f")
    st.plotly_chart(fig, use_container_width=True)

travel_df = filtered.groupby("BusinessTravel")["Attrition"].mean().reset_index()
travel_df["Attrition Rate (%)"] = travel_df["Attrition"] * 100
fig = px.bar(travel_df, x="BusinessTravel", y="Attrition Rate (%)", title="Business Travel vs Attrition", text_auto=".1f")
st.plotly_chart(fig, use_container_width=True)

# Distance and promotion
d1, d2 = st.columns(2)
with d1:
    dist = filtered.copy()
    dist["DistanceBand"] = pd.cut(dist["DistanceFromHome"], [-1, 5, 10, 20, 1000],
                                  labels=["0-5 km", "6-10 km", "11-20 km", "21+ km"])
    x = dist.groupby("DistanceBand", observed=False)["Attrition"].mean().reset_index()
    x["Attrition Rate (%)"] = x["Attrition"] * 100
    fig = px.bar(x, x="DistanceBand", y="Attrition Rate (%)", title="Distance from Home vs Attrition", text_auto=".1f")
    st.plotly_chart(fig, use_container_width=True)

with d2:
    promo = filtered.groupby("YearsSinceLastPromotion")["Attrition"].mean().reset_index()
    promo["Attrition Rate (%)"] = promo["Attrition"] * 100
    fig = px.line(promo, x="YearsSinceLastPromotion", y="Attrition Rate (%)",
                  markers=True, title="Promotion Gap vs Attrition")
    st.plotly_chart(fig, use_container_width=True)

# Executive findings
st.header("5. Key Findings")
overall = df["Attrition"].mean() * 100
ot_yes = df.loc[df["OverTime"] == "Yes", "Attrition"].mean() * 100
ot_no = df.loc[df["OverTime"] == "No", "Attrition"].mean() * 100
young = df.loc[df["AgeGroup"] == "<25", "Attrition"].mean() * 100
early = df.loc[df["TenureBucket"] == "0-2 years", "Attrition"].mean() * 100

st.markdown(f"""
- Overall attrition in the supplied dataset is **{overall:.1f}%**.
- Employees working overtime show **{ot_yes:.1f}%** attrition versus **{ot_no:.1f}%** without overtime.
- Employees aged below 25 show **{young:.1f}%** attrition.
- Employees with 0–2 years at the company show **{early:.1f}%** attrition.
- Use department, role, tenure, overtime and travel patterns to prioritize retention interventions.
""")

st.info("Important: These are diagnostic associations, not proof that any single factor causes attrition. The dashboard should support HR investigation and targeted retention planning.")
