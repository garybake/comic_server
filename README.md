# comic_server
Tornado based web server for comic (cbr/cbz) files.
- Serves each comic page as a web page.
- Supports left/right swipe
- Scratching an itch where I was unable to read large comics on my ipad 2

Install
pip install -r requirements.txt

Config
Open comics archive files and extract to folder in ./src/static/comic/<comic_name>

TODO: add a mgmt screen that takes a folder of cbr|z files and does this automagically

Run
python src/server.py
Open hostname:9000
