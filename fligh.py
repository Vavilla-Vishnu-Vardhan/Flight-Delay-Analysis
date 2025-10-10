import streamlit as st
import ollama

convo = []

def stream_response(prompt):
    convo.append({'role': 'user', 'content': prompt})
    response = ''
    stream = ollama.chat(model='llama3.1:8b', messages=convo, stream=True)
    for chunk in stream:
        response += chunk['message']['content']
        print(chunk['message']['content'], end='', flush=True)
    convo.append({'role': 'assistant', 'content': response})
    return response

# Streamlit UI
st.title("Predictive Flight Delay Analysis System")

st.header("Flight Delay Scenario")

# Dropdown for flight delay parameters
delay_reason = st.selectbox("Select the reason for flight delay:", [
    "Weather Conditions: Adverse weather can disrupt flight schedules.",
    "Air Traffic Control: Congestion and restrictions can lead to delays.",
    "Technical Issues: Mechanical problems require repairs, causing delays.",
    "Airport Congestion: Busy airports with high traffic can experience delays.",
    "Crew Availability: Delays can occur if flight crews are delayed on previous flights.",
    "Security Delays: Enhanced security checks can slow down boarding.",
    "Passenger Issues: Late arrivals of passengers or medical emergencies can cause delays.",
    "Operational Delays: Delays in baggage handling, refueling, catering can impact departure times.",
    "Regulatory Issues: Compliance with aviation regulations can cause delays.",
    "Airline Scheduling: Inefficient scheduling can result in cascading delays."
])

# Input for Passenger 1
st.header("Passenger 1")
passenger1_situation = st.selectbox("Select the situation for Passenger 1:", [
    "Passenger wants to reach the destination despite delay",
    "Passenger is okay with the delay and willing to wait",
    "Passenger does not want to reach the destination and wants a refund"
])
passenger1_explanation = st.text_area("Explain the situation for Passenger 1:")

# Input for Passenger 2
st.header("Passenger 2")
passenger2_situation = st.selectbox("Select the situation for Passenger 2:", [
    "Passenger wants to reach the destination despite delay",
    "Passenger is okay with the delay and willing to wait",
    "Passenger does not want to reach the destination and wants a refund"
])
passenger2_explanation = st.text_area("Explain the situation for Passenger 2:")

# Input for Passenger 3
st.header("Passenger 3")
passenger3_situation = st.selectbox("Select the situation for Passenger 3:", [
    "Passenger wants to reach the destination despite delay",
    "Passenger is okay with the delay and willing to wait",
    "Passenger does not want to reach the destination and wants a refund"
])
passenger3_explanation = st.text_area("Explain the situation for Passenger 3:")

if st.button("Analyze"):
    # Generate recommendation
    prompt = (f"Flight delay scenario: {delay_reason}\n"
              f"Passenger 1 situation: {passenger1_situation}\nExplanation: {passenger1_explanation}\n"
              f"Passenger 2 situation: {passenger2_situation}\nExplanation: {passenger2_explanation}\n"
              f"Passenger 3 situation: {passenger3_situation}\nExplanation: {passenger3_explanation}\n"
              "Provide the best possible solutions for the passengers.")
    response = stream_response(prompt=prompt)
    
    st.write("**Solutions:**")
    st.write(response)
