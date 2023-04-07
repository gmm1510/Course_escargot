# -*- coding: utf-8 -*-
"""
"1- Importation de la base de données"
"""

import pandas as pd
import numpy as np
#import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
#from scipy import stats
#import random
import streamlit as st
import plotly.express as px





def load_database():

    df_logement_comm = pd.read_excel("C:/IA/logement_communes.xlsx")
    df_logement_comm = pd.DataFrame(df_logement_comm)
    df_logement_comm = df_logement_comm.set_index("LIBGEO")
    df_logement_comm = df_logement_comm.drop(['codGeo'], axis=1)

    df_demog_comm = pd.read_excel('C:/IA/demog_villes_2021_communale.xlsx')
    df_demog_comm = pd.DataFrame(df_demog_comm)
    df_demog_comm = df_demog_comm.set_index("LIBGEO")
    df_demog_comm = df_demog_comm.drop(['CODGEO'], axis=1)


    df_pop = pd.read_excel('C:/IA/base-cc.xlsx')
    df_pop = pd.DataFrame(df_pop)
    df_pop = df_pop.set_index("LIBGEO")
    
    """
    # d1 = pd.concat([df_logement_comm, df_demog_comm])
    database_commune = pd.merge(df_logement_comm, df_demog_comm, on='LIBGEO', how='inner')
    database_commune = database_commune.set_index("LIBGEO")
    database_commune = database_commune.drop(['codGeo'], axis=1)
    #database_commune = pd.merge(database_commune, df_pop, on='LIBGEO', how='inner')
    #print(database_commune.columns)
    """
    
    df_demog_econom_reg = pd.read_excel('C:/IA/demog_eco_reg.xlsx')
    df_demog_econom_reg = pd.DataFrame(df_demog_econom_reg)

    df_PIB_reg = pd.read_excel('C:/IA/PIB_par_emploi_regionnal.xlsx')
    df_PIB_reg = pd.DataFrame(df_PIB_reg)
    
    database_region = pd.merge(df_demog_econom_reg, df_PIB_reg, on='Région', how='inner')
    database_region = database_region.set_index("Région")
    
    
    #### Gestion des valeurs manquantes ######
    
    valeur_manquante1 = df_logement_comm.isnull().sum()
    valeur_manquante2 = df_demog_comm.isnull().sum()
    valeur_manquante_region = database_region.isnull().sum()

    
    df_logement_comm['txVac'].fillna(df_logement_comm['txVac'].mean(), inplace=True)
    df_logement_comm['txVac3m'].fillna(df_logement_comm['txVac3m'].mean(), inplace=True)
    df_logement_comm['txRot'].fillna(df_logement_comm['txRot'].mean(), inplace=True)
    df_logement_comm['txLsCol'].fillna(df_logement_comm['txLsCol'].mean(), inplace=True)
    df_logement_comm['txLsInd'].fillna(df_logement_comm['txLsInd'].mean(), inplace=True)
    df_logement_comm['moyLoy'].fillna(df_logement_comm['moyLoy'].mean(), inplace=True)
    
    df_demog_comm['A_ETUD'].fillna(df_demog_comm['A_ETUD'].mean(), inplace=True)
    
    
    database_commune = pd.merge(df_logement_comm, df_demog_comm, on='LIBGEO', how='inner')
    
    for col in database_commune.columns:
        database_commune[str(col)].fillna(database_commune[str(col)].mean(), inplace=True)

    ###################################################
    
    ### Renommer des colonnes ########################
    
    database_region = database_region.rename(columns={'Taux de croissance de la population entre \n2016 et 2021 \n(en %)':'Taux de croissance de la pop entre 2016 et 2021'})
    database_region = database_region.rename(columns={'Taux de chômage(c)\n (en %) ':'Taux chomage'})
    database_region = database_region.drop(['PIB (euro par emploi)'],axis=1)
    l3 = database_region.columns
    ##################################################

    
    
    l1 = database_commune.columns
    l2 = ['Part des résidences principales',
         "Part des résidences secondaires",	"Part des logements occasionnels", "Part des logements vacants",
         "Part des résidences principales de type appartement",	"Part des résidences principales de type maison",
         "Part des ménages propriétaires", "Nombre de personnes par résidence principale",
         "Nombre de logements du Parc Locatif Social", "Taux de vacance des logements sociaux",
         "Taux de vacance de plus de 3 mois des logements sociaux",	"Taux de rotation des logements sociaux",
         "Part des logements sociaux collectifs",
         "Part des logements sociaux individuels",
         "Moyenne loyer par m² des logements sociaux",
         "Part des logements sociaux parmi les résidences principales",
         "Taux d’emménagement", "Part des femmes parmi la population",	
         "Part des personnes de 0 à 24 ans parmi la population",
         "Part des personnes de 60 ans ou plus parmi la population",
         "Indice de jeunesse",
         "Part des étrangers parmi la population",
         "Part des étrangères parmi les femmes",
         "Nombre total d allocataires",
         "Personnes couvertes",
         "Allocataires mono-parent"	,
         "Allocataires isolés sans enfant",
         "Allocataires couples sans enfant",
         "Allocataires couples avec enfant(s)",
         "Allocataires étudiants",
         "Enfants couverts par au moins une prestation CAF"]
    
    
    
    return database_commune, database_region, df_pop, l1, l2, l3

