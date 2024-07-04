import re
import csv
import datetime
etudiants = {
    "001": {
        "nom": "Dupont",
        "prenom": "Jean",
        "date_naissance": "01/01/1999",
        "adresse": "12 rue des Étudiants, 75000 Paris",
        "email": "jean.dupont@example.com",
        "telephone": "01 23 45 67 89",
        "section": "maths",
        "niveau_etude": "licencel2"
    },
    "002": {
        "nom": "Martin",
        "prenom": "Sophie",
        "date_naissance": "15/05/2000",
        "adresse": "Tunis",
        "email": "sophie.martin@example.com",
        "telephone": "04 56 78 90 12",
        "section": "tic",
        "niveau_etude": "master"
    },
    "003": {
        "nom": "Nguyen",
        "prenom": "Minh",
        "date_naissance": "10/12/1998",
        "adresse": "Tunis",
        "email": "minh.@example.com",
        "telephone": "06 78 90 12 34",
        "section": "informatique",
        "niveau_etude": "licencel1"
    },
    "004": {
        "nom": "yassin",
        "prenom": "amri",
        "date_naissance": "10/12/1998",
        "adresse": "nabeul",
        "email": "rami@gmail.com",
        "telephone": "06 78 90 12 34",
        "section": "informatique",
        "niveau_etude": "cycle ingénieur"
    },
    "005": {
        "nom": "wakel",
        "prenom": "hiba",
        "date_naissance": "8/12/2003",
        "adresse": "nabeul",
        "email": "hiba@gmail.com",
        "telephone": "06 78 90 12 34",
        "section": "informatique",
        "niveau_etude": "cycle ingénieur"
    },
    "006": {
        "nom": "hammadi",
        "prenom": "islem",
        "date_naissance": "9/12/2002",
        "adresse": "tunis",
        "email": "islem@gmail.com",
        "telephone": "2526795",
        "section": "tic",
        "niveau_etude": "licencel1"
    }
}





def ajouter_etudiant(inscri, nom, prenom, date_naissance, adresse, mail, section, niveau_etude, telephone):
    if inscri in etudiants:
        return "Ce numero existe deja."
    else:
        etudiant = {'inscri': inscri, 'nom': nom, 'prenom': prenom, 'date_naissance': date_naissance, 'adresse': adresse, 'mail': mail, 'section': section, 'niveau_etude': niveau_etude, 'telephone': telephone}
        etudiants[inscri] = etudiant
        return "L'etudiant a ete ajoute."

    enregistrement_etudiant()
def supprimer_etudiant(num_inscription):
    global etudiants
    if num_inscription in etudiants:
        del etudiants[num_inscription]
        return f"L'étudiant ayant le numéro d'inscription {num_inscription} a été supprimé avec succès."
    else:
        return f"Aucun étudiant n'a été supprimé. Le numéro d'inscription {num_inscription} n'existe pas dans la liste des étudiants."

def supprimer_etudiants_niveau(niveau):
    global etudiants
    etudiants_supprimes = 0
    inscriptions = list(etudiants.keys()) # copie de la liste des clés
    for inscri in inscriptions:
        etudiant = etudiants[inscri]
        if etudiant['niveau_etude'] == niveau:
            del etudiants[inscri]
            etudiants_supprimes += 1
    if etudiants_supprimes > 0:
        return (f"{etudiants_supprimes} étudiant(s) du niveau {niveau} ont été supprimés.")
    else:
        return (f"Aucun étudiant n'a été supprimé.")

def supprimer_section2(section):
    global etudiants
    etudiants_supprimes = 0
    inscriptions = list(etudiants.keys())
    for inscri in inscriptions:
        etudiant = etudiants[inscri]
        if etudiant['section'] == section:
            del etudiants[inscri]
            etudiants_supprimes += 1
    if etudiants_supprimes > 0:
        return (f"{etudiants_supprimes} étudiant(s) de la section {section} ont été supprimés.")
    else:
        return (f"Aucun étudiant n'a été supprimé.")

    

def supprimer_etudiants_section_niveau(section, niveau):
    global etudiants
    etudiants_supprimes = 0
    inscriptions = list(etudiants.keys()) # copie de la liste des clés
    for inscri in inscriptions:
        etudiant = etudiants[inscri]
        if etudiant['section'] == section and etudiant['niveau_etude'] == niveau:
            del etudiants[inscri]
            etudiants_supprimes += 1
    if etudiants_supprimes > 0:
        return (f"{etudiants_supprimes} étudiant(s) de la section {section} et du niveau {niveau} ont été supprimés.")
    else:
        return (f"Aucun étudiant n'a été supprimé pour la section {section} et le niveau {niveau}.")
