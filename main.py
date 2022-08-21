from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
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
    column_to_join = request.form["column_to_join"]
    if (
        uploaded_first_file.filename != ""
        and uploaded_second_file.filename != ""
        and column_to_join != ""
    ):
        # Merge them

        return join_csv(uploaded_first_file, uploaded_second_file, column_to_join)

    return redirect(url_for("index"))


def join_csv(uploaded_first_file, uploaded_second_file, column_to_join):

    # reading two csv files
    data1 = pd.read_csv(uploaded_first_file)
    data2 = pd.read_csv(uploaded_second_file)

    output1 = pd.merge(data1, data2, on=column_to_join, how="outer")

    return Response(
        output1.to_csv(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=joined.csv"},
    )


if __name__ == "__main__":
    app.run()
