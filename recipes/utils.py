from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
    """
    Convert a matplotlib figure to a base64-encoded string for embedding in HTML.
    """
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, labels=None):
    """
    Generate a chart based on the type and data.
    
    Parameters:
    - chart_type: str ('bar', 'pie', 'line')
    - data: pandas DataFrame with 'name' and 'cooking_time' columns
    - labels: Optional labels for charts (e.g., for pie charts)
    
    Returns:
    - Base64-encoded string for embedding in HTML
    """
    plt.switch_backend('AGG')  # Use Anti-Grain Geometry backend for rendering
    fig = plt.figure(figsize=(8, 4))  # Adjust figure size for better responsiveness

    if chart_type == 'bar':
        # Create a bar chart with rotated labels
        plt.bar(data['name'], data['cooking_time'], color='skyblue')
        plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate x-axis labels
        plt.ylabel('Cooking Time (mins)', fontsize=10)
        plt.xlabel('Recipe Name', fontsize=10)
        plt.title('Cooking Time by Recipe', fontsize=12)

    elif chart_type == 'pie':
        # Create a pie chart
        plt.pie(data['cooking_time'], labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title('Cooking Time Distribution', fontsize=12)

    elif chart_type == 'line':
        # Create a line chart
        plt.plot(data['name'], data['cooking_time'], marker='o', linestyle='-', color='skyblue')
        plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate x-axis labels
        plt.ylabel('Cooking Time (mins)', fontsize=10)
        plt.xlabel('Recipe Name', fontsize=10)
        plt.title('Cooking Time by Recipe', fontsize=12)

    else:
        return None  # Return None if the chart type is not recognized

    plt.tight_layout()  # Ensure layout fits within the figure area
    return get_graph()