# Model Card Generator

The following is a Streamlit app to generate Model Cards. It aims to provide a simple interface to build a new model card from scratch. The app is based on the [Huggingface Model Card Writing Tool](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool) but is meant to work on your servers.

## Getting Started

### Requirements

To run this app, you will need:

- [Docker](https://www.docker.com/get-started)
- [Python 3.9+](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eroma934/model-card-generator
2. Navigate to the cloned repository:
   ```bash
   cd model-card-generator
3. Build the Docker image
    ```bash
   docker build -t model-card-generator .
4. Run the Docker container:
    ```bash
    docker run -p 8501:8501 model-card-generator
5. Navigate to http://localhost:8501 in your web browser to access the app.

## Usage
1. Complete the necessary information about your model in the application:
    * Model Details
    * Uses
    * Limits & Risks
    * Model Training
    * Model Evaluation
    * Technical Specifications
    * How to Get Started
    * Citations (Optional)
    * Glossary (Optional)
    * More Information (Optional)
2. Click on the "Download Model Card" tab to download the completed model card
3. The file will be generated in Markdown format using Jinja.