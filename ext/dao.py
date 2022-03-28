import json

from flask import Response, request

from ext.config.config import db
from model import Sales


def init_app(app):
    @app.route("/sales", methods=["GET"])
    def select():
        select = Sales.query.all()
        sales_json = [sales.to_json() for sales in select]
        
        return response(200, "Vendas", sales_json)


    @app.route("/sale/<id>", methods=["GET"])
    def select_sale(id):
        select = Sales.query.filter_by(id=id).fisrt()
        sale_json = select.to_json()

        return response(200, "Vendas", sale_json)

    @app.route("/sale", methods=["POST"])
    def create():
        body = request.get_json()

        try:
            sale = Sales(value=body["value"], monthyPrice=body["monthyPrice"], setuPrice=body["setuPrice"], currency=body["currency"])
            db.session.add(sale)
            db.session.commit()
            return response(201, "sale", sale.to_json(), "Venda cadastrada com sucesso")
        except Exception as e:
            print('Error', e)
            return response(400, "sale", {}, "Erro ao cadastrar venda")

    @app.route("/sale/<id>", methods=["PUT"])
    def update(id):
        select = Sales.query.filter_by(id=id).fisrt()
        body = request.get_json()

        try:
            if('value' in body):
                select.value = body['value']
            if('monthyPrice' in body):
                select.monthyPrice = body['monthyPrice']
            if('setuPrice' in body):
                select.setuPrice = body['setuPrice']
            if('currency' in body):
                select.currency = body['currency']

            db.session.add(select)
            db.session.commit()
            return response(200, "sale", select.to_json(), "Venda atualizada com sucesso")
        except Exception as e:
            print('Error', e)
            return response(400, "sale", {}, "Erro ao atualizar venda")  

    @app.route("/sale/<id>", methods=["DELETE"])
    def delete(id):
        select = Sales.query.filter_by(id=id).fisrt()

        try:
            db.session.delete(select)
            db.sessioncommit()
            return response(200, "sale", select.to_json(), "Venda atualizada com sucesso")
        except Exception as e:
            print('Error', e)
            return response(400, "sale", {}, "Erro ao atualizar venda")


    def response(status, name_content, content, message=False):
        body = {}
        body[name_content] = content

        if(message):
            body["message"] = message

        return Response(json.dumps(body), status=status, mimetype="application/json")