#load_database()
    
    

    
#Bar charts: useful for comparing quantities corresponding to different groups
def diagram_1arg(db, liste_ville, ind, crit, crit_reel):

    if ind==0:
        
        Critere = ['partResPrinc', 'partResSec', 'partResoccas',
           'partResVac', 'partResPrincApp', 'partResPrincMai', 'partMenProp',
           'nbPersResPrinc', 'nbLsPls', 'txVac', 'txVac3m', 'txRot', 'txLsCol',
           'txLsInd', 'moyLoy', 'TxLsRp', 'txMobGlob', 'CODGEO', 'POP_MUN', 'TX_F',
           'TX_TOT_0A24', 'TX_TOT_60ETPLUS', 'IND_JEUNE', 'TX_TOT_ET', 'TX_F_ET',
           'A', 'PERCOU', 'AM', 'AI', 'ACSSENF', 'ACAVENF', 'A_ETUD', 'ENF']

        plt.figure(figsize=(14,6))
        txt1="Diagramme représentant le critère " + str(crit_reel)
        plt.title(txt1)
        plt.xlabel("Villes")


        for c in Critere:
            if crit == c:
                y=[]
                for v in liste_ville:
                    y.append(db.loc[v,c])
                    #y.reverse()
        sns.barplot(x = liste_ville, y = y, hue = liste_ville )



    if ind==1:
        plt.figure(figsize=(14,6))
        txt1="Diagramme représentant le critère " + str(crit_reel)
        plt.title(txt1)
        plt.xlabel("Region")
        y=[]
        for v in liste_ville:
            y.append(db.loc[v,crit])
            #y.reverse()
        
        sns.barplot(x = liste_ville, y = y, hue = liste_ville)
    
    

