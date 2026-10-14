Multimodal AI Project --- Implementation Notes

1. Starting point: prove the model works first

We started with the smallest possible project:

multimodal-ai/
├── .env
├── .gitignore
├── requirements.txt
├── main.py
└── outputs/

The first goal was not to design the final architecture. The goal
was to prove that a Hugging Face hosted text model could actually run
successfully.

The first main.py was responsible for:

Loading environment variables.

Reading the Hugging Face token.

Creating the Hugging Face InferenceClient.

Defining a prompt.

Calling the text-generation model.

Extracting the generated text.

Printing the result.

Conceptually:

main.py
│
├── configuration
├── Hugging Face client setup
├── prompt
├── model invocation
└── output

This gave us a working vertical slice before introducing
abstractions.

2. First refactor: extract configuration

Once the text generation worked, we moved configuration out of
main.py.

Before

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is missing from .env")

After

multimodal-ai/
├── .env
├── .gitignore
├── requirements.txt
├── config.py
├── main.py
└── outputs/

config.py became responsible for:

Loading .env

Reading configuration/environment variables

Validating required configuration

The important architectural idea:

Configuration is a separate responsibility from model generation.

3. Extract the Hugging Face client

As soon as we had a reusable external dependency, we separated the
Hugging Face client setup.

app/
├── __init__.py
└── clients/
    ├── __init__.py
    └── huggingface.py

huggingface.py owns the creation/configuration of:

InferenceClient(...)

The application should not need to know how the Hugging Face client is
authenticated or configured.

The dependency direction became:

main.py
   ↓
application logic
   ↓
Hugging Face client
   ↓
Hugging Face API

4. Extract text generation

Next we separated what our application does from how it
communicates with Hugging Face.

We created:

app/
├── clients/
│   └── huggingface.py
│
└── generators/
    ├── __init__.py
    └── text.py

text.py owns the text-generation capability:

def generate_text(prompt: str) -> str:
    ...

Now main.py can focus on the application flow:

def main():
    prompt = "..."
    result = generate_text(prompt)
    print(result)

This gives us an important separation:

main.py
    │
    ▼
generate_text()
    │
    ▼
Hugging Face client
    │
    ▼
Hugging Face API

We deliberately used a simple function instead of creating a
TextGenerator class. A class was not necessary yet.

5. Prove image generation independently

Before integrating image generation into the application, we created a
temporary:

test_image.py

The purpose was to verify:

prompt
  ↓
Hugging Face image model
  ↓
PIL Image
  ↓
PNG file

Once image generation worked, the temporary logic was moved into:

app/generators/image.py

The function became conceptually:

def generate_image(prompt: str, output_path: str | Path) -> Path:
    ...

The generator owns image generation and saving the generated artifact.

6. Current modular structure

After the refactoring, the project evolved toward:

multimodal-ai/
│
├── app/
│   ├── __init__.py
│   │
│   ├── clients/
│   │   ├── __init__.py
│   │   └── huggingface.py
│   │
│   └── generators/
│       ├── __init__.py
│       ├── text.py
│       └── image.py
│
├── outputs/
│   ├── images/
│   └── videos/
│
├── .env
├── .gitignore
├── requirements.txt
├── config.py
└── main.py

The responsibilities are now roughly:

File/folder                Responsibility

config.py                Application configuration/environment
clients/huggingface.py   Hugging Face client setup
generators/text.py       Text generation
generators/image.py      Image generation
main.py                  Application entry point/orchestration
outputs/                 Generated artifacts

7. The most important architectural lesson

We did not design the entire folder structure at the beginning.

Instead:

Make it work
     ↓
Observe responsibilities
     ↓
Extract distinct responsibility
     ↓
Make it work again
     ↓
Add next capability
     ↓
Refactor when complexity appears

The rule is:

Create a new file when a distinct responsibility, reusable component,
testing boundary, or meaningful complexity emerges.

Do not create folders simply because a tutorial or "standard
architecture" says they should exist.

For example, we did not initially create:

services/
repositories/
factories/
interfaces/
utils/
core/
workflows/

because we had not earned those abstractions yet.

8. Vertical slice principle

For each new model/modality, we follow the same pattern:

1. Make the raw capability work
2. Verify the model/API
3. Save/inspect the output
4. Extract the working logic
5. Integrate it into the application

For example:

Text:
single-file test → working → generators/text.py

Image:
single-file test → working → generators/image.py

Video:
single-file test → working → generators/video.py

This prevents us from debugging model/API problems and architecture
problems at the same time.

9. Where we are heading

Once text, image, and video generators work independently, we can
introduce an actual workflow:

User prompt
    ↓
Text model
    ↓
image prompt + video prompt + narration
    ↓
┌──────────────┬───────────────┐
▼              ▼               ▼
Text         Image           Video
generator    generator       generator

At that point a workflows/ package becomes justified, and we can
introduce LangGraph.

The eventual architecture can become:

app/
├── clients/
│   └── huggingface.py
│
├── generators/
│   ├── text.py
│   ├── image.py
│   └── video.py
│
└── workflows/
    └── content_generation.py

The important point is that the workflow layer comes after we
understand and verify the individual capabilities.

10. Rule to remember

When unsure where code belongs, ask:

"What is the single responsibility of this piece of code?"

Then group code around that responsibility.

Avoid asking:

"Which folder is normally used for this?"

The folder structure should emerge from the responsibilities of the
application.