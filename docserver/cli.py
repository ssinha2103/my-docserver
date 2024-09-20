# cli.py

import click
from docserver.server import app, configure_app

@click.group()
def cli():
    """Documentation Server CLI"""
    pass

@cli.command()
@click.option('--host', default='127.0.0.1', help='Host address')
@click.option('--port', default=5000, help='Port number')
@click.option('--docs-path', default='docs', help='Path to documentation directory')
def start(host, port, docs_path):
    """Start the documentation server."""
    configure_app(docs_path)
    app.run(host=host, port=port, debug=True)
