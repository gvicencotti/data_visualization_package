import matplotlib.pyplot as plt
import plotly.express as px

def plot_line(dataframe, x_column, y_column, title='Line Graph', xlabel='X Axis', ylabel='Y axis', color='blue'):
    plt.plot(dataframe[x_column], dataframe[y_column], color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_bar(dataframe, x_column, y_column, title='Bar Chart', xlabel='X Axis', ylabel='Y axis', color='blue'):
    plt.bar(dataframe[x_column], dataframe[y_column], color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_scatter_interactive(dataframe, x_column, y_column, title='Interactive Scatter Chart'):
    fig = px.scatter(dataframe, x=x_column, y=y_column, title=title)
    fig.show()

def save_plot(filename, format='png'):
    try:
        plt.savefig(f"{filename}.{format}", format=format)
        print(f"Gráfico salvo como {filename}.{format}")
    except Exception as e:
        print(f"Erro ao salvar gráfico: {e}")