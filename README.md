# Classifying-Brain-Tumour-Using-CNN
In the recent times, we have been seeing a massive raise in brain stroke cases all over the world. Stroke is one of the leading causes of the death worldwide these days. About 1/5th of patients with an acute stroke dies within a month of event and at least 1/2 of those who survive are left with physical disability. So, we have developed a model to predict whether a person is affected with brain stroke or not. so, on top of this we have also created a Front-End framework with Tkinter GUI where we can input the image and the model will try to predict the output and display it on the window.

# Base paper
https://www.academia.edu/73710547/Brain_Tumor_Detection_using_Deep_Learning

# Algorithm Description
So, we have used **Convolutional neural networks** to identify whether a person has brain tumour or not, as we all know, how sophisticated CNNs are and how they can learn almost anything like a brain does, this can help us save a lot of time and also giving almost accurate predictions for the disease. As we discussed convolutional neural networks are very sophisticated and more advanced version of neural networks, these are very superior to other neural networks which works better with images and audio/speech input signal. A CNN network comprises of 3 important layers such as a convolutional layer, pooling layer and fully connected layer. we can have as many layers as possible depending on the domain and project we are working on.

**Reference:**
https://www.ibm.com/cloud/learn/convolutional-neural-networks

# How to Execute?
So, before execution we have some pre-requisites that we need to download or install i.e., anaconda environment, python and a code editor.
**Anaconda**: Anaconda is like a package of libraries and offers a great deal of information which allows a data engineer to create multiple environments and install required libraries easy and neat.

**Download link:**
https://www.anaconda.com/

**Python**: Python is a most popular interpreter programming language, which is used in almost every field. Its syntax is very similar to English language and even children and learning it nowadays, due to its readability and easy syntax and large community of users to help you whenever you face any issues.

**Download link:**
https://www.python.org/downloads/

**Code editor**: Code editor is like a notepad for a programming language which allows user to write, run and execute program which we have written. Along with these some code editors also allows us to debug, which usually allows users to execute the code line by line and allows them to see where and how to solve the errors. But I personally feel visual code is very good to work with any programming language and makes a great deal of attachment with user.

**Download links:**
https://code.visualstudio.com/Download, 
https://www.jetbrains.com/pycharm/download/#section=windows

# Steps to execute.
1. Install the prerequisites mentioned above.
2. open anaconda prompt and create a new environment.
  1. conda create -n "env_name"
  2. conda activate "env_name"
3. Install necessary libraries from requirements.txt file provided.
4. Run pip install -r requirements.txt or conda install requirements.txt 
(Requirements.txt is a text file consisting of all the necessary libraries required for executing this python file. If it gives any error while installing libraries, you might need to install them individually.)
5. Run main.py or main.ipynb file on jupyter notebook.

# Data Description
The model is trained on MRI scanned brain tumor images collected from kaggle data repository, Before training the model, the images have gone through some preprocessing, such as Data augmentation and Images have being resized to fit to the model.

# Issues faced.
1. Install each library if you face any issue installing them through requirments.txt
2. Adding path to environment variables in order to run python files and to use anaconda environment in code editor, specifically in visual studio code.

# Evaluation metrics
Evaluation metrics are considered as one of the most important steps in any machine learning and deep learning projects, where it will allow us to evaluate how good our model is performing on the new data or on unseen data. There are a lot of evaluation metrics such as **confusion matrix, roc_auc curver, f1_score, recall, precision** and each of which work for specific problem we deal. So, for our project we have gone with confusion matrix the OG of every evaluation matric, where using it, we have calculated the accuracy and other metric, which has given a conclusion that the model is performing very well on new data.

# Note:
The Model weights and dataset haven't been provided here since, it didn’t allow us, obviously.
Feel free to contact if you face any issues.
abhiabhinay629@gmail.com

**Credits to the owner of the Research Paper for giving reference to the project.**
