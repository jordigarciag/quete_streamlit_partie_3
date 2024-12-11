import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)



# Afffichage du formulaire

authenticator.login()


# Gestion de l'accès

def accueil():
      st.title("Bienvenu sur le contenu réservé aux data analysts en recherche de style")
      

def accueil_photo():
      st.title("Choisis tes chaussures pour ton rendez-vous data")
      


if st.session_state["authentication_status"]:
    with st.sidebar:
        st.write("Bienvenu")
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        selection = option_menu(
                    menu_title=None,
                    options = ["Accueil", "Photos"]
                )
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        
    if selection == "Accueil" : 
        accueil()
        st.image("data_analyst.jpg")
    
    elif selection == "Photos" :
        accueil_photo()
        # ici autre photo

        col1, col2, col3 = st.columns(3)
        with col1:
            #img
            st.image("sport.jpg")
            #text
            st.write("Sport")
        with col2:
            #img
            st.image("chaussures.jpg")
            #text
            st.write("Classe")
        with col3:
            #img
            st.image("bottines.jpg")
            #text
            st.write("Bottines")
    
   

    if st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    if st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')




# Création du menu

#import streamlit as st
# Importation du module
#from streamlit_option_menu import option_menu





# On indique au programme quoi faire en fonction du choix
#if selection == "Accueil":
#    st.write("Bienvenue sur la page d'accueil !")
#elif selection == "Photos":
#    st.write("Bienvenue sur mon album photo")
# ... et ainsi de suite pour les autres pages
















# -------------------------------------------------- 

# Pour runer il faut faire :
# streamlit run quete_streamlit_partie_3.py

# -------------------------------------------------- 
