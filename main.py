from config import *
import datetime, shutil, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import customtkinter

def appli():
    print(
        user_id,
        pwd,
        file_csv,
        admin_1
    )

def backup():
   #Date actuem format année-mois-jour_heure-mins-sec
    current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    #Définition du chemin du backup ainsi que du nom de fichier
    backup = "backup"
    backup_file_name = "backup/"f"{backup}{current_date}.txt"

    os.chdir("..")

    os.makedirs(backup, exist_ok=True)

    #Copie du fichier .csv dans le dossier backup
    #shutil.copy2(file_csv, backup_file_name)
    try:
        shutil.copy2(file_csv, backup_file_name)
        print("Backup terminé !")
    except FileNotFoundError:
        print(f"Erreur : le fichier {file_csv} est introuvable !")
    except Exception as e:
        print(f"Erreur lors du backup : {e}")

    #print(backup_file_name)
    print("Backup terminée !")

def envoie_mail():
    load_dotenv()

    # Récupérer les variables
    mail_exp = os.getenv("MAIL_EXP")
    pwd_exp = os.getenv("PWD_EXP")
    admin = os.getenv("ADMIN")

    

    # Paramètres de l'email
    sujet = "Sujet de l'email"
    corps = "Voici le corps de l'email."

    message = MIMEMultipart()
    message["From"] = mail_exp
    message["To"] = admin
    message["Subject"] = sujet

    # Ajouter du contenue du message
    message.attach(MIMEText(corps, "plain"))

    try:
        # Se connecter au serveur SMTP de Gmail (ou un autre)
        serveur_smtp = smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525)
        serveur_smtp.starttls()  # Sécuriser la connexion

        # Se connecter avec les identifiants
        serveur_smtp.login(mail_exp, pwd_exp)  # Remplace par ton mot de passe

        serveur_smtp.sendmail(mail_exp, admin, message.as_string())

        serveur_smtp.quit()

        print("Email envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")


########################################################################################
#                               Fenetre GUI                                            #
########################################################################################

#app = customtkinter.CTk()
#app.mainloop()

#app.title("my app")
#app.geometry("900x500")

#appli()
backup()
#envoie_mail()

