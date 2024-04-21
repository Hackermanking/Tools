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

def get_facebook_cookie(email, password):
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
    else:
        print("Échec de la connexion. Veuillez vérifier vos identifiants.")

if __name__ == "__main__":
    # Description formatée avec des couleurs
    owner_description = f"{M}Owner    : {M}Princi Sz{M}"
    tool_name_description = f"TOOL NAME : {warna}{P}get-cokkies&token{P}{warna}"
    groupe_fb_description = f"GROUPE-FB   : [TERMUX-COMAND]"
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