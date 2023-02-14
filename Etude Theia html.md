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

## `https://elffe.theia.fr/learning/exam/access/X`







