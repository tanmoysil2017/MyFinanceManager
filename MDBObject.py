

class MDBObject():
    def __init__(self, json_data = {}):
        self.id = ''
        if json_data:
            self.id = json_data['_id']


    def encode_to_json(self):
        json_data = {}
        if self.id == '':
            self.id = self.populate_key()

        json_data['_id'] = self.id
        return json_data

    def populate_key(self):
        return ''