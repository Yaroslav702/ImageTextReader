## Image text reader

This soft is created to simplify the search process of the questions on the images.

### How does it work?

When you input the question in the console, the script runs through the "questions" folder and checks whether the text on the image includes at least 50% of the prompted question. <br>
As a result, all the matched images will be displayed in the new window. <br>
**P.S.** The images are displayed one by one (if you press any key - previous image will be closed and the next one will be displayed.)

### Installation

1. Ensure that Python >3.8 is installed on your PC.
2. Run commands:

```python3 -m venv env``` <br>
```source env/bin/activate```<br>
```pip install -r requirements.txt```

3. Fill your **<u>questions</u>** folder with the images with allowed extensions: .png, .jpg, .jpeg.
4. Launch the "main.py" file.