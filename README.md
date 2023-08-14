# Training-Helment-detection-model-for-custom-dataset
This repo consists of step by step procedure of I trained my "helmet detection model on my custom dataset" using YOLOV3 and alexyAB's Darknet repo.


Here I am using it for "Helment detection" mainly. Using this model, we will be able to detect following 5 objects.

1. Helmet: The human head without helmet/ just helmet is labeled as "Helmet".

2. No-Helmet: The human head without helmet is labeled as "No Helmet".

3. Person: The person/ human is labeled as "Person".

4. Motorcycle: The motorbike/ motorcycle in the image is labeled as "Motorcycle".

5. Registration Plate: The registration plate of bike(any) is labeled as "Registration Plate".


In the training of the model,

Step1: I first downloaded the images that contains all or either of helmet, person/human, human head, motorcycle, Registraion plate from various sites like google image, google, etc... 

I downloaded 4000 images for training the model. The exact partition is given below.

Helmet: 800

No Helmet: 800

Person: 800

Motorcycle: 800

Registration Plate: 800


Step2: Then I created the labels for the images manually using labelImg tool( https://github.com/HumanSignal/labelImg ). This helped me to create label files that are suited for yolov3.

This Repo contains how I did the above two steps.

Step3: Then I uploaded images to gdrive for easy working with images in Google colab. The colab notebook "My cutom Training model.ipyb" contains the code and detailed instructions 
on how I trained and tested.

Resources and References:

1. The AI Guy youtube Channel: https://www.youtube.com/@TheAIGuy
2. Custom Training by Thw AI GUY: https://www.youtube.com/watch?v=10joRJt39Ns
3. ALexyAB's Darknet Repo



