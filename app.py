import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Alkhorayef Work Management System",
    page_icon="📋",
    layout="wide"
)

# Initialize session state for task details and actions
if 'show_details' not in st.session_state:
    st.session_state.show_details = {}
if 'task_actions' not in st.session_state:
    st.session_state.task_actions = {}

# Custom CSS for styling
st.markdown("""
<style>
    /* Main title styling */
    .main-title {
        background-color: #ADD8E6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 28px;
        margin-bottom: 30px;
        color: #2E4057;
    }
    
    /* Table styling */
    .dataframe {
        width: 100%;
        margin: 0 auto;
    }
    
    .dataframe th {
        background-color: #4A90E2 !important;
        color: white !important;
        text-align: center !important;
        font-weight: bold !important;
        padding: 12px !important;
    }
    
    .dataframe td {
        text-align: center !important;
        padding: 10px !important;
        border-bottom: 1px solid #ddd !important;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        height: 35px;
        border-radius: 50%;
        border: none;
        font-size: 16px;
        margin: 2px;
    }
    
    .stButton > button:hover {
        transform: scale(1.1);
        transition: transform 0.2s;
    }
    
    /* Status color coding */
    .status-pending {
        background-color: #FFF3CD !important;
        color: #856404 !important;
        font-weight: bold !important;
    }
    
    .status-progress {
        background-color: #D4EDDA !important;
        color: #155724 !important;
        font-weight: bold !important;
    }
    
    .status-completed {
        background-color: #D1ECF1 !important;
        color: #0C5460 !important;
        font-weight: bold !important;
    }
    
    .status-rejected {
        background-color: #F8D7DA !important;
        color: #721C24 !important;
        font-weight: bold !important;
    }
    
    /* Priority color coding */
    .priority-high {
        color: #DC3545 !important;
        font-weight: bold !important;
    }
    
    .priority-medium {
        color: #FFC107 !important;
        font-weight: bold !important;
    }
    
    .priority-low {
        color: #28A745 !important;
        font-weight: bold !important;
    }
    
    /* Hide streamlit style */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Alkhorayef Work Management System</div>', unsafe_allow_html=True)

# Enhanced data with detailed information
task_details = {
    1: {
        "description": "Review and approve the quarterly financial document submitted by the finance team.",
        "due_date": "2024-08-15",
        "created_by": "Finance Manager",
        "comments": "Requires executive approval before Q3 reporting."
    },
    2: {
        "description": "Review purchase request for new office equipment worth $15,000.",
        "due_date": "2024-08-10",
        "created_by": "HR Manager",
        "comments": "Urgent - equipment needed for new hires."
    },
    3: {
        "description": "Upload the monthly sales performance report to the company dashboard.",
        "due_date": "2024-08-20",
        "created_by": "Sales Director",
        "comments": "Data from all regional offices required."
    },
    4: {
        "description": "Update the company website banner for the upcoming product launch.",
        "due_date": "2024-08-05",
        "created_by": "Marketing Team",
        "comments": "Banner design already approved by creative team."
    },
    5: {
        "description": "Sign the Power of Attorney agreement for the new business partnership.",
        "due_date": "2024-08-12",
        "created_by": "Legal Department",
        "comments": "Rejected due to incomplete documentation."
    },
    6: {
        "description": "Verify and approve the bank details for the new supplier registration.",
        "due_date": "2024-08-18",
        "created_by": "Procurement Team",
        "comments": "Requires verification of company registration documents."
    },
    7: {
        "description": "Complete onboarding process for the new technician including training and documentation.",
        "due_date": "2024-08-08",
        "created_by": "HR Manager",
        "comments": "Successfully completed all onboarding requirements."
    }
}

# Data
data = [
    [1, "Document Approval", "Approval", "Pending", "Renier Annandale", "Medium"],
    [2, "Purchase Request Review", "Approval", "In Progress", "Renier Annandale", "High"],
    [3, "Monthly Sales Report Upload", "Task", "Pending", "Renier Annandale", "Medium"],
    [4, "Update Website Banner", "Task", "Completed", "Renier Annandale", "Low"],
    [5, "POA Agreement Signature", "Approval", "Rejected", "Renier Annandale", "High"],
    [6, "Verify Supplier Bank Details", "Approval", "Pending", "Renier Annandale", "Medium"],
    [7, "New Technician Onboarding", "Task", "Completed", "Renier Annandale", "High"]
]

# Column names
columns = ["#", "Task", "Type", "Status", "Assigned to", "Priority"]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Function to style the dataframe
def style_dataframe(df):
    def apply_status_style(val):
        if val == "Pending":
            return 'background-color: #FFF3CD; color: #856404; font-weight: bold'
        elif val == "In Progress":
            return 'background-color: #D4EDDA; color: #155724; font-weight: bold'
        elif val == "Completed":
            return 'background-color: #D1ECF1; color: #0C5460; font-weight: bold'
        elif val == "Rejected":
            return 'background-color: #F8D7DA; color: #721C24; font-weight: bold'
        return ''
    
    def apply_priority_style(val):
        if val == "High":
            return 'color: #DC3545; font-weight: bold'
        elif val == "Medium":
            return 'color: #FFC107; font-weight: bold'
        elif val == "Low":
            return 'color: #28A745; font-weight: bold'
        return ''
    
    styled_df = df.style.applymap(apply_status_style, subset=['Status'])
    styled_df = styled_df.applymap(apply_priority_style, subset=['Priority'])
    
    # Apply general styling
    styled_df = styled_df.set_table_styles([
        {'selector': 'th', 'props': [
            ('background-color', '#4A90E2'),
            ('color', 'white'),
            ('font-weight', 'bold'),
            ('text-align', 'center'),
            ('padding', '12px')
        ]},
        {'selector': 'td', 'props': [
            ('text-align', 'center'),
            ('padding', '10px'),
            ('border-bottom', '1px solid #ddd')
        ]},
        {'selector': 'table', 'props': [
            ('width', '100%'),
            ('margin', '0 auto'),
            ('border-collapse', 'collapse')
        ]}
    ])
    
    return styled_df

# Display the table with interactive buttons
st.markdown("""
<div style="background-color: #4A90E2; color: white; font-weight: bold; padding: 12px; display: flex; text-align: center;">
    <div style="flex: 0.5; border-right: 1px solid white; padding: 8px;">#</div>
    <div style="flex: 3; border-right: 1px solid white; padding: 8px;">Task</div>
    <div style="flex: 1.5; border-right: 1px solid white; padding: 8px;">Type</div>
    <div style="flex: 1.5; border-right: 1px solid white; padding: 8px;">Status</div>
    <div style="flex: 2; border-right: 1px solid white; padding: 8px;">Assigned to</div>
    <div style="flex: 1; border-right: 1px solid white; padding: 8px;">Priority</div>
    <div style="flex: 1.5; padding: 8px;">Action</div>
</div>
""", unsafe_allow_html=True)

# Display each row with interactive elements
for index, row in df.iterrows():
    task_id = row['#']
    task_name = row['Task']
    task_type = row['Type']
    status = row['Status']
    assigned_to = row['Assigned to']
    priority = row['Priority']
    
    # Determine status color
    status_color = {
        "Pending": "#FFF3CD",
        "In Progress": "#D4EDDA", 
        "Completed": "#D1ECF1",
        "Rejected": "#F8D7DA"
    }.get(status, "#FFFFFF")
    
    status_text_color = {
        "Pending": "#856404",
        "In Progress": "#155724",
        "Completed": "#0C5460", 
        "Rejected": "#721C24"
    }.get(status, "#000000")
    
    # Determine priority color
    priority_color = {
        "High": "#DC3545",
        "Medium": "#FFC107",
        "Low": "#28A745"
    }.get(priority, "#000000")
    
    # Create columns for the row
    cols = st.columns([0.5, 3, 1.5, 1.5, 2, 1, 1.5])
    
    with cols[0]:
        st.markdown(f"<div style='text-align: center; padding: 10px; border-bottom: 1px solid #ddd;'>{task_id}</div>", unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown(f"<div style='text-align: center; padding: 10px; border-bottom: 1px solid #ddd;'>{task_name}</div>", unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown(f"<div style='text-align: center; padding: 10px; border-bottom: 1px solid #ddd;'>{task_type}</div>", unsafe_allow_html=True)
    
    with cols[3]:
        st.markdown(f"<div style='text-align: center; padding: 10px; border-bottom: 1px solid #ddd; background-color: {status_color}; color: {status_text_color}; font-weight: bold;'>{status}</div>", unsafe_allow_html=True)
    
    with cols[4]:
        st.markdown(f"<div style='text-align: center; padding: 10px; border-bottom: 1px solid #ddd;'>{assigned_to}</div>", unsafe_allow_html=True)
    
    with cols[5]:
        st.markdown(f"<div style='text-align: center; padding: 10px; border-bottom: 1px solid #ddd; color: {priority_color}; font-weight: bold;'>{priority}</div>", unsafe_allow_html=True)
    
    with cols[6]:
        # Action buttons
        btn_cols = st.columns(2)
        with btn_cols[0]:
            if st.button("👁️", key=f"view_{task_id}", help="View Details"):
                st.session_state.show_details[task_id] = not st.session_state.show_details.get(task_id, False)
        
        with btn_cols[1]:
            if st.button("✅", key=f"action_{task_id}", help="Take Action"):
                st.session_state.task_actions[task_id] = not st.session_state.task_actions.get(task_id, False)

# Display task details if view button was clicked
for task_id in st.session_state.show_details:
    if st.session_state.show_details[task_id]:
        with st.expander(f"📋 Task #{task_id} Details", expanded=True):
            details = task_details[task_id]
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Description:** {details['description']}")
                st.write(f"**Due Date:** {details['due_date']}")
            
            with col2:
                st.write(f"**Created By:** {details['created_by']}")
                st.write(f"**Comments:** {details['comments']}")
            
            if st.button("Close Details", key=f"close_{task_id}"):
                st.session_state.show_details[task_id] = False
                st.rerun()

# Display action forms if action button was clicked
for task_id in st.session_state.task_actions:
    if st.session_state.task_actions[task_id]:
        with st.expander(f"⚡ Take Action on Task #{task_id}", expanded=True):
            task_row = df[df['#'] == task_id].iloc[0]
            st.write(f"**Task:** {task_row['Task']}")
            st.write(f"**Current Status:** {task_row['Status']}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                new_status = st.selectbox(
                    "Update Status:",
                    ["Pending", "In Progress", "Completed", "Rejected"],
                    index=["Pending", "In Progress", "Completed", "Rejected"].index(task_row['Status']),
                    key=f"status_{task_id}"
                )
            
            with col2:
                new_assignee = st.text_input(
                    "Reassign to:",
                    value=task_row['Assigned to'],
                    key=f"assignee_{task_id}"
                )
            
            action_comments = st.text_area(
                "Action Comments:",
                placeholder="Enter your comments about this action...",
                key=f"comments_{task_id}"
            )
            
            action_cols = st.columns(3)
            with action_cols[0]:
                if st.button("💾 Save Changes", key=f"save_{task_id}"):
                    st.success(f"✅ Task #{task_id} updated successfully!")
                    st.session_state.task_actions[task_id] = False
                    st.rerun()
            
            with action_cols[1]:
                if st.button("📧 Send Notification", key=f"notify_{task_id}"):
                    st.info(f"📨 Notification sent to {new_assignee}")
            
            with action_cols[2]:
                if st.button("❌ Cancel", key=f"cancel_{task_id}"):
                    st.session_state.task_actions[task_id] = False
                    st.rerun()

# Summary statistics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Tasks", len(df))

with col2:
    pending_count = len(df[df['Status'] == 'Pending'])
    st.metric("Pending", pending_count)

with col3:
    completed_count = len(df[df['Status'] == 'Completed'])
    st.metric("Completed", completed_count)

with col4:
    high_priority_count = len(df[df['Priority'] == 'High'])
    st.metric("High Priority", high_priority_count)
