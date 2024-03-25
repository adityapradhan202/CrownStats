import stats
import overall_stats as ostats
import streamlit as st
import time
import stats_plot as splot
import matplotlib.pyplot as plt

# session state variables
if 'pname' not in st.session_state:
    st.session_state.pname = 'Crispy veg'
if 'month1' not in st.session_state:
    st.session_state.month1 = None
if 'month2' not in st.session_state:
    st.session_state.month2 = None
if 'month3' not in st.session_state:
    st.session_state.month3 = None

# headers and tabs
st.header('CrownStats :crown:')
tab_names = ['Overal-stats', 'Product-stats','Sales-stats']
t1,t2,t3 = st.tabs(tabs = tab_names)

# first tab
with t1:
    st.subheader('Overal stats of the food :hamburger:...')
    
    # overall layout of first tab
    uc1,uc2 = st.columns(2)
    c1,c2,c3 = st.columns(3)
    st.divider()
    # st.subheader('Some more stats :hamburger:...')
    c4,c5,c6 = st.columns(3)
    c7,c8,c9 = st.columns(3)

    # column uc1 and uc2
    with uc1:
        st.image(image = 'https://t3.ftcdn.net/jpg/05/98/04/96/360_F_598049668_VUcKmKkdc0yZvR2E4s0xSyjeDLnwEXrV.jpg', width=340)   
    with uc2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write('CrownStats gives you the best overall statistics of Burger King using the power of data science! Click on this button to get the overal statistics :smile:')

    
    # column c1, c2 and c3
    with c1:
        st.write(f'Average quantity of the food item = :orange[{ostats.qty_avg} grams]')
        st.write(f'Average calories present in the food item = :orange[{ostats.cal_avg} calories]')
        st.write(f'Average carbs present in the food item = :orange[{ostats.carbs_avg} grams]')
    with c2:
        st.write(f'Average sugar present in the food item = :orange[{ostats.sugar_avg} grams]')
        st.write(f'Average fat present in the food item = :orange[{ostats.fat_avg} grams]')
        st.write(f'Average saturated fat present in the food item = :orange[{ostats.satfat_avg} grams]')
    with c3:
        st.write(f'Average trans fat present in the food item = :orange[{ostats.transfat_avg} grams]')
        st.write(f'Average protein present in the food item = :orange[{ostats.protein_avg} grams]')
        st.write(f'Average sodium present in the food item = :orange[{ostats.sodium_avg} calories]')
    
    st.divider()
    st.write('These stats were produced by using a dataset from kaggle. We dont know if the data is really relevant or not. This is just a prototype of a data app. So please dont rely on these stats :sweat_smile:')

    # column c4 and c5
    with c4:
        st.image(image='https://adsofbrands.net/images/commercial_origin/1/16212530834686.jpeg', width=215)

    with c5:
        st.image(image='https://adsofbrands.net/images/commercial_origin/1/16212533169692.jpeg', width=215)
    with c6:
        st.write(f':orange[25%] of the food items have more than :orange[{ostats.cal75} calories] of energy.')
        st.write(f':orange[25%] of the food items have more than :orange[{ostats.carb75} grams] of carbs.')
        st.write(f':orange[25%] of the food items have more than :orange[{ostats.fat75} grams] of fat.')
        st.write(f':orange[25%] of the food items have more than :orange[{ostats.prot75} grams] of protein.')
        st.write(f':orange[25%] of the food items have more than :orange[{ostats.sod75} grams] of sodium.')

    # column c7, c8 and c9
    with c7:
        st.write(f':orange[50%] of the food items have more than :orange[{ostats.cal50} calories] of energy.')
        st.write(f':orange[50%] of the food items have more than :orange[{ostats.carb50} grams] of carbs.')
        st.write(f':orange[50%] of the food items have more than :orange[{ostats.fat50} grams] of fat.')
        st.write(f':orange[50%] of the food items have more than :orange[{ostats.prot50} grams] of protein.')
        st.write(f':orange[50%] of the food items have more than :orange[{ostats.sod50} grams] of sodium.')
    with c8:
        st.image(image='https://adsofbrands.net/images/commercial_origin/1/16212533169692.jpeg', width=215)
    with c9:
        st.image(image='https://storage.googleapis.com/adforum-media/34635466/ad_34635466_b183e0a0ec5a5cfb_web.jpg', width=215)

