FROM mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu22.04:latest
# FROM mcr.microsoft.com/azureml/curated/mlflow-model-inference:1

RUN mkdir -p /var/azureml-app-swastik

COPY ./requirements.txt /var/azureml-app-swastik/
RUN pip install -r /var/azureml-app-swastik/requirements.txt

COPY ./score.py /var/azureml-app-swastik/
RUN rm -rf /var/runit/gunicorn/run
COPY ./run /var/runit/gunicorn
ENV MY_AML_APP_ROOT=/var/azureml-app-swastik/
ENV MY_AZUREML_ENTRY_SCRIPT=score.py

RUN chmod +x /var/runit/*/*

# Print environment variables and list files in /var/azureml-app/
RUN echo "Environment Variables:" && env && \
    echo "Files in ${MY_AML_APP_ROOT}" && ls -l "${MY_AML_APP_ROOT}"

RUN echo "MY_AZUREML_ENTRY_SCRIPT: ${MY_AZUREML_ENTRY_SCRIPT}"
