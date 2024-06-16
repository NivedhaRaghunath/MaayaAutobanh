import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Setting title for the page
st.markdown("<h1 style='text-align: center;'>Maaya Autobahn</h1>", unsafe_allow_html=True)

# Main menu
with st.sidebar:
    page = option_menu(
        menu_title='Menu',  # If required
        options=['Home', 'Dashboard', 'Log entry', 'Stock Movement Tracker', 'Oil / Lubricant Tracker',
                 'Indent Tracker', 'Expense Tracker', 'Sales summary'],
        icons=['house-check', 'people-fill', 'database', 'bar-chart', 'heart-pulse',
               'envelope-paper-heart', 'cloud', 'book'],
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "#E8751A", "font-size": "18px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#90D26D"},
            "nav-link-selected": {"background-color": "green"},
        }
    )

if page == "Home":
    st.write('Company information')
if page == 'Dashboard':
    pass
if page == 'Log entry':
    # Data entry Layout
    st.title('Routine Stock Check')

    date, location = st.columns(2)
    Date = date.date_input('Date : ', format="DD/MM/YYYY", key='start')
    Location = location.selectbox('Location: ', ['Bengaluru', 'Vijayawada', 'Dharwad'])

    st.markdown('1. Dip measurement')
    # Dip testing
    head, value = st.columns(2)
    tanker = head.selectbox('Tanker Name: ', ['Tanker 1', 'Tanker 2', 'Tanker 3'])
    fuel = value.selectbox('Fuel Type: ', ['MS', 'Power', 'HSD'])

    dip, stock = st.columns(2)
    dip_ = dip.number_input('DIP in cm: ')
    stk = stock.number_input('Stock in L: ')

    lsk = st.number_input('Previous day stock: ')

    # Observation
    water_level = stk - lsk
    if water_level > 0:
        st.write('Inference   :   Water in the tanker')
        st.write(f"Water level in cm  :  {water_level}")
    else:
        st.write('Inference   :   No water in tanker')

    action = st.selectbox('Action taken: ', ['No water No action', 'Water pumped out'])

    # Button to add data
    cols = st.columns(2)
    save = cols[1].button('SAVE')
    main_df = pd.DataFrame(
        columns=['Date',
                'Location',
                'Tanker Name',
                'Fuel Type',
                'DIP in cm',
                'Stock in L',
                'Previous day Closing Stock',
                'Water level',
                'Action taken',
                'Day Opening stock']
    )

    if save:
        data_dict = {'Date' : Date,
                'Location' : Location,
                'Tanker Name' : tanker,
                'Fuel Type' : fuel,
                'DIP in cm' : dip_,
                'Stock in L' : stk,
                'Previous day Closing Stock' : lsk,
                'Water level' : water_level,
                'Action taken' : action,
                'Day Opening stock' : stk-water_level
        }

        data_df = pd.DataFrame(data=data_dict, index=['Date'])
        # main_df = main_df.append(data_dict, ignore_index=True)
        main_df = pd.concat([main_df, data_df], axis=0)
        st.write('Data view: ')
        st.table(main_df)

        
