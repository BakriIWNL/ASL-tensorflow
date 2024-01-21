# Model
To start, ensure that 'model.py' is executable, and run

`python3.9 model.py` to start training (This will take a while, I suggest playing around with EPOCHS and image size)

---
## Model Architecture

![Model Architecture](model_plot.png)

---
## Expected output

### Accuracies/Evaluation Metrics
![Accuracies/Evaluation Metrics](acc.png)

### Confusion matrix heatmap
![Confusion matrix heatmap](confmatrix.png)

---
## Adding the dataset

Head into the `dataset` directory, and add the installed `asl_alphabet_train` to it, this is **Required** to start training the model.

---
## Changing the code

Changing content of the code is encouraged, this is my personal testing and the best results I could reach given my hardware `GTX 1660 Super`, so all variables are
clear and easy to see to change and play around with, alongside comments that explain the entire code.
