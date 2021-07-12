user_schema = {
  "id": {'type': 'number'},
  "name": {'type': 'string'},
  "username": {'type': 'string'},
  "email": {'type': 'string'},
  "address": {
    "street": {'type': 'string'},
    "suite": {'type': 'string'},
    "city": {'type': 'string'},
    "zipcode": {'type': 'string'},
    "geo": {
      "lat": {'type': 'string'},
      "lng": {'type': 'string'}
    }
  },
  "phone": {'type': 'string'},
  "website": {'type': 'string'},
  "company": {
    "name": {'type': 'string'},
    "catchPhrase": {'type': 'string'},
    "bs": {'type': 'string'}
  }
}
