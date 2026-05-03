# script simple pour lancer l'app arena d'un coup
import uvicorn
import webbrowser
import threading
import time

def ouvrir_navigateur():
    # attend 1.5 seconde que le serveur demarre et ouvre la page web
    time.sleep(1.5)
    webbrowser.open("http://localhost:8034")

if __name__ == "__main__":
    print("------------------------------------------------------------------")
    print(" ⚔️  Lancement de ARENA Competitive Geography UI on port 8034")
    print(" Ouverture du navigateur sur http://localhost:8034")
    print("------------------------------------------------------------------")
    
    # ouvrir la page automatiquement
    threading.Thread(target=ouvrir_navigateur, daemon=True).start()
    
    # demarrage du serveur web fastapi
    uvicorn.run("arena_competitive_geography.api:app", host="127.0.0.1", port=8034, reload=True)
