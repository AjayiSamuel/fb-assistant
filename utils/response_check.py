from wit import Wit

access_token = "FHAUGNM3OYTM3HFMLMB7SKNHE7356O5H"

client = Wit(access_token = access_token)

message_text = "i need data"

resp = client.message(message_text)

print(resp)


# {'_text': 'i need airtime', 'entities': {'intent': [{'confidence': 0.99739483327139, 'value': 'airtime'}]}