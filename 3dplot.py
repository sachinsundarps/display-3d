import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from flask import Flask, render_template, send_from_directory, request
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)


def plot3d():
    x, y, z = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 200).transpose()
    trace1 = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=12,
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=0.8
        )
    )

    x2, y2, z2 = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 200).transpose()
    trace2 = go.Scatter3d(
        x=x2,
        y=y2,
        z=z2,
        mode='markers',
        marker=dict(
            color='rgb(255, 0, 0)',
            size=12,
            symbol='circle',
            line=dict(
                color='rgb(204, 204, 204)',
                width=1
            ),
            opacity=0.9
        )
    )

    x3, y3, z3 = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 200).transpose()
    trace3 = go.Scatter3d(
        x=x3,
        y=y3,
        z=z3,
        mode='markers',
        marker=dict(
            color='rgb(0, 255, 0)',
            size=12,
            symbol='circle',
            line=dict(
                color='rgb(204, 204, 204)',
                width=1
            ),
            opacity=0.9
        )
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='simple-3d-scatter')
    return send_from_directory('C:/Users/Sachin/PycharmProjects/MCproject/', 'simple-3d-scatter.html')


@app.route('/plot', methods = ['POST'])
def plot():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
        print file
    return plot3d()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    try:
        app.run(host='0.0.0.0', debug=True, port=port)
    except ValueError as err:
        print err
