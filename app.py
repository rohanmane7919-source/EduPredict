import streamlit as st
import joblib

st.set_page_config(page_title="EduPredict", page_icon="🎓", layout="wide")

st.markdown(
    """
    <style>
    .css-18e3th9 { 
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        margin: 0;
    }
    body {
       background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
        background-attachment: fixed;
        margin: 0;
        height: 100vh;
        width: 100%;
    }
    .stApp, .css-1d391kg {
        background-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎓 EduPredict")
st.markdown(
    "<p style='font-size:18px;color:#555;'>AI-powered student performance prediction dashboard</p>",
    unsafe_allow_html=True
)

st.markdown("### 📘 Student Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🕒 Study & Attendance")
    Hours_Studied = st.slider("Hours Studied (per day)", 0, 12, 6)
    Attendance = st.slider("Attendance (%)", 0, 100, 75)
    
    st.markdown("""
    <style>
    div[data-testid="stSelectbox"] > div {
        background-color: #ffffff;
        border: 2px solid #764ba2;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)


    Access_to_Resources = st.selectbox("Access to Resources", ["High", "Medium", "Low"])
    Family_Income = st.selectbox("Family Income", ["High", "Medium", "Low"])
    Teacher_Quality = st.selectbox("Teacher Quality", ["High", "Medium", "Low"])
    School_Type = st.selectbox("School Type", ["Public", "Private"])

with col2:
    st.markdown("#### 🧠 Lifestyle & Activities")
    Extracurricular_Activities = st.selectbox("Extracurricular Activities", ["Yes", "No"])
    Sleep_Hours = st.slider("Sleep Hours", 0, 12, 6)
    Previous_Scores = st.slider("Previous Scores", 0, 100, 75)
    Peer_Influence = st.selectbox("Peer Influence", ["Positive", "Neutral", "Negative"])
    Physical_Activity = st.slider("Physical Activity (hrs/week)", 0, 20, 5)
    Learning_Disabilities = st.selectbox("Learning Disabilities", ["No", "Yes"])

with col3:
    st.markdown("#### 🏠 Background")
    Internet_Access = st.selectbox("Internet Access", ["Yes", "No"])
    Tutoring_Sessions = st.slider("Tutoring Sessions (per month)", 0, 20, 5)
    Parental_Education_Level = st.selectbox(
        "Parental Education Level",
        ["High School", "College", "Postgraduate"]
    )
    Distance_from_Home = st.selectbox("Distance from Home", ["Near", "Moderate", "Far"])
    Gender = st.selectbox("Gender", ["Male", "Female"])

CATEGORY_MAP = {
    "Access_to_Resources": {"Low": 0, "Medium": 1, "High": 2},
    "Family_Income": {"Low": 0, "Medium": 1, "High": 2},
    "Teacher_Quality": {"Low": 0, "Medium": 1, "High": 2},
    "School_Type": {"Public": 0, "Private": 1},
    "Extracurricular_Activities": {"No": 0, "Yes": 1},
    "Peer_Influence": {"Negative": 0, "Neutral": 1, "Positive": 2},
    "Learning_Disabilities": {"No": 0, "Yes": 1},
    "Internet_Access": {"No": 0, "Yes": 1},
    "Parental_Education_Level": {"High School": 0, "College": 1, "Postgraduate": 2},
    "Distance_from_Home": {"Near": 0, "Moderate": 1, "Far": 2},
    "Gender": {"Male": 0, "Female": 1}
}

Access_to_Resources = CATEGORY_MAP["Access_to_Resources"][Access_to_Resources]
Family_Income = CATEGORY_MAP["Family_Income"][Family_Income]
Teacher_Quality = CATEGORY_MAP["Teacher_Quality"][Teacher_Quality]
School_Type = CATEGORY_MAP["School_Type"][School_Type]
Extracurricular_Activities = CATEGORY_MAP["Extracurricular_Activities"][Extracurricular_Activities]
Peer_Influence = CATEGORY_MAP["Peer_Influence"][Peer_Influence]
Learning_Disabilities = CATEGORY_MAP["Learning_Disabilities"][Learning_Disabilities]
Internet_Access = CATEGORY_MAP["Internet_Access"][Internet_Access]
Parental_Education_Level = CATEGORY_MAP["Parental_Education_Level"][Parental_Education_Level]
Distance_from_Home = CATEGORY_MAP["Distance_from_Home"][Distance_from_Home]
Gender = CATEGORY_MAP["Gender"][Gender]

input_data = [[
    Hours_Studied,
    Attendance,
    Access_to_Resources,
    Extracurricular_Activities,
    Sleep_Hours,
    Previous_Scores,
    Internet_Access,
    Tutoring_Sessions,
    Family_Income,
    Teacher_Quality,
    School_Type,
    Peer_Influence,
    Physical_Activity,
    Learning_Disabilities,
    Parental_Education_Level,
    Distance_from_Home,
    Gender
]]

model = joblib.load("Gradient-Boosting")

st.markdown("---")

colA, colB, colC = st.columns([1, 2, 1])

with colB:
    if st.button("🚀 Predict Exam Score", use_container_width=True):
        pred = model.predict(input_data)
        st.metric("📊 Predicted Exam Score", f"{pred[0]:.2f} %")
