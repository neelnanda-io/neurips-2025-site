Call for Papers
We are inviting submissions of short (max 4 pages) and long (max 9 pages) papers outlining new research, due August 22, 2025. We welcome all submissions that convincingly argue for why they further the field: i.e. which further our ability to use the internal states of neural networks to understand them. Submit here.


We are extremely grateful to all who volunteer as reviewers, you can express interest here. We request but do not require that (co-)first authors of submitted papers volunteer as reviewers.


Details:
* The workshop is non-archival.
* Authors will be notified of acceptance by September 22.
* We do not accept submissions of work that has been accepted to an archival venue.
* Submissions undergoing peer review (on August 22) are welcome, including works under review at the main NeurIPS conference.
* All submissions must be made via OpenReview
  * Note: If you do not have an institutional email, be aware that it can take up to 2 weeks to get an OpenReview account approved. Let us know if this prevents you from submitting.
* Please use the NeurIPS 2025 LaTeX Template for all submissions (no need for a checklist).
* Both short (max 4 page) and long (max 9 page) papers allow unlimited pages for references and appendices, but reviewers are not expected to read these.
* Accepted papers will be allowed one additional page in the camera ready version, to integrate reviewer feedback.
* Long works will be held to a higher standard of rigour and depth than short works.
* Authors are encouraged but not required to attend the workshop in person
* The reviewing process is double-blind, and authors are responsible for ensuring no identifying details are included
  * We recommend searching the manuscript for the names, GitHub usernames and HuggingFace username of all core contributors before submission
* Authors are strongly encouraged to open source any code, models, prompts, data and interactive demos. A highly engaged reader should be able to replicate your results, if possible
  * We recommend https://anonymous.4open.science/ to anonymously share a GitHub repo
    * For larger files like model weights and datasets, we recommend making an anonymous HuggingFace account
  * For including interactive demos we recommend making an anonymous website or streamlit
* We welcome any work that furthers the field of mechanistic interpretability, even if in unconventional ways. In addition to standard empirical work, this includes:
  * Rigorous negative results
  * Rigorous replications of important results
  * Critiques or compelling failed replications of past work
  * Open source software (e.g. TransformerLens, nnsight, pyvene, or Penzai) and tools (e.g. Neuronpedia or Docent)
  * Models or datasets that may be of value to the community (e.g. Pythia, MultiBERTs or Gemma Scope)
  * Educational materials (e.g. the ARENA materials)
  * Distillations of key and poorly explained concepts (e.g. Ferrando et al)
  * Position pieces that bring clarity to complex topics and debates (e.g. the ‘strong’ feature hypothesis could be wrong)


Strong empirical works will clearly articulate (i) specific falsifiable hypotheses, and how the evidence provided does and does not support them; or (ii) convincingly show clear practical benefits over well-implemented baselines.


Works that clearly document the strengths and weaknesses of their evidence, and what we can learn from this are welcomed, even if it weakens the narrative or conclusions remain inconclusive. Works that downplay or omit significant limitations will not be accepted.


Authors may find Neel Nanda’s advice on paper writing to be a helpful perspective, especially those new to writing mechanistic interpretability papers.
Topics of Interest
The field is young, and there are many exciting open questions. We are particularly interested in, but not limited to, the following directions:
* Model Biology & Cognition:
  * What can we understand about the high-level properties of models? Can we find evidence for cognitive phenomena like implicit planning, search algorithms, or internal world models?
    * What does it look like for a model to "believe" something? Can we find and manipulate these beliefs? Can we probe for what a model believes to be true? Or is the entire notion of a model’s beliefs confused?
  * Do models internally represent different personas or simulators that drive their behavior, and how are these selected from context?
* Circuits and Causal Analysis:
  * Circuit analysis is a core part of mech interp, but our methods are still nascent. What are the best ways to find and validate circuits?
    * How can we improve existing approaches like attribution graphs?
  * What can we learn from the field of causal inference to make our analysis more rigorous?
  * What are the failure modes of current causal methods, and what alternative approaches might bear fruit?
  * How far can we push weight-based analysis?
* Unsupervised Discovery & Dictionary Learning:
  * A key promise of interpretability is its potential to surprise us by revealing unexpected structure. How well do unsupervised methods like sparse autoencoders, patchscopes, or training data attribution actually work for this?
  * These methods have shown great promise, but their utility on downstream tasks remains unclear. We welcome work that rigorously tests their practical value against strong baselines.
