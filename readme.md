


# GraphQL
## Crear Usuario
``` 
mutation
{
  createUser(username:"juanber",email:"juanber2.0@gmail.com", password:"juanber", phone:"234234234") {
    user{
      id
      username
      email

    }
  }
}
```

## login

### request
``` 
mutation {
  tokenAuth(username:"admin", password:"admin") {
    token
  }
}
```

### response
```
{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTcwMjk2NzU1LCJvcmlnSWF0IjoxNTcwMjk2NDU1fQ.ZC5CFlGJ-HK8l1dxKVqnxfliHXJHpvZQMvaFElMBY3I"
    }
  }
}
```