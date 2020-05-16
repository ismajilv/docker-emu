import falcon
import json


class DataResource(object):
    esp32_input_data_list = []

    def on_get(self, req, resp):
        resp.body = json.dumps({"input data from ESP32": self.esp32_input_data_list})

    def on_post(self, req, resp):
        raw_data = req.stream.read()
        raw_data = raw_data.decode("utf-8")        
        data = json.loads(raw_data, strict=False)

        if data:
            esp32_input_data = data.get("input data").strip()
            self.esp32_input_data_list.append(esp32_input_data)
            resp.status = falcon.HTTP_200
            resp.body = ""
        else:
            resp.status = falcon.HTTP_400

app = falcon.API()

data = DataResource()

app.add_route('/data', data)
