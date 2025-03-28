$(document).ready(() => {
    const initializeValidation = async () => {
        try {
            // Obtener el idioma desde el atributo lang del elemento html
            let selectedLang = document.documentElement.lang || Object.keys(dcatapesConfig)[0]; // Usar el primer valor de dcatapesConfig si no existe lang
            if (!dcatapesConfig[selectedLang]) {
                // Si no existe, usar el primer idioma disponible en dcatapesConfig
                selectedLang = Object.keys(dcatapesConfig)[0];
                //console.log(`Idioma no encontrado: ${selectedLang}. Usando idioma por defecto: ${selectedLang}`);
            }

            const { codeblock_messages: msg, validator, converter } = dcatapesConfig[selectedLang];

            // Seleccionar solo bloques no procesados
            const codeBlocks = $(".tabbed-set .highlight pre code").not('[dcatapesConfig-processed="true"]');

            codeBlocks.each((index, element) => {
                const $element = $(element);
                const languageClass = $element.closest('.highlight').attr('class').split(' ')[0];
                const language = languageClass.split('-')[1];

                // Obtener el contenido del elemento
                const content = $element.text();

                // Inferir el formato de entrada
                const inputFormat = inferInputFormat(content);

                // Generar los botones de conversión
                const buttonContainer = generateConversionButtons(converter, content, inputFormat, msg, $element);

                // Verificar si el validador está habilitado
                const validatorEnabled = validator.enabled !== undefined ? validator.enabled : false;
                if (validatorEnabled) {
                    // Generar el icono de validación
                    const { validateIcon, description } = generateValidationIcon(validator, content, language, $element, msg, index);
                    buttonContainer.append(validateIcon);
                    buttonContainer.append(description);
                }

                // Insertar el contenedor de botones después del contenedor .highlight
                $element.closest('.highlight').after(buttonContainer);

                // Marcar el bloque como procesado
                $element.attr('dcatapesConfig-processed', 'true');
            });
        } catch (error) {
            console.error('Error al inicializar la validación:', error);
        }
    };

    // Función para inferir el formato de entrada a partir del contenido
    function inferInputFormat(content) {
        const trimmedContent = content.trim();
        if (trimmedContent.startsWith('<?xml')) {
            return 'rdfxml';
        } else if (trimmedContent.startsWith('{')) {
            return 'jsonld';
        } else if (trimmedContent.includes('@prefix') || trimmedContent.includes('PREFIX')) {
            return 'turtle';
        } else {
            return 'turtle';
        }
    }

    // Función para generar los botones de conversión
    function generateConversionButtons(converter, content, inputFormat, msg, $element) {
        const buttonContainer = $('<div>', { class: 'button-container' });
        const outputFormats = converter.output_formats;

        Object.keys(outputFormats).forEach((format) => {
            if (format !== inputFormat) {
                const convertButton = $('<button>', {
                    class: 'convert-button',
                    text: `${msg.convert_to} ${outputFormats[format]}`,
                    click: () => {
                        convertContent(converter, content, inputFormat, format, $element, msg);
                    }
                });
                buttonContainer.append(convertButton);
            }
        });

        return buttonContainer;
    }

    // Función para realizar la conversión y abrir el resultado
    function convertContent(converter, content, inputFormat, outputFormat, $element, msg) {
        const form = $('<form>', {
            method: 'POST',
            action: converter.base_url,
            target: '_blank'
        });

        form.append($('<input>', {
            type: 'hidden',
            name: 'data',
            value: content
        }));
        form.append($('<input>', {
            type: 'hidden',
            name: 'uri',
            value: converter.uri,
        }));
        form.append($('<input>', {
            type: 'hidden',
            name: 'in',
            value: inputFormat || 'guess'
        }));
        form.append($('<input>', {
            type: 'hidden',
            name: 'out',
            value: outputFormat
        }));

        $('body').append(form);
        form.trigger('submit');
        form.remove();
    }

    // Función para generar el icono de validación
    function generateValidationIcon(validator, content, language, $element, msg, index) {
        const format = language === 'ttl' ? 'text/turtle' :
                        language === 'xml' ? 'application/rdf+xml' : 'application/ld+json';
        const validateIcon = $('<span>', {
            class: 'twemoji validate-icon',
            'aria-describedby': `validate-description-${index}`,
            html: '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8z"></path></svg>',
            click: () => {
                validateContent(validator.base_url, validator.model, validator.api_action, validator.version, content, format, $element, msg);
            }
        });

        const description = $('<span>', {
            id: `validate-description-${index}`,
            class: 'sr-only',
            text: msg.click_to_validate
        });

        return { validateIcon, description };
    }

    // Función para validar el contenido
    function validateContent(baseUrl, model, apiAction, version, content, format, $element, msg, retry = true) {
        
        const request = {
            contentToValidate: content,
            contentSyntax: format,
            embeddingMethod: "STRING",
            validationType: version,
            reportSyntax: "text/turtle"
        }; 
        const itbapi = `${baseUrl}/${model}/${apiAction}`;

        $.ajax({
            type: "POST",
            url: itbapi,
            data: JSON.stringify(request),
            contentType: "application/json; charset=utf-8",
            crossDomain: true,
            dataType: "text",
            success: response => {
                showReport(response, $element, msg);
            },
            error: (jqXHR, exception) => {
                let msgText = '';
                if (jqXHR.status === 0) {
                    msgText = msg.not_connected;
                } else if (jqXHR.status == 404) {
                    msgText = msg.page_not_found;
                } else if (jqXHR.status == 500) {
                    msgText = msg.internal_server_error;
                    if (retry) {
                        // Retry with format = "text/turtle"
                        validateContent(baseUrl, model, apiAction, version, content, "text/turtle", $element, msg, false);
                        return;
                    }
                } else if (exception === 'parsererror') {
                    msgText = msg.json_parse_failed;
                } else if (exception === 'timeout') {
                    msgText = msg.timeout_error;
                } else if (exception === 'abort') {
                    msgText = msg.ajax_aborted;
                } else {
                    msgText = msg.uncaught_error + jqXHR.responseText;
                }
                alert(`No fue posible validar. Mensaje: ${msgText}`);
            }
        });
    }

    // Función para mostrar el reporte de validación
    function showReport(response, $element, msg) {
        const isValid = /sh:conforms\s+true/.test(response);
        const reportClass = isValid ? 'success' : 'failure';
        const summaryStyle = isValid ? 'color: #00c853;' : 'color: #ff5252;';
        const reportHtml = `
            <details class="${reportClass}">
                <summary style="${summaryStyle}">${msg.validation_result}</summary>
                <pre class="code-block">${response}</pre>
            </details>
        `;
        // Eliminar cualquier reporte existente
        $element.closest('.highlight').next('.report').remove();
        // Insertar el nuevo reporte
        $element.closest('.highlight').after(`<div class="report">${reportHtml}</div>`);
    }

    // Ejecutar la función de inicialización al cargar la página
    initializeValidation();

    // Ejecutar la función de inicialización al cambiar el hash de la URL
    $(window).on('hashchange', initializeValidation);
});