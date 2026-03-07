# LLM Fine-Tuning Assignment

Design and implement an experiment where you fine-tune a chosen base LLM using two methods: **full fine-tuning** and one **PEFT (Parameter-Efficient Fine-Tuning)** method (e.g., LoRA, QLoRA). Compare the performance, efficiency, and resource requirements of the two methods, then submit a 1-page experiment report and all related code.

---

## Assignment Requirements

### 1. Experiment Design & Implementation

- **Base Model Selection:** Choose an open-source LLM (e.g., Llama 3, Qwen, Gemma, DeepSeek, Mistral) from platforms like Hugging Face Hub. Prioritize smaller models (e.g., 0.5B, 3B parameters) if using free GPUs to avoid memory constraints.
- **Task Selection:** Pick a downstream NLP task suitable for fine-tuning. The task should have a clear evaluation metric (e.g., accuracy for classification, BLEU for generation).
- **Dataset Selection:** Use a ready-to-use dataset (no need to create your own) that matches your chosen task.
- **Fine-Tuning Methods:**
  - **Full Fine-Tuning:** Update all parameters of the base model during training.
  - **PEFT Method:** Implement LoRA (Low-Rank Adaptation) or QLoRA (quantized LoRA) — both are popular, efficient, and well-supported by easy-to-use frameworks.

---

### 2. Submission Requirements

#### 1-Page Experiment Report (PDF format)

- **Introduction:** Briefly describe your chosen base model, task, and dataset (1-2 sentences).
- **Methodology:** Explain the two fine-tuning methods and key hyperparameters (e.g., learning rate, batch size, number of epochs).
- **Results:** Present a clear comparison of the two methods (e.g., performance metric, training time, GPU memory usage).
- **Conclusion:** Summarize your findings — which method performed better, which was more efficient, and why.

#### All Experiment Code (ZIP file or GitHub link)

- Include all code used for fine-tuning (e.g., notebook files, configuration files).

---

## Key Resources

### 1. Free GPUs for Fine-Tuning

Free GPUs are ideal for this assignment (no cost, no need for local hardware). Options ordered by ease of use:

- **Google Colab** *(Recommended)*
- **Kaggle Kernels**

> **Note:** Free GPUs have session limits (e.g., Colab sessions end after ~12 hours if inactive). Save your progress frequently (e.g., to Google Drive for Colab) to avoid losing work.

---

### 2. Tasks & Ready-to-Use Datasets

All datasets below are ready to use on [Hugging Face Datasets](https://huggingface.co/datasets) — no preprocessing required for most frameworks.

| Task Type | Dataset | Task Description | Evaluation Metric | Notes |
|---|---|---|---|---|
| Sentiment Analysis (Text Classification) | `imdb` | Classify movie reviews as positive or negative. | Accuracy | Small dataset (~50k samples), easy to fine-tune quickly. |
| Question Answering (QA) | `squad` | Answer questions based on a given context paragraph. | Exact Match (EM), F1 Score | Standard QA dataset, well-supported by all frameworks. |
| Text Completion | `hellaswag` | Complete a given prompt with the most logical continuation. | Accuracy | Ideal for testing text generation capabilities of fine-tuned models. |
| Instruction Following | `alpaca_gpt4_zh` | Generate responses that follow user instructions (Chinese/English). | BLEU, ROUGE | Built-in in LLaMA-Factory; no extra preprocessing needed. |

---

### 3. Fine-Tuning Frameworks

These frameworks eliminate the need to write fine-tuning code from scratch. You can configure and run fine-tuning with minimal setup via UI or simple configuration files.

#### LLaMA-Factory *(Recommended for Beginners)*

An open-source, low-code framework with a Web UI for one-click fine-tuning.

- **Supported Models:** 50+ base models (Llama 3, Qwen, ChatGLM, etc.)
- **Supported Methods:** Full fine-tuning, LoRA, QLoRA
- **Built-in Datasets:** Includes `alpaca_gpt4_zh` and others
- **Workflow:**
  1. Install the framework
  2. Launch the Web UI at `http://localhost:7860`
  3. Select base model, fine-tuning method, and dataset
  4. Click **Start** to begin training
- **GitHub:** https://github.com/hiyouga/LLaMA-Factory

#### Hugging Face Transformers

You may also use the `transformers` library directly from Hugging Face for a more hands-on, code-first approach.
