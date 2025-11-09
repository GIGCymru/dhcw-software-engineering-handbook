# API gateway pattern

APIs **SHOULD** be deployed behind a gateway. This ensures that the
security policies provided by the gateway are used rather than
implementing them directly in your back-end API.

Typically, deploy to Apigee or your own API gateway if building APIs
exclusively for your app. Consult the API platform and Cyber Security
teams for further advice.
