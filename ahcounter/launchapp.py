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

st.subheader("Enter Record")
col4, col5 = st.columns(2)

with col4:
    if "active_speaker" not in st.session_state:
        st.session_state.active_speaker = None
    
    st.write("Current Speaker(s)")

    for x in session.return_speakers():
        if st.button(x):
            st.session_state.active_speaker = x
    
    if st.session_state.active_speaker:
        st.write(f"active speaker: :green[{st.session_state.active_speaker}] :sunglasses:")

with col5:
    
    for x in session.filler_word_set:
        if st.button(x) and st.session_state.active_speaker:
            session.log_input(st.session_state.active_speaker, x)
            st.write(f"logged {st.session_state.active_speaker}, {x}")



st.title("Ah Counter's Report Dashboard")
st.write(session.print_results())

