import streamlit as st

#commentaire==========================================================================================
st.title('Maimouna Demba Ba')
st.subheader('Ingénieur Agronome')
st.write('_____________________________________________________________________________________________')

with st.sidebar:
    st.subheader('📬Contact')
    st.write('EMAIL: mimounassba656@gmail.com')
    st.write('ADRESS: Thiès, Sénégal')

st.subheader('PROFIL')
st.markdown('             ')
st.write('Ingénieur agronome passionné par les domaines de l'agriculture durable et de la sécurité alimentaire. Rigoureux et doté d'une solide expérience de terrain, je maîtrise les techniques de production végétale, l'analyse des sols et la cartographie des zones de culture. Mon expertise inclut également le traitement de données techniques pour optimiser les rendements agricoles.')
st.subheader('PARCOURS ACADEMIQUE')
st.markdown('             ')
st.write('2026–2027 :licence en Sciences et Techniques Agricoles, Alimentaires et Nutritionnelles à l’Université Amadou Mahtar Mbow.')
st.write('2023–2024 : Diplôme en Sciences et Techniques Agricoles et Alimentaires au Lycée Technique Professionnel François Xavier Ndione.')
st.subheader('COMPETENCES')
st.markdown('              ')
st.subheader(' Compétences pratiques agricoles :')
col1, col2 = st.columns(2)
with col1:
    st.write('* Semis des graines')
with col2:
    st.write('* Entretien des cultures')
col1, col2 = st.columns(2)
with col1:
    st.write('* Arrosage des plantes')
with col2:
    st.write('* Récolte des productions agricoles')
st.subheader('Compétences scientifiques :')
col1 , col2 = st.columns(2)
with col1:
    st.write('* Pratiques de microbiologie')
with col2:
    st.write('* Notions en biologie animale et végétale')
st.subheader('Competence en bureautique :')
st.write('* Utilisation de microsoft office')


st.markdown('              ')
st.subheader('PROJET REALISES')
st.subheader(' Activités agricoles ')
st.write('J’ai participé à des activités pratiques , notamment :')
col1, col2, col3  = st.columns(3)
with col1:
    st.write('* Semis des graines')
with col2:
    st.write('* Arrosage et entretien des cultures')
with col3:
    st.write('* Récolte des produits agricoles')
st.write('Ces activités m’ont permis de comprendre les bases des travaux agricoles.')


    
    
    
      
    

    














