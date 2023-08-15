# Training-Helmet-detection-model-for-custom-dataset
This repo consists of the procedure I followed for training my "helmet detection model on my custom dataset" using YOLOV3 and alexyAB's Darknet repo.

Here I am using it for "Helmet detection" mainly
Using this model, we will be able to detect the following 5 objects.

1. Helmet: The human head without a helmet/ just a helmet is labeled as "Helmet."

2. No-Helmet: The human head without a helmet is labeled as "No Helmet."

3. Person: The person/ human is labeled as a "Person."

4. Motorcycle: The motorbike/ motorcycle in the image is labeled as "Motorcycle."

5. Registration Plate: The registration plate of bike(any) is labeled as "Registration Plate".

I created two models based on different images I collected.

MODEL -1: IMAGES FROM OIDv4_ToolKit

I downloaded 4000 images for training the model. The exact partition is given below.

Helmet: 800

No Helmet: 800

Person: 800

Motorcycle: 800

Registration Plate: 800

This Repo contains how I downloaded images[ ].

Then I uploaded images to drive for easy working with images in Google Colab.

The colab notebook "My custom Training model_4000.ipyb" contains the code and detailed instructions on how I trained and tested.

Here is the output on test dataset:

![image](https://github.com/Hrushi-E/Training-Helment-detection-model-for-custom-dataset--using-Yolov3/assets/122773291/c91b533a-0bbd-4ead-b586-0f7529c3f803)






MODEL -2: IMAGE download from Various sites GOOGLE IMAGES, OIDv4_ToolKit etc for task specific.

In the training of the model,

Step 1: I first downloaded the images that contain all or either of the helmet, person/human, human head, motorcycle, registration plate from various sites like Google Open Image Dataset, Kaggle Datasets, Image download via Google, etc

I downloaded around 2800 images for training the model. The exact partition is very difficult to say( since in a somee image we label, I labelled all 5 also). But in and around, we can say

Helmet: 800

No Helmet: 800

Person: 800

Motorcycle: 800

Registration Plate: 800


Step 2: Then, I created the labels for the images manually using the labelImg tool( https://github.com/HumanSignal/labelImg ). This helped me to create label files that are suited for yolov3.



Step 3: Then I uploaded images to drive for easy working with images in Google Colab. The colab notebook "My custom Training model_2800.ipyb" contains the code and detailed instructions on how I trained and tested.

NOTE: For this model, I selected 10 % already trained iamges randomly as test and Here is the output on test dataset:

![image](https://github.com/Hrushi-E/Training-Helment-detection-model-for-custom-dataset--using-Yolov3/assets/122773291/23c14f6d-f09c-4108-b017-26212b0e8722)




Resources and References:

1. The AI Guy youtube Channel: https://www.youtube.com/@TheAIGuy
2. Custom Training by Thw AI GUY: https://www.youtube.com/watch?v=10joRJt39Ns
3. ALexyAB's Darknet Repo



