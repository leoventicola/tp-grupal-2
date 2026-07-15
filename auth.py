from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

token = 'este-es-un-token-global'

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if (credentials.credentials != token):
        raise HTTPException(
            status_code=401,
            detail="Token invalido"
        )
    return credentials.credentials