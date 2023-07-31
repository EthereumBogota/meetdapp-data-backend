from fastapi import FastAPI


app = FastAPI()
app.title = 'Meet Dapp API'
app.version = '0.0.1'


@app.get('/',tags=["home"])
def onboarding(): 
    return "Welcome Meet Dapp dev"