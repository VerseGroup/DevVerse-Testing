from pydantic import BaseModel

class OauthPostRequest(BaseModel):
    client_id: str
    client_secret: str
    code: str
    redirect_uri: str

class RelayRequest(BaseModel):
    endpoint: str
    data: str
    method: str
    oauth_token: str

class AddUserRequest(BaseModel):
    oauth_token: str
    phone_number: str

