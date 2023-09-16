import requests
import time

# Fonction pour envoyer le message à un webhook Discord
def envoyer_message_discord(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message envoyé avec succès sur Discord")
    else:
        print("Échec de l'envoi du message sur Discord")

# Fonction principale
def main():
    # Demander à l'utilisateur de saisir son webhook Discord
    webhook_url = input("Veuillez entrer votre webhook Discord : ")

    # Envoyer le message de spam
    while True:
        message = "IS WORK WITH PYTHON join the server for more https://discord.gg/HuATM8aYAt"
        envoyer_message_discord(webhook_url, message)
        time.sleep(0)  # Attendre 1 seconde entre chaque envoi

if __name__ == "__main__":
    main()