def modifier_mail(num_inscription, nouveau_mail):
    global etudiants
    if num_inscription in etudiants:
        etudiant = etudiants[num_inscription]
        etudiant["email"] = nouveau_mail
        return f"L'adresse e-mail de l'étudiant {etudiant['prenom']} {etudiant['nom']} a été modifiée avec succès. Nouvelle adresse : {nouveau_mail}"
    else:
        return f"Le numéro d'inscription {num_inscription} n'existe pas dans la liste des étudiants."
def modifier_telephone(num_inscription, nouveau_telephone):
    global etudiants
    if num_inscription in etudiants:
        etudiant = etudiants[num_inscription]
        etudiant["telephone"] = nouveau_telephone
        return f"Le numéro de téléphone de l'étudiant {etudiant['nom']} {etudiant['prenom']} a été modifié : {nouveau_telephone}."
    else:
       return f"Le numéro d'inscription {num_inscription} n'existe pas dans la liste des étudiants. Aucun téléphone n'a été modifié."
def modifier_adresse(num_inscription, nouvelle_adresse):
    global etudiants
    if num_inscription in etudiants:
        etudiant = etudiants[num_inscription]
        etudiant["adresse"] = nouvelle_adresse
        return f"L'adresse de l'étudiant {etudiant['nom']} {etudiant['prenom']} a été modifiée : {nouvelle_adresse}."
    else:
        return f"Le numéro d'inscription {num_inscription} n'existe pas dans la liste des étudiants. Aucune adresse n'a été modifiée."

#gestion de livres
livres = {
    "10": {
        "titre": "Les Misérables",
        "auteur": "Victor Hugo",
        "annee_edition": 1862,
        "nombre_exemplaires": 5
    },
    "20": {
        "titre": "Le Rouge et le Noir",
        "auteur": "Stendhal",
        "annee_edition": 1830,
        "nombre_exemplaires": 3
    },
    "30": {
        "titre": "Germinal",
        "auteur": "Emile Zola",
        "annee_edition": 1885,
        "nombre_exemplaires": 2
    }
}


#livres 

def ajouter_livre(reference, titre, nom_auteur, prenom_auteur, annee_edition, nb_exemplaires):
    if reference in livres:
        return("Cette référence existe déjà.")
    else:
        auteur = {"nom": nom_auteur, "prenom": prenom_auteur}
        livre = {"titre": titre, "auteur": auteur, "annee_edition": annee_edition, "nb_exemplaires": nb_exemplaires}
        livres[reference] = livre
        return("Le livre a été ajouté.")
    

def supprimer_livre(reference):
    global livres
    if reference in livres:
        del livres[reference]
        return f"Le livre ayant la référence {reference} a été supprimé avec succès."

    else:
        return f"Aucun livre n'a été supprimé. La référence {reference} n'existe pas dans la liste des livres."

def supprimer_livres_auteur(auteur):
    global livres
    livres_supprimes = 0
    refs_a_supprimer = []

    for ref_livre, livre in livres.items():
        if livre["auteur"].lower() == auteur.lower():
            refs_a_supprimer.append(ref_livre)

    for ref_livre in refs_a_supprimer:
        del livres[ref_livre]
        livres_supprimes += 1
    
    if livres_supprimes > 0:
        return f"{livres_supprimes} livres de {auteur} ont été supprimés avec succès."
    else:
        return f"Aucun livre de {auteur} n'a été trouvé dans la liste des livres."

def supprimer_livres_par_annee(annee):
    global livres
    livres_a_supprimer = [ref_livre for ref_livre, livre in livres.items() if livre["annee_edition"] == annee]
    if not livres_a_supprimer:
        return f"Aucun livre n'a été supprimé. Aucun livre n'a été publié en {annee}."
    for ref_livre in livres_a_supprimer:
        del livres[ref_livre]
    return f"Tous les livres publiés en {annee} ont été supprimés avec succès."
  
