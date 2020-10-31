from flask import Flask, redirect, url_for, request, render_template
from API import Api

app = Flask(__name__)
text = dict()


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        data_name = request.form["name"]
        text["name"] = data_name
        return redirect(url_for("search"))
    else:
        return render_template("booksearch.html")


@app.route("/searched_data")
def search():
    if "name" in text and len(text["name"]) > 0:
        print(text['name'])
        search_data = Api().list(text["name"])
        dataset_search = list()
        for i in range(len(search_data["items"])):
            title = search_data['items'][i]['volumeInfo']['title']
            authors = str(search_data['items'][i]['volumeInfo']['authors'][0])
            src = search_data['items'][i]['volumeInfo']['imageLinks']['thumbnail']
            img = search_data['items'][i]['volumeInfo']['infoLink']

            t = {"title": title, "authors": authors, "src": src, "img": img}
            dataset_search.append(t)

        return render_template("search_result.html", dataset_search=dataset_search)
    else:
        #text.pop("name")
        return redirect(url_for("root"))


app.run(debug=True)
