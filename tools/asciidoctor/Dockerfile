FROM asciidoctor/docker-asciidoctor:1.84

# Set up environment variables
ENV APP_DIR=/srv/app \
    DOC_DIR=/srv/app/documents \
    OUTPUT_DIR=${DOC_DIR}/output \
    RESOURCES_DIR=${DOC_DIR}/resources

# Set working directory
WORKDIR ${DOC_DIR}

# Install dependencies with hybrid version approach:
# - Critical packages: version major.minor fixed (allowing patch updates)
# - Build tools: major version fixed
# - Utilities: no version fixing
RUN apk add --no-cache \
        graphviz~=12.2 \
        rsync~=3.4 \
    && apk add --no-cache --virtual .build-deps \
        build-base~=0.5 \
        ruby-dev \
    && gem install --no-document rouge -v 4.5.1 \
    && apk del .build-deps

# Copy entrypoint script and set permissions
COPY tools/asciidoctor/docker-entrypoint.d/00_create_pdfs.sh ${APP_DIR}/00_create_pdfs.sh
COPY docs/adoc/ ${DOC_DIR}/

# Create img directory and copy images without overwriting
RUN mkdir -p ${DOC_DIR}/img/
COPY docs/img/ ${DOC_DIR}/img_temp/
RUN rsync -av --ignore-existing ${DOC_DIR}/img_temp/ ${DOC_DIR}/img/ && \
    rm -rf ${DOC_DIR}/img_temp/

COPY examples ${DOC_DIR}/examples/

RUN chmod +x ${APP_DIR}/00_create_pdfs.sh

# Set the entrypoint
ENTRYPOINT ["/bin/sh", "-c", "${APP_DIR}/00_create_pdfs.sh"]