# K-Net95-Alzheimer
The project entitled “**Implementation of a predictive model based on 3D convolutional neural networks for the transition from mild cognitive impairment to Alzheimer’s disease using magnetic resonance imaging**” presents a 3D convolutional neural network architecture whose objective is to serve as medical support for the early detection of Alzheimer’s disease.

This was a thesis carried out with the aim of developing new techniques to support the detection of neurodegenerative diseases and thus enable more people to obtain a more reliable and accurate diagnosis for appropriate treatment.

##

_The files found in the repository were used throughout the project. It should be noted that the folders provided contain only five image packages each, solely for the purpose of illustrating an example of the selected data, as the full datasets are considerably large. Only files from the ADNI database were included; the images provided by the clinic will not be published in this repository due to confidentiality considerations._

##

### **1. Databases**
The well-known ADNI repository was used for the training and validation phases. For the testing phase, the database provided by the _Comfamiliar_ clinic in Pereira, Colombia was used.

### **2. Feature selection**
The selection of a middle-to-advanced age group (50 to 80 years) was fundamental in order to allow for better comparison among the magnetic resonance imaging datasets. The weighting used was T1.

### **3. Image processing**
Continuing with the division in the Databases section, the methods used for the training and validation phases differed from those used in the testing phase.

For the initial phases, the _FreeSurfer_ software was used to generate a clean three-dimensional brain model. For the testing phase, a lighter method that allowed faster acquisition of image datasets was used, known as _FastSurfer_, which is based on the technique presented by the software used in the earlier phases.

### **4. Structure and configuration**
The structure of the final neural network was based on the _AlexNet_ architecture, which is notable for its fully connected and pooling layers, enabling deep learning of three-dimensional features. This architecture was modified so that it could receive magnetic resonance imaging datasets during the training, validation, and testing phases, thereby facilitating the detection of relevant features and patterns for the identification and classification of diseased and healthy patients.

### **5. Training and validation**
The progress of the network was monitored based on the results obtained for accuracy, loss, and the learning curves derived from these metrics. Based on these results, it was necessary to modify the base network proposed during the Structure and Configuration phase. Some of the changes included increasing the number of neurons per layer, adjusting the number of image datasets used in each experiment, and varying the activation functions, among others.

### **6. Testing**
These experiments were divided into three stages. First, parameter modifications previously described were carried out, in which a total of ten experiments were conducted to obtain the final network. Next, a comparison was performed between the resulting network, referred to as “K-Net95,” and other well-known models (_UNet3D_ and _ResNet3D_) to determine which performs better in terms of efficiency, accuracy, and computational capacity. For this comparison, a similar number of image datasets was used for each model. Finally, the resulting network was evaluated using the test group (30% of the total data) in order to determine its ability to classify a diseased patient (1) versus a healthy patient (0) based on a prediction.


##

### Thank you for being interested <3





