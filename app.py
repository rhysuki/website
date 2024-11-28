from flask import Flask, g, request, render_template, url_for, make_response

app = Flask(__name__)
files = {
	"logo": "images/logo.png",
	"pink_star": "images/icons/pink_star.png"
}

### Functions

def read(path: str) -> str:
	with open(path, "r") as file:
		return file.read()

def render_main_page(name: str):
	return render_template("main.html.j2", title=name, content=read(f"static/main_pages/{name}.html"))

@app.before_request
def before_request():
	g.load_static = lambda path: url_for("static", filename=path)

### App Routes

# @app.route("/")
# def index():
# 	return read("static/placeholder.html")

@app.route("/", defaults={"name": "placeholder"})
@app.route("/about/", defaults={"name": "about"})
@app.route("/credits/", defaults={"name": "credits"})
@app.route("/links/", defaults={"name": "links"})
@app.route("/link_to_me/", defaults={"name": "link_to_me"})
@app.route("/resources/", defaults={"name": "resources"})
@app.route("/other_sites/", defaults={"name": "other_sites"})
def main_page(name):
	return render_main_page(name)

# I tried and tried and couldn't find a better way than this. Maybe one day.
# @app.route("/about/")
# def about():
# 	return render_main_page("about")

# @app.route("/credits/")
# def credits():
# 	return render_main_page("credits")

# @app.route("/links/")
# def links():
# 	return render_main_page("links")

@app.errorhandler(404)
def not_found(_):
	return render_template("404.html.j2"), 404