#Line charts: to show trends over a period of time, and multiple lines 
#can be used to show trends in more than one group.
def line_chart_ville(db, liste_ville, ind, crit):
    
    data = db.columns
    annee1 = [2019,2013,2008,1999,1990,1982,1975,1968]
    annee = [2019,2013,2008,1999,1990,1982,1975]
    data2 = range(1990,2021)
    y=[]

    if ind==0:   
        plt.figure(figsize=(14,6))
        txt1="Evolution de " + str(crit) + " dans le temps"
        plt.title(txt1)
        plt.xlabel("Année")
        
        if crit == "Population": 
            data1=data[0:8]
            for v in liste_ville:
                y=[]
                for i in data1:
                    y.append(db.loc[v,i])
                #y.reverse()
                sns.lineplot(x = annee1, y = y, label = v)
        
        if crit == "Naissance":
            data1=data[9:16]
            print(data1)
            for v in liste_ville:
                y=[]
                for i in data1:
                    y.append(db.loc[str(v),i])
                y.reverse()
                sns.lineplot(x = annee, y = y, label = v)
        
        if crit == "Deces":
            data1=data[16:23]
            for v in liste_ville:
                y=[]
                for i in data1:
                    y.append(db.loc[str(v),i])
                y.reverse()
                sns.lineplot(x = annee, y = y, label = v)
        
        if crit == "Logement":
            data1=data[23:31]
            for v in liste_ville:
                y=[]
                for i in data1:
                    y.append(db.loc[str(v),i])
                sns.lineplot(x = annee1, y = y, label = v)
        
        if crit == "Residence principale":
            data1=data[31:39]
            for v in liste_ville:
                y=[]
                for i in data1:
                    y.append(db.loc[str(v),i])
                sns.lineplot(x = annee1, y = y, label = v)
                
        
        if crit == "Residence secondaire":
            data1=data[39:47]
            for v in liste_ville:
                y=[]
                for i in data1:
                    y.append(db.loc[str(v),i])
                sns.lineplot(x = annee1, y = y, label = v)

        if crit == "Logements vacants":
            data1=data[47:]
            for v in liste_ville:
                y=[]
                for i in data1:
                    y.append(db.loc[str(v),i])
                y.reverse()
                sns.lineplot(x = annee1, y = y, label = v)
            
    
    if ind==1: #evlution pop? #aniamtion? 
        txt2 = "Evolution du PIB dans le temps"
        plt.figure(figsize=(14,6))
        plt.title(txt2)
        plt.xlabel("Année")
        plt.ylabel("PIB en millier d'euro")
        
        for v in liste_ville:
            y=[]
            for i in data2:
                y.append(db.loc[str(v),i])
            sns.lineplot(x = data2, y = y, label=v)
        



#Scatter show the relationship between 2 continuous variables; if color-coded
#we can also show the relationship with a third categorical variable.
def scatter_1arg(db, liste_ville, ind, list_crit, list_crit_reel):
    
    if ind==0:

        plt.figure(figsize=(14,6))
        txt1="Nuage de points représentant différents critère: "
        plt.title(txt1)
        plt.xlabel("Villes")
        plt.ylabel("Valeurs")
        
        
        
    if ind==1:
        plt.figure(figsize=(14,6))
        txt1="Nuage de points représentant différents critère: "
        plt.title(txt1)
        plt.xlabel("Region")
        plt.ylabel("Valeurs")
        

    l1=len(liste_ville)
    l2=len(list_crit)
    array = np.zeros(l2*l1) 
    array = array.reshape(l1,l2)
    #print(array.shape)
    #print(array)
    
    k=0
    for v in liste_ville:
        j=0
        for c in list_crit:
            #y.append(db.loc[v,c])
            array[k][j] = db.loc[v,c]
           
            #print(y)
            #print(liste_ville[i])
            #y.reverse()
            j=j+1
        k+=1
    
    df2 = pd.DataFrame(array, index=liste_ville, columns=list_crit_reel)
    #df2['Ville'] = liste_ville
    #df2['Critere'] = list_crit_reel

    sns.scatterplot(data=df2)


"""
#Histograms show the distribution of a single numerical variable
def histogram_1arg(liste: list, critere: str):
    pass
"""    

def diag_multi_arg(df, ville, ind, L, Lr):
    
    if ind==0:
        y=[]
        plt.figure(figsize=(18,8))
        txt1="Diagramme représentant différents critères sur la ville de " + str(ville)
        plt.title(txt1)
        plt.xlabel("Critères")
        
        for c in L:
            y.append(df.loc[str(ville),c])
        
        sns.barplot(x=Lr, y=y)
        
    else:
        pass


def pie_fig(df, ville, ind, L, Lr):
    
    if ind==0:
        y=[]
        plt.figure(figsize=(14,6))
        txt1="Diagramme représentant différentes répartitions sur la ville de " + str(ville)
        plt.title(txt1)
        #plt.xlabel("Critères")
        colors = sns.color_palette('pastel')[0:len(L)]
        
        for c in L:
            y.append(df.loc[str(ville),c])
        
        
        plt.pie(y, labels = Lr, colors = colors, autopct='%.0f%%')
        plt.show()

    else:
        y=[]
        plt.figure(figsize=(14,6))
        txt1="Diagramme représentant différentes répartitions sur la région " + str(ville)
        plt.title(txt1)
        #plt.xlabel("Critères")
        colors = sns.color_palette('pastel')[0:len(L)]
        
        cpt=0
        for c in L:
            if Lr[cpt][0:4]=='Part':
                a = df.loc[str(ville),c]/100
                y.append(340440 - a*340440)
            else:
                y.append(df.loc[str(ville),c])
            cpt+=1


        
        
        plt.pie(y, labels = Lr, colors = colors, autopct='%.0f%%')
        plt.show()        



