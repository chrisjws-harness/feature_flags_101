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
docker run -p 5000:5000 flask-app
```

2. Open a web browser and navigate to http://localhost:5000 to see the "Hello, World!" message.

## Working with feature flags

You can progress though this tutorial by switching from main to ff-01, ff-02 ... ff-n

* FF-01 covers your first feature flag
* FF-02 covers your first multi-variate flag and persona targeting
* FF-03 covers proxy/offline mode, pipelines, RBAC, and governance

### FF-01

* Add SDK key
* Add Feature flag `new_ui`
* Toggle new UI

### FF-02 
* Add Multi-Variate Feature Flag `different_greetings` with variations `Hello`, `What's up`, and `Yo`
* Add Boolean Feature Flag `personalization`
* Toggle different greetings
* Turn on personalization
* Target your user

### FF-03
* Setup proxy
* Create a pipeline and attach to a flag
* Use Harness RBAC & Governance controls