def modifier_nombre_exemplaires(ref_livre, nouveau_nb_exemplaires):
    global livres
    
    if ref_livre in livres:
        livres[ref_livre]["nombre_exemplaires"] = nouveau_nb_exemplaires
        return f"Le nombre d'exemplaires du livre {livres[ref_livre]['titre']} a été modifié avec succès. Le nouveau nombre d'exemplaires est {nouveau_nb_exemplaires}."
    else:
        return f"Aucun livre avec la référence {ref_livre} n'a été trouvé dans la liste des livre"
#emprunts
emprunts = {
    "1": {
        'num_inscription': '123',
        'ref_livre': '10',
        'date_emprunt': '2022-05-02',
        'date_retour': '2022-05-09',
           },
    "2": {
        'num_inscription': '456',
        'ref_livre': '20',
        'date_emprunt': '2022-04-15',
        'date_retour': '2022-04-22',
      
    }
}


from datetime import datetime


def ajouter_emprunt(num_inscription, ref_livre):
    global livres, emprunts, etudiants
    
    if num_inscription not in etudiants:
        return "Erreur : numéro d'inscription invalide"
    
    if ref_livre not in livres:
        return "Erreur : référence de livre invalide"
    
    if livres[ref_livre]["nombre_exemplaires"] == 0:
        return "Erreur : aucun exemplaire disponible"
    
    date_emprunt = datetime.now().strftime("%Y-%m-%d")
    livres[ref_livre]["nombre_exemplaires"] -= 1
    
    emprunts[num_inscription] = {
        "num_inscription": num_inscription,
        "ref_livre": ref_livre,
        "date_emprunt": date_emprunt,
        "date_retour": None
    }
        

    
    return "L'emprunt a été ajouté avec succès."

def retour_livre(num_inscription):
    global livres, emprunts
    
    emprunt_trouve = False
    
    for emprunt in emprunts.values():
        if emprunt["num_inscription"] == num_inscription:
            emprunt_trouve = True
            ref_livre = emprunt["ref_livre"]
            livres[ref_livre]["nombre_exemplaires"] += 1
            date_retour = datetime.now().strftime("%Y-%m-%d")
            emprunt["date_retour"] = date_retour
    
    if not emprunt_trouve:
        return "Erreur : emprunt introuvable pour ce numéro d'inscription"
    
    return "Livre retourné avec succès"

    
    return "Livre retourné avec succès"
def modifier_date_emprunt(num_inscription, nouvelle_date):
    global emprunts
    
    for emprunt in emprunts.values():
        if emprunt["num_inscription"] == num_inscription:
            emprunt["date_emprunt"] = nouvelle_date
            return "La date d'emprunt a été modifiée"

    return "Erreur : emprunt introuvable"

def modifier_date_retour(num_inscription, nouvelle_date_retour):
    global emprunts
    
    for emprunt in emprunts.values():
        if emprunt["num_inscription"] == num_inscription:
            emprunt["date_retour"] = nouvelle_date_retour
            return "La date de retour a été modifiée avec succès."

    return "Erreur : emprunt introuvable"

def enregistrement_etudiant():
        with open('etudi.csv', 'w', newline='') as f:
          writer = csv.writer(f, delimiter=';')
          for key, value in etudiants.items():
              ch = [key] + list(value.values())
              writer.writerow(ch)


def enregistrement_livre():
    with open('livress.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for key in livres.keys():
            ch = [key] + list(livres[key].values())
            writer.writerow(ch)

            



def enregistrement_emprunts():
    with open('emprunts.csv', 'a', newline='') as f:
        pass  # ajouter cette ligne
        writer = csv.writer(f, delimiter=';')
        for key in emprunts.keys():
            ch = [key] + list(emprunts[key].values())
            writer.writerow(ch)

def supprimer_emprunt(num_inscription, ref_livre):
      for emprunt_id in emprunts:
        emprunt = emprunts[emprunt_id]
        if emprunt['num_inscription'] == num_inscription and emprunt['ref_livre'] == ref_livre:
            del emprunts[emprunt_id]
            return True
        return False
def is_valid_email(email):
      pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
      match = re.match(pattern, email)
      return bool(match)
def  recuperation_etudiants(): 
    etudiants={}
    with open ('etudi.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=";")
        for row in csv_file:
            etudiants[row[0]]=row[1:]
        
def  recuperation_livres(): 
    livres={}
    with open ('livress.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=";")
        for row in csv_file:
            livres[row[0]]=row[1:]
       
def  recuperation_emprunrs(): 
    emprunts={}
    with open ('emptre.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=";")
        for row in csv_file:
            emprunts[row[0]]=row[1:]
       

     



