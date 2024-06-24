import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired


# getting the data
X_data = pd.read_csv("Heart Disease data.csv").drop(columns="target")

class InputForm(FlaskForm):
    age = IntegerField(
        label="Age",
        validators=[DataRequired()]
    )
    sex = SelectField(
        label="Sex",
        choices=X_data.sex.unique().tolist(),
        validators=[DataRequired()]
    )
    cp = SelectField(
        label="CP",
        choices=X_data.cp.unique().tolist(),
        validators=[DataRequired()]
    )
    trestbps = IntegerField(
        label="Trestbps",
        validators=[DataRequired()]
    )
    chol = IntegerField(
        label="Chol",
        validators=[DataRequired()]
    )
    fbs = SelectField(
        label="FBS",
        choices=X_data.fbs.unique().tolist(),
        validators=[DataRequired()]
    )
    restecg = SelectField(
        label="Restecg",
        choices=X_data.restecg.unique().tolist(),
        validators=[DataRequired()]
    )
    thalach = IntegerField(
        label="Thalach",
        validators=[DataRequired()]
    )
    exang = SelectField(
        label="Exang",
        choices=X_data.exang.unique().tolist(),
        validators=[DataRequired()]
    )
    oldpeak = SelectField(
        label="oldpeak",
        choices=X_data.oldpeak.unique().tolist(),
        validators=[DataRequired()]
    )
    slope = SelectField(
        label="Slope",
        choices=X_data.slope.unique().tolist(),
        validators=[DataRequired()]
    )
    ca = SelectField(
        label="CA",
        choices=X_data.ca.unique().tolist(),
        validators=[DataRequired()]
    )
    thal = SelectField(
        label="Tha",
        choices=X_data.thal.unique().tolist(),
        validators=[DataRequired()]
    )
        
    submit = SubmitField("Predict")