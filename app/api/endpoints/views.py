from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


@app.post("/sync-contacts")
async def sync_contacts(background_tasks: BackgroundTasks):

    background_tasks.add_task(sync_contacts_task)
    return {"message": "La sincronización de contactos ha comenzado en segundo plano"}


@app.post("/contacts")
async def create_contact(contact: ContactCreate):
    # recibir la información

    # consultar existencia del contacto en la api

    # registrar consulta en postgres

    # creación del contacto en api

    # si la respuesta es ok, registrar contacto en postgres

    contact_data = {
        "email": contact.email,
        "firstname": contact.firstname,
        "lastname": contact.lastname,
        "phone": contact.phone,
        "website": contact.website
    }

    response = hubspot_client.contacts.create_contact(contact_data)

    if response["status"] == "error":
        return {"error": response["message"]}

    return {"message": "Contacto creado exitosamente"}
