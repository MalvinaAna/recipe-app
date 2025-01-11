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
    """
    plt.switch_backend('AGG')  # Use Anti-Grain Geometry backend for rendering
    fig = plt.figure(figsize=(6, 3))

    if chart_type == 'bar':
        plt.bar(data['name'], data['cooking_time'])
        plt.title('Cooking Time by Recipe')
    elif chart_type == 'pie':
        plt.pie(data['cooking_time'], labels=labels, autopct='%1.1f%%')
        plt.title('Cooking Time Distribution')
    elif chart_type == 'line':
        plt.plot(data['name'], data['cooking_time'], marker='o')
        plt.title('Cooking Time by Recipe')
    else:
        return None

    plt.tight_layout()
    return get_graph()