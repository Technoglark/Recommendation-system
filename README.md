# 📝 Recommendation system📝
Overview

This project implements a recommendation system that suggests items based on user preferences and similarity metrics. The system is demonstrated with both synthetic test data and real-world apartment listing data.

## Project Structure
 - main.ipynb: The main Jupyter notebook containing the implementation and experiments

 - recommendation.py: Module containing the RecommendationSystem class implementation

 - apartments_domovita_*.csv: Real-world apartment listing datasets (1-3 room apartments)

## Key Components 💡
 - RecommendationSystem Class

     - Distance-based similarity metrics

     - Mean calculation of visited items

     - Prediction of recommended items based on similarity to the mean

## Experiments :chart_with_upwards_trend:
#### Synthetic Data Test 
 
 - Generates two clusters of 2D and 3D points 

 - Demonstrates the recommendation algorithm on this test data

 - Visualizes the clusters, visited points, mean point, and recommendations

#### Real Apartment Data Test

 - Uses apartment listing data with features:

   - Price

   - Price per square meter

   - Area

   - Floor
  
   - Metro station
  
   - Distinct
  
   - Time to metro

 - Shows both results with data scaling and without

 - Includes visualizations of the recommendation results

