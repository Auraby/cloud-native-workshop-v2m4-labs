FROM tiangolo/meinheld-gunicorn-flask:python3.6

ENV APP /app
ENV MODULE_NAME admin.main

# Edit the Port
ENV PORT 5081
ENV LISTEN_PORT $PORT

# To set up the enviroment with the AWS DynamoDB
ENV AWS_REGION ap-southeast-1
ENV RUNTIME DOCKER

# Create the directory and instruct Docker to operate
# from there from now on
WORKDIR $APP

# Expose the port uWSGI will listen on
EXPOSE $PORT

# We copy the rest of the codebase into the image
COPY . $APP

# Install Python dependencies
RUN pip install -r requirements.txt