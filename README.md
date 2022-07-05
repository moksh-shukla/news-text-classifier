# The Hindu News Article Class Predictor
This is a web app where upon entering the news article link from the leading Indian daily `The Hindu`, the app classifies the news into the category(National, International, Sports etc) it falls into.

## To run the web app

The web app uses Flask as a lightweight backend. The frontend is a simple HTML-CSS-JS bundle located in `static` folder.

```
pip install -r requirements.txt
python3 -m flask run
```

This runs a development server at http://localhost:5000. Navigate to the page on your browser to use the app.

## Directory Structure
This code folder has a subfolder `files` which contains the data files. The subfolder `scraping` contains the code for scraping. The file `ModelBuild.ipynb` containg the jupyter notebook for building the model.
