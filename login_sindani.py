import streamlit as st
from PIL import Image
import pandas as pd
#st.balloons()
st.set_page_config(page_title="Effectifs", layout="wide")
def page_accueil():
    col2,col1,col3=st.columns(3)
    with col1:
        st.title("TABLEAU DE BORD CELLULE NUMERIQUE HEC-KIN")
    with col2:
        image = Image.open("G:/Mon Drive/RAPPORTS DG ISC KIN/LOGO_HEC.png")
        st.image(image)
    with col3:
        image = Image.open("G:/Mon Drive/RAPPORTS DG ISC KIN/LOGO_ESU.jpeg")
        st.image(image, caption='ESU')
    emoji_list = [
    "🏠 Accueil",
    "👥 Effectifs",
    "💰 Frais",
    "📚 Diplômes et Identification Numérique",
    "🎓 Diplômes",
    "🔢 Cellule Numérique",
    "📋 Listes Déclaratives"]
    # Display the Folium map in Streamlit
# Affichage de la liste
    col3,col2,col1=st.columns(3)
    with col1:
        image1 = Image.open("G:/Mon Drive/RAPPORTS DG ISC KIN/batiment1.jpg")
        st.image(image1, caption='image HEC')
    with col2:
        for item in emoji_list:
            st.markdown(f'<span style="color: #3498db;">{item}</span>', unsafe_allow_html=True)
    with col3:
        image1 = Image.open("G:/Mon Drive/RAPPORTS DG ISC KIN/NUMERISATION.jpeg")
        st.image(image1)
def page_effectifs():
    st.title("Effectifs de nos Etudiants")
    if st.button("Afficher les effectifs"):
        file_path1 = "G:/Mon Drive/RAPPORTS DG ISC KIN/Bases de données sources/BD_ETUDIANTS.xlsx"
        df = pd.read_excel(file_path1, sheet_name="Sheet1")
        st.title("Effectifs")

    # Display crosstab
        col3,col4=st.columns(2)
        with col3:
            st.header("Nombre d'étudiants par Section, Promotion, genre")
            crosstab_result = pd.crosstab(df["Section"],df["Sexe"],margins=True)
            st.dataframe(crosstab_result)
        with col4:
            st.header("Nombre d'étudiants par Section, Promotion, genre")
            crosstab_result = pd.crosstab(df["Section"],df["Sexe"],normalize=True)
            crosstab_result["F"]=crosstab_result["F"]*100
            crosstab_result["M"]=crosstab_result["M"]*100
            st.bar_chart(crosstab_result)
    if st.button("Master Complémentaire"):
        file_path2 = "G:/Mon Drive/RAPPORTS DG ISC KIN/Bases de données sources/BD_MASTER.xlsx"
        df_master = pd.read_excel(file_path2, sheet_name="Sheet1")
        st.title("Effectifs")

    # Display crosstab
        col3,col4=st.columns(2)
        with col3:
            st.header("Nombre d'étudiants En Master")
            crosstab_result = pd.crosstab(df_master["Section"],df_master["Sexe"])
            st.dataframe(crosstab_result)
        with col4:
            st.header("chart")
            crosstab_result = pd.crosstab(df_master["Section"],df_master["Sexe"],normalize=True)
            crosstab_result["F"]=crosstab_result["F"]*100
            crosstab_result["M"]=crosstab_result["M"]*100
            st.bar_chart(crosstab_result)
def page_frais():
    st.title("Frais")

def page_diplomes_identification():
    st.title("Diplômes et Identification Numérique")
    # Ajoutez ici le contenu de la page des diplômes et de l'identification numérique.

def page_diplomes():
    st.title("Diplômes")
    # Ajoutez ici le contenu de la page des diplômes.

def page_cellule_numerique():
    st.title("Cellule Numérique")
    # Ajoutez ici le contenu de la page de la cellule numérique.

def page_listes_declaratives():
    st.title("Listes Déclaratives")
    # Ajoutez ici le contenu de la page des listes déclaratives.
pages = {
    "🏠 Accueil": page_accueil,
    "👥 Effectifs": page_effectifs,
    "💰 Frais": page_frais,
    "📚 Diplômes et Identification Numérique": page_diplomes_identification,
    "🎓 Diplômes": page_diplomes,
    "🔢 Cellule Numérique": page_cellule_numerique,
    "📋 Listes Déclaratives": page_listes_declaratives,
}
st.sidebar.title("RAPPORTS DU CONSEIL NUMERIQUE")
selected_page = st.sidebar.radio("Menu Principal", list(pages.keys()), index=0)
st.sidebar.map(pd.DataFrame({'lat':[-4.32609],'lon':[15.31357]}))
pages[selected_page]()


if __name__ == '__main__':
	main()
