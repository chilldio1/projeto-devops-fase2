from http.server import HTTPServer, BaseHTTPRequestHandler
import psycopg2
import os

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "banco"),
        database=os.getenv("DB_NAME", "estudos"),
        user=os.getenv("DB_USER", "diogo"),
        password=os.getenv("DB_PASSWORD", "senha123")
    )

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM visitas;")
            count = cur.fetchone()[0]
            cur.execute("INSERT INTO visitas (momento) VALUES (NOW());")
            conn.commit()
            cur.close()
            conn.close()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Visitas: {count + 1}".encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Erro: {e}".encode())

    def log_message(self, format, *args):
        pass

print("Servidor rodando na porta 8080...")
HTTPServer(("", 8080), Handler).serve_forever()
