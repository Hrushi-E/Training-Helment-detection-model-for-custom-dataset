# Training-Helmet-detection-model-for-custom-dataset
This repo consists of step by step procedure. I trained my "helmet detection model on my custom dataset" using YOLOV3 and alexyAB's Darknet repo.


Here I am using it for "Helmet detection" mainly. Using this model, we will be able to detect the following 5 objects.

1. Helmet: The human head without a helmet/ just a helmet is labeled as "Helmet."

2. No-Helmet: The human head without a helmet is labeled as "No Helmet."

3. Person: The person/ human is labeled as a "Person."

4. Motorcycle: The motorbike/ motorcycle in the image is labeled as "Motorcycle."

5. Registration Plate: The registration plate of bike(any) is labeled as "Registration Plate".


In the training of the model,

Step 1: I first downloaded the images that contain all or either of the helmet, person/human, human head, motorcycle, registration plate from various sites like Google Open Image Dataset, Kaggle Datasets, Image download via Google, etc

I downloaded 4000 images for training the model. The exact partition is given below.

Helmet: 800

No Helmet: 800

Person: 800

Motorcycle: 800

Registration Plate: 800


Step 2: Then, I created the labels for the images manually using the labelImg tool( https://github.com/HumanSignal/labelImg ). This helped me to create label files that are suited for yolov3.

This Repo contains how I did the above two steps.

Step 3: Then I uploaded images to drive for easy working with images in Google Colab. The colab notebook "My custom Training model.ipyb" contains the code and detailed instructions 
on how I trained and tested.

Resources and References:

1. The AI Guy youtube Channel: https://www.youtube.com/@TheAIGuy
2. Custom Training by Thw AI GUY: https://www.youtube.com/watch?v=10joRJt39Ns
3. ALexyAB's Darknet Repo



