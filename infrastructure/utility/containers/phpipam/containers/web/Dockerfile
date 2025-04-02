FROM ubuntu:24.10

# Set non-interactive mode to prevent prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update, upgrade, and install packages
RUN apt update && \
    apt upgrade -y && \
    apt install -y curl vim git && \
    apt install -y apache2 && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Expose the HTTP port
EXPOSE 80

# Set the default command to start apache
CMD ["apachectl", "-D", "FOREGROUND"]