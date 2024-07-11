import streamlit as st
import numpy as np

st.title("Control-I/Q glicemia")

glicemia=st.number_input("Glicemia:\n")
    
if st.button("Misurazione"):
    if glicemia <=40:
        st.write(f"Molto BASSA: {glicemia}")
    elif 45<= glicemia <= 75:
        st.write(f"Glicemia bassa: {glicemia}")
    elif  80<= glicemia <= 175:
        st.write(f"Glicemia stabile: {glicemia}")
    elif glicemia >= 180:
        st.write(f"Glicemia alta: {glicemia}")
    elif 400<= glicemia <=700:
        st.write(f"Molto ALTA: {glicemia}")
    else:
        st.info("valori indecisi")

st.title("Carb(on)")
cho_insert=st.number_input("Carb(on):\n")
ic1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
ic=st.selectbox("IC\n",ic1)
glicemia=st.number_input("Lettura cgm\n",key="seconds")
target_glicemico=110

if st.button("Bolo"):
    if target_glicemico <=80:
            #differenza tra target e glicemia
        tg=target_glicemico-glicemia
        if target_glicemico !=0:
            divi=(tg/target_glicemico)
            insulina=(cho_insert/ic)-divi
            st.write(f"BOLO: {insulina}\n")

        else:
            st.info("error non convertibile")

    elif 85 <= target_glicemico <= 180:
        tg=target_glicemico-glicemia
        if target_glicemico !=0:
            divi=(tg/target_glicemico)
            insulina=(cho_insert/ic)-divi
            st.write(f"BOLO: {insulina}\n")
        
        else:
            st.info("error non convertibile")
    elif 200 <= target_glicemico <= 400:
        tg=target_glicemico-glicemia
        if target_glicemico !=0:
            divi=(tg/target_glicemico)
            insulina=(cho_insert/ic)+divi
            st.write(f"BOLO: {insulina}\n")
        else:
            st.info("error non convertibile")
    else:
        st.write("fine")
else:
    st.warning("\n")

st.title("Grafico")

glicemia_box=[100,170,200,120,80,90,110,95]
if st.button("Grafico"):
   media_cgm=np.mean(glicemia_box)
   
   if media_cgm <=80:
       st.write(f"BASSA {media_cgm}")
   elif 90 <= media_cgm <= 150:
       st.write(f"NORMALE {media_cgm}")
   elif 170<= media_cgm <=200:
       st.write(f"MEDIO {media_cgm}")
   elif 250<= media_cgm<=400:
       st.write(f"MOLTO_ALTA {media_cgm}")
   else:
       st.info("\n")