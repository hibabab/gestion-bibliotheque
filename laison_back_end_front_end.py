
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from ui_interface import Ui_MainWindow 
import biblio 
from PyQt5.QtWidgets import QMessageBox
import datetime





class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.main_win)


        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

        self.ui.actionajouter_etudiants.triggered.connect(self.show_ajouter_etudiant)
        self.ui.actionSuppression_un_tudiants_donn_e.triggered.connect(self.show_Suppression_etudiant)
        self.ui.actionSuppression_des_etudiants_d_une_section_donn_e.triggered.connect(self.show_Suppression_etudiant_section)
        self.ui.actionSuppression_des_etudiants_d_un_niveau_donn_e.triggered.connect(self.show_Suppression_etudiant_niveau)
        self.ui.actionSuppression_des_etudiants_d_une_section_et_un_niveau_donn_e.triggered.connect(self.show_Suppression_etudiant_section_niveau)
        self.ui.actionmodifier_t_l_phone.triggered.connect(self.show_modifier_phone)
        self.ui.actionmail.triggered.connect(self.show_modifier_mail)
        self.ui.actionAdresse.triggered.connect(self.show_modifier_adresse)
        self.ui.actioncontenu_du_dictionnaire_tudaints.triggered.connect(self.show_affiche_contenu)
        self.ui.actionrecherche_par_num_inscription.triggered.connect(self.show_recherche_inscription)
        self.ui.actionrecherche_par_niveau.triggered.connect(self.show_recherche_niveau)
        self.ui.actionrecherche_par_section.triggered.connect(self.show_recherche_section)
        self.ui.actionrecherche_par_section_et_niveau.triggered.connect(self.show_recherche_section_niveau)
        self.ui.actionajouter_un_nouvel_livre.triggered.connect (self.show_ajouter_livre)
        self.ui.actionsuppression_livre_donn.triggered.connect(self.show_supprimer_livre)
        self.ui.actionsuppression_livre_d_un_auteur_donn.triggered.connect(self.show_supprimer_livre_auteur)
        self.ui.actionsuppression_livre_d_une_ann_e_donn_e.triggered.connect(self.show_supprimer_livre_annee)
        self.ui.actionmodifier_nombre_d_exemplaire_d_un_livre. triggered.connect(self.show_modifier_exemplaire)
        self.ui.actioncontenu_de_dictionnaire_livre.triggered.connect(self.show_affiche_contenu_livre)
        self.ui.actionajouter_un_nouvel_emprunt.triggered.connect(self.show_ajout_emprunt)
        self.ui.actionconteenu_de_dictionnaire_emprunt.triggered.connect(self.show_contenu_emprunt)
        self.ui.actionretour_d_un_emprunt.triggered.connect(self.show_retour)
        self.ui.actiondate_emprunt.triggered.connect(self.show_modi_date)
        self.ui.actiondate_retour.triggered.connect(self.show_modi_retour)
        self.ui.actionenragistrement.triggered.connect(self.show_enregistrement)
        self.ui.actionrecup_raytion.triggered.connect(self.show_recuperation)
        self.ui.actionrecherche_par_r_ference.triggered.connect(self.show_affiche_ref)
        self.ui.actionrecherche_par_titre.triggered.connect(self.show_affiche_titre)
        self.ui.actionrecherhce_livre_par_ann_e_dition_donn_e.triggered.connect(self.show_affiche_anne)
        self.ui.actionrecherche_livre_d_un_auteur_donn.triggered.connect(self.show_affiche_auteur)
        self.ui.actionrecherche_et_affichage_des_livres_par_ordre_alphab_tique.triggered.connect(self.show_affiche_orde)
        self.ui.actionrecherche_emprunts_par_livre.triggered.connect(self.show_affiche_livre_em)
        self.ui.actionrecherche_emprunts_par_etudiant.triggered.connect(self.show_affiche1)
        self.ui.actionrecherche_livre_emprent_s_a_une_date_donn_e.triggered.connect(self.show_affiche2)
        self.ui.actionrecherche_livre_retourn_s_a_une_date_donn_e.triggered.connect(self.show_affiche3)
        self.ui.actionrecherche_livre_emprent_s_a_entre_deux_date_donn_e.triggered.connect(self.show_affiche4)
        self.ui.actionrecherche_livre_retourn_s_entre_deux_dates_donn_es.triggered.connect(self.show_affiche5)
        self.ui.actionsupprimer_d_un_emprunt.triggered.connect(self.show_affiche6)
        

    
     

        
        

        self.ui.ajouter.clicked.connect(self.ajouter)
        self.ui.supp_etudi.clicked.connect(self.supprimer_inscri)
        self.ui.supp_niveau_2.clicked.connect(self.supprimer_niveau)
        self.ui.affiche_contenu.clicked.connect(self.afficher_tous_les_etudiants)
        self.ui.supp_section_2.clicked.connect(self.supprimer_section)
        self.ui.supp_section_niveau.clicked.connect(self.supprimer_niveau_section)
        self.ui.modi_phone.clicked.connect(self.modi_phone)
        self.ui.modi_mail.clicked.connect(self. modi_mail)
        self.ui.modi_adresse.clicked.connect(self.modi_adresse)
        self.ui.recherche_inscri.clicked.connect(self. rechercher_par_inscription)
        self.ui.recherche_niveau_2.clicked.connect(self. rechercher_par_niveau)
        self.ui.recherche_sec.clicked.connect(self.rechercher_par_section)
        self.ui.recherchesection_niveau.clicked.connect(self. rechercher_par_section_et_niveau)
        self.ui.ajouter_livre.clicked.connect(self.ajouter_livre)
        self.ui.suppremier_ref.clicked.connect(self.supprimer_livre1)
        self.ui.supprimer_auteur.clicked.connect(self.supprimer_auteur)
        self.ui.supp_annee.clicked.connect(self.supprimer_annee)
        self.ui.modi_exmplaire.clicked.connect(self.modifier_exemplaire)
        self.ui.affiche_contenu_livres.clicked.connect(self.afficher_tous_les_livres)
        self.ui.ajout_emprunt_2.clicked.connect(self.ajout_empreinte)
        self.ui.affiche_emprunt.clicked.connect(self.affiche_emp)
        self.ui.retour.clicked.connect(self.retour_livre)
        self.ui.enregistre_etud.clicked.connect(self.enregistrement_etudiant)
        self.ui.enregistre_livre.clicked.connect(self.enregistrement_livres)
        self.ui.enregistre_emprunt.clicked.connect(self.enregistrement_emprunts)
        self.ui.affiche_reff.clicked.connect(self.afficher_livre_ref)
        self.ui.affiche_titre.clicked.connect(self.afficher_livre_titre)
        self.ui.aff_anne.clicked.connect(self.afficher_livre_annee)
        self.ui.affiche_atteur.clicked.connect(self.afficher_livre_auteur)
        self.ui.affiche_alpha.clicked.connect(self.afficher_livres_ordre_alphabetique)   
        self.ui.modi_retour.clicked.connect(self.modi_retour)    
        self.ui.modifier_date_2.clicked.connect(self.modi_date)                            
        self.ui.affiche_livre.clicked.connect(self.afficher_emprunts_livre)
        self.ui.supprime_em.clicked.connect(self.suprimer)
        self.ui.afficher_em.clicked.connect(self.recherche_livre_par_date_emprunt)
        self.ui.ret.clicked.connect(self.recherche_livre_par_date_retour)
        self.ui.aff4.clicked.connect(self.recherche_livre_emprunte_entre_dates)
        self.ui.affiche_ret.clicked.connect(self.recherche_livre_retour_entre_dates)
        self.ui.affich.clicked.connect(self.recherche_par_etudiant)
        self.ui.recupration1.clicked.connect(self.recuperer_etudiants)
        self.ui.rcupration2.clicked.connect(self.recuperer_livres)
        self.ui.recuperation3.clicked.connect(self.recuperer_emprunts)
         
        
   

    def show(self):
        self.main_win.show()

    def show_ajouter_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Ajouter_etudiant)
    def show_Suppression_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.supp_inscri)
    def show_Suppression_etudiant_section(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.supp_section)
    def show_Suppression_etudiant_niveau(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.supp_niveau)
    def show_Suppression_etudiant_section_niveau(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.supp_niveau_section)
    def show_modifier_phone(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.modifier_phone)
    def show_modifier_mail(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.modifier_mail)
    def show_modifier_adresse(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.modifier_adresse)
    def show_affiche_contenu(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_contenu_2)
    def show_recherche_inscription(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.recherche_numero)
    def show_recherche_niveau(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.recherche_niveau)
    def show_recherche_section(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.recherche_section)
    def show_recherche_section_niveau(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.recherche_niveau_section)
    def show_ajouter_livre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ajoute_livre)
    def  show_supprimer_livre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.suppression_reference)
    def show_supprimer_livre_auteur(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.supp_auter)
    def show_supprimer_livre_annee(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.suppression_annee)
    def show_modifier_exemplaire(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.modifier_exemplaire)
    def show_affiche_contenu_livre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.contenu_livre)

    def show_ajout_emprunt(self):
          self.ui.stackedWidget.setCurrentWidget(self.ui.ajout_emprunt_3)

    def show_contenu_emprunt(self):
          self.ui.stackedWidget.setCurrentWidget(self.ui.contenu_emprunt)
    def show_retour(self):
          self.ui.stackedWidget.setCurrentWidget(self.ui.retour_emprente)
    def show_modi_date(self):
          self.ui.stackedWidget.setCurrentWidget(self.ui.modifier_date)
    def show_modi_retour(self):
          self.ui.stackedWidget.setCurrentWidget(self.ui.modi_retor)
    def show_enregistrement(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.enregistrement)
    def show_recuperation(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.rcupration)

    def show_affiche_ref(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ref_affiche)
    def show_affiche_auteur(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_auteur)
    def show_affiche_titre(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.titre_affiche)
    def show_affiche_anne(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.anne_affiche)
    def show_affiche_orde(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.alpha_affiche)
    def show_affiche_livre_em(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_em)
    def show_affiche1(self): 
         self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_em_etudiant) 
    def show_affiche2(self): 
         self.ui.stackedWidget.setCurrentWidget(self.ui.date_em)    
    def show_affiche3(self): 
         self.ui.stackedWidget.setCurrentWidget(self.ui.date_retour)    
    def show_affiche4(self): 
         self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_entre2_em)    
    def show_affiche5(self): 
         self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_entre2_ret)    
    def show_affiche6(self): 
         self.ui.stackedWidget.setCurrentWidget(self.ui.supp_em)    
      
          






    def rechercher_par_inscription(self):
        num_inscription = self.ui.inscri_recherche.text()
        if num_inscription in biblio.etudiants:
           etudiant = biblio.etudiants[num_inscription]
           texte = f"{etudiant['nom']} {etudiant['prenom']}, né(e) le {etudiant['date_naissance']}, adresse : {etudiant['adresse']}, mail : {etudiant['email']}, téléphone : {etudiant['telephone']}, section : {etudiant['section']}, niveau : {etudiant['niveau_etude']}"
           self.ui.res11.setText(texte)
        else:
          self.ui.res11.setText("Aucun étudiant trouvé avec ce numéro d'inscription.")

    
    def ajout_empreinte(self):
        inscri_em=self.ui.inscri_emprunt.text()
        ref_em=self.ui.ref_emprunt.text()
        res=biblio. ajouter_emprunt(inscri_em, ref_em)
        QMessageBox.about(None,"massage",res)
        #self.affiche_emp()
    def affiche_emp(self):
        text = ""
        for num_emp, emp in biblio.emprunts.items():
            text += f"Numéro d'emprunt: {num_emp}\n"
            text += f"Référence du livre: {emp['ref_livre']}\n"
            text += f"Date d'emprunt: {emp['date_emprunt']}\n"
            text += f"Date de retour: {emp['date_retour']}\n"
        self.ui.res_contenu_emprunt.setText(text)
        
    def retour_livre(self):
        inscri1 = self.ui.inscri_retour.text()
        res_retour=biblio.retour_livre(inscri1)
        QMessageBox.about(None,"massage",res_retour)
    
    
    def ajouter(self):
    # Get the input values from the UI
       inscri1 = self.ui.inscri.text()
       prenom1 = self.ui.prenom.text()
       date1 = self.ui.date.text()
       adresse1 = self.ui.adresse.text()
       mail1 = self.ui.mail.text()
       section1 = self.ui.section.currentText()
       niveau1 = self.ui.niveau.currentText()
       phone1 = self.ui.phone1.text()
       nom1=self.ui.nom.text()
       #if not inscri1 or not nom1 or not prenom1 or not date1 or not phone1 or not mail1 or not adresse1:
         # QMessageBox.about(None, "Message", "Veuillez remplir les champs obligatoires (*)")
          #return
      # if not inscri1.isnumeric() or not phone1.isnumeric() :
            #res_ajoute=("Erreur : La référence, l'année et le nombre d'exemplaires doivent être des nombres entiers.")
            #QMessageBox.about(None,"massage",res_ajoute)
            #return
       result = biblio.ajouter_etudiant(inscri1, nom1, prenom1, date1, adresse1, mail1, section1, niveau1, phone1)
       QMessageBox.about(None,"massage",result)

    def supprimer_inscri(self):
         num=self.ui.inscri1.text()
         if not num:
           QMessageBox.about(None, "Message", "Veuillez remplir les champs obligatoires (*)")
           return
         if not num.isnumeric():
            message1="Erreur : Veuillez saisir un numéro d'inscription valide."
            QMessageBox.about(None,"massage",message1)
            return
    
         #self.ui.res12.setText(biblio.supprimer_etudiant(num))
         res=biblio.supprimer_etudiant(num)
         QMessageBox.about(None,"massage",res)

         self.afficher_tous_les_etudiants()
    def supprimer_niveau(self):
         niveau2=self.ui.niveau1.currentText()
         res3=biblio.supprimer_etudiants_niveau( niveau2)
         QMessageBox.about(None,"massage",res3)

         self.afficher_tous_les_etudiants()
    def supprimer_section(self):
         section2=self.ui.section1.currentText()
         res4=biblio.supprimer_section2(section2)
         QMessageBox.about(None,"massage",res4)
         self.afficher_tous_les_etudiants()
    def supprimer_niveau_section(self):
         section4=self.ui.section2.currentText()
         niveau4=self.ui.niveau2.currentText()
         res5=biblio. supprimer_etudiants_section_niveau(section4,niveau4)
         QMessageBox.about(None,"massage",res5)
         self.afficher_tous_les_etudiants()
      
    def modi_phone(self):
        inscri8=self.ui.inscription_1.text()
        phone=self.ui.phone1.text()
        if not inscri8 or not phone:
             res6="Erreur : remplir tous les champs."
             QMessageBox.about(None,"massage",res6)
             return
             
        if not inscri8.isnumeric() or not phone.isnumeric()  :
           res6="Erreur : Veuillez saisir un numéro d'inscription et télephone valide."
           QMessageBox.about(None,"massage",res6)
           return
    
        res6=biblio. modifier_telephone(inscri8, phone)
        QMessageBox.about(None,"massage",res6)
        self.afficher_tous_les_etudiants()
    def modi_mail(self):
         inscri9=self.ui.inscription_2.text()
         mail=self.ui.mail1.text()
         if not inscri9 or not mail:
             res6="Erreur : remplir tous les champs."
             QMessageBox.about(None,"massage",res6)
             return
         if not biblio. is_valid_email(mail):
             QMessageBox.about(None, "Message", "Adresse e-mail invalide")
             return
             
         if not inscri9.isnumeric()   :
           res6="Erreur : Veuillez saisir un numéro d'inscription  valide."
           QMessageBox.about(None,"massage",res6)
           return
         res7=biblio. modifier_mail(inscri9, mail)
         QMessageBox.about(None,"massage",res7)
         self.afficher_tous_les_etudiants()
    def modi_adresse(self):
         inscri10=self.ui.inscri10.text()
         adresse=self.ui.adresse1.text()
         if not inscri10 or not adresse:
             res6="Erreur : remplir tous les champs."
             QMessageBox.about(None,"massage",res6)
             return
             
         if not inscri10.isnumeric() :
           res6="Erreur : Veuillez saisir un numéro d'inscription valide."
           QMessageBox.about(None,"massage",res6)
           return
         res8=biblio. modifier_adresse(inscri10, adresse)
         QMessageBox.about(None,"massage",res8)
         self.afficher_tous_les_etudiants()
      




    def afficher_tous_les_etudiants(self):
      texte = ""
      for inscri, etudiant in biblio.etudiants.items():
          texte += f"{inscri} - {etudiant['nom']} {etudiant['prenom']} , {etudiant['date_naissance']}  {etudiant['adresse']} {etudiant['email']} {etudiant['telephone']} ({etudiant['section']} - {etudiant['niveau_etude']})\n"
          self.ui.res11.setText(texte)
    def rechercher_par_inscription(self):
        texte=""
        num = self.ui.inscri_recherche.text()
        if not num.isnumeric()   :
           res6="Erreur : Veuillez saisir un numéro d'inscription  valide."
           QMessageBox.about(None,"massage",res6)
           return
        if num in biblio.etudiants:
            etudiant = biblio.etudiants[num]
            texte +=f"{etudiant['nom']} {etudiant['prenom']}, né(e) le {etudiant['date_naissance']}, adresse : {etudiant['adresse']}, e-mail : {etudiant['email']}, téléphone : {etudiant['telephone']}, section : {etudiant['section']}, niveau : {etudiant['niveau_etude']}"
            self.ui.res20.setText(texte)
        else:
            self.ui.res20.setText("Aucun étudiant trouvé avec ce numéro d'inscriptiocn.")
    def  rechercher_par_niveau(self):
        niveau = self.ui.niveau_recherhce.currentText()
        etudiants_trouves = []
        for etudiant in biblio.etudiants.values():
            if etudiant["niveau_etude"] == niveau:
               etudiants_trouves.append(etudiant)
        if len(etudiants_trouves) > 0:
            texte = ""
            for etudiant in etudiants_trouves:
               texte += f"{etudiant['nom']} {etudiant['prenom']}, né(e) le {etudiant['date_naissance']}, adresse : {etudiant['adresse']}, e-mail : {etudiant['email']}, téléphone : {etudiant['telephone']}, section : {etudiant['section']}, niveau : {etudiant['niveau_etude']}\n"
            self.ui.res22.setText(texte)
        else:
              self.ui.res22.setText("Aucun étudiant trouvé pour ce niveau.")
    def rechercher_par_section(self):
        section = self.ui.section_recherhce.currentText()
        etudiants_trouves = []
        for etudiant in biblio.etudiants.values():
            if etudiant["section"] == section:
                etudiants_trouves.append(etudiant)
        if len(etudiants_trouves) > 0:
           texte = ""
           for etudiant in etudiants_trouves:
               texte += f"{etudiant['nom']} {etudiant['prenom']}, né(e) le {etudiant['date_naissance']}, adresse : {etudiant['adresse']}, e-mail : {etudiant['email']}, téléphone : {etudiant['telephone']}, section : {etudiant['section']}, niveau : {etudiant['niveau_etude']}\n"
           self.ui.res21.setText(texte)
        else:
            self.ui.res21.setText("Aucun étudiant trouvé pour cette section.")


    def rechercher_par_section_et_niveau(self):
        section = self.ui.section_recher.currentText()
        niveau = self.ui.niveau_recher.currentText()
        etudiants_trouves = []
        for etudiant in biblio.etudiants.values():
            if etudiant["section"] == section and etudiant["niveau_etude"] == niveau:
                etudiants_trouves.append(etudiant)
        if len(etudiants_trouves) > 0:
            texte = ""
            for etudiant in etudiants_trouves:
                texte += f"{etudiant['nom']} {etudiant['prenom']}, né(e) le {etudiant['date_naissance']}, adresse : {etudiant['adresse']}, e-mail : {etudiant['email']}, téléphone : {etudiant['telephone']}, section : {etudiant['section']}, niveau : {etudiant['niveau_etude']}\n"
            self.ui.res23.setText(texte)
        else:
                self.ui.res23.setText("Aucun étudiant trouvé pour cette section et ce niveau.")
