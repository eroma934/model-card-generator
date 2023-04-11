---
{{card_data}}
---

# {{ model_id }} Model Card

#  Table of Contents

- [Model Details](#model-details)
  - [Model Description](#model-description)
- [Uses](#uses)
  - [Direct Use](#direct-use)
  - [Downstream Use [Optional]](#downstream-use-optional)
  - [Out-of-Scope Use](#out-of-scope-use)
- [Bias, Risks, and Limitations](#bias-risks-and-limitations)
  - [Recommendations](#recommendations)
- [Training Details](#training-details)
  - [Training Data](#training-data)
  - [Training Procedure](#training-procedure)
    - [Data Collection & Preprocessing](#preprocessing)
    - [Training Time](#speeds-sizes-times)
- [Evaluation](#evaluation)
  - [Testing Data, Factors & Metrics](#testing-data-factors--metrics)
    - [Testing Data](#testing-data)
    - [Metrics](#metrics)
  - [Results](#results)
- [Technical Specifications](#technical-specifications-optional)
  - [Model Architecture and Objective](#model-architecture-and-objective)
  - [Compute Infrastructure](#compute-infrastructure)
    - [Hardware](#hardware)
    - [Software](#software)
- [How to Get Started with the Model](#how-to-get-started-with-the-model)
- [Citation](#citation)
- [Glossary [optional]](#glossary-optional)
- [More Information [optional]](#more-information-optional)



# Model Details

## Model Description

{{ model_description | default("More information needed", true)}}

|                          |                                                                  |
|--------------------------|------------------------------------------------------------------|
| **Developer(s)**         | {{ developers | default("More information needed", true)}}      |
| **Model & Repo Links**   | {{"[GitHub Repo]({0})".format(repo_link) if repo_link }}          |
| **Modality**             | {{ modality | default("More information needed", true)}}        |
| **Task(s)**              | {{ task | default("More information needed", true)}}           |
| **Learning Method**      | {{ learning_method | default("More information needed", true)}} |
| **Algorithm Type**       | {{ algo_type | default("More information needed", true)}}       |

## Related Models
- **Related Models:**
{{ "    -  [Parent Model]({0})".format(repo_link) if parent_model_link }}
- **Resources for more information:**
{{ "    - [Associated Paper]({0})".format(paper_link) if paper_link }}
{{ "    - [Blog Post]({0})".format(blog_link) if blog_link }}

# Uses

<!--> This section addresses questions around how the model is intended to be used, discusses the foreseeable users of the model (including those affected by the model), and describes uses that are considered out of scope or misuse of the model. <!-->

## Direct Use

<!--> This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. <!-->

{{ direct_use | default("More information needed", true)}}

## Downstream Use [Optional]

<!--> This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app <!-->

{{ downstream_use | default("More information needed", true)}}

## Out-of-Scope Use

<!--> This section addresses misuse, malicious use, and uses that the model will not work well for. <!-->

{{ oos_use | default("More information needed", true)}}

# Bias, Risks, and Limitations

<!--> This section is meant to convey both technical and sociotechnical limitations. <!-->

{{ risks | default("More information needed", true)}}

# Training Details

## Training Data

<!--> This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. <!-->

{{ training_data | default("More information needed", true)}}

## Training Procedure

<!--> This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. <!-->

### Preprocessing

{{ model_preprocessing | default("More information needed", true)}}

### Training Time

<!--> This section provides information about throughput, start/end time, checkpoint size if relevant, etc. <!-->

{{ training_time | default("More information needed", true)}}
 
# Evaluation

<!--> This section describes the evaluation protocols and provides the results. <!-->

## Testing Data, Factors & Metrics

### Testing Data

<!--> This should link to a Data Card if possible. <!-->

{{ testing_data | default("More information needed", true)}}

### Metrics

<!--> These are the evaluation metrics being used, ideally with a description of why. <!-->

{{ metrics | default("More information needed", true)}}

## Results 

{{ model_results | default("More information needed", true)}}

# Model Examination

{{ model_examination | default("More information needed", true)}}


# Technical Specifications

## Model Architecture and Objective

{{ model_specs | default("More information needed", true)}}

## Compute Infrastructure

{{ compute_infrastructure | default("More information needed", true)}}

### Hardware

{{ hardware | default("More information needed", true)}}

### Software

{{ software | default("More information needed", true)}}

# How to Get Started with the Model

Use the code below to get started with the model.

<details>
<summary> Click to expand </summary>

{{ how_to | default("More information needed", true)}}

</details>
<br>

# Citation [optional]

<!--> If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. <!-->

**BibTeX:**

{{ citation_bibtex | default("More information needed", true)}}

**APA:**

{{ citation_apa | default("More information needed", true)}}

# Glossary [optional]

<!--> If relevant, include terms and calculations in this section that can help readers understand the model or model card. <!-->

{{ glossary | default("More information needed", true)}}

# More Information [optional]

{{ more_information | default("More information needed", true)}}

## Model Card Authors

{{ model_card_authors | default("More information needed", true)}}

## Model Card Contact

{{ model_card_contact | default("More information needed", true)}}

