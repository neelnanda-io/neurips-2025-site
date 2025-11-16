# Call for Papers
### EDIT: The call for papers is now closed, thanks all for your submissions!
We are inviting submissions of **short** (max 4 pages) and **long** (max 9 pages) papers outlining new research, due **August 22, 2025** (EDIT: Call for papers closed). We welcome all submissions that convincingly argue for why they further the field: i.e. which further our ability to use the internal states of neural networks to understand them. [Submit here](https://openreview.net/group?id=NeurIPS.cc/2025/Workshop/MechInterp). 

We are extremely grateful to all who volunteer as reviewers, you can [express interest here](https://docs.google.com/forms/d/e/1FAIpQLSdiw1SJllzoTz_nqzDTzTOGb9DV3W_truQyh-WvYj_QGIi7Mg/viewform?usp=dialog). We request but do not require that (co-)first authors of submitted papers volunteer as reviewers. 

Details: 
* The workshop is **non-archival**.
* Authors will be notified of acceptance by **September 22**.
* We **do not accept** submissions of work that has been accepted to an **archival** venue.
* Submissions **undergoing peer review** (on August 22) are **welcome**, including works under review at the main NeurIPS conference.
* All submissions must be made [via OpenReview](https://openreview.net/group?id=NeurIPS.cc/2025/Workshop/MechInterp)
  * **Note**: If you do not have an institutional email, be aware that it can take **up to 2 weeks** to get an OpenReview account approved. [Let us know](mailto:neurips2025@mechinterpworkshop.com) if this prevents you from submitting.
* Please use the [NeurIPS 2025 LaTeX Template](https://media.neurips.cc/Conferences/NeurIPS2025/Styles.zip) for all submissions (no need for a checklist).
* Both short (max 4 page) and long (max 9 page) papers allow unlimited pages for references and appendices, but reviewers are not expected to read these.
* Accepted papers will be allowed **one additional page in the camera ready** version, to integrate reviewer feedback.
* Long works will be held to a higher standard of rigour and depth than short works.
* Authors are encouraged but not required to attend the workshop in person
* The reviewing process is **double-blind**, and authors are responsible for ensuring no identifying details are included
  * We recommend searching the manuscript for the names, GitHub usernames and HuggingFace username of all core contributors before submission
* Authors are strongly encouraged to open source any code, models, prompts, data and interactive demos. A highly engaged reader should be able to replicate your results, if possible
  * We recommend [https://anonymous.4open.science/](https://anonymous.4open.science/) to anonymously share a GitHub repo
  * For larger files like model weights and datasets, we recommend making an anonymous HuggingFace account
  * For including interactive demos we recommend making an anonymous website or streamlit
* We welcome any work that furthers the field of mechanistic interpretability, even if in **unconventional ways**. In addition to standard empirical work, this includes:
  * Rigorous negative results
  * Rigorous replications of important results
  * Critiques or compelling failed replications of past work
  * Open source software (e.g. [TransformerLens](https://github.com/neelnanda-io/TransformerLens), [nnsight](https://github.com/ndif-team/nnsight), [pyvene](https://github.com/stanfordnlp/pyvene/tree/main/pyvene/models/mlp), or [Penzai](https://github.com/google-deepmind/penzai)) and tools (e.g. [Neuronpedia](http://neuronpedia.org) or [Docent](https://transluce.org/introducing-docent))
  * Models or datasets that may be of value to the community (e.g. [Pythia](https://arxiv.org/abs/2304.01373), [MultiBERTs](https://arxiv.org/abs/2106.16163) or [Gemma Scope](https://arxiv.org/abs/2408.05147))
  * Educational materials (e.g. [the ARENA materials](https://arena3-chapter1-transformer-interp.streamlit.app/))
  * [Distillations](https://distill.pub/2017/research-debt/) of key and poorly explained concepts (e.g. [Ferrando et al](https://arxiv.org/abs/2405.00208))
  * Position pieces that bring clarity to complex topics and debates (e.g. [the ‘strong’ feature hypothesis could be wrong](https://www.alignmentforum.org/posts/tojtPCCRpKLSHBdpn/the-strong-feature-hypothesis-could-be-wrong))

Strong empirical works will clearly articulate (i) **specific falsifiable hypotheses**, and how the evidence provided does and does not support them; **or** (ii) convincingly show **clear practical benefits** over well-implemented baselines. 

Works that clearly document the strengths and weaknesses of their evidence, and what we can learn from this are welcomed, even if it weakens the narrative or conclusions remain inconclusive. Works that downplay or omit significant limitations **will not be accepted**. 

Authors may find [Neel Nanda’s advice on paper writing](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers) to be a helpful perspective, especially those new to writing mechanistic interpretability papers. 
### Topics of Interest
The field is young, and there are many exciting open questions. We are particularly interested in, but not limited to, the following directions: 
* **Model Biology & Cognition**:
  * What can we understand about the high-level properties of models? Can we find evidence for cognitive phenomena like [implicit planning](https://transformer-circuits.pub/2025/attribution-graphs/biology.html%23dives-poems), search algorithms, or [internal world models](https://arxiv.org/abs/2210.13382)?
  * What does it look like for a model to "believe" something? Can we find and manipulate these beliefs? Can we probe for what a model [believes to be true](https://arxiv.org/abs/2310.06824)? Or is the entire notion of a model’s beliefs confused?
  * Do models internally represent different [personas](https://arxiv.org/abs/2406.12094) or [simulators](https://www.nature.com/articles/s41586-023-06647-8) that drive their behavior, and how are these selected from context?
* **Circuits and Causal Analysis**:
  * [Circuit analysis](https://distill.pub/2020/circuits/zoom-in/) is a core part of mech interp, but our methods are still nascent. What are the best ways to find and validate circuits?
  * How can we improve existing approaches like [attribution](https://arxiv.org/abs/2406.11944) [graphs](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)?
  * What can we learn from [the field of causal inference](https://arxiv.org/abs/2407.04690) to make our analysis more rigorous?
  * What are the [failure modes](https://arxiv.org/abs/2307.15771) of current causal methods, and what alternative approaches might bear fruit?
  * How far can we push [weight-based](https://arxiv.org/abs/2301.05217) [analysis](https://arxiv.org/abs/2410.08417)?
* **Unsupervised Discovery & Dictionary Learning**:
  * A key promise of interpretability is its potential to surprise us by revealing unexpected structure. How well do unsupervised methods like [sparse](https://arxiv.org/abs/2103.15949) [autoencoders](https://transformer-circuits.pub/2023/monosemantic-features), [patch](https://arxiv.org/abs/2401.06102)[scopes](https://arxiv.org/abs/2403.10949v2), or [training](https://proceedings.mlr.press/v70/koh17a?ref=https://githubhelp.com) [data](https://arxiv.org/abs/2308.03296) [attribution](https://arxiv.org/abs/2205.11482) actually work for this?
  * These methods have [shown](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) [great](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) [promise](https://arxiv.org/abs/2503.10965), but their [utility](https://arxiv.org/abs/2502.16681) [on](https://www.tilderesearch.com/blog/sieve) [downstream](https://arxiv.org/abs/2501.17148) [tasks](https://transformer-circuits.pub/2024/features-as-classifiers/index.html) [remains](https://arxiv.org/abs/2502.04382) [unclear](https://www.alignmentforum.org/posts/4uXCAJNuPKtKBsi28/negative-results-for-saes-on-downstream-tasks). We welcome work that rigorously tests their practical value against strong baselines.
* **Practical Applications & Benchmarking**:
  * If our interpretability tools are teaching us something real, they should be useful. How well do they perform on real-world downstream [tasks](https://www.lesswrong.com/posts/wGRnzCFcowRCrpX4Y/downstream-applications-as-validation-of-interpretability) against well-implemented baselines?
  * How can we develop objective benchmarks that require genuine understanding to solve, such as eliciting [secret knowledge](https://arxiv.org/abs/2505.14352) or [hidden goals](https://arxiv.org/abs/2503.10965)?
  * Can we move beyond proxies and find ways to objectively measure what we actually care about, like the ["understanding" captured by a natural language hypothesis](https://arxiv.org/abs/2502.04382)?
  * Can we develop other compelling benchmarks for our mech interp capabilities? (e.g. [Mueller et al](https://arxiv.org/abs/2504.13151))
  * Can we achieve outcomes with interpretability that may not be practical with purely black box methods, like [convincing models that they are not being tested](https://arxiv.org/abs/2505.14617v2)?
* **Interpreting Reasoning & Chain of Thought**:
  * Reasoning models are a big deal, we understand very little about them, and they introduce significant new challenges for interpretability. What should the paradigm for reasoning model interpretability look like?
  * Are black box methods performing causal interventions on the steps in a reasoning trace [a valuable tool](https://arxiv.org/abs/2506.19143), or fundamentally flawed?
  * When is a model's Chain of Thought a [faithful representation](https://arxiv.org/abs/2305.04388) of its computation, and when is it [post-hoc rationalization](https://arxiv.org/abs/2503.08679)? How can we determine what role it actually plays in the model's final output?
  * How might we interpret [latent reasoning models](https://arxiv.org/abs/2412.06769) that replace transparent text-based thoughts with opaque vectors?
* **Auditing & Evaluating Safety-Relevant Behaviors**:
  * Recent work has shown sophisticated and sometimes concerning behaviors in models, like [alignment faking](https://arxiv.org/abs/2412.14093) or [blackmailing](https://www.anthropic.com/research/agentic-misalignment). What's really going on here? Is this just anthropomorphism, or can interpretability tools help us determine if this is concerning?
  * Can we build and interpret model organisms exhibiting hypothesised properties, such as [hidden goals](https://arxiv.org/abs/2503.10965)? Do our techniques work in a realistic simulation?
  * Can we use interpretability to improve our ability to red team models, and find the conditions that induce harmful behavior?
* **Debugging & Fixing Models**:
  * How can we apply the interpretability toolkit to understand and ideally fix unexpected model behaviors, like simple logical errors (e.g., [thinking 9.8 < 9.11](https://transluce.org/observability-interface))?
  * How can interpretability shed light on complex real-world problems like [jailbreaks](https://transformer-circuits.pub/2025/attribution-graphs/biology.html%23dives-jailbreak), [implicit bias](https://arxiv.org/abs/2506.10922) and [hallucinations](https://arxiv.org/abs/2411.14257)? In which settings is it the best tool for resolving these problems, when compared to baselines in a fair fight?
* **Monitoring & Inference-Time Interventions**:
  * How can we use interpretability techniques ([probes](https://arxiv.org/abs/2102.12452), anomaly detection, sparse autoencoders) to monitor models in deployment?
  * Do these methods actually beat simple, strong baselines like just prompting or fine-tuning another language model? (e.g. [Cunningham et al](https://alignment.anthropic.com/2025/cheap-monitors/))
  * How well do cheap methods like probing work on frontier models, including in more complex situations like 1M+ token context windows, and multi-modal inputs? How can they be made more effective and efficient?
* **Developmental Interpretability**:
  * What can we learn about what happens during training? How and why do models and their circuits form the way they do?
* **Scaling & Generalizing Interpretability**:
  * How do findings and techniques from prior work on small models hold up at the frontier? What breaks and what scales? (e.g. [Lieberum et al](https://arxiv.org/abs/2307.09458))
  * How do multimodal models represent, and combine information from different modalities? What [problems](https://openreview.net/pdf?id=VUhRdZp8ke) can this introduce?
  * What can we learn by interpreting alternative architectures like diffusion models, state space models, or graph neural networks?
* **Conceptual & Foundational Work**:
  * Our field is built on concepts like "features", "[circuits](https://distill.pub/2020/circuits/zoom-in/)" and “[linear representations](https://transformer-circuits.pub/2024/july-update/index.html%23linear-representations)” that remain poorly defined. We welcome position papers that bring conceptual clarity and rigor to these foundational questions.
* **Automating Interpretability**:
  * How much of the interpretability research process can be automated using LLMs? How does automated analysis compare to human performance? This includes both automating specific steps like [interpreting maximum activating dataset examples](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html), and [building an agent](https://arxiv.org/abs/2404.14394) to perform some of the research work autonomously
* **Basic science**:
  * There are many fundamental mysteries of model internals, and we welcome work that can shed any light on them: Are activations [sparse linear](https://arxiv.org/abs/1601.03764) [combinations of features](https://transformer-circuits.pub/2022/toy_model/index.html)? Are features universal? Are circuits and features even the right way to think about models?
* **Rigorous Case Studies**:
  * We welcome rigorous, "[biology-inspired](https://distill.pub/2020/circuits/curve-circuits/)" analyses of [specific model](https://arxiv.org/abs/2310.04625) [components](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) [or](https://arxiv.org/abs/2305.01610) [phenomena](https://arxiv.org/abs/2306.09346). Strong works here will combine deep qualitative case studies with quantitative sanity checks and falsifiable hypotheses.
* **Novel paradigms**:
  * We welcome any original and rigorous approach to achieving understanding of models and the computation happening inside of them, even if it does not fit the standard conception of mech interp (e.g. work leveraging black box methods like [Bogdan et al](https://arxiv.org/abs/2506.19143) and [Rajamanoharan et al](https://www.alignmentforum.org/posts/wnzkjSmrgWZaBa2aC/self-preservation-or-instruction-ambiguity-examining-the))
* Along with any other works that further the mission of understanding models via their internals!