def infographie_villes(echelle: str, liste: list, Critere: list):
    
    #df_commu , df_reg, df_pop, liste_crit_diag, L_Critere_diag = load_database()
    df_commu , df_reg, df_pop, liste_crit_diag, L_Critere_diag, list_crit_reg = load_database()
    
    liste_crit_line = ["Population","Naissance","Deces","Logement","Residence principale","Residence secondaire","Logements vacants"]
    
    list_crit_reg2 = list_crit_reg[0:9] #+ "Evolution PIB"
    crit_reg_reel = ["Population","Taux de croissance de la pop entre 2016 et 2021",'Superficie', 'Densité', 'Nombre de communes',
    'Part population de moins de 20 ans', 'Part population de moins de 60 ans', 'Taux chomage',
    'PIB']
    
    
    ########################## VILLE #########################################
    if echelle == 'ville':
        
        if len(Critere)==1:
            critere = Critere[0]
            cpt=0
            
            for i in liste_crit_line:
                if critere == i:
                    line_chart_ville(df_pop, liste, 0, i)
                    cpt+=1

            if cpt==0:
                k1=0
                for k in L_Critere_diag:
                    if critere == k:
                        diagram_1arg(df_commu, liste, 0, liste_crit_diag[k1], k)
                    else:
                        k1 = k1 +1

        elif len(Critere)>1:
            if len(liste)==1:
                k1=0
                L_ind=[]
                for k in L_Critere_diag:
                    for j in Critere:
                        if j == k:
                            L_ind.append(L_Critere_diag.index(k))
                        else:
                            k1 = k1 +1
                L1=[]
                L2=[]
                L1_reel=[]
                L2_reel=[]
                for l in L_ind:
                    crit = str(liste_crit_diag[l])
                    crit_r = str(L_Critere_diag[l])
                    if crit_r[0:4]=='Part':
                        L1.append(crit)
                        L1_reel.append(crit_r)
                    else:
                        L2.append(crit)
                        L2_reel.append(crit_r)
                        
                        
                if len(L2)==0:
                    pie_fig(df_commu, liste[0], 0, L1, L1_reel)
                    
                else:
                    L3 = L1 + L2
                    L3_r = L1_reel + L2_reel
                    diag_multi_arg(df_commu, liste[0], 0, L3, L3_r)
            
            if len(liste)>1:
                k1=0
                L_ind=[]
                for k in L_Critere_diag:
                    for j in Critere:
                        if j == k:
                            L_ind.append(L_Critere_diag.index(k))
                        else:
                            k1 = k1 +1
                L=[]
                for l in L_ind:
                    L.append(liste_crit_diag[l])

                scatter_1arg(df_commu, liste, 0, L, Critere)



    ############################# REGION ###################################
    elif echelle == 'region':
        if len(Critere)==1:
            critere = Critere[0]
            dico={}
            if len(liste)>1 and critere=='Evolution PIB':
                #data_progression(df_reg,liste,critere)
                line_chart_ville(df_reg, liste, 1, critere)
            else:
                k1=0
                for k in crit_reg_reel:
                    if critere == k:
                        diagram_1arg(df_reg, liste, 1, list_crit_reg2[k1], k)
                    else:
                        k1 = k1 +1
        
        
        
        if len(Critere)>1:
            if len(liste)==1:
                k1=0
                L_ind=[]
                for k in crit_reg_reel:
                    for j in Critere:
                        if j == k:
                            L_ind.append(crit_reg_reel.index(k))
                        else:
                            k1 = k1 +1
                L1=[]
                L2=[]
                L1_reel=[]
                L2_reel=[]
                L3=[]
                for l in L_ind:
                    crit = str(list_crit_reg2[l])
                    crit_r = str(crit_reg_reel[l])
                    
                    if crit_r[0:4]=='Part' or crit_r[0:2]=='Po':
                        L1.append(crit)
                        L1_reel.append(crit_r)
                        
                    else:
                        L2.append(crit)
                        L2_reel.append(crit_r)
                        
                        
                if len(L2)==0:
                    pie_fig(df_reg, liste[0], 1, L1, L1_reel)
                    
                else:
                    L3 = L1 + L2
                    L3_r = L1_reel + L2_reel
                    diag_multi_arg(df_reg, liste[0], 1, L3, L3_r)
                 
                
            
            else:
                k1=0
                L=[]
                for k in crit_reg_reel:
                    for j in Critere:
                        if j == k:
                            L.append(list_crit_reg2[k1])
                    k1 = k1 +1

                scatter_1arg(df_reg, liste, 1, L, Critere)
    
    


