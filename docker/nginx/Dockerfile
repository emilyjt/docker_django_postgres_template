ARG NGINX_VERSION
FROM nginx:$NGINX_VERSION

ARG CONF_FILE
COPY ./docker/nginx/$CONF_FILE /etc/nginx/conf.d/default.conf