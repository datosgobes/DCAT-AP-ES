FROM ruby:3.4-slim

# Set up environment variables
ENV APP_DIR=/srv/app \
    DOC_DIR=/srv/app/documents \
    OUTPUT_DIR=${DOC_DIR}/output \
    RESOURCES_DIR=${DOC_DIR}/resources

# Install required packages and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && gem install kramdown-asciidoc

# Set working directory
WORKDIR ${DOC_DIR}

# Create necessary directories
RUN mkdir -p ${OUTPUT_DIR} ${RESOURCES_DIR}

# Copy entrypoint script and set permissions
COPY tools/md2adoc/docker-entrypoint.d/00_convert_docs.sh ${APP_DIR}/00_convert_docs.sh
COPY docs/*.md ${DOC_DIR}/
COPY docs/img/ ${DOC_DIR}/img/
COPY examples ${DOC_DIR}/examples/

RUN chmod +x ${APP_DIR}/00_convert_docs.sh

# Set the entrypoint
ENTRYPOINT ["/bin/sh", "-c", "${APP_DIR}/00_convert_docs.sh"]