# Readme

## Tech Stack

- Fast API - Python web framework
- AWS DynamoDB - NoSQL Database
- AWS Elastic search - for searching
- Docker

## Setup Instructions

- Create a dynamo db table called "Youtube"
- Create an elastic search domain on AWS ElasticSearch
- Create a lambda trigger from the dynamo db table to stream data to elastic search
- The blueprint for the lambda trigger is in the file app/lambda.py
- All the environment variables like region, elastic search domain need to be set for the lambda
- The lambda should be given all access(read/write/list) to dynamo db and to the elastic search domain
- Create a google developer api key with access to Youtube V3 api and insert it in the API_KEY variable in the file recurring_task.py
- The AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY need to be entered in the app/.env file
- The elastic search domain without https:// (starting with [search-XXXXX.ap-south-1.es.amazonaws.com](http://search-amplify-elasti-23tej89cv8rz-ylpz32lnmn5u54pgzwxfdlknrq.ap-south-1.es.amazonaws.com/)) should be entered in [main.py](http://main.py) in the variable named host
- After everything is setup, run the application from the root directory using the following command

```jsx
docker-compose up -d
```

- Swagger UI can be now accessed at https://localhost:80/docs
- The list/search api can be tested through swagger UI

## API

- There is a unified api to do both the get and search operations
- The search implemented is very efficient (done through elastic search) and paginated
- The service is highly scalable and optimised as dynamo db has a very low latency for reads and writes, elastic search is highly optimised for searching
- The service has relevant validations for various request parameters
