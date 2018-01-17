from flask import Flask
app = Flask("Miss 敏敏！")

@app.route('/')
def hello_world():
    return 'Hello ,敏敏！'

app.run()

# if __name__ == '__main__':
#     app.run()