# Flask App with Feature Flag

## Building the Docker Image
To build the Docker image, follow these steps:

1. Clone this repository and navigate into the project directory:

```
git clone https://github.com/chrisjws-harness/feature_flags_101.git
cd feature_flags_101
```

2. Build the Docker image:

Copy code
```
docker build -t flask-app .
```
This will create a new Docker image called flask-app that includes the Flask app and all its dependencies.

## Running the Docker Container
To run the Docker container, follow these steps:

1. Start the Docker container:

```
docker run -p 5000:5000 flask-app --env HARNESS=true
```

2. Open a web browser and navigate to http://localhost:5000 to see the "Hello, World!" message.

