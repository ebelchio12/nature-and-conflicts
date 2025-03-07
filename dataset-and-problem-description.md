Identify the dataset you will be working with. Describe the dataset and the problem you are looking to solve. List the stakeholders of the project and company key performance indicators (KPIs) (bullet points).

Idea 1:
Inspired by the following paper: https://www.jstor.org/stable/10.1086/421174?seq=1

For certain countries, such as those in Sub-Saharan Africa, agriculture is a proponent industry holding a large share of GDP. Hence, increasing climate fluctuations has a large influence on these coutnries' GDP as well as other societal outcomes including civil unrest. As global climate patterns continue to shift, understanding how climate variability affects national economies is critical to predicting future challenges. Building on Miguel, Satyanath and  Sergenti's 2004 paper, we aim to build a predictive model on how climate factors, e.g., temperature fluctuations, precipitation, extreme weather events, natural disasters, ground water availability, etc. impact GDP in various countries who largely depends on agriculture as their main source of economic growth. Additionally, it will examine how these economic pressures may, in turn, contribute to social instability and civil conflicts. Through these models, we aim to provide tools that may be of interest to policymakers and international organizations seeking to mitigate the adverse effects of climate change and prevent its escalation into broader conflict.

The datasets we plan to work with:
 * https://growup.ethz.ch/rfe
   - Dataset of different type of conflicts by year, group, and country. Types of conflict include territorial,  governmental.
   - dummy variables whether conflict is an onset of one, or just an ongoing one
 * https://ourworldindata.org/grapher/average-precipitation-per-year
   - lots of different datasets by country, by year e.g., GDP, precipitation, temperature anomalies, natural disasters 
 * https://search.earthdata.nasa.gov/search?g=G1627839617-GES_DISC&q=precipitation&lat=0.5625&long=1.6875&zoom=0
   - climate data that's a lot more granular than ourworldindata

General plan:
  * Identify countries where agriculture has a large share of GDP (ourworldindata) ~ 50% consistently across the past 20 years
  * Examine how much data we have for each of these countries in terms of conflict and predictors
  * Determine the range of year we'll be working with (10 vs 15 vs 20 years, etc.) depending on how much data is available across the different countries
  * Exploratory data analysis
  * Model building/comparisons
    
Idea 2:
Similar to above, but taking a slightly different spin by focusing on protests in the US and/or Europe. This paper and discussion may be helpful: https://onlinelibrary.wiley.com/doi/10.1111/eufm.12539#:~:text=For%20instance%2C%20Hadzi%2DVaskov%2C,in%20consumer%20and%20business%20confidence.
https://www.imf.org/external/pubs/ft/fandd/2021/08/economics-of-social-unrest-imf-barrett-chen.htm

The intersection of economic instability and social unrest has been previously documented. For example, in western countries, some evidence has emerged that social disruptions are influenced by factors such as inflation, unemployment, income inequality, and economic stagnation. We propose models to predict how different measures of economic instability may be associated with triggering protests and public dissatisfaction in Western countries. Some of these measures may include income inequality, rate of unemployment, living costs (price of staples), and the stock market. By focusing on the economic stressors—ranging from rising living costs to the erosion of job security—this analysis seeks to explore how economic hardships can fuel public discontent and ultimately spark large-scale protests. Also would be interesting to see how this trend may be followed by increased political polarization. 

Datasets we plan to work with:
From this compilation by Yale (https://guides.library.yale.edu/c.php?g=956915&p=6961578), we're interested in:
 * https://dataverse.harvard.edu/dataverse/crowdcountingconsortium/
   - Dataset of US protests, split by event, includes dates, topics, and valence (i.e., right wing, left wing, neither)
 * https://farpo.eu/
   - Dataset of far-right protests in Europe between 2008-2018, has country names and actors of protests
 * IPUMS (current population survey) https://cps.ipums.org/cps-action/variables/group
   - Data on population/household income, unemployment, US-based information
   - Might have to find similar things for European contingencies if we plan to also use European countries in model
 * https://www.bls.gov/charts/consumer-price-index/consumer-price-index-average-price-data.htm
   - Food prices data in the US
   - Might have to find similar things for European contingencies if we plan to also use European countries in model


Idea 3:

