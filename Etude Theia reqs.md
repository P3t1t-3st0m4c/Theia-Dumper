# Theia

## Page d'accueil (https://elffe.theia.fr/learning/exam/index)
---
### POST `/learning/exam/index`
#### Paramètres :
---
Nom | Type | Description
--- | --- | ---
`grid_3f31d346c14f369a4c47908d3a0d82e3[id][from]` | Integer | `L'ID de l'examen`
`grid_3f31d346c14f369a4c47908d3a0d82e3[title][from]` | String | `Le titre de l'examen`
`grid_3f31d346c14f369a4c47908d3a0d82e3[type][from][]` | String | `Le type de l'examen`
`grid_3f31d346c14f369a4c47908d3a0d82e3[assessmentStatus][from][]` | Integer | `Le status de l'examen`
`grid_3f31d346c14f369a4c47908d3a0d82e3[tag][from]` | Object ({}) / Unknown | `Le tag de l'examen ?`

### Valeurs possibles pour `grid_3f31d346c14f369a4c47908d3a0d82e3[type][from][]` :

Valeur | Description
--- | ---
`"exam"` | Examen
`"conference"` | Conférence

### Valeurs possibles pour `grid_3f31d346c14f369a4c47908d3a0d82e3[assessmentStatus][from][]` :

Valeur | Description
--- | ---
`0` | A venir
`1` | En cours
`2` | Fini
`3` | Aujourd'hui


### Réponse :
> Code : 302  
> Redirection vers : https://elffe.theia.fr/learning/exam/index  

Redirige vers la page d'accueil des examens avec les paramètres lié à la requête changés dans la page d'accueil des examens.  

### ***Exemple*** :

```http
POST /learning/exam/index HTTP/2
Host: elffe.theia.fr
Cookie: THEIASESSIDB=...

grid_3f31d346c14f369a4c47908d3a0d82e3%5Bid%5D%5Bfrom%5D=123456&grid_3f31d346c14f369a4c47908d3a0d82e3%5Btitle%5D%5Bfrom%5D=TEST&grid_3f31d346c14f369a4c47908d3a0d82e3%5Btype%5D%5Bfrom%5D%5B%5D=0&grid_3f31d346c14f369a4c47908d3a0d82e3%5BassessmentStatus%5D%5Bfrom%5D%5B%5D=2&grid_3f31d346c14f369a4c47908d3a0d82e3%5Btag%5D%5Bfrom%5D=%7B%7D
```
### ***Beautifyed*** :
```http
POST /learning/exam/index HTTP/2
Host: elffe.theia.fr
Cookie: THEIASESSIDB=...

grid_3f31d346c14f369a4c47908d3a0d82e3[id][from]=123456
grid_3f31d346c14f369a4c47908d3a0d82e3[title][from]=TEST
grid_3f31d346c14f369a4c47908d3a0d82e3[type][from][]=0
grid_3f31d346c14f369a4c47908d3a0d82e3[assessmentStatus][from][]=2
grid_3f31d346c14f369a4c47908d3a0d82e3[tag][from]={}
```
### ***Réponse*** :
```http
HTTP/2 302 Found
Location: /learning/exam/index

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="refresh" content="0;url='/learning/exam/index'"/>

        <title>Redirecting to /learning/exam/index</title>
    </head>
</html>
```
---
### GET `/learning/exam/index?grid_3f31d346c14f369a4c47908d3a0d82e3[_reset]=`
#### Réponse :
> Code : 302
> Redirection vers : https://elffe.theia.fr/learning/exam/index

Redirige vers la page d'accueil des examens en réinitialisant les paramètres de la page d'accueil des examens.

---

## Page de correction (https://elffe.theia.fr/learning/exam/access/`XXXXXX`)

### GET `/learning/exam/access/XXXXXX`
#### Paramètres :

---

## Page d'examen (https://elffe.theia.fr/playtest/`XXXXXX`/`YYYYYYYY`)



---

## Requête de sélection d'une réponse (	https://elffe.theia.fr/playtest/validateandanswer/`XXXXXXX`/`YYYYYY`)

### POST `/playtest/validateandanswer/XXXXXXX/YYYYYY`

#### Paramètres de l'url :

---

Nom | Type | Description
--- | --- | ---
`XXXXXXX` | Integer | `L'ID de l'examen`
`YYYYYY` | Integer | `L'ID de la question`

#### Paramètres :

---

Nom | Type | Description
--- | --- | ---
`numeric_responses` | Object ({}) | `Les réponses aux questions`
`pending` | Boolean | `Si l'examen est en attente`
`synched` | Boolean | `Si l'examen est synchronisé`
`question_state` | Integer | `Le status de la question`

### Valeurs possibles pour `question_state` :

Valeur | Description
--- | ---
`0` | Aucune réponse
`1` | Réponse en cours
`2` | Réponse validée

### Valeurs possibles pour `numeric_responses` :

Valeur | Description
--- | ---
`"XXXXXXX"` | `L'ID de la question`
`"YYYYYY"` | `La réponse à la question`

### Réponse :

> Code : 200

### ***Réponse*** :

```json
{
    "success":true
}


