# Lit les fiches du dossier kb/ et affiche le titre et la source de chacune.
# À lancer depuis la racine du dépôt, car le chemin "kb" est relatif.

# Path est une classe du module pathlib (bibliothèque standard de Python).
from pathlib import Path
from answer import Answer

# dossier est un objet Path qui contient l'adresse "kb".
dossier = Path("kb")

# Liste des fichiers .md de kb/, triés par ordre alphabétique.
fichiers = sorted(dossier.glob("*.md"))

# À chaque tour, "fichier" désigne la fiche suivante de la liste.
for fichier in fichiers:
    # Lit tout le texte de la fiche (utf-8 pour garder les accents).
    texte = fichier.read_text(encoding="utf-8")
    # Découpe le texte en lignes et garde les 5 premières (l'en-tête).
    liste_de_lignes = texte.splitlines()[:5]
    # Examine ces lignes une par une.
    for ligne in liste_de_lignes:
        # Si la ligne commence par "titre:", on range le titre dans "titre" ;
        # si elle commence par "source:", on range la source dans "source".
        # Dans les deux cas, on enlève le préfixe et les espaces autour.
        if ligne.startswith("titre:"):
            titre = ligne.removeprefix("titre:").strip()
        elif ligne.startswith("source:"):
            source = ligne.removeprefix("source:").strip()
    answer = Answer(titre, [source])
    print(answer.texte, answer.sources)
