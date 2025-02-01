from config import *
import datetime, shutil, os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    shutil.copy2(file_csv, backup_file_name)
    #print(backup_file_name)
    print("Backup terminée !")

def envoie_mail():
    #Récupération des variables d'envrionnements
    mail_exp = os.getenv("MAIL_EXP")
    pwd_exp = os.getenv("PWD_EXP")
    admin = os.getenv("ADMIN")

    print("MAIL_EXP:", os.getenv("MAIL_EXP"))
    print("PWD_EXP:", os.getenv("PWD_EXP"))
    print("ADMIN:", os.getenv("ADMIN"))

    # Paramètres de l'email
    sujet = "Sujet de l'email"
    corps = "Voici le corps de l'email."

    # Créer le message MIME
    message = MIMEMultipart()
    message["From"] = mail_exp
    message["To"] = admin
    message["Subject"] = sujet

    # Ajouter le corps du message
    message.attach(MIMEText(corps, "plain"))

    try:
        # Se connecter au serveur SMTP de Gmail (ou un autre)
        serveur_smtp = smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525)
        serveur_smtp.starttls()  # Sécuriser la connexion

        # Se connecter avec les identifiants
        serveur_smtp.login(mail_exp, pwd_exp)  # Remplace par ton mot de passe

        # Envoyer l'email
        serveur_smtp.sendmail(mail_exp, admin, message.as_string())

        # Fermer la connexion SMTP
        serveur_smtp.quit()

        print("Email envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

#appli()
#backup()
envoie_mail()