import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("DASHBOARD")
st.title("Control-IQ")
glicemia=st.number_input("Glicemia:\n")
basale=[0,0.10,0.40,0.80,1,1.5,2,2.5,3]
if st.button("Misurazione"):
    if glicemia <=40:
        st.write(f"Molto BASSA: {glicemia}")
        if any(0<= b <=0.20 for b in basale):
            st.write(f"B rosso")
        else:
            st.write("Sospesa")

    elif 45<= glicemia <= 75:
        st.write(f"Glicemia bassa: {glicemia}")
        if any(0.30<= b <= 0.40 for b in basale):
            st.write(f"B rosso")
        else:
            st.write("sospesa")
    elif  80<= glicemia <= 175:
        st.write(f"Glicemia stabile: {glicemia}")
        if any(0.8<=b<=1 for b in basale):
            st.write(f"B normale")
        else:
            st.write("Aumento costante")
    elif glicemia >= 180:
        st.write(f"Glicemia alta: {glicemia}")
        if any(1.5<=b<=2 for b in basale):
            st.write(f"B blu Aumento")
        else:
            st.write("Aumento basale 1x")
    elif 400<= glicemia <=700:
        st.write(f"Molto ALTA: {glicemia}")
        if any(2.5<=b<=3 for b in basale):
            st.write(f"B blu_scuro")
        else:
            st.write("Aumento basale 2x")
    else:
        st.info("valori indecisi")

st.title("Carb(on)")
cho_insert=st.number_input("Carb(on):\n")
ic1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
ic=st.selectbox("IC\n",ic1)
glicemia=st.number_input("Lettura cgm\n",key="seconds")
target_glicemico=110
basale1=[0,0.10,0.40,0.80,1,1.5,2,2.5,3]
if st.button("Bolo"):
    if glicemia <=40:
        tg=target_glicemico-glicemia
        if target_glicemico !=0:
            divi=(tg/target_glicemico)
            insulina=(cho_insert/ic)-divi
            st.write(f"BOLO: {insulina}\n")

            if any(b<=0 for b in basale1):
                st.write(f"B rosso")
            else:
                st.write("Sospesa")
        else:
            st.write("error")
    if 45<=glicemia <=75:
            #differenza tra target e glicemia
        tg=target_glicemico-glicemia
        if target_glicemico !=0:
            divi=(tg/target_glicemico)
            insulina=(cho_insert/ic)-divi
            st.write(f"BOLO: {insulina}\n")

            if any(0<= b <=0.30 for b in basale1):
                st.write(f"B rosso")
            else:
                st.write("Sospesa")

        else:
            st.info("error non convertibile")

    elif 85 <= glicemia <= 180:
        tg=target_glicemico-glicemia
        if target_glicemico !=0:
            divi=(tg/target_glicemico)
            insulina=(cho_insert/ic)-divi
            st.write(f"BOLO: {insulina}\n")

            if any(0.4<=b<=1.5 for b in basale1):
                st.write(f"B Normale")
            else:
                st.write("Aumento costante")
        
        else:
            st.info("error non convertibile")
    elif 200 <= glicemia <= 400:
        tg=target_glicemico-glicemia
        if target_glicemico !=0:
            divi=(tg/target_glicemico)
            insulina=(cho_insert/ic)+divi
            st.write(f"BOLO: {insulina}\n")

            if any(2<=b<=3 for b in basale1):
                st.write(f"B blu_scuro")
            else:
                st.write("Aumento basale 2x")
        else:
            st.info("error non convertibile")
    else:
        st.write("fine")
else:
    st.write("\n")

st.title("Grafico")
CGM_00=st.number_input("Lettura 00\n")
CGM_04=st.number_input("Lettura 04\n")
CGM_08=st.number_input("Lettura 08\n")
CGM_10=st.number_input("Lettura 10\n")
CGM_13=st.number_input("Lettura 13\n")
CGM_16=st.number_input("Lettura 16\n")
CGM_20=st.number_input("Lettura 20\n")
CGM_22=st.number_input("Lettura 22\n")
glicemia_box={'CGM_00':CGM_00,'CGM_04':CGM_04,'CGM_08':CGM_08,'CGM_10':CGM_10,'CGM_13':CGM_13,'CGM_16':CGM_16,'CGM_20':CGM_20,'CGM_22':CGM_22}
CGM=st.multiselect("Letture\n",list(glicemia_box.keys()))
if st.button("Grafico"):
   if CGM:
    valori=[glicemia_box[item] for item in CGM]
    orari = [item.split('_')[1] for item in CGM]
    media_cgm=np.mean(valori)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(orari, valori, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Orario')
    ax.set_ylabel('Glicemia')
    ax.set_title('Andamento della glicemia')
    st.pyplot(fig)

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

st.title("Carb Total")
Carb_08=st.number_input("Carb 08\n")
Carb_10=st.number_input("Carb 10\n")
Carb_13=st.number_input("Carb 13\n")
Carb_16=st.number_input("Carb 16\n")
Carb_20=st.number_input("Carb 20\n")
Carb_22=st.number_input("Carb 22\n")

carbtotal={'Carb_08':Carb_08,'Carb_10':Carb_10,'Carb_13':Carb_13,'Carb_16':Carb_16,'Carb_20':Carb_20,'Carb_22':Carb_22}
if st.button("Carb giornalieri"):
    if carbtotal:
        valori_sum=[carbtotal[item] for item in carbtotal]
        carb_sum=np.sum(valori_sum)
        st.write(f"Carb totali {carb_sum}")
        valori_media=[carbtotal[item] for item in carbtotal]
        carb_media=np.mean(valori_media)
        st.write(f"Media Carb giornaliera {carb_media}")
    else:
        st.write("\n")
else:
    st.write("\n")

st.title("Totale insulina")
Bolo_08=st.number_input("Bolo_08\n")
Bolo_10=st.number_input("Bolo_10\n")
Bolo_13=st.number_input("Bolo_13\n")
Bolo_16=st.number_input("Bolo_16\n")
Bolo_20=st.number_input("Bolo_20\n")
Bolo_22=st.number_input("Bolo_22\n")

Bolo_tot={'Bolo_08':Bolo_08,'Bolo_10':Bolo_10,'Bolo_13':Bolo_13,'Bolo_16':Bolo_16,'Bolo_20':Bolo_20,'Bolo_22':Bolo_22}

if st.button("Calcolo insulina giornaliera"):
    if Bolo_tot:
        valori_Bolo_sum=[Bolo_tot[item] for item in Bolo_tot]
        bolo_sum=np.sum(valori_Bolo_sum)
        st.write(f"Insulina totale {bolo_sum}")
        valori_bolo_media=[Bolo_tot[item] for item in Bolo_tot]
        Bolo_media=np.mean(valori_bolo_media)
        st.write(f"Media giornaliera di insulina {Bolo_media}")
    else:
        st.info("\n")
else:
    st.write("\n")

st.title("Bolo Correttivo")

misurazione=st.number_input("Glicemia", min_value=40, max_value=800)
fsi_box= [70]
fsi_select= st.selectbox("FSI", fsi_box)
target_micro=120

if st.button("Bolo Rapido"):

    if misurazione >= 30:

        calcolo_bolo= (misurazione - target_micro) / fsi_select
        st.write(f"Bolo Rapido (ON)\n{calcolo_bolo:.2f}")
    else:
        st.write("error")
else:
    st.write("\n")