# second tab
with t2:

    # overall layout of tab2
    c1,c2, = st.columns(2)

    with c1:
        pname = st.selectbox(label = 'Select food item', options = stats.df3['Product'], key = 'pname')
        st.write('Click on the button given below to generate nutrition info!')
        nt_btn = st.button(label = 'Generate nutrition info', type = 'primary')
    with c2:
        if nt_btn:
            with st.status(label = 'Fetching data... Please wait for a few seconds...'):
                st.write('Searching for the nutrition info...')
                time.sleep(3)
                st.write('Setting the details in right order...')
                time.sleep(1.5)
                st.write('Rounding of the numeric values...')
                time.sleep(1)

    if nt_btn:
        with st.sidebar:
            st.markdown(f"### Here is the nutrition info for {pname}...")
            time.sleep(0.25)
            st.write(f'1. Qty - :orange[{stats.qty(pname)} grams/ml]')
            time.sleep(0.25)
            st.write(f'2. Cal - :orange[{stats.cal(pname)} calories]')
            time.sleep(0.25)
            st.write(f'3. Carbs - :orange[{stats.carb(pname)} grams]')
            time.sleep(0.25)
            st.write(f'4. Fats - :orange[{stats.fat(pname)} grams]')
            time.sleep(0.25)
            st.write(f'5. Sugar - :orange[{stats.sug(pname)} grams]')
            time.sleep(0.25)
            st.write(f'6. Sodium - :orange[{stats.sodi(pname)} grams]')
            time.sleep(0.25)
            st.write(f'7. Protein - :orange[{stats.prot(pname)} grams]')
            time.sleep(0.25)
            st.write(f'8. Trans fat - :orange[{stats.tfat(pname)} grams]')
            time.sleep(0.25)
            st.write(f'9. Saturated fat - :orange[{stats.sfat(pname)} grams]')

            close_sidebar = st.button(label = 'Close sidebar', type = 'primary')
            if close_sidebar:
                st.rerun()
        
        st.write(f'You can see the nutrition info of {pname} on the left sidebar...')
        st.write(f"Important message - Don't rely on this data! The dataset used for creating this data app might not be relevant! This app is just a prototype :smile:")


# third tab
with t3:
    st.subheader('Generate visuals...')
    st.write("Select all the three months, then click on the 'Generate visuals' button to generate visuals of sales of the last six years...")
    c1,c2 = st.columns(2)
    with c1:
        month1 = st.selectbox(label = 'Select the first month', options = splot.months, key='month1')
        month2 = st.selectbox(label = 'Select the second month', options = splot.months, key='month2')
        month3 = st.selectbox(label = 'Select the third month', options = splot.months, key='month3')
    with c2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write("Visuals are being generated using dummy data! It is not based on actual data!")
        visual_btn = st.button(label = "Generate visuals", type = 'primary')
        

        if visual_btn:
            with st.status(label = 'Generating visuals...'):
                time.sleep(2)
                st.write('Generating first image...')
                time.sleep(2)
                st.write('Generating second image...')
                time.sleep(2)
                st.write('Generating third image...')
                time.sleep(0.5)
                st.write('Getting all images ready!')

            clr_vis_btn = st.button(label = 'Clear all the visuals', type = 'primary')

            if clr_vis_btn:
                with st.spinner(text = 'Clearing visuals... Plz wait...'):
                    time.sleep(3)
                    st.rerun()
            
    
    if visual_btn:
        st.markdown("#### Here are your visuals...")
        st.pyplot(splot.generate_plt(month1, month2, month3))




    
