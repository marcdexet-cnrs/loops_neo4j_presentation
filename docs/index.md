class: inverse middle center

# Bases Graphes &amp; Neo4j
Incursion dans le monde des bases graphes  
avec Neo4J

.footnote[marc.dexet(at)ias.u-psud.fr]
.headnote[Café Loops]

---
name: what_is_a_graph
# C'est quoi un "graphe" ?


---

template: what_is_a_graph

Un _graphe_ est une structure composée de 
* noeud (_vertex_)
* d'arêtes (_edge_)

Les _arêtes_ relient les _noeuds_.

<a href="graphes/graph_01.html" target="_blank">
	<center>
		<img src="graphes/graph_01.png" width="800px">
	</center>
</a>

---

template: what_is_a_graph

Un _graphe_ est une structure composée de 
* noeud (_vertex_)
* d'arêtes (_edge_)

Les _arêtes_ relient les _noeuds_ et peuvent être **orientées**

<a href="graphes/graph_02.html" target="_blank">
	<center>
		<img src="graphes/graph_02.png" width="800px">
	</center>
</a>

---

template: what_is_a_graph

Un _graphe_ est une structure composée de 
* noeud (_vertex_)
* d'arêtes (_edge_)

Quand tous les noeuds sont reliés entre eux, le graphe est dit **complet**

<a href="graphes/graph_03.html" target="_blank">
	<center>
		<img src="graphes/graph_03.png" width="800px">
	</center>
</a>


---

<a href="graphes/graph_complexe.html" target="_blank">
	<center>
		<img src="graphes/graph_complexe.png" width="800px">
	</center>
</a>

---
class: inverse middle center
# Un peu d'histoire

---
# Base graphe, un vieux concept

.left-column[
## CODASYL
* _Conference on Data Systems Languages_
* Réseau utilisé en _COBOL_.
 * Données organisées en _Record_ et liées par des liens 2 à 2
* Navigation par pointeur vers les enregistremets liés.
]

.right-column[
<center>
	<img src="http://www.cs.aucegypt.edu/~csci253/DBConcepts%20v2_files/image026.jpg" width="500px">
</center>
]

.reset-column[
* Accès aux données en mode _navigationnel_ en mentionnant les relations _explicitement_ en passant d'un record à un autre.
]

.footnote[.small[ [Cours sur sgbd.developpez.com](https://sgbd.developpez.com/tutoriels/cours-complet-bases-de-donnees/?page=bases-de-donnees-reseaux-et-hierarchiques)]]

???
Image http://www.cs.aucegypt.edu/~csci253/DBConcepts%20v2.htm


---
name: graph_renew_sql
# Base graphe, le renouveau NoSQL


---
template: graph_renew_sql

## L'hégémonie de l'approche SQL
* Un standard de fait
* **SQL** langage de manipulation abstrait
* **ACID** (Atomicité, Cohérence, Isolation, Durabilité)
* Plusieurs rôles : DBA, développeurs

--

## Les limites de l'approche SQL
* Peu adapté à des domaines très évolutifs
 * Processus lourd avec nombreux rôles
* ACID => Problèmes de performance dans certains contextes
 * bases distribuées

--

_Emergence du mouvement NoSql_

???
 * Atomicité &rarr; transaction
 * Cohérence &rarr; conservation de l'intégrité
 * Isolation
 * Durabilité
* Vision unifiée: [12 règles de CODD](https://fr.wikipedia.org/wiki/12_r%C3%A8gles_de_Codd)


---
template: graph_renew_sql

.big[**N**ot **O**nly **SQL**]

## Un mouvement venu du terrain
* Mouvement initié par le web, big data
* Solutions pensées par et pour des développeurs
* Acteurs type Géant du web

---
template: graph_renew_sql

## Théorème CAP
* Un SGDB ne pourra jamais avoir que 2 propriétés sur 3.

<center>
	<img src="images/cap_theorem.png" width="500px">
</center>


---
# Base graphe, le renouveau NoSQL

## Passage de ACID à BASE
* **ACID**
 * **A**tomicity &rarr; transaction
 * **C**onsistency &rarr; intégrité d'une transaction à une autre
 * **I**solation &rarr; pas d'interférence entre transactions
 * **D**urability &rarr; la pérénité est assurée, même en cas de défaillance
* **BASE**
 * **B**asically **A**vailable &rarr; disponibilité la plupart du temps
 * **S**oft-state &rarr; la consistence n'est pas toujours garantie
 * **E**ventually consistent &rarr; la consistence arrivera à un moment


## Proposition d'autres modèles
* clef-valeur
* document
* colonne
* **graphe**

???

Basic Availability
*   The database appears to work most of the time.

Soft-state
*  Stores don’t have to be write-consistent, nor do different replicas have to be mutually consistent all the time.

Eventual consistency
*  Stores exhibit consistency at some later point (e.g., lazily at read time).



Difference entre base réseau et base graphe
https://stackoverflow.com/questions/5040617/what-is-the-difference-between-a-graph-database-and-a-network-database

En gros, une base graphe est plus flexible alors qu'une base réseau à plus de contraintes.
Une base réseau a une notion de _nested_ avec une relation de _owner-member_

---
class: inverse middle center

# Les acteurs du marché des bases graphes
* https://db-engines.com/en/ranking/graph+dbms







class: inverse middle center

# Notions de base

---
name: notion_de_base_node
# Node

Un `Node` est une **entité**

---
template: notion_de_base_node

<center>
  <img src="images/node_detail_0.svg">
</center>

Avec

---
template: notion_de_base_node

<center>
  <img src="images/node_detail_1.svg">
</center>

Avec
* des **propriétés** 


---
template: notion_de_base_node

<center>
  <img src="images/node_detail_2.svg">
</center>

Avec
* des propriétés 
* un **label** 

Un label est une étiquette apposé sur le noeud.

---
template: notion_de_base_node

<center>
  <img src="images/node_detail_3.svg">
</center>


Avec
* des propriétés 
* un ou **plusieurs labels** 

Les labels servent également à l'indexation.

---
name: notion_de_base_relationship

# Relationship

Une `relationship` est une **entitée**


---
template: notion_de_base_relationship

<center>
  <img src="images/relationship_details_0.svg">
</center>

Avec
* un noeud de **départ** et un noeud d'**arrivé**



---
template: notion_de_base_relationship

<center>
  <img src="images/relationship_details_1.svg">
</center>

Avec
* un noeud de départ et un noeud d'arrivé
* un et un seul **type**

---
template: notion_de_base_relationship

<center>
  <img src="images/relationship_details_2.svg">
</center>

Avec
* un noeud de départ et un noeud d'arrivé
* un et un seul type
* et des **propriétés**


---
# Node et Relationship

## First-Class Citizen

Les deux types sont de la même importance, il n'y a pas d'entité privilégiée par rapport à une autre, comme la table définie en SQL et la jointure comme un moyen de relier les tables.

--

## Instance vs classe

Chaque entité est autonome dans sa définition. Il n'y a pas de **schéma dans la base** qui décrit ce qu'est un auteur ou un livre.

<center>
	<img src="images/no_schema.svg">
</center>



---
# SQL vs Graphe
Passage obligatoire, après la théorie

---
class: inverse middle center
# Un peu de théorie

---
# Plan un peu de théorie

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