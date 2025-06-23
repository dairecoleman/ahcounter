import streamlit as st
import pandas as pd
import ahcounter

#ahcounter.ToastmasterMeeting()

st.title("Ah Counter's Report Dashboard")

ahcounter_table = None#LOAD Default/ Current DATA
# Initialize session object ONCE and store in session_state
if "session" not in st.session_state:
    st.session_state.session = ahcounter.ToastmasterMeeting()

session = st.session_state.session  # use the persistent one

# example log input function call
#session.log_input("Judy", "Oh")


# Controls Block
st.subheader("Controls")
col1, col2, col3 = st.columns(3)

#if st.button("Load Data Button"):
#    ahcounter_table = [1,2,3,4,5,6]

#if ahcounter_table is not None:
#    st.write("data loaded")

#    if st.button("Clck me baby"):
#        st.write("we made it")

with col1:
    name = st.text_input("Enter speaker's name")
    if st.button("Add a Speaker") and name:
        session.add_speaker(name) # add dropdown or txt field
        st.write(f"Addedspeaker: {name}")

with col2:
    word = st.text_input("Enter filler word")
    if st.button("Add a Filler Word") and word:
        session.update_filler_word_set(word) # dropdown and text field
        st.write("Added filler Word")

with col3:
    if st.button("Clear Table"):
        session.clear_data()
        session.print_results()


st.title("Ah Counter's Report Dashboard")
st.write(session.print_results())

