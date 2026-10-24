# missingness-coupling-forge

## Français

Générer des valeurs manquantes selon un mécanisme déclaré et rejouable.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m missingness_coupling_forge examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Crée une copie masquée et un journal des probabilités MCAR ou MAR logistiques déclarées. Les prédicteurs MAR doivent rester observés ; distingue lacune préexistante et masquage ajouté.

### Limites

Mécanisme imposé pour simulation, pas identifié sur des données réelles ; aucune conclusion causale ni garantie d’imputation. Ordre des lignes conservé, contenu utilisateur original non modifié.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Generate missing values under a declared replayable mechanism.

Synthetic data; no network access or secret required.

```sh
python -m missingness_coupling_forge examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Creates a masked copy and receipts for declared MCAR or logistic MAR probabilities. MAR predictors must remain observed; distinguishes preexisting missingness from added masking.

### Limits

Mechanism imposed for simulation, not identified from real data; no causal conclusion or imputation guarantee. Row order preserved and original user content unchanged.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Generar valores ausentes según un mecanismo declarado y reproducible.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m missingness_coupling_forge examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Crea copia enmascarada y recibos de probabilidades MCAR o MAR logísticas declaradas. Predictores MAR deben seguir observados; distingue ausencia previa y máscara añadida.

### Límites

Mecanismo impuesto para simulación, no identificado de datos reales; sin conclusión causal o garantía de imputación. Orden conservado y contenido original sin modificar.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://doi.org/10.1093/biomet/63.3.581