* Practical Applications & Benchmarking:
  * If our interpretability tools are teaching us something real, they should be useful. How well do they perform on real-world downstream tasks against well-implemented baselines?
  * How can we develop objective benchmarks that require genuine understanding to solve, such as eliciting secret knowledge or hidden goals?
  * Can we move beyond proxies and find ways to objectively measure what we actually care about, like the "understanding" captured by a natural language hypothesis?
  * Can we develop other compelling benchmarks for our mech interp capabilities? (e.g. Mueller et al)
  * Can we achieve outcomes with interpretability that may not be practical with purely black box methods, like convincing models that they are not being tested?
* Interpreting Reasoning & Chain of Thought:
  * Reasoning models are a big deal, we understand very little about them, and they introduce significant new challenges for interpretability. What should the paradigm for reasoning model interpretability look like?
  * Are black box methods performing causal interventions on the steps in a reasoning trace a valuable tool, or fundamentally flawed?
  * When is a model's Chain of Thought a faithful representation of its computation, and when is it post-hoc rationalization? How can we determine what role it actually plays in the model's final output?
  * How might we interpret latent reasoning models that replace transparent text-based thoughts with opaque vectors?
* Auditing & Evaluating Safety-Relevant Behaviors:
  * Recent work has shown sophisticated and sometimes concerning behaviors in models, like alignment faking or blackmailing. What's really going on here? Is this just anthropomorphism, or can interpretability tools help us determine if this is concerning?
  * Can we build and interpret model organisms exhibiting hypothesised properties, such as hidden goals? Do our techniques work in a realistic simulation?
  * Can we use interpretability to improve our ability to red team models, and find the conditions that induce harmful behavior?
* Debugging & Fixing Models:
  * How can we apply the interpretability toolkit to understand and ideally fix unexpected model behaviors, like simple logical errors (e.g., thinking 9.8 < 9.11)?
  * How can interpretability shed light on complex real-world problems like jailbreaks, implicit bias and hallucinations? In which settings is it the best tool for resolving these problems, when compared to baselines in a fair fight?
* Monitoring & Inference-Time Interventions:
  * How can we use interpretability techniques (probes, anomaly detection, sparse autoencoders) to monitor models in deployment?
  * Do these methods actually beat simple, strong baselines like just prompting or fine-tuning another language model? (e.g. Cunningham et al)
  * How well do cheap methods like probing work on frontier models, including in more complex situations like 1M+ token context windows, and multi-modal inputs? How can they be made more effective and efficient?
* Developmental Interpretability:
  * What can we learn about what happens during training? How and why do models and their circuits form the way they do?
* Scaling & Generalizing Interpretability:
  * How do findings and techniques from prior work on small models hold up at the frontier? What breaks and what scales? (e.g. Lieberum et al)
  * How do multimodal models represent, and combine information from different modalities? What problems can this introduce?
  * What can we learn by interpreting alternative architectures like diffusion models, state space models, or graph neural networks?
* Conceptual & Foundational Work:
  * Our field is built on concepts like "features", "circuits" and “linear representations” that remain poorly defined. We welcome position papers that bring conceptual clarity and rigor to these foundational questions.
* Automating Interpretability:
  * How much of the interpretability research process can be automated using LLMs? How does automated analysis compare to human performance? This includes both automating specific steps like interpreting maximum activating dataset examples, and building an agent to perform some of the research work autonomously
* Basic science:
  * There are many fundamental mysteries of model internals, and we welcome work that can shed any light on them: Are activations sparse linear combinations of features? Are features universal? Are circuits and features even the right way to think about models?
* Rigorous Case Studies:
  * We welcome rigorous, "biology-inspired" analyses of specific model components or phenomena. Strong works here will combine deep qualitative case studies with quantitative sanity checks and falsifiable hypotheses.
  * Novel paradigms:
  * We welcome any original and rigorous approach to achieving understanding of models and the computation happening inside of them, even if it does not fit the standard conception of mech interp (e.g. work leveraging black box methods like Bogdan et al and Rajamanoharan et al)
* Along with any other works that further the mission of understanding models via their internals!