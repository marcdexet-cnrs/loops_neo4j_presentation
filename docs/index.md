class: inverse middle center

# Bases Graphes &amp; Neo4j
Incursion dans le monde des bases graphes  
avec Neo4J

.footnote[marc.dexet(at)ias.u-psud.fr]
.headnote[Café Loops]


---
class: inverse middle center
# Un peu d'histoire

---
# PLAN un peu d'histoire
## Base Graphe, un vieux concept
* listes chainés
* codasyl

## Victoire du modèle relationnel

## Retour en grâce 
* Mouvement NoSQL
* Théorème CAP
* Problèmatiques multi-silo
* Prise de pouvoir par le monde du développement

.quote[
    traiter des données fortement connectées
    gérer facilement un modèle complexe et flexible
    offrir des performances exceptionnelles pour les lectures locales, par parcours de graphe.
]

---
# SQL vs Graphe
Passage obligatoire

---
class: inverse middle center
# Un peu de théorie

---
# Plan un pu de théorie

* graphe &rarr; adjacence
* parcours par pointeur
* Traversée possible à partir d'un point de départ sans passer par un index
* Algorithmes classiques de la théorie des graphes (plus court chemin, Dijsktra, A\*, calcul de centralité…)

---
class: inverse middle center
# Etat de lieux rapides

---
# PLAN Etat de lieux rapides
## Dynamisme du marché
* nombreuses bases graphes

---
class: inverse middle center
# Présentation NEO4J

---
# PLAN Présentation NEO4J

---
class: inverse middle center
# Principes de base

---
# PLAN principes de base


---
class: inverse middle center
# Sous le capot
* Neo4j utilise assez habilement des indexes et de  l'adjacence. Les indexes pour localiser les points de départs