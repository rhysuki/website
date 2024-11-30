from flask import Flask, g, request, render_template, url_for, make_response
import markdown # type: ignore

app = Flask(__name__)

@app.before_request
def before_request():
	g.load_static = lambda path: url_for("static", filename=path)

@app.route("/", defaults={"name": "placeholder"})
@app.route("/about/", defaults={"name": "about"})
@app.route("/news/", defaults={"name": "news"})
@app.route("/credits/", defaults={"name": "credits"})
@app.route("/links/", defaults={"name": "links"})
@app.route("/link_to_me/", defaults={"name": "link_to_me"})
@app.route("/resources/", defaults={"name": "resources"})
@app.route("/other_sites/", defaults={"name": "other_sites"})
def main_page(name):
	with open(f"static/main_pages/{name}.md", "r", encoding="utf-8") as file:
		return render_template(
			"main.html.j2",
			title=name,
			content=markdown.markdown(file.read())
		)

@app.errorhandler(404)
def not_found(_):
	return render_template("404.html.j2"), 404