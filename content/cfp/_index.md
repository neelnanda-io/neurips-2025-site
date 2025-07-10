# Call for Papers

We are inviting submissions of short (4 pages) and long (9 pages) papers outlining new research, due August 22, 2025. The workshop is non-archival. We do not accept submissions of work that has been accepted to an archival venue. Submissions undergoing peer review on August 22 are welcome, including works under review at the main NeurIPS conference.






We welcome papers on any of the following topics (see the Topics for Discussion section for more details and example papers), or anything else where the authors convincingly argue that it moves forward the field of mechanistic interpretability.


* Techniques: Work inventing new mechanistic interpretability techniques, evaluating the quality of existing techniques, or proposing benchmarks and tools for future evaluations.

* Exploratory analysis: Qualitative, biologically-inspired analysis of components, circuits or phenomena inside neural networks.

* Decoding superposition: Work that deepens our understanding of the hypothesis that models activations are represented in superposition, and explores techniques to decode superposed activations, such as sparse autoencoders.

* Applications of interpretability: Can we study jailbreaks/hallucinations/other interesting real-world phenomena of LLMs? Where are places where mech interp provides value, in a fair comparison with e.g. linear probing or finetuning baselines?

* Scaling and automation: How can we reduce the dependence of mechanistic interpretability on slow, subjective and expensive human labor? How much do our current techniques scale?

* Basic science: There are many fundamental mysteries of model internals, and we welcome work that can shed any light on them: Are activations sparse linear combinations of features? Are features universal? Are circuits and features even the right way to think about models?

We also welcome work that furthers the field of mechanistic interpretability in less standard ways, such as by providing rigorous negative results, or open source software, models or datasets that may be of value to the community, coding tutorials, distillations of key and poorly explained concepts, or position pieces discussing future use cases of mechanistic interpretability or that bring clarification to complex topics such as "what is a feature?".


## Reviewing and Submission Policy

All submissions must be made via OpenReview (link forthcoming). Please use the [NeurIPS 2025 LaTeX Template](https://www.google.com/url?q=https://media.neurips.cc/Conferences/NeurIPS2025/Styles.zip&sa=D&source=editors&ust=1752118866668195&usg=AOvVaw3I2-YPEzZhsitxYC2hioCJ) for all submissions (no need for a .


Submissions are non-archival. We are happy to receive submissions that are also undergoing peer review elsewhere at the time of submission, but we will not accept submissions that have already been previously published or accepted for publication at peer-reviewed conferences or journals. Submission is permitted for papers presented or to be presented at other non-archival venues (e.g. other workshops).


Reviewing for our workshop is double blind: reviewers will not know the authors' identity (and vice versa). Both short (max 4 page) and long (max 8 page) papers allow unlimited pages for references and appendices, but reviewers are not expected to read these. Evaluation of submissions will be based on the originality and novelty, the technical strength, and relevance to the workshop topics. Notifications of acceptance will be sent to applicants by email.


## Important Information

Note: You will require an OpenReview account to submit. If you do not have an institutional email (e.g. a .edu address), OpenReview moderation can take up to 2 weeks. Please make an account well before the deadline if this applies to you.


### Topics of Interest

We welcome submissions on any topic that furthers our understanding of models by leveraging their internal states. The field is young, and there are many exciting open questions. We are particularly interested in, but not limited to, the following directions:


* Model Biology & Cognition

* What can we understand about the high-level properties of models? Can we find evidence for cognitive phenomena like implicit planning, search algorithms, or internal world models?

* What does it look like for a model to "believe" something? Can we find and manipulate these beliefs?

* Do models internally represent different personas or simulators that drive their behavior, and how are these selected from context?

* Circuits and Causal Analysis

* Circuit analysis is a core part of mech interp, but our methods are still nascent. What are the best ways to find and validate circuits?

* How can we improve existing approaches like attribution graphs? What can we learn from the field of causal inference to make our analysis more rigorous?

* What are the failure modes of current causal methods, and what alternative approaches might bear fruit?

* Unsupervised Discovery & Dictionary Learning

* A key promise of interpretability is its potential to surprise us by revealing unexpected structure. How well do unsupervised methods like SAEs, patch-scopes, or training data attribution actually work for this?

* These methods have shown great promise, but their utility on downstream tasks remains an open question. We welcome work that rigorously tests their practical value against strong baselines.

* Practical Applications & Benchmarking

* If our interpretability tools are teaching us something real, they should be useful. How well do they perform on real-world downstream tasks against well-implemented baselines?

* How can we develop objective benchmarks that require genuine understanding to solve, such as eliciting secret knowledge or hidden goals?

* Can we move beyond proxies and find ways to objectively measure what we actually care about, like the "understanding" captured by a natural language hypothesis?

* Interpreting Reasoning & Chain of Thought

* Reasoning models are a big deal, we understand very little about them, and they introduce significant new challenges for interpretability.

* When is a model's Chain of Thought a faithful representation of its computation, and when is it post-hoc rationalization? What role does it actually play in the model's final output?

* How might we interpret latent reasoning models that replace transparent text-based thoughts with opaque vectors?

* Auditing & Evaluating Safety-Relevant Behaviors

* Recent work has shown sophisticated and sometimes concerning behaviors in models, like self-preservation or alignment faking. What's really going on here?

* Is this just anthropomorphism, or can interpretability tools help us find something genuinely concerning?

* Debugging & Fixing Models

* How can we apply the interpretability toolkit to understand and ideally fix unexpected model behaviors, from simple logical errors (e.g., thinking 9.8 < 9.11) to complex real-world problems like jailbreaks and hallucinations?

* Monitoring & Inference-Time Interventions

* How can we use interpretability techniques (probes, anomaly detection, SAEs) to monitor models in deployment?

* A key challenge is making these methods cheap, fast, and effective enough for production, especially in models with million-token context windows.

* Do these methods actually beat simple, strong baselines like just prompting another language model?

* Developmental Interpretability

* What can we learn about what happens during training? How and why do models and their circuits form the way they do?

* Scaling & Generalizing Interpretability

* How do findings and techniques from prior work on small models hold up at the frontier? What breaks and what scales?

* How do multimodal models represent, combine, and interfere with information from different modalities?

* What can we learn by interpreting alternative architectures like diffusion models, state space models, or graph neural networks?

* Conceptual & Foundational Work

* Our field is built on concepts like "features" and "circuits" that remain poorly defined. We welcome position papers that bring conceptual clarity and rigor to these foundational questions.

* Automating Interpretability

* How much of the interpretability research process can be automated using LLMs? How does automated analysis compare to human performance?

* Rigorous Case Studies

* We welcome rigorous, "biology-inspired" analyses of specific components or phenomena, especially those combining deep qualitative case studies with quantitative sanity checks and falsifiable hypotheses.

* Open Source & Tooling

* We strongly encourage submissions that provide open-source resources to accelerate the research of others, from better tooling and datasets to trained interpretability models (e.g., SAEs).

We enthusiastically welcome both positive and negative results—the goal is to learn. Distillations of key-but-confusing concepts and high-quality educational materials are also highly valued.