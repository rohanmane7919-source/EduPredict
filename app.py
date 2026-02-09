import streamlit as st
import streamlit.components.v1 as components
import joblib
import json

st.set_page_config(page_title="EduPredict", page_icon="🎓", layout="wide")

model = joblib.load("Gradient-Boosting.pkl")

def predict(data):
    input_data = [[
        data["Hours_Studied"],
        data["Attendance"],
        data["Access_to_Resources"],
        data["Extracurricular_Activities"],
        data["Sleep_Hours"],
        data["Previous_Scores"],
        data["Internet_Access"],
        data["Tutoring_Sessions"],
        data["Family_Income"],
        data["Teacher_Quality"],
        data["School_Type"],
        data["Peer_Influence"],
        data["Physical_Activity"],
        data["Learning_Disabilities"],
        data["Parental_Education_Level"],
        data["Distance_from_Home"],
        data["Gender"]
    ]]
    return float(model.predict(input_data)[0])

if "prediction" not in st.session_state:
    st.session_state.prediction = None

html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    font-family: Arial;
    background: #f9fbff;
}}
.container {{
    max-width: 900px;
    margin: auto;
    background: white;
    padding: 30px;
    border-radius: 16px;
}}
.grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}}
.card {{
    background: #eef4ff;
    padding: 20px;
    border-radius: 12px;
}}
button {{
    width: 100%;
    padding: 15px;
    font-size: 16px;
    background: #2b5cff;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
}}
input, select {{
    width: 100%;
    padding: 8px;
    margin-top: 5px;
}}
.result {{
    margin-top: 30px;
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #2b5cff;
}}
</style>
</head>
<body>
<div class="container">
<h1>🎓 EduPredict</h1>

<div class="grid">
<div class="card">
<label>Hours Studied</label>
<input id="Hours_Studied" type="number" value="6">
<label>Attendance</label>
<input id="Attendance" type="number" value="75">
<label>Sleep Hours</label>
<input id="Sleep_Hours" type="number" value="6">
<label>Previous Scores</label>
<input id="Previous_Scores" type="number" value="75">
</div>

<div class="card">
<label>Access to Resources</label>
<select id="Access_to_Resources">
<option value="2">High</option>
<option value="1">Medium</option>
<option value="0">Low</option>
</select>
<label>Extracurricular</label>
<select id="Extracurricular_Activities">
<option value="1">Yes</option>
<option value="0">No</option>
</select>
<label>Internet Access</label>
<select id="Internet_Access">
<option value="1">Yes</option>
<option value="0">No</option>
</select>
<label>Peer Influence</label>
<select id="Peer_Influence">
<option value="2">Positive</option>
<option value="1">Neutral</option>
<option value="0">Negative</option>
</select>
</div>

<div class="card">
<label>Family Income</label>
<select id="Family_Income">
<option value="2">High</option>
<option value="1">Medium</option>
<option value="0">Low</option>
</select>
<label>Teacher Quality</label>
<select id="Teacher_Quality">
<option value="2">High</option>
<option value="1">Medium</option>
<option value="0">Low</option>
</select>
<label>School Type</label>
<select id="School_Type">
<option value="1">Private</option>
<option value="0">Public</option>
</select>
<label>Gender</label>
<select id="Gender">
<option value="0">Male</option>
<option value="1">Female</option>
</select>
</div>
</div>

<br>
<button onclick="send()">Predict Exam Score</button>
<div class="result" id="result"></div>
</div>

<script>
function send() {{
    const data = {{
        Hours_Studied: Number(document.getElementById("Hours_Studied").value),
        Attendance: Number(document.getElementById("Attendance").value),
        Access_to_Resources: Number(document.getElementById("Access_to_Resources").value),
        Extracurricular_Activities: Number(document.getElementById("Extracurricular_Activities").value),
        Sleep_Hours: Number(document.getElementById("Sleep_Hours").value),
        Previous_Scores: Number(document.getElementById("Previous_Scores").value),
        Internet_Access: Number(document.getElementById("Internet_Access").value),
        Tutoring_Sessions: 5,
        Family_Income: Number(document.getElementById("Family_Income").value),
        Teacher_Quality: Number(document.getElementById("Teacher_Quality").value),
        School_Type: Number(document.getElementById("School_Type").value),
        Peer_Influence: Number(document.getElementById("Peer_Influence").value),
        Physical_Activity: 5,
        Learning_Disabilities: 0,
        Parental_Education_Level: 1,
        Distance_from_Home: 1,
        Gender: Number(document.getElementById("Gender").value)
    }};
    window.parent.postMessage(data, "*");
}}
</script>
</body>
</html>
"""

components.html(html, height=900)

event = st.experimental_get_query_params()

if st.session_state.get("incoming"):
    st.session_state.prediction = predict(st.session_state.incoming)

def handle_message():
    if st.session_state.get("incoming"):
        st.session_state.prediction = predict(st.session_state.incoming)

if st.session_state.prediction is not None:
    st.success(f"Predicted Exam Score: {st.session_state.prediction:.2f}%")

st.markdown("""
<script>
window.addEventListener("message", (event) => {
    fetch("/_stcore/handle", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(event.data)
    });
});
</script>
""", unsafe_allow_html=True)
