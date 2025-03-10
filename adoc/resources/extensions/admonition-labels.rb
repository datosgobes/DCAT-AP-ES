class PDFConverterAdmonitionLabel < (Asciidoctor::Converter.for 'pdf')
  register_for 'pdf'

  def arrange_block node, &block
    # Solo procesar si es un admonition
    return super unless node.context == :admonition
    
    # Obtener el tipo
    type = node.attr 'name'
    
    # Solo procesar tipos específicos
    valid_types = ['caution', 'warning', 'tip']
    return super unless valid_types.include?(type)
    
    # Obtener configuración del theme para este tipo
    key_prefix = %(admonition_#{type}_)
    badge_entries = theme.each_pair.select {|name, val| name.to_s.start_with? key_prefix }
    return super if badge_entries.empty?

    # Configurar valores del badge
    background_color = theme[%(#{key_prefix}badge_background_color)] || '#666666'
    font_color = theme[%(#{key_prefix}badge_font_color)] || '#FFFFFF'
    font_size = theme[%(#{key_prefix}badge_font_size)] || 9
    text = theme[%(#{key_prefix}badge_text)].upcase || type.upcase

    # Llamar al convertidor base dentro de un bloque
    super node do |extent|
      return_val = instance_exec extent, &block
      
      # Solo dibujar el label si tenemos extent y no estamos en modo scratch
      if extent && !scratch?
        float do
          # Ir a la página y posición correcta
          go_to_page extent.from.page
          bounds.current_column = extent.from.column if ColumnBox === bounds
          move_cursor_to extent.from.cursor

          # Usar theme_font como en el code block
          theme_font :base do
            # Crear el badge a la derecha
            bounding_box([bounds.right - 90, cursor], width: 80, height: 20) do
              # Usar el color de fondo del theme
              fill_color background_color

              # Dibujar rectángulo redondeado con radio ajustado
              fill_rounded_rectangle [0, 16], 80, 20, 6

              # Dibujar el texto usando configuración del theme
              fill_color font_color
              font_size font_size do
                text_box text,
                  at: [5, 17],
                  width: 70,
                  height: 20,
                  align: :center,
                  valign: :center,
                  style: :bold
              end
            end
          end
        end
      end
      return_val
    end
  end
end