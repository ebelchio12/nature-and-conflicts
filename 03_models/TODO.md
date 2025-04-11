# Models to try

### 1. Rainfall -> GDP change
Irem will tidy this up.

### 1b. Rainfall + temperature rise -> GDP change
(Irem)

### 1c. Rainfall after separating based on mean temperature
(Irem)

### 2. GDP change -> protests
(Felicia)

Target:
- was there an event? (`bool`)
- the number of events (`int`)
- high protest threshold (`bool`) (?)

Feats:
- `Year`
- `gdp`
- `gdp_g` (normalized first derivative of `gdp`)
- `oil_rent` (as a feature or as a primary partioning of data?)
- `democracy_polity`
- `ethnic_fractionation_index`

Mostly classification, but regression for number of events.

### 3. Rainfall -> protests
(Irem)

Excluding GDP-related measures (because they may not capture people's hardships properly).

Target:
- was there an event?
- the number of events
- high protest threshold

Features from 2.

### 4. Modeling the "troubled 20"
(Guga)

Features:
- all feats (too much?)
- choose feats after PCA
- Feats from 2.

Target:
- number of people protesting
- fraction of population protesting

Estimators:
- catboost
- and all the other methods already tried

Do a train-test split, try different models, pick the best one with RMSE as a measure. With the best model, use `GridSearchCV` to search over the optimum hyperparameters. (For tree-based ensemble models, `n_estimators`, `learning_rate`, `max_depth`).

### 5. Democracy polity index prediction
(Ewerton)

Features:
- rainfall variation
- percent agriculture
- gdp per capita
- `gdp_g` (variation in gdp normalized)

Target:
- `democracy_polity`

Estimators:
- kNN regression
- random forests
- xgboost

### 6. Democracy index vs. number of protests
(Ewerton)

Hypothesis: the number of protests are actually higher when the democracy index is higher (because people are less repressed?). Or at least it's a nonmonotonic relationship?

Features:
- democracy index
- gdp
- gdp_g

Target:
- number of events
- total number of people at events

Estimators:
- kNN
- random forest
- xgboost