from flask import Flask, render_template
import datetime
import folium

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template("index.html", datetime_now=datetime.datetime.now())

@microweb_app.route("/map")
def show_map():
    # Create a map centered on Brussels
    m = folium.Map(location=[50.8503, 4.3517], zoom_start=14)

    # Add markers or any other map content here

    return m._repr_html_()

if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5050)

