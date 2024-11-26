# South Bay Specials

## Overview

South Bay Specials is a Django-based web application designed to manage and display special offers for various locations. This project includes a Django backend API, React TS frontend, and Traefik proxy for routing.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)

## Project Repositories

This project consists of multiple repositories:

1. [Backend API](https://github.com/Aarenrice89/south-bay-specials)
2. [Frontend](https://github.com/Aarenrice89/south-bay-specials-frontend)
3. [Traefik Proxy](https://github.com/Aarenrice89/traefik-proxy)

## Installation

### Step 1: Install Docker Desktop

Download and install Docker Desktop from Docker's official website. Follow the installation instructions for your operating system.

### Step 2: Clone the Repositories Locally

Clone the South Bay Specials repositories:

- [Backend](https://github.com/Aarenrice89/south-bay-specials)
- [Frontend](https://github.com/Aarenrice89/south-bay-specials-frontend)
- [Proxy Service](https://github.com/Aarenrice89/traefik-proxy)

```sh
git clone git@github.com:Aarenrice89/traefik-proxy.git
git clone git@github.com:Aarenrice89/south-bay-specials.git
git clone git@github.com:Aarenrice89/south-bay-specials-frontend.git
```

### Step 3: Set Up Proxy and Docker Network

Set up the Docker network `proxy` to manage communication between containers:

```sh
docker network create proxy
```

Start the proxy container. Navigate to the proxy project root and run:

```sh
docker compose -f docker-compose.local.yml up -d --build
```

Add generated web certs to browser:

##### On Windows:

- Open Cert Manager
- Expand Trusted Root Certification Authorities
- Right click on Certificates and select All Tasks > Import
- Import the `ca.crt` file from the certs folder

#### Firefox Special Instructions:

Firefox uses its own certificate manager

- Go to settings
- Search for certs
- Click View Certificates
- Select the Authorities tab
- Select import
- Import the `ca.crt` file from the certs folder

### Step 4: Add project Environment Variables

Create a .env file in the `/compose/envs` directory of the backend repository with the content supplied in the template file

### Step 5: Build and Run the Containers

Navigate to the backend repository and run the following commands to build and start the backend Docker containers:

```sh
docker compose -f ./compose/docker-compose.yml up -d --build
```

or use VSCode Dev Container for extended development features

[VS Code Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)

### Step 6: Start the FE React application

See README for the [frontend](https://github.com/Aarenrice89/south-bay-specials-frontend) application for installation and setup instructions

### Step 7: Access the Application

Once the containers are up and running, you can access the application at:

| Service                  | URL                                                                              |
| ------------------------ | -------------------------------------------------------------------------------- |
| Backend API Swagger      | [Swagger UI](https://api.south-bay-specials.localhost/api/v1/schema/swagger-ui/) |
| Backend API Django admin | [Django Admin](https://api.south-bay-specials.localhost/admin/)                  |
| Frontend                 | [Frontend](https://web.south-bay-specials.localhost/)                            |
| Traefik Dashboard        | [Dashboard](http://localhost:8080/dashboard/#/)                                  |

## Development

For local development, you can use the provided Docker Compose configuration to set up the development environment. Make sure to follow the steps above to get started.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or inquiries, please contact Aaren Rice at aarenrice@gmail.com.
