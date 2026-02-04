# Scorigami Prediction
A machine learning tool to predict the occurence of unique game scores in NFL games

## Introduction
NFL football games tend to end in a few common scores because scoring occurs in discrete intervals with different values for each scoring type. While some final game scores have occurred thousands of times in the history of the NFL, some scores have only happened a few times and some scores have never happened... yet. Fans have come up with the name "scorigami" to refer to a game which ends in a new final score. You can see the below video for some more information on Scorigami:

https://www.youtube.com/watch?v=FHNwUiu_8Eg

This project demonstrates the use of machine learning techniques to predict the occurence of scorigami. An eventual objective will be to develop a program that will be able to predict in real-time the probability that an ongoing NFL game will end in a scorigami.

## Dataset
The dataset used in this project is available as a .npy file. This dataset is an array of shape (6473, 60, 16); 6473 games from the 2021 through 2024 NFL seasons where each game is divided into 60 observations (one at each minute of regulation time gameplay) of 16 variables which tally the cumulative number of different scoring events and game statistics. These data were obtaiend through the nflreadpy API.

## Project Contents
* **X.npy and y.npy:** The numpy arrays that are used to train the model
* **X_features.csv:** feature labels corresponding to the data contained in X.npy
* **getData.py:** A python script that queries the NFLreadpy API and outputs a cleaned numpy array. Variables may be adjusted to change the data used in the array.
* **scoirgami.ipynb:** The jupyter notebook containing the machine learning models, metrics, and evaluations
