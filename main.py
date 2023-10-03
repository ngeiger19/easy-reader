from website import create_app
from easyreader import easypdf


app = create_app()

if __name__ == '__main__':
    #app.run(debug=True)

    pages = easypdf.readPattern("patterns/crochet_pattern1.pdf")

    print(pages)