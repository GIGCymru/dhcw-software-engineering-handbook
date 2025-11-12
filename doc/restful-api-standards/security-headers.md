# Security headers

Use [HTTP response headers](http-implementation.md) to specify security
controls in HTTP communications. These serve as an extra layer of
protection against common vulnerabilities and privacy risks.

## Minimise information disclosure

You **SHOULD** remove unnecessary HTTP response headers that expose
details about the server and its underlying technologies. For example,
consider the following response which includes headers that reveal
server information:

!!! danger "Examples of practices to avoid"
    ```sh
        *HTTP/1.1 201 Created*

        *Content-Type: application/json; charset=utf-8*

        *Location: /api/patients/9991234568*

        *Date: 2024-02-17T12:00:00Z*

        *Server: Microsoft-IIS/10.0*

        *X-AspNet-Version: 6.0.0*

        *X-AspNetMvc-Version: 6.0.0*
    ```

You **SHOULD** remove these sensitive headers. A valid response might
look like this:

!!! example "Examples of good practice"
    ```sh
        *HTTP/1.1 201 Created*

        *Content-Type: application/json; charset=utf-8*

        *Location: /api/patients/9991234568*

        *Date: 2024-02-17T12:00:00Z*
    ```
