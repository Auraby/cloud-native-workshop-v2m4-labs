FROM tiangolo/meinheld-gunicorn-flask:python3.9

ENV APP /app
ENV MODULE_NAME admin.main

# Edit the Port
ENV PORT 5000
ENV LISTEN_PORT $PORT

# To set up the enviroment with the AWS DynamoDB
ENV RUNTIME DOCKER

# Create the directory and instruct Docker to operate
# from there from now on
WORKDIR $APP

# Expose the port uWSGI will listen on
EXPOSE $PORT

# We copy the rest of the codebase into the image
COPY . $APP

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt