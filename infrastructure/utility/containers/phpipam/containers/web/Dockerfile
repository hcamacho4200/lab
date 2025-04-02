# Use the official Apache2 image
FROM php:8.2-apache
VOLUME /var/www/html

# Install additional PHP extensions and system dependencies
RUN docker-php-ext-install mysqli pdo pdo_mysql && \
    apt-get update && apt-get install -y libpng-dev libjpeg-dev libfreetype6-dev && \
    docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install gd

RUN docker-php-ext-install sockets
RUN docker-php-ext-install sockets

RUN apt-get install -y libldap2-dev \
    && docker-php-ext-configure ldap --with-ldap \
    && docker-php-ext-install ldap

RUN apt-get install -y libgmp-dev \
    && docker-php-ext-install gmp

RUN apt install -y gettext && docker-php-ext-install gettext
RUN docker-php-ext-install pcntl

# Enable mod_rewrite
RUN a2enmod rewrite

# Set the working directory
WORKDIR /var/www/html

# Expose the HTTP port
EXPOSE 80

# Set the default command to start apache
CMD ["apachectl", "-D", "FOREGROUND"]