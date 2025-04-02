# Use the official Apache2 image
FROM php:8.2-apache
VOLUME /var/www/html

# Install additional PHP extensions and system dependencies
RUN docker-php-ext-install mysqli pdo pdo_mysql && \
    apt-get update && apt-get install -y libpng-dev libjpeg-dev libfreetype6-dev && \
    docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install gd

# Set the working directory
WORKDIR /var/www/html

# Expose the HTTP port
EXPOSE 80

# Set the default command to start apache
CMD ["apachectl", "-D", "FOREGROUND"]