FROM registry.access.redhat.com/ubi8/python-39

LABEL maintainer="Mark Curwen<macurwen@redhat.com>"

LABEL io.k8s.description="This is an api to get the quart page" \
      io.k8s.display-name="test_quart"

ENV CONFIGURATION_SETUP=development
ENV PORT 8900
ENV DATA_SERVICE_HOST http://50.16.125.1
ENV DATA_SERVICE_PORT 8500

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 8900

ENTRYPOINT [ "python" ]

CMD ["main.py"]