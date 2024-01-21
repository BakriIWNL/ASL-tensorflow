# OPENCV implementation
This code uses openCV to test out the code using your camera.

---
## To start
First make sure the `implementationcode.py` is made executable.

Once training is done, move the `h5` file that has been outputted by the training in this directory,
and run the code using

`python3.9 implementationcode.py`

![Testing using Camera](test.png)

---
## How to use
When the code is working the user can press `x` to take a screenshot of the current frame
the model then predicts and outputs said prediction on the top left of the screen,
if the user wishes to try another letter they can press `y` and if they wish to close the program
they can press `n`.

The `ASL2.h5` in this directory is from my personal training, other training outputs may be better.
