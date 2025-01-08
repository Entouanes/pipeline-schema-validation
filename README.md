<div align="center">
  <h1>🎯 Pipeline Schema Validation</h1>
  
  <p align="center">
    <strong>Azure DevOps pipeline to validate outputs against Graph REST API guidelines</strong>
  </p>
  <p align="center">
    <a href="#-quickstart">Quickstart</a> •
    <a href="#-key-features">Features</a> •
    <a href="#-installation">Installation</a> •
    <a href="#%EF%B8%8F-usage">Usage</a>
  </p>
  <p align="center">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge">
    <img alt="Python" src="https://img.shields.io/badge/python-3.x-blue?style=for-the-badge">
    <img alt="Azure" src="https://img.shields.io/badge/azure-devops-0078D4?style=for-the-badge">
  </p>
</div>

## 🌟 What is Pipeline Schema Validation?

Pipeline Schema Validation is a project that demonstrates the use of Azure DevOps pipelines to validate outputs against Graph REST API guidelines. This codebase showcases how to integrate validation logic into a CI/CD workflow.

- 🤖 **Automated Validation**: Uses Azure DevOps to automate the validation process
- 🎯 **Focused Validation**: Validates outputs against specific Graph REST API guidelines

## 🚀 Quickstart

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pipeline-schema-validation.git
    cd pipeline-schema-validation
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the tests:
    ```sh
    pytest
    ```

## 📝 Example

Here's a sample validation function:

```python
from graph_api_guidelines import guidelines

def validate_schema(output: dict) -> bool:
    # Implement validation logic based on guidelines
    return True  # Placeholders
```

Running the tests produces this output:

```sh
$ pytest
============================= test session starts ==============================
collected 1 item

tests/test_validate_bicep.py .                                          [100%]

============================== 1 passed in 0.01s ===============================
```

## ✨ Key Features
### 🔍 Smart Validation
- **Guideline-Based Validation:** Validates Bicep files against established best practices
- **Automated Testing:** Integrates with Azure DevOps pipelines for automated validation
### 📊 Comprehensive Reporting
- **Test Results:** Clear pass/fail results for each validation test
## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/pipeline-schema-validation.git

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
## 🛠️ Usage
1. Define your Bicep file validation logic in src/validate_bicep.py.
2. Define the Bicep best practices in src/bicep_guidelines.py.
3. Write tests for your Bicep file validation logic in `tests/test_validate_bicep.py`.
## 🔧 Azure DevOps Pipeline
The Azure DevOps pipeline configuration is located in the azure-pipelines.yml file. This pipeline will automatically run the Bicep file validation tests on each push to the repository.
