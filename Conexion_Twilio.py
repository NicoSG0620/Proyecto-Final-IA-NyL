from twilio.rest import Client

# Twilio account SID and auth token
account_sid = 'AC648ec667106cd9fd4e3378e8dc4a39d0'
auth_token = 'f72a01b95768ff74754a1294ba84a42e'

def send_whatsapp(to_phone_number, message):
    client = Client(account_sid, auth_token)
    

    from_phone_number = 'whatsapp:+12544593307'
    
    try:
        message = client.messages.create(
            body=message,
            from_=from_phone_number,
            to=to_phone_number
        )
        
        print(f"WhatsApp message sent successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Error sending WhatsApp message: {str(e)}")

# Prueba
to_phone_number = 'whatsapp:+12544593307'
message = 'Hola!! Soy Lisa, la asistente virtual de la empresa Fashion Boutique ¿En que puedo ayudarte?'

send_whatsapp(to_phone_number, message)
