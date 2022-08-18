from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    Response,
)
import pandas as pd


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_file():
    uploaded_first_file = request.files["first_csv"]
    uploaded_second_file = request.files["second_csv"]
    if uploaded_first_file.filename != "" and uploaded_second_file.filename != "":
        # Merge them
        return join_csv(uploaded_first_file, uploaded_second_file)
    return redirect(url_for("index"))


def join_csv(uploaded_first_file, uploaded_second_file):

    # reading two csv files
    data1 = pd.read_csv(uploaded_first_file)
    data2 = pd.read_csv(uploaded_second_file)

    # using merge function by setting how='inner'
    output1 = pd.merge(data1, data2, on="id", how="outer")

    return Response(
        output1.to_csv(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=filename.csv"},
    )


if __name__ == "__main__":
    app.run()
