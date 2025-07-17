
import streamlit as st

st.set_page_config(page_title="WMS Front-End Simulation", layout="wide")

st.title("📦 Process-Aware Work Management System")
st.markdown("A front-end simulation of task assignment and execution for business processes.")

# Sidebar: Select user
users = ["Ali", "Fatima", "Ahmed", "Sara"]
user = st.sidebar.selectbox("🔑 Select User", users)

# Static task list per user (for front-end simulation)
simulated_tasks = {
    "Ali": [{"Task": "Asset Request", "Has Form": True}],
    "Fatima": [{"Task": "Delivery Confirmation", "Has Form": False}],
    "Ahmed": [{"Task": "Contract Review", "Has Form": True}],
    "Sara": [{"Task": "New Hire Setup", "Has Form": True}]
}

# Display tasks
st.header(f"📝 Tasks Assigned to {user}")
for idx, task in enumerate(simulated_tasks.get(user, []), start=1):
    with st.expander(f"Task {idx}: {task['Task']}"):
        st.write(f"Assigned to: {user}")
        if task["Has Form"]:
            st.write("📝 Please fill in the form below:")
            st.text_input("Enter value for required field:")
            st.button("Submit Form")
        else:
            st.write("🔧 This is a manual task. Mark as complete when done.")
            st.button("Mark as Completed")