#livre

    def afficher_tous_les_livres(self):
       texte = ""
       for ref, livre in biblio.livres.items():
        texte += f"{ref} - {livre['titre']}, {livre['auteur']}, {livre['annee_edition']}, {livre['nombre_exemplaires']} exemplaires\n"
        self.ui.res_contenu_livres.setText(texte)
   
    def afficher_livre_ref(self):
        ref = self.ui.ref_affiche_2.text()
        if ref in biblio.livres:
            livre = biblio.livres[ref]
            texte = f"{ref} - {livre['titre']}, {livre['auteur']}, {livre['annee_edition']}, {livre['nombre_exemplaires']} exemplaires\n"
            self.ui.res_ref.setText(texte)
        else:
            self.ui.res_ref.setText("Référence inconnue")
    def afficher_livre_auteur(self):
        
        auteur = self.ui.auteur4.text()
         
        if not auteur:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        ref = None
        for ref_livre, livre in biblio.livres.items():
             if livre['auteur'] == auteur:
                ref = ref_livre
                break
        if ref is not None:
            livre = biblio.livres[ref]
            texte = f"{ref} - {livre['titre']}, {livre['auteur']}, {livre['annee_edition']}, {livre['nombre_exemplaires']} exemplaires\n"
            self.ui.affich_auteur.setText(texte)
        else:
            self.ui.affich_auteur.setText("Auteur inconnu")
    def afficher_livre_annee(self):
        annee_edition = self.ui.annee_2.text()
        if not annee_edition:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        ref = None
        for ref_livre, livre in biblio.livres.items():
            if livre['annee_edition'] == annee_edition:
                ref = ref_livre
                break
        if ref is not None:
            livre = biblio.livres[ref]
            texte = f"{ref} - {livre['titre']}, {livre['auteur']}, {livre['annee_edition']}, {livre['nombre_exemplaires']} exemplaires\n"
            self.ui.affiche_anne.setText(texte)
        else:
            self.ui.affiche_anne.setText("Année d'édition inconnue")
    def afficher_livres_ordre_alphabetique(self):
        liste_livres = sorted(biblio.livres.items(), key=lambda x: x[1]['titre'])
        texte = ""
        for ref, livre in liste_livres:
            texte += f"{ref} - {livre['titre']}, {livre['auteur']}, {livre['annee_edition']}, {livre['nombre_exemplaires']} exemplaires\n"
        self.ui.res_alphabitique.setText(texte)


    def ajouter_livre(self): 
    # Get the input values from the UI
      reference1 = self.ui.ref1.text()
      titre1 = self.ui.titre1.text()
      nom_auteur1 = self.ui.nom_auteur1.text()
      prenom_auteur1 = self.ui.prenom_auteur1.text()
      annee1 = self.ui.annee1.text()
      nombre1 = self.ui.nombre1.text()
    
      if not reference1 or not titre1 or not nom_auteur1 or not prenom_auteur1 or not annee1 or not nombre1:
         res_ajoute=("Erreur : Veuillez remplir tous les champs.")
         QMessageBox.about(None,"massage",res_ajoute)

         return
    
      if not reference1.isnumeric() or not annee1.isnumeric() or not nombre1.isnumeric():
        res_ajoute=("Erreur : La référence, l'année et le nombre d'exemplaires doivent être des nombres entiers.")
        QMessageBox.about(None,"massage",res_ajoute)
        return
    
      result = biblio.ajouter_livre(reference1, titre1, nom_auteur1, prenom_auteur1, annee1, nombre1)
      QMessageBox.about(None,"massage",result)
    
   
    

    def supprimer_livre1(self):
        ref=self.ui.ref_suppression.text()
         
        if not ref.isnumeric() :
            res_ajoute=("Erreur : La référence doivent être des nombres entiers.")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        re=biblio.supprimer_livre( ref)
        QMessageBox.about(None,"massage",re)
        self.afficher_tous_les_livres()
    def supprimer_auteur(self):
         auteur=self.ui.nom_auteur_2.text()
         if not auteur:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
         res_suppression=biblio.supprimer_livres_auteur( auteur)
         QMessageBox.about(None,"massage",res_suppression)
         self.afficher_tous_les_livres()
    def supprimer_annee(self):
         annee=self.ui.annee.text()
         if not annee:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
         supp_annee=biblio.supprimer_livres_par_annee(annee )
         QMessageBox.about(None,"massage",supp_annee)
         self.afficher_tous_les_livres()
    def modifier_exemplaire(self):
         ref=self.ui.ref2.text()
         exempliare1=self.ui.exemplaire.text()
         if not ref or not exempliare1:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
         if not ref.isnumeric() or not exempliare1.isnumeric() :
            res_ajoute=("Erreur : La référence et nombre d'exemplaire doivent être des nombres entiers.")
            QMessageBox.about(None,"massage",res_ajoute)
            return
         res_modi_exemplaire=biblio.modifier_nombre_exemplaires(ref,exempliare1 )
         QMessageBox.about(None,"massage",res_modi_exemplaire)
         self.afficher_tous_les_livres()
    
    def modi_date(self):
         inscri=self.ui.inscri_modi.text()
         date=self.ui.date2.text()
         if not inscri or not date:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
         res_modi=biblio.modifier_date_emprunt(inscri,date)
         QMessageBox.about(None,"massage",res_modi)
         self.affiche_emp()
    def modi_retour(self):
         inscri=self.ui.inscri5.text()
         date=self.ui.date8.text()
         if not inscri or not date:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
         res_retour_2=(biblio.modifier_date_retour(inscri,date))
         QMessageBox.about(None,"massage",res_retour_2)
         self.affiche_emp()
    def afficher_resultats_emprunts(emprunts):
    # Convertir le dictionnaire d'emprunts en une chaîne de caractères
        resultats = ""
        for emprunt in emprunts.values():
            resultats += f"Numéro d'inscription: {emprunt['num_inscription']}\n"
            resultats += f"Référence de livre: {emprunt['ref_livre']}\n"
            resultats += f"Date d'emprunt: {emprunt['date_emprunt']}\n"
            resultats += f"Date de retour: {emprunt['date_retour']}\n\n"
          #  self.ui.res_ref.setText(resultats)
    def afficher_emprunts_livre(self):
      ref_livre = self.ui.ref4.text()
      if not ref_livre.isnumeric() :
            res_ajoute=("Erreur : La référence doivent être des nombres entiers.")
            QMessageBox.about(None,"massage",res_ajoute)
            return
      

      if ref_livre not in biblio.livres:
        self.ui.affiche.setText(f"Le livre {ref_livre} n'existe pas dans la bibliothèque")
        return
      emprunts_livre = []
      for num_inscription, emprunt in biblio.emprunts.items():
        if emprunt['ref_livre'] == ref_livre:
            emprunts_livre.append((num_inscription, emprunt))
      if not emprunts_livre:
        self.ui.affiche.setText("Aucun emprunt enregistré pour ce livre")
      else:
        texte = f"Emprunts pour le livre {ref_livre} :\n\n"
        for num_inscription, emprunt in emprunts_livre:
            ref = emprunt['ref_livre']
            date_emprunt = emprunt['date_emprunt']
            date_retour = emprunt['date_retour']
            texte += f"{ref}- {date_emprunt} / {date_retour}\n"
        self.ui.affiche.setText(texte)
      
    def enregistrement_etudiant(self):
        biblio. enregistrement_etudiant()
        res=("Le fichier des étudiants a été mis à jour")
        QMessageBox.about(None,"massage",res)

    def enregistrement_livres (self) :
        biblio.enregistrement_livre()
        resl=("le dictionnaire des livres est enregistré avec succes ")
        QMessageBox.about(None,"massage",resl)
    def enregistrement_emprunts(self) :
        biblio.enregistrement_emprunts()
        resem=("le dictionnaire des empruts est enregistré avec succes ")
        QMessageBox.about(None,"massage",resem)
    def recherche_par_etudiant(self):
        iscription=self.ui.inscri_em.text()
        if not iscription.isnumeric() :
            res_ajoute=("Erreur : La référence doivent être des nombres entiers.")
            QMessageBox.about(None,"massage",res_ajoute)
            return

        texte = ""
        for emprunt in biblio.emprunts.values():
           if emprunt['num_inscription'] == iscription:

              texte += f"Référence de livre: {emprunt['ref_livre']}\n"
              texte += f"Date d'emprunt: {emprunt['date_emprunt']}\n"
              texte += f"Date de retour: {emprunt['date_retour']}\n"
             

        if texte:
            self.ui.res100.setText(texte)
        else:
            self.ui.res100.setText("Aucun emprunt trouvé pour cet étudiant.")
   
    
    def recherche_livre_emprunte_entre_dates(self):
      date_emprunt_debut = self.ui.debut_em.text()
      date_emprunt_fin = self.ui.fin_em.text()
      if not  date_emprunt_debut or not date_emprunt_fin :
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
      texte = ""
      for livre in biblio.livres.values():
        emprunts = livre.get("emprunts", [])
        for emprunt in emprunts:
            date_emprunt = datetime.datetime.strptime(emprunt["date_emprunt"], '%Y-%m-%d').date()
            if date_emprunt_debut <= date_emprunt <= date_emprunt_fin:
                texte += f"Titre: {livre['titre']}\n"
                texte += f"Auteur: {livre['auteur']}\n"
                texte+= f"anne_edition : {livre['annee_edition']}\n"
                texte += f"Nombre d'exemplaires: {livre['nb_exemplaires']}\n"
                texte += f"Date d'emprunt: {emprunt['date_emprunt']}\n"
      if texte == "":
        texte = "Aucun livre n'a été emprunté entre ces deux dates."
      self.ui.res2et2.setText(texte)
        
    def recherche_livre_par_date_retour(self):
        date_retour = self.ui.date_ret.text()
        if not  date_retour :
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        livres = biblio.livres
        emprunts = biblio.emprunts

        resultat = ""
        for ref_livre, livre in livres.items():
            for emprunt in emprunts.values():
               if emprunt['ref_livre'] == ref_livre and emprunt['date_retour'] == date_retour:
                resultat += f"Titre : {livre['titre']}\n"
                resultat += f"Auteur(s) : {livre['auteur']}\n"
                resultat += f"annee_edition : {livre['annee_edition']}\n"
                resultat += f"Nombre d'exemplaires : {livre['nombre_exemplaires']}\n"
                resultat += f"Référence : {ref_livre}\n\n"

        if resultat == "":
              resultat = "Aucun livre n'a été trouvé pour cette date de retour."
        self.ui.res101.setText(resultat)
    def recherche_livre_par_date_emprunt(self):
        date_emprunt = self.ui.date100.text()
        if not  date_emprunt:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        livres = biblio.livres
        emprunts = biblio.emprunts

        resultat = ""
        for ref_livre, livre in livres.items():
            for emprunt in emprunts.values():
               if emprunt['ref_livre'] == ref_livre and emprunt['date_emprunt'] == date_emprunt:
                resultat += f"Référence : {ref_livre}\n\n"
                resultat += f"Titre : {livre['titre']}\n"
                resultat += f"Auteur(s) : {livre['auteur']}\n"
                resultat += f"anne_edition : {livre['annee_edition']}\n"
                resultat += f"Nombre d'exemplaires : {livre['nombre_exemplaires']}\n"
                resultat += f"Référence : {ref_livre}\n\n"

        if resultat == "":
              resultat = "Aucun livre n'a été trouvé pour cette date de emprunt."
        self.ui.label_50.setText(resultat)
    def recherche_livre_retour_entre_dates(self):
        date_retour_debut = self.ui.ret1.text()
        date_retour_fin = self.ui.ret2.text()
        if not  date_retour_debut or not date_retour_fin :
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        texte = ""
        for livre in biblio.livres:
            emprunts = livre["emprunts"]
            for emprunt in emprunts:
                if  date_retour_debut <= emprunt["date_emprunt"] <=  date_retour_fin:
                    texte += f"Titre: {livre['titre']}\n"
                    texte += f"Auteur: {livre['auteur']}\n"
                    texte+= f"anne_edition : {livre['annee_edition']}\n"
                    texte += f"Nombre d'exemplaires: {livre['nb_exemplaires']}\n"
            

        if texte == "":
            texte = "Aucun livre n'a été emprunté entre ces deux dates."
    
        self.ui.res_ret.setText((texte))



    def afficher_livre_titre(self):
        titre = self.ui.titre3.text()
        if not titre:
            res_ajoute=("Erreur : remplir tout les champs")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        texte = ""
        for ref, livre in biblio.livres.items():
           if titre.lower() in livre['titre'].lower():
            texte += f"{ref} - {livre['titre']}, {livre['auteur']}, {livre['annee_edition']}, {livre['nombre_exemplaires']} exemplaires\n"
        if texte:
           self.ui.res_titre.setText(texte)
        else:
           self.ui.res_titre.setText("Aucun livre trouvé avec ce titre")
    def suprimer(self):
        inscri1 = self.ui.inscri_2.text()
        ref = self.ui.ref_liv.text()
        if not ref or not ref :
            res_ajoute=("Erreur : remplir tous les champs.")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        if not ref.isnumeric() or not ref .isnumeric():
            res_ajoute=("Erreur : La référence doivent être des nombres entiers.")
            QMessageBox.about(None,"massage",res_ajoute)
            return
        res_retour = biblio.supprimer_emprunt(inscri1, ref)
        if res_retour:
           QMessageBox.about(None, "Message", "L'emprunt a été supprimé avec succès.")
        else:
           QMessageBox.about(None, "Message", "L'emprunt n'a pas été trouvé.")
    def recuperer_etudiants (self) :
        biblio.recuperation_etudiants()
        resl="fichier etudiant recupere avec succé" 
        QMessageBox.about(None,"massage",resl)
    def recuperer_livres (self) :
        biblio.recuperation_etudiants()
        resl="fichier livre recupere avec succé" 
        QMessageBox.about(None,"massage",resl)
    def recuperer_emprunts (self) :
        biblio.recuperation_etudiants()
        resl="fichier emprunts recupere avec succé" 
        QMessageBox.about(None,"massage",resl)
  

    
    
if __name__ == "__main__":
    app = QApplication([])
    main_win = MainWindow()
    main_win.show()
    app.exec_()