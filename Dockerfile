FROM gcr.io/google-containers/python:3.5.1-slim
RUN echo "hello"
RUN this-command-should-error && exit 158

