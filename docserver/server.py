import os
from flask import Flask, render_template, send_from_directory, abort, url_for
import markdown

app = Flask(__name__)


def configure_app(docs_path):
    app.config['DOCS_PATH'] = os.path.abspath(docs_path)
    app.config['TEMPLATES_AUTO_RELOAD'] = True


def generate_toc():
    """
    Generate a table of contents (ToC) by recursively walking through the docs directory.
    Group markdown files under their respective directories.
    """
    docs_path = app.config.get('DOCS_PATH', 'docs')
    toc = []

    for root, dirs, files in os.walk(docs_path):
        # Skip hidden directories and files
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        # Get the relative directory path
        rel_dir = os.path.relpath(root, docs_path)
        section = {"folder": rel_dir if rel_dir != '.' else '', "files": []}

        # Add markdown files to the section
        for file in sorted(files):
            if file.endswith('.md'):
                file_name = file.replace('.md', '')  # Remove the .md extension
                rel_file = os.path.join(rel_dir, file) if rel_dir != '.' else file
                section["files"].append((file_name, rel_file))

        # Add section only if it contains markdown files
        if section["files"]:
            toc.append(section)

    return toc


@app.route('/')
def index():
    """Serve the table of contents."""
    toc = generate_toc()  # Get the table of contents
    return render_template('toc.html', toc=toc)


@app.route('/<path:filepath>')
def serve_docs(filepath):
    """Serve individual markdown files."""
    docs_path = app.config.get('DOCS_PATH', 'docs')
    full_path = os.path.join(docs_path, filepath)

    if os.path.isdir(full_path):
        full_path = os.path.join(full_path, 'index.md')
    elif not full_path.endswith('.md'):
        full_path += '.md'

    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        html = markdown.markdown(content, extensions=['fenced_code', 'tables'])
        toc = generate_toc()  # Get the ToC for the sidebar
        return render_template('index.html', content=html, toc=toc)
    else:
        abort(404)


@app.route('/assets/<path:filename>')
def assets(filename):
    assets_dir = os.path.join(app.config.get('DOCS_PATH', 'assets'))
    return send_from_directory(assets_dir, filename)


@app.route('/static/<path:filename>')
def static_files(filename):
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    return send_from_directory(static_dir, filename)
