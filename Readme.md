# Self-Hosted Documentation Python Package

### **Purpose**  
The purpose of this project is to allow developers to self-host documentation for their projects easily, providing an intuitive interface for managing, serving, and displaying markdown-based documentation locally.

---

## **1. High-Level Architecture**
### **Diagram:**

```plaintext
  +--------------------+        +----------------------+       +-------------------+
  |    User's Project   |        |     Documentation     |       |  Python Library   |
  |                    |        |      Directory         |       |                   |
  | +----------------+ |        | +-------------------+ |       | +---------------+ |
  | |   Python Code   | | -----> | | Markdown (.md)     | | ----> | | Local Web     | |
  | +----------------+ |        | | Docs Structure     | |       | | Server (Flask)| |
  |                    |        | +-------------------+ |       | +---------------+ |
  |                    |        |                       |       |                   |
  +--------------------+        +----------------------+       +-------------------+
```

### **Components**:
- **User's Project**: A project where developers will install your Python package and integrate it with their project.
- **Documentation Directory**: A folder containing the project's markdown documentation files, organized into sections/subsections.
- **Python Library**: The package that handles the server setup, markdown parsing, and serving the documentation via a local web server (Flask/FastAPI).

---

## **2. Directory and File Structure**
### **Diagram:**

```plaintext
  /project-directory
  ├── docs
  │   ├── introduction.md
  │   ├── setup.md
  │   ├── sections
  │   │   ├── api_reference.md
  │   │   └── deployment.md
  │   └── assets
  │       └── image1.png
  ├── src
  │   └── app.py
  └── ...
```

### **Explanation**:
- **docs/**: This is the folder where all documentation-related files will be stored.
  - **introduction.md**: A markdown file containing introductory information.
  - **sections/**: A subfolder that groups related markdown files (topics/sections).
  - **assets/**: A subfolder containing images or other assets used in the documentation.
  
This structure ensures that documentation is organized, and markdown files are easy to map to sections.

---

## **3. Component Overview**
### **Diagram:**

```plaintext
  +--------------------------+          +---------------------------+
  |       CLI Interface       | <------> |    Server (Flask/FastAPI)  |
  +--------------------------+          +---------------------------+
           |                                            |
           v                                            v
  +----------------------------+         +----------------------------------+
  |     Markdown Parser         |         |      Template Renderer          |
  +----------------------------+         +----------------------------------+
           |                                            |
           v                                            v
  +----------------------------+         +----------------------------------+
  |  Documentation Directory    |         |        Localhost (127.0.0.1)    |
  +----------------------------+         +----------------------------------+
```

### **Explanation**:
1. **CLI Interface**: Provides command-line tools to start the server, view documentation, or manage the docs folder.
2. **Server (Flask/FastAPI)**: Hosts a local web server to display documentation.
3. **Markdown Parser**: Converts `.md` files to HTML for display in the web browser.
4. **Template Renderer**: Uses templates (like Jinja2) to render the parsed markdown into a structured HTML layout.
5. **Documentation Directory**: Stores the markdown files that will be displayed.

---

## **4. Workflow**

### **Diagram**:
```plaintext
 +-------------------------+
 |  User Installs Package   |
 +-------------------------+
            |
            v
 +-------------------------+
 |  User Runs CLI Command   |  ---> `docserver start`
 +-------------------------+
            |
            v
 +-------------------------+       +--------------------------+
 |  Local Web Server Starts | ----> |  Documentation Rendered   |
 +-------------------------+       +--------------------------+
            |                                   |
            v                                   |
 +-------------------------+                   |
 |  Parses Markdown Files   | <----------------+
 +-------------------------+
```

### **Steps**:
1. **User installs the package**: `pip install docserver`
2. **User runs the CLI command**: `docserver start` creates a local server at `http://localhost:5000`.
3. **Server processes the markdown files**: The server reads markdown files from the `/docs` folder.
4. **Localhost website**: The parsed markdown is rendered in a structured way (topics, sections, etc.) and served on a local web page.
  
---
