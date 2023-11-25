# Theia

## Page d'accueil (https://elffe.theia.fr/learning/exam/index)
---
## `/learning/exam/index`

## Tableau des examens :  

### Dans un formulaire (`<form>`)
Id : `grid_3f31d346c14f369a4c47908d3a0d82e3`  
Action : `POST /learning/exam/index`

## 🔽

### Tableau (`<table>`)  
Classes : `alpaca`, `table`, `table-striped`, `table-hover`

## 🔽

### Rangée (`<tr>`)  
Data-id : `Id de l'examen` (ex: `123456`)  
Classes : `grid-row-cells`, `even`

## 🔽

### Colonne (`<td>`)

Type | Classes | Elements | Description
--- | --- | --- | ---
`Id` | `grid-column-id`, `align-right` | Text | Id de l'examen
`Type` | `grid-column-type`, `text-center` | `<div>` | Type d'examen
`Status` | `grid-column-assessmentStatus`, `text-center` | `<span>` | Status de l'examen
`Titre` | `grid-column-title`, `table-textoverflow` | Text | Titre de l'examen
`Date de début` | `grid-column-startDate`, `text-center` | Text | Date de début de l'examen
`Date de fin` | `grid-column-endDate`, `text-center` | Text | Date de fin de l'examen
`Durée` | `grid-column-assessmentOptions_timeLimit` | Text | Durée de l'examen
`Status de la session` | `grid-column-sessionStatus`, `text-center` | `<span>` | Status de la session
`Temps additionnel (Accordé)` | `grid-column-individualAdditionalTime`, `text-center` | `<span>` | Temps additionnel (Oui/Non)
`Temps additionnel (Temps)` | `grid-column-extraTime`, `text-center` | `<span>` | Temps additionnel (Temps)
`Accès` | `grid-column-access`, `text-center` | `<span>` | Accès
`Actions` | `grid-column-__actions`, `last-column` | `<ul>` | Actions


#### Details de `Actions` (`<ul>`)

Forme :
```html
<ul>
    <li>
        <a></a>
    </li>
</ul>
```

Details de `<a>` :

Attribut | Valeur | Description
--- | --- | ---
`href` | Lien | Lien vers la page
`data-href` | Lien | Lien vers la page de correction / de l'examen
`target` | `_self` | Ouvre la page dans la même fenêtre
`ajax` | Bool | Ouvre la page en AJAX (true/false)

Exemple :
Attribut | Valeur
--- | ---
`href` | `#`
`data-href` | `https://elffe.theia.fr/learning/exam/access/114482`
`target` | `_self`
`ajax` | `1`

---

## Page d'examen (https://elffe.theia.fr/playtest/`XXXXXX`/`YYYYYYYY`)

## `/playtest/`**`XXXXXX`**`/`**`YYYYYYYY`**

## Pool de questions :

### 1. Dans un div (`<div>`)  
Classes : `zonePool`  
Id : `pool_`**XXXXX**  

## 🔽  
---
### 2. Div d'intro (`<div>`) (il peut y en avoir plusieurs)  
Classes : `textIntroPool`, `quest`, `intro`  

### 2. Div de question (`<div>`) (il peut y en avoir plusieurs)  
Classes : `quest`, `alpaca`  
Id : `pq_`**YYYYYY**  

---
## 🔽 (question)

### 3. Formulaire de question (`<form>`)  

## 🔽🔽🔽...  
---
### 4. Div de header (`<div>`)  
Classes : `panel-heading`, `question-heading`  
Contient : `<h4>`  

---
### 4. Div de body (`<div>`)  
Classes : `panel-body`  

## 🔽 (dans le body)  

### 4.1 Div de question (`<div>`)  
Classes : `question-content`  
Spécial : `player-mode="player"`  

## 🔽

### 4.2 Div de question (`<div>`)  
Classes : `enonQuest`  

---
## 🔽 (enonQuest)

### 4.2.1 Div de question (`<div>`)  
Classes : `textEnon`, `firstPart`  

## 🔽

### 4.2.2 Div de question (`<div>`)  
#### Bloc principal de la question  
#### Il contient plusieurs divs pour les différentes parties de la question  
Classes : `theia-container-block`  

## 🔽

### 4.2.3 Div de data (`<div>`)
Classes : `theia-text-block`
#### Contient les données de la question (texte, images, etc.)  
#### Le text block contient plusieurs `p` pour sauter des lignes, il y a aussi des `h2` pour les titres, des listes avec `ul` et `li`
---

### 4.3 Div de reponse (`<div>`)
Classes : `propQuest`

## 🔽

### 4.4 Div de reponse (`<div>`)
Classes : `form-group`

## 🔽

### 4.5 Input de reponse (`<input>`)
Classes : `form-control`, `mt5`
Id : `num_`**XXXXXX**`_`**YYYYYYY**
#### L'id est composé de 2 parties :   `num_`**XXXXXX**`_`**YYYYYYY**  
#### **XXXXXX** est l'id de la question  
#### **YYYYYYY** est inconnu pour le moment  

---
### 4. Div de footer (`<div>`)  
Classes : `panel-footer`  

## 🔽

### 4.1 Div de footer (`<div>`)
Classes : `row`

## 🔽

### 4.2 Div "non enregistré" (`<div>`)
Classes : `col-xs-12`, `pb5`, `col-sm-6`
#### Affiche un message si la question n'est pas enregistrée
```html
<div class="col-xs-12 pb5 col-sm-6">
    <span class="label label-danger">
        <i class="fas fa-exclamation-triangle"></i>
    Réponse non enregistrée
    </span>
</div>
```
#### N'est pas présent si la question est enregistrée

### 4.2 Div "d'enregistrement" (`<div>`)  
Classes : `col-xs-12`, `col-sm-6`  
#### Bouton pour enregistrer la question
```html
<div class="col-xs-12 col-sm-6">
    <a class="btn btn-warning">
        <span class="fas fa-download"></span>
        &nbsp;Enregistrer la réponse
    </a>
</div>
```
#### Change de couleur si la question est enregistrée
```html
<div class="col-xs-12 col-sm-6">
    <a class="btn btn-success">
        <span class="fas fa-downloadd"></span>
        &nbsp;Réponse enregistrée
    </a>
</div>
```












