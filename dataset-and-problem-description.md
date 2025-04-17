<h3>Motivation</h3>

For certain countries, such as those in Sub-Saharan Africa, agriculture is a proponent industry holding a large share of GDP. Hence, increasing climate fluctuations has a large influence on these countries' GDP as well as other societal outcomes including civil unrest. As global climate patterns continue to shift, understanding how climate variability affects economies is critical to prevent national and international conflicts. 

Building on [Miguel, Satyanath and  Sergenti's 2004](https://www.jstor.org/stable/10.1086/421174?seq=1) paper, we aim to build a predictive model on how climate factors, e.g., temperature fluctuations, precipitation, extreme weather events, and natural disasters impact economic factors such as GDP, commodity prices, income inequality, and eventually incidence and size of protests. We will be focusing on data from years 1990 - 2020. 

Through these models, we aim to provide tools that may be of interest to policymakers and international organizations seeking to mitigate the adverse effects of climate change and prevent its escalation into broader conflict.

<h3>Stakeholders:</h3>  

* Policymakers and government officials
* Humanitarian organizations
* International businesses

<h3>Question and KPIs:</h3>  

Q: Can we predict the incidence of protests in several regions in the world using climate and economic data?
KPI:
* Replicate models from paper above to predict GDP variations and number of protests with competitive R2 value as the paper (R2=0.2) 
* Predict protest incidences (whether protests happen or not) within a 70% accuracy, recall of >80% and false negative rate of 5%
* Create a user dashboard where users can get estimates for likelihood of protests given climate and economic data

<h3>General plan:</h3>  

* Exploratory data analysis
  * Identify regions of the world that are of interest: this may end up being specific countries, or general regions.
  * Narrow predictors
* Model building/comparisons
  * Start with simple linear regression
  * Examine whether time series analysis is appropriate
* Create user dashboard
    
<h3>Datasets:</h3>  

* Protest data: from this compilation by [Yale](https://guides.library.yale.edu/c.php?g=956915&p=6961578)
* Agriculture outputs, economic factors: [ourworld in data](https://ourworldindata.org/)
* Rainfall data: [CRU TS datasets](https://crudata.uea.ac.uk/cru/data/hrg/)
* Ethnic fractionalization index: [EUI Research Repository](https://cadmus.eui.eu/handle/1814/68317)




