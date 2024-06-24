import pandas as pd
import pickle
from flask import (
    Flask,
    url_for,
    render_template
)
from form import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

with open("heart_disease_model.pkl", "rb") as file:
    model_tuple = pickle.load(file)
    # Print the loaded object to understand its structure
    print(model_tuple)
    # Assuming the model is the first element in the tuple
    model = model_tuple[0]  
    
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            age=[form.age.data],
            sex=[form.sex.data],
            cp=[form.cp.data],
            trestbps=[form.trestbps.data],
            chol=[form.chol.data],
            fbs=[form.fbs.data],
            restecg=[form.restecg.data],
            thalach=[form.thalach.data],
            exang = [form.exang.data],
            oldpeak=[form.oldpeak.data],
            slope=[form.slope.data],
            ca=[form.ca.data],
            thal=[form.thal.data]
        ))
        prediction = model.predict(x_new)[0]
        if prediction == 1:
            message="Sorry,you are heart disease!"
        else:
            message="congradulation,you are safe!"
    else:
        message = "Please provide valid input details!"
    return render_template("predict.html", title="Predict", form=form, output=message)


if __name__ == "__main__":
    app.run(debug=True)