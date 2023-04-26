import streamlit as st
import moving_loads_modules as ilm

st.title("Bridge Stick Beam Analysis Tool")

tab1, tab2, tab3 = st.tabs(["Bridge definition","Influence lines","Moving loads"])


with tab1: 
    # span span definition input
    st.subheader("Span Definition:")
    number_spans = st.number_input("Number of spans:",min_value=1, step = 1, value=1)

    span_length=[]
    for k in range(number_spans):
        length = st.number_input(f"Span Length {k+1} (m):",value=20.00)
        span_length.append(length)

    # span properties input
    st.subheader("Beam Properties:")
    span_property=[]
    for k in range(number_spans):
        property= st.number_input(f"EI for Span {k+1} (kN/m2):", value=39e6)
        span_property.append(property)

    # supports input
    st.subheader("Supports (0=released, -1=fixed):")
    span_supports=[]
    for k in range(number_spans+1):
        vertical = st.number_input(f"Support {k+1} vertical:",min_value=-1,max_value=0, step = 1)
        rotation = st.number_input(f"Support {k+1} rotation:",min_value=-1,max_value=0, step = 1)
        span_supports.append(vertical)
        span_supports.append(rotation)

    # element type 
    st.subheader("Element Type:")
    st.text("(1- fixed-fixed, 2- fixed-pinned, 3- pinned-fixed, 4- pinned-pinned)")
    etype=[]
    for k in range(number_spans):   
        e_type = st.number_input(f"Element {k+1} type:",min_value=1,max_value=4, step = 1,value=1)
        etype.append(e_type)

with tab2:
    # influence lines input
    st.header("Influence Lines")
    #increment = st.sidebar.number_input("Influence line increment:", min_value=0)
    x_location = st.number_input("Influence line @ x =", min_value=0.00)

###################################################################
with tab3:
    st.header("Design Vehicle") 

    # number of axles input
    st.subheader("Number of axles:")
    number_axles = st.number_input("Number of axles:",min_value=1, step = 1, value=1)

    # axle spacing input
    st.subheader("Axel Spacings:")
    axle_spacings=[]
    for k in range(number_axles-1):
        axles = st.number_input(f"Axle {k+1} spacing (m):",step=0.1, min_value=0.00, value = 1.25)
        axle_spacings.append(axles)

    # axle load input
    st.subheader("Axel Loads:")
    axle_loads=[]
    for k in range(number_axles):
        a_loads = st.number_input(f"Axle {k+1} loads (kN):", min_value=0, value = 120)
        axle_loads.append(a_loads)

    # vehicle position input
    st.subheader("Satic Vehicle Position")
    #increment = st.sidebar.number_input("Influence line increment:", min_value=0)
    x_veh = st.number_input("Front axel position @ x =", step=1.00)

###################################################################

# calculation of influence lines
influence_results = ilm.influence_lines(
    L = span_length, 
    EI = span_property, 
    R = span_supports, 
    etype = etype,
    x_location = x_location
)

# calculation of static moving load
static_moving_results = ilm.static_bridge_analysis(
    L = span_length, 
    EI = span_property, 
    R = span_supports,
    etype = etype, 
    axle_loads = axle_loads, 
    axle_spacings = axle_spacings,
    x_position = x_veh, 
)
with tab3:
    st.header("Static Vehicle Results")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(static_moving_results)


# calculation of envelopes of moving load
envelope_moving_results = ilm.envelope_bridge_analysis(
    L = span_length, 
    EI = span_property, 
    R = span_supports,
    etype = etype, 
    axle_loads = axle_loads, 
    axle_spacings = axle_spacings, 
)
with tab3:
    st.header("Envelopes")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(envelope_moving_results)

# calculation of maximum and minimum of moving load envelope
envelope_moving_results2 = ilm.envelope_bridge_analysis2(
    L = span_length, 
    EI = span_property, 
    R = span_supports,
    etype = etype, 
    axle_loads = axle_loads, 
    axle_spacings = axle_spacings, 
)
with tab3:
    st.header("Maximums/Minimums")
    Mmax, Mmin, Vmax, Vmin = envelope_moving_results2
    f"Mmax = {round(Mmax)} kNm" 
    f"Mmin = {round(Mmin)} kNm"
    f"Vmax= {round(Vmax)} kN" 
    f"Vmin= {round(Vmin)} kN"




###################################################################
with tab2:
    st.pyplot(influence_results)




