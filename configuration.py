# plot_settings.py

TABLE_STYLE = {
    'border_width': 1,
    'cell_padding': 5,
    'header_color': '#f0f0f0',
    'row_colors': ['#ffffff', '#e0e0e0'],
    'font_family': 'Arial',
    'font_size': 10,
    'header_font_weight': 'bold',
    'text_align': 'center',
    'border_color': '#000000',
    'header_height': 30,
    'row_height': 25,
    'column_width': 100,
    'header_text_color': '#000000',
    'cell_text_color': '#333333',
    'significant_figures': {
        'displacement': 4,  # For displacement values (meters)
        'velocity': 3,      # For velocity values (m/s)
        'acceleration': 2,  # For acceleration values (m/s^2)
        'time': 3,         # For time values (seconds)
        'force': 2,        # For force values (N)
        'mass': 2,         # For mass values (kg)
        'stiffness': 0,    # For stiffness values (N/m)
        'damping': 0,      # For damping values (Ns/m)
        'default': 3       # Default for other numeric values
    }
}

PLOT_STYLE = {
    'font_size': 12,
    'font_family': 'Arial',
    'title_size': 14,
    'title_weight': 'bold',
    'axis_label_size': 11,
    'line_width': 2,
    'marker_size': 6,
    'colors': ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c', '#34495e', '#e67e22', '#95a5a6', '#c0392b'],
    'grid_style': {
        'color': '#d3d3d3',
        'linestyle': '--',
        'alpha': 0.7,
        'width': 0.5
    },
    'figure_size': (10, 6),
    'dpi': 100,
    'legend_location': 'best',
    'legend_font_size': 10,
    'axis_line_width': 1.0,
    'tick_label_size': 10,
    'axis_significant_figures': {
        'x_axis': 3,
        'y_axis': 3,
        'legend': 3
    }
}
