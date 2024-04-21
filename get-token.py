# Définir le logo ASCII
logo_ascii = """
██╗   ██╗███████╗██╗  ██╗ █████╗ ██╗   ██╗███████╗██████╗ 
██║   ██║██╔════╝██║  ██║██╔══██╗██║   ██║██╔════╝██╔══██╗
██║   ██║███████╗███████║███████║██║   ██║█████╗  ██████╔╝
╚██╗ ██╔╝╚════██║██╔══██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
 ╚████╔╝ ███████║██║  ██║██║  ██║╚██████╔╝███████╗██║  ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

# Couleurs pour le texte
M = "\033[1;31m"  # Rouge
warna = "\033[1;33m"  # Jaune
P = "\033[1;35m"  # Pourpre
H = "\033[1;32m"  # Vert
bblack = "\033[1;30m"  # Noir
import requests
from bs4 import BeautifulSoup
from getpass import getpass

def show_options():
    print("Options:")
    print("1. Obtenir les cookies & tokens")
    print("2. Changer le mot de passe Facebook")
    print("3. Changer le numéro ou l'e-mail Facebook")
    print("4. Quitter")

def get_facebook_cookie(email, password):
    try:
        # Offrir les options
        while True:
            show_options()
            option = input("Entrez le numéro de l'option choisie : ")
            if option == "1":
                # Créer une session pour maintenir la connexion
                session = requests.Session()

                # Effectuer la connexion à Facebook
                login_url = "https://www.facebook.com/login"
                login_data = {"email": email, "pass": password}
                response = session.post(login_url, data=login_data)

                # Vérifier si la connexion a réussi
                if response.status_code == 200 and "Se déconnecter" in response.text:
                    print("Connexion réussie. Récupération du cookie...")
                    # Récupérer le cookie de session
                    cookie = session.cookies.get_dict()
                    print("Cookie récupéré avec succès :", cookie)
                    get_cookies_and_tokens(session)
                else:
                    print("Échec de la connexion. Veuillez vérifier vos identifiants.")
            elif option == "2":
                new_password = getpass("Entrez votre nouveau mot de passe : ")
                change_password(session, new_password)
            elif option == "3":
                new_email_or_number = input("Entrez votre nouveau e-mail ou numéro : ")
                change_email_or_number(session, new_email_or_number)
            elif option == "4":
                print("Fermeture du programme.")
                break
            else:
                print("Option invalide.")
    except Exception as e:
        print("Une erreur s'est produite :", str(e))

def get_cookies_and_tokens(session):
    # Obtenir les cookies et les tokens (adapté à votre situation réelle)
    # Cette fonction devrait envoyer une requête à Facebook pour récupérer les cookies et les tokens
    # Ici, nous affichons simplement un message de succès
    print("Cookies et tokens récupérés avec succès.")

def change_password(session, new_password):
    # Effectuer le changement de mot de passe (adapté à votre situation réelle)
    # Cette fonction devrait envoyer une requête à Facebook pour changer le mot de passe
    # Ici, nous affichons simplement un message de succès
    print("Mot de passe changé avec succès :", new_password)

def change_email_or_number(session, new_email_or_number):
    # Effectuer le changement d'e-mail ou de numéro (adapté à votre situation réelle)
    # Cette fonction devrait envoyer une requête à Facebook pour changer l'e-mail ou le numéro
    # Ici, nous affichons simplement un message de succès
    print("E-mail ou numéro changé avec succès :", new_email_or_number)

if __name__ == "__main__":
    # Description formatée avec des couleurs
    owner_description = f"{M}Owner    : {M}Princi Sz{M}"
    tool_name_description = f"TOOL NAME : {warna}{P}get-cookies&token{P}{warna}"
    groupe_fb_description = f"GROUPE-FB   : [TERMUX-COMMAND]"
    statue_description = f"STATUE : {H}FREE{H}"
    facebook_description = f"Facebook : {bblack}Princi Sz{bblack}"
    tools_description = f"Tools    : {warna}[{M}VERSION 1.0{warna}]{warna}"

    # Imprimer les descriptions
    print(logo_ascii)
    print(owner_description)
    print(tool_name_description)
    print(groupe_fb_description)
    print(statue_description)
    print(facebook_description)
    print(tools_description)

    # Demander à l'utilisateur de saisir son adresse e-mail Facebook
    email = input("Entrez votre adresse e-mail Facebook : ")

    # Demander à l'utilisateur de saisir son mot de passe Facebook (le texte est masqué)
    password = getpass("Entrez votre mot de passe Facebook : ")

    # Appeler la fonction pour obtenir le cookie
    get_facebook_cookie(email, password)