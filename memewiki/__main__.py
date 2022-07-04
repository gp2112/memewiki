from memewiki import app
import sys

def main():
    host='localhost'
    if len(sys.argv) > 1:
        host = sys.argv[1]
    app.run(host=host)
