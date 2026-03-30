---
title: "Call for Papers"
type: "cfp"
---

We are inviting submissions of **short** (max 4 pages) and **long** (max 8 pages) papers outlining new research, due **May 8th, 2026 (AOE)**. We welcome all submissions that convincingly argue for why they further the field: i.e. which further our ability to use the internal states of neural networks to understand them. **Submission link coming soon.**

**We require at least one reciprocal reviewer per submission!** Each reciprocal reviewer will be assigned 3 papers to review. You can be a reciprocal reviewer on max 3 papers.

We are extremely grateful to all who volunteer as reviewers, you can [express interest here](https://forms.gle/LRpywTjuAoFqbWaB7).

Details:

* The workshop is **non-archival**.
* Authors will be notified of acceptance by **June 12th (AOE)**.
* We welcome submissions of papers that have already been accepted to ICML 2026. There will be an option to request a fast-track submission, in which authors will be asked to provide evidence of previous reviews and acceptance. Fast-track submissions are still subject to additional reviews (e.g., theme fit) once all other reviews are completed.
* We **do not accept** submissions of work that has been accepted to an **archival** venue other than ICML 2026.
* Submissions **undergoing peer review** (e.g., COLM, NeurIPS) at the time of the paper submission deadline are **welcome.**
* All submissions must be made via OpenReview
  * **Note**: If you do not have an institutional email, be aware that it can take **up to 2 weeks** to get an OpenReview account approved. Please plan accordingly.
* Please use the [ICML 2026 LaTeX Template](https://icml.cc/Conferences/2026/AuthorInstructions) for all submissions. We will also accept submissions in NeurIPS format, but accepted papers must be converted to the ICML format for the camera ready deadline.
* Both short (max 4 page) and long (max 8 page) papers allow unlimited pages for references and appendices, but reviewers are not expected to read these.
* Accepted papers will be allowed **one additional page in the camera ready** version, to integrate reviewer feedback.
* Long works will be held to a higher standard of rigor and depth than short works.
* Authors are encouraged but not required to attend the workshop in person
* The reviewing process is **double-blind**, and authors are responsible for ensuring no identifying details are included
  * We recommend searching the manuscript for the names, GitHub usernames and HuggingFace username of all core contributors before submission
* Authors are strongly encouraged to open source any code, models, prompts, data and interactive demos. Reviewers will specifically be asked to take into account reproducibility, code, and/or data access.
  * We recommend [https://anonymous.4open.science/](https://anonymous.4open.science/) to anonymously share a GitHub repo
  * For larger files like model weights and datasets, we recommend making an anonymous HuggingFace account
  * For including interactive demos we recommend making an anonymous website or streamlit
* We welcome any work that furthers the field of mechanistic interpretability, even if in **unconventional ways**. In addition to standard empirical work, this includes:
  * Rigorous negative results
  * Rigorous replications of important results
  * Critiques or compelling failed replications of past work
  * Open source software (e.g. [TransformerLens](https://github.com/neelnanda-io/TransformerLens), [nnsight](https://github.com/ndif-team/nnsight), [pyvene](https://github.com/stanfordnlp/pyvene/tree/main/pyvene/models/mlp), or [Penzai](https://github.com/google-deepmind/penzai)) and tools (e.g. [Neuronpedia](http://neuronpedia.org/) or [Docent](https://transluce.org/introducing-docent))
  * Models or datasets that may be of value to the community (e.g. [Pythia](https://arxiv.org/abs/2304.01373), [MultiBERTs](https://arxiv.org/abs/2106.16163) or [Gemma Scope](https://arxiv.org/abs/2408.05147))
  * Educational materials (e.g. [the ARENA materials](https://arena3-chapter1-transformer-interp.streamlit.app/))
  * [Distillations](https://distill.pub/2017/research-debt/) of key and poorly explained concepts (e.g. [Ferrando et al](https://arxiv.org/abs/2405.00208))
  * Position pieces that bring clarity to complex topics and debates (e.g. [the 'strong' feature hypothesis could be wrong](https://www.alignmentforum.org/posts/tojtPCCRpKLSHBdpn/the-strong-feature-hypothesis-could-be-wrong))

Strong empirical works will clearly articulate (i) **specific falsifiable hypotheses**, and how the evidence provided does and does not support them; **or** (ii) convincingly show **clear practical benefits** over well-implemented baselines.

Works that clearly document the strengths and weaknesses of their evidence, and what we can learn from this are welcomed, even if it weakens the narrative or conclusions remain inconclusive. Works that downplay or omit significant limitations **will not be accepted**.

Authors may find [Neel Nanda's advice on paper writing](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers) to be a helpful perspective, especially those new to writing mechanistic interpretability papers.

### Topics of Interest

We are particularly interested in, but not limited to, the following directions:

* **Understanding Model Internals**
  * What can we learn about high-level properties (i.e., representations, feature geometry) of models, as well as how they are used internally?
  * Can we find evidence for cognitive phenomena such as latent reasoning, implicit planning, search algorithms, or internal world models?
  * Ex: How are {beliefs, personas, world models, reasoning processes, implicit goals} represented?
* **Methods for Mechanistic Discovery**
  * How can we effectively uncover and validate internal structures?
  * How can {circuit analyses, causal methods, attribution graphs, dictionary learning, training-data attributions} be improved? What are other novel paradigms we should consider?
* **Interpretability for Practical Applications, Development, and Benchmarking**
  * How can interpretability tools and/or insights help us with real-world downstream applications, model development, or evaluations?
  * How can interpretability help us identify, "debug", and fix undesirable/unexpected model behaviors?
  * How can we benchmark our progress in our field?
* **Interpretability for Safety, Monitoring, and Model Repair**
  * How can interpretability help us develop safer models? How can interpretability help us detect undesirable phenomena such as alignment faking, subliminal learning, or emergent misalignment?
  * How can such tools help us monitor deployed models?
* **Scaling, Generalizing, and Automating Interpretability**
  * How can we expand beyond studying controlled, templated domains to more realistic settings, on larger frontier models?
  * How well do insights from toy settings generalize to scaled-up, more complex models?
  * How can we automate interpretability efforts, perhaps with the help of recent ML developments (e.g., agents, Activation Oracle-style decoding)?
* **Interpreting Domain-specific Foundation Models for Knowledge Discovery**
  * Can we reverse-engineer or understand foundation models in other domains to learn from models?
* **Conceptual & Foundational Work**
  * What is the right framework to characterize model internals? How should concepts like "features" or "circuits" be defined?
