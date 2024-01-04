import ghasedakpack


sms = ghasedakpack.Ghasedak("b0b57dd4655e0fe43ab9670becd99d")
sms.verification({'receptor': '09xxxxxxxxx','type': '1','template': 'Your Template','param1': 'test'})