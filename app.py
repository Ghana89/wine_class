from flask import Flask , render_template ,request
from artifacts.utils import prediction

app = Flask(__name__)

@app.route('/' )
def index():
    return render_template ('index.html')

@app.route("/predict", methods = ['POST'])
def predict():
    data = request.form
    obj = prediction(data)
    predict_output =obj.result()
    return render_template('index.html', pred =predict_output )

if __name__ == "__main__":
    app.run(debug= True)