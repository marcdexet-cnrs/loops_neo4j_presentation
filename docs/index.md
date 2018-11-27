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
# La gestion des données
Un problème vieux comme l'humanité

## Un problème guidé par les moyens technologiques et le coût.
* argile, papirus, papier, ...
* bandes magnétiques, disques, mémoire

.left-column[
.center[*Bandes magnétiques*]
<center>
	<img src="images/bandes_magnetiques.png" width="300px">
</center>
]

.right-column[
.center[*Disques durs*]
<center>
	<img src="images/ibm350.jpg" width="300px">
</center>
]

---
# Base graphe, un vieux concept

## CODASYL (Conference on Data Systems Languages)
* Réseau utilisé en _COBOL_.
* Navigation par pointeur vers les enregistrements liés.

.left-column[
.center[*Modèle hiérarchique*]
<center>
	<img src="images/hierachique.png" width="200px">
</center>
]

.right-column[
.center[*Modèle en réseau*]
<center>
	<img src="images/reseau.png" width="200px">
</center>
]

.reset-column[
* Accès aux données en mode _navigationnel_   
en mentionnant les relations _explicitement_   
en passant d'un _record_ à un autre.
]

.footnote[.small[ [Cours "bases de données réseau et hiérarchiques" sur sgbd.developpez.com](https://sgbd.developpez.com/tutoriels/cours-complet-bases-de-donnees/?page=bases-de-donnees-reseaux-et-hierarchiques)]]

???
Image http://www.cs.aucegypt.edu/~csci253/DBConcepts%20v2.htm


---
# L'hégémonie des Base de Données Relationnelles

## Approche par table de données et jointure par clef.
<center>
	<img src="images/SGBD_RELATIONNEL.png" width="400px">
</center>

## Un standard de fait
* **SQL** langage de manipulation abstrait
* **ACID** (Atomicité, Cohérence, Isolation, Durabilité)
* Plusieurs rôles : DBA, développeurs

_Oracle, Postgres, MySQL, MariaDB, SQLServer, ..._


---
name: graph_renew_sql
# Base graphe, le renouveau NoSQL

---
template: graph_renew_sql

## Les limites de l'approche relationelle
* Peu adapté à des domaines très évolutifs (agilité, first time to market)
 * Processus lourd avec nombreux rôles
* ACID => Problèmes de performance complexes dans certains contextes
 * bases distribuées, sharding

--

## Emergence du mouvement NoSql

.center[.big[**N**ot **O**nly **SQL**]]


???
 * Atomicité &rarr; transaction
 * Cohérence &rarr; conservation de l'intégrité
 * Isolation
 * Durabilité
* Vision unifiée: [12 règles de CODD](https://fr.wikipedia.org/wiki/12_r%C3%A8gles_de_Codd)


---
template: graph_renew_sql

## NoSQL, un mouvement venu du terrain
* Initié par les acteurs du web, du big data
* Solutions pensées *par* et *pour* des développeurs

--

## Disparité des approches
* Avant tout recherche de solutions en dehors des bases SQL.

--

### Propriétés **souvent** (mais pas toujours) associées :
* Open source
* API first (REST)
* Grande influence du langage (ERLANG, javascript, java, C/C++)
* Distribuée
* Simples à installer (...)
* Autonomie du développeur

---
template: graph_renew_sql

Légitimation par le théorème CAP

## CAP (Availability, Consistency, Partition tolerance)
* Un SGDB ne pourra jamais avoir que 2 propriétés sur 3.

<center>
	<img src="images/cap_theorem.png" width="500px">
</center>


---
# Base graphe, le renouveau NoSQL
(discutable)

## Passage de ACID à BASE
* **ACID**
 * **A**tomicity &rarr; transaction
 * **C**onsistency &rarr; intégrité d'une transaction à une autre
 * **I**solation &rarr; pas d'interférence entre transactions
 * **D**urability &rarr; la pérénité est assurée, même en cas de défaillance
--

* **BASE**
 * **B**asically **A**vailable &rarr; disponibilité la plupart du temps
 * **S**oft-state &rarr; la consistence n'est pas toujours garantie
 * **E**ventually consistent &rarr; la consistence arrivera à un moment

--

## Proposition d'autres modèles
* Clef-valeur
* Document
* Colonne
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
# Les acteurs du monde des bases de données

## Les bases graphes sont très minoritaires

<center>
  <img src="images/2018-11-27_DB-Engines_Ranking_per_database_model_category_SCORE.png" width="600px">
</center>


.footnote[.small[https://db-engines.com/]]

---
# Les acteurs du monde des bases de données

## Les bases graphes intéressent de plus en plus

<center>
  <img src="images/2018-11-27_DB-Engines_Ranking_per_database_model_category_all.png" width="800px">
</center>


.footnote[.small[https://db-engines.com/]]


---
# Les acteurs du monde des bases de données

## Parmis ces bases, Neo4j

<center>
  <img src="images/2018-11-27_DB-Engines_Ranking.png" width="800px">
</center>


.footnote[.small[https://db-engines.com/]]


---
# Les acteurs du monde des bases de données

## Parmis ces bases, Neo4j

<center>
  <img src="images/2018-11-27_DB-Engines_Ranking_graph.png" width="600px">
</center>


.footnote[.small[https://db-engines.com/]]

---
class: inverse middle center

# Neo4j


---
# Neo4j, la société

Neo4j est développé par la société suédoise _Neo4j Inc._ 

## Histoire
* **2000**: Constat d'échecs à gérer des données très connectées
* **2002**: Premier prototype de Neo4j
* **2007**: Création de la société Neo4j
* **2010**: Neo4j V1 en 2010 (GPL)
* **2016**: Neo4j V3

## Clients 
* Walmart, UBS, ebay, Cisco, LinkedIn, HP, Airbus...


???
Emil, Peter et Johan se battent pour trouver des connexions entre données dans une base Informix.  
Les requêtes deviennent très complexes et inmaintenables.

Series A and Series B rounds are funding rounds for earlier stage companies and range on average between $1M–$30M.

Series C rounds and onwards are for later stage and more established companies. These rounds are usually $10M+ and are often much larger.

---
# Neo4j, le produit

* Développé en open-source (https://github.com/neo4j/neo4j)
* Moteur écrit en Java

## Double licence

* **Community** :  GPL v3
* **Enterprise**: AGPL avec licence commerciale  
étend la version community avec des composants en _closed source_.

## Usage Open source
La version Entreprise peut-être [utilisée pour des produits open-source](https://neo4j.com/Open-Source/) 

.center[.quote["If you are building an open source project to benefit the world at large, we are pleased to offer Neo4j Enterprise Edition under the AGPL for this express use."]]

---
# Neo4j, le produit

## Base graphe 
* Transactionnelle ACID
* Haute disponibilité

## Plusieurs drivers

* _Officiels_ : java, python, javascript, .Net.
* _Community_ : Ruby, PHP, R, Go, Erlang, C/C++, Clojure, Perl, Haskell

## Plusieurs API 
* Endpoint REST like 
* Protocole BOLT : connecté binaire sur TCP ou web sockets.

## Un langage CYPHER
```cypher
CREATE (p:Person {firstName:{name}}) RETURN p
```

---
class: inverse middle center

# Notions de base
Culture Neo4j

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

* `Node` et `RelationShip` &rarr; même *importance*, 
* Pas de type privilégié par rapport à un autre
 * Comme les tables en SQL et la jointure comme un moyen de relier les tables.

--

## Pas de schéma
Absence de **schéma dans la base** qui décrit ce qui doit être.

<center>
	<img src="images/no_schema.svg">
</center>

--

.quote[.big[La cohérence doit être garantie par le processus]]

---
# Label et Type

---
# Properties

Les  propriétés sont un dictionniaire de clef-valeur
* clef : chaîne de caractères
* valeur : scalaire ou liste de scalaire

## Types de scalaire ou liste de scalaire
.left-column[
* _Numérique_ :
 * Integer
 * Float
* Chaîne de caractère
* Booléen
]

.right-column[
* _Spatial_:
  * Point
* _Temporel_:
  *  Date
  *  Time
  *  LocalTime
  *  DateTime
  *  LocalDateTime
  *  Duration
]

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
# SQL vs Graphe
Passage obligatoire, après la théorie



---
class: inverse middle center
# Sous le capot
* Neo4j utilise assez habilement des indexes et de  l'adjacence. Les indexes pour localiser les points de départs