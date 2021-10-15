import streamlit as st
from simplequeue import Queue
import pandas as pd


if 'ticketNo' not in st.session_state:
    st.session_state.ticketNo = 1000

if 'ticketSystem' not in st.session_state:
    st.session_state.ticketSystem = Queue()

st.title('A basic queueing system simulator.')
st.markdown('Source codes can be found [here](https://github.com/juli4nteo/basicqueuesim).')

container_customer = st.container()
container_officer = st.container()
container_list = st.container()

container_customer.header('Customer Registration')
container_customer.markdown('If you are a customer, start by filling in your details below and press the\n **Queue Me!** button.')

container_list.subheader('Customer queue list')


with container_customer:
    name = st.text_input('Name:')
    if st.button('Queue Me!'):
        if name != '':
            st.session_state.ticketNo = st.session_state.ticketNo + 1
            st.session_state.ticketSystem.enqueue(name, st.session_state.ticketNo)
            st.write('Greetings {}. Your queue number is #{}. You will be served shortly.'.format(name, st.session_state.ticketNo))
            st.write("Your estimated waiting time is {} minutes.\n\n".format(2*st.session_state.ticketSystem.size))
            
        else:
            st.markdown('**:exclamation:** Please enter a name!')

container_officer.header('Customer Officers')
container_officer.markdown('Click on **Next Customer** buttons to serve the next customer')

col1, col2 = container_officer.columns(2)

if 'counter1_Num' not in st.session_state:
    st.session_state.counter1_Num = 'N/A'
if 'counter2_Num' not in st.session_state:
    st.session_state.counter2_Num = 'N/A' 

def getNextCustomer():
    if st.session_state.ticketSystem.size >0:
        customerNum = st.session_state.ticketSystem.getFirstElement()[1]
        st.session_state.ticketSystem.dequeue()
        return customerNum
    else:
        return 'N/A'

with col1:
    if st.button('Next Customer', key = 1):
        st.session_state.counter1_Num = getNextCustomer()
        
    st.metric('Counter 1', st.session_state.counter1_Num)
    

with col2:
    if st.button('Next Customer', key = 2):
        st.session_state.counter2_Num = getNextCustomer()

    st.metric('Counter 2', st.session_state.counter2_Num)    

# if st.button('Customer List'):
#     st.session_state.ticketSystem.traverse()
container_list.write(pd.DataFrame(st.session_state.ticketSystem.traverse(),columns=["Name", "Ticket #"]))