if __name__ == "__main__":
    """
    infographie_villes(echelle = 'ville', liste = ['Paris','Brest','Toulouse','Lyon'], Critere = ["Allocataires couples sans enfant",
    "Allocataires couples avec enfant(s)",
    "Allocataires étudiants",])
    """
    df_commu , df_reg, df_pop, liste_crit_diag, L_Critere_diag, list_crit_reg = load_database()
    
    st.set_page_config(page_title='Data Power', page_icon=':bar_chart:',layout='wide')


    st.dataframe(df_commu)







"""
  Warning: to view this Streamlit app on a browser, run it with the following
  command:

    streamlit run C:\Users\Paul Genty\Desktop\Cours 2022 - 2023\Projet\code\code_database.py [ARGUMENTS]

"""






















"""
ARGUMENT DATABASE REGION de 1990 à 2021:
'Population(a)','Taux de croissance de la pop entre 2016 et 2021',
'Superficie \n(en km²)','Densité \n(en hab. / km²)','Nombre_communes',
'part_population(-20ans)','Part_population(-60ans)','Taux chomage',
'PIB (millions euro)','PIB (euro par emploi)'




ARGUMENT DATABASE COMMUNE:
['codGeo', 'LIBGEO', 'partResPrinc', 'partResSec', 'partResoccas',
       'partResVac', 'partResPrincApp', 'partResPrincMai', 'partMenProp',
       'nbPersResPrinc', 'nbLsPls', 'txVac', 'txVac3m', 'txRot', 'txLsCol',
       'txLsInd', 'moyLoy', 'TxLsRp', 'txMobGlob', 'CODGEO', 'POP_MUN', 'TX_F',
       'TX_TOT_0A24', 'TX_TOT_60ETPLUS', 'IND_JEUNE', 'TX_TOT_ET', 'TX_F_ET',
       'A', 'PERCOU', 'AM', 'AI', 'ACSSENF', 'ACAVENF', 'A_ETUD', 'ENF']

Part des résidences principales	
Part des résidences secondaires	
Part des logements occasionnels	
Part des logements vacants	
Part des résidences principales de type appartement	
Part des résidences principales de type maison
Part des ménages propriétaires
Nombre de personnes par résidence principale	
Nombre de logements du Parc Locatif Social	
Taux de vacance des logements sociaux	
Taux de vacance de plus de 3 mois des logements sociaux	
Taux de rotation des logements sociaux	
Part des logements sociaux collectifs
Part des logements sociaux individuels
Loyer par m² des logements sociaux (Moyenne)
Part des logements sociaux parmi les résidences principales
Taux d’emménagement
Part des femmes parmi la population	
Part des personnes de 0 à 24 ans parmi la population
Part des personnes de 60 ans ou plus parmi la population
Indice de jeunesse
Part des étrangers parmi la population	
Part des étrangères parmi les femmes
Nombre total d allocataires	
Personnes couvertes	
Allocataires mono-parent	
Allocataires isolés sans enfant	
Allocataires couples sans enfant	
Allocataires couples avec enfant(s) 
Allocataires étudiants	
Enfants couverts par au moins une prestation CAF





Ville BDD PIB :
Auvergne-Rhône-Alpes
Bourgogne-Franche-Comté
Bretagne
Centre-Val de Loire
Corse
Grand Est
Hauts-de-France
Île-de-France
Normandie
Nouvelle-Aquitaine
Occitanie
Pays de la Loire
Provence-Alpes-Côte d'Azur
France métropolitaine hors Île-de-France
France métropolitaine
Guadeloupe
Martinique
Guyane
Réunion 
Mayotte
Dom
France métropolitaine et DOM






ARGUMENT BDD POPULATION VILLE:
REG	Région
DEP	Département
LIBGEO	Libellé géographique
P19_POP	Population en 2019 (princ)
P13_POP	Population en 2013 (princ)
P08_POP	Population en 2008 (princ)
D99_POP	Population en 1999 (dnbt)
D90_POP	Population en 1990 (dnbt)
D82_POP	Population en 1982 (dnbt)
D75_POP	Population en 1975 (dnbt)
D68_POP	Population en 1968 (dnbt)
SUPERF	Superficie (en km²)
NAIS1319	Naissances entre 2013 et 2019
NAIS0813	Naissances entre 2008 et 2013
NAIS9908	Naissances entre 1999 et 2008
NAIS9099	Naissances entre 1990 et 1999
NAIS8290	Naissances entre 1982 et 1990
NAIS7582	Naissances entre 1975 et 1982
NAIS6875	Naissances entre 1968 et 1975
DECE1319	Décès entre 2013 et 2019
DECE0813	Décès entre 2008 et 2013
DECE9908	Décès entre 1999 et 2008
DECE9099	Décès entre 1990 et 1999
DECE8290	Décès entre 1982 et 1990
DECE7582	Décès entre 1975 et 1982
DECE6875	Décès entre 1968 et 1975
P19_LOG	Logements en 2019 (princ)
P13_LOG	Logements en 2013 (princ)
P08_LOG	Logements en 2008 (princ)
D99_LOG	Logements en 1999 (dnbt)
D90_LOG	Logements en 1990 (dnbt)
D82_LOG	Logements en 1982 (dnbt)
D75_LOG	Logements en 1975 (dnbt)
D68_LOG	Logements en 1968 (dnbt)
P19_RP	Résidences principales (Ménages) en 2019 (princ)
P13_RP	Résidences principales (Ménages) en 2013 (princ)
P08_RP	Résidences principales (Ménages) en 2008 (princ)
D99_RP	Résidences principales (Ménages) en 1999 (dnbt)
D90_RP	Résidences principales (Ménages) en 1990 (dnbt)
D82_RP	Résidences principales (Ménages) en 1982 (dnbt)
D75_RP	Résidences principales (Ménages) en 1975 (dnbt)
D68_RP	Résidences principales (Ménages) en 1968 (dnbt)
P19_RSECOCC	Rés secondaires et logts occasionnels en 2019 (princ)
P13_RSECOCC	Rés secondaires et logts occasionnels en 2013 (princ)
P08_RSECOCC	Rés secondaires et logts occasionnels en 2008 (princ)
D99_RSECOCC	Rés secondaires et logts occasionnels en 1999 (dnbt)
D90_RSECOCC	Rés secondaires et logts occasionnels en 1990 (dnbt)
D82_RSECOCC	Rés secondaires et logts occasionnels en 1982 (dnbt)
D75_RSECOCC	Rés secondaires et logts occasionnels en 1975 (dnbt)
D68_RSECOCC	Rés secondaires et logts occasionnels en 1968 (dnbt)
P19_LOGVAC	Logements vacants en 2019 (princ)
P13_LOGVAC	Logements vacants en 2013 (princ)
P08_LOGVAC	Logements vacants en 2008 (princ)
D99_LOGVAC	Logements vacants en 1999 (dnbt)
D90_LOGVAC	Logements vacants en 1990 (dnbt)
D82_LOGVAC	Logements vacants en 1982 (dnbt)
D75_LOGVAC	Logements vacants en 1975 (dnbt)
D68_LOGVAC	Logements vacants en 1968 (dnbt)


"""