# Machine Learning
This is the documentation for ML models. This model attempts to solve VRP problem, We use Reinforcement Learning - Deep Q Learning Unsupervised Learning for this problem.

## Inputs and Outputs
1. The inputs are longitude and latitude coordinates, which will be taken from Open Street Maps(OSM) API
2. The outputs are the routes which can be visualize into OSM API, and the distance which then we can get the time, etc.

## Files and Dependencies
There are few files in this project, the main one is vrp_dqn_model.tflite which contains the RL-DQN algorithm and few python files containing the algorithm so that the model can produce routes for VRP.

1. libaries = this file contains the library used for this project to work, it is not needed to import this file as importing libraries will be done in each files.
2. logic = this contains algoritms needed to run the model, this includes ReplayBuffer(), VRPAgent(), train_vrp_agent(). This file is a neccesity for the model to work, so this must be included when running the model
3. main = this includes the algorithm to convert the coordinates gotten from the user to distance_matrix which is crucial for the logic alogirithms. This must be included.
4. test = this is for testing the tflite model, this is not neccesary to be included as this is file to check wheter or not the tflite is successfuly exported.
5. vis = this contains the visualization algorithm using folium which will be in html file, this is a documentation that the algorithm works and can be used as reference for MD as the visualization code.

## Notes
As Reinforcement Learning is Unsupervised Learning, there wont be a training or test datasets needed
