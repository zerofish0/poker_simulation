# Les probabilités et le dénombrement dans le poker
## Télécharger l'exécutable
Pour une utilisation plus simple, téléchargez simplement l'exécutable windows disponible dans le dossier (`executable/`) ou à [cette addresse](https://www.mediafire.com/file/o4nacx9ot3om1pg/poker_simulation.exe/file)

## Prérequis
- Python 3.12 ou version supérieure
- Git (facultatif)

## Installation
1. Cloner le dépôt :  
```bash
git clone https://github.com/zerofish0/poker_simulation.git
```

ou télécharger directement le dépôt depuis GitHub.

2. Se placer dans le répertoire du projet :

```bash
cd poker_simulation
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python3 main.py
```

## Fonctionnement interne

Le programme parcourt toutes les mains possibles (`ALL_POSSIBLE_HANDS`) et teste si chaque main valide une combinaison spécifique (paire, double paire, brelan, quinte, flush, full, carré, straight flush, royal flush, hauteur). Les résultats sont ensuite comptabilisés pour chaque catégorie.

