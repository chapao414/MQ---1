from flask import Flask, request
import requests

app = Flask(__name__)

ESP32_URL = "http://IP_DO_ESP32/liberar"


@app.route("/")
def inicio():
    return "Servidor da maquina funcionando"


@app.route("/webhook", methods=["POST"])
def webhook():

    dados = request.json

    print(dados)

    if dados.get("status") == "paid":

        requests.get(ESP32_URL)

        print("Ficha liberada")

    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
