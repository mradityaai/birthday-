from pathlib import Path
import http.server
import socketserver
import webbrowser

# ==========================================================
# BIRTHDAY SURPRISE
# Put your photos in the "photos" folder.
# Rename them: photo1.jpg, photo2.jpg, photo3.jpg
# Then run this file.
# ==========================================================

BASE = Path(__file__).resolve().parent
PORT = 8765

print("\n💖 Birthday Surprise")
print("1. Add your photos to:", BASE / "photos")
print("2. Open index.html through the server.")
print("3. Your browser will launch automatically.\n")

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as server:
    url = f"http://127.0.0.1:{PORT}/index.html"
    webbrowser.open(url)
    print("✨ Surprise is running at", url)
    print("Press Ctrl+C in this terminal to stop it.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nBye! 💗")
