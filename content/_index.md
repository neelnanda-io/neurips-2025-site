## Why this workshop?

Larger and more capable models are having an increasing impact on the world, yet our ability to understand their internal mechanisms remains a fundamental scientific challenge. While we can observe what models do, we have limited insight into how they do it—their internal representations, learned algorithms, and how this all connects to their outward behavior remain largely opaque. This gap between performance and understanding limits our ability to predict model behavior, ensure reliability, and detect sophisticated adversarial or deceptive behavior. And many of the deepest scientific mysteries in machine learning may remain out of reach if we cannot look inside the black box.


Mechanistic interpretability addresses this challenge by developing principled methods to analyze and understand a model’s internals–weights and activations–and to use this understanding to gain greater insight into its behavior, and the computation underlying it. The field has grown rapidly, with sizable communities in academia, industry and independent research, 140+ papers submitted to our ICML 2024 workshop, dedicated startups, and producing a rich ecosystem of tools and techniques. This workshop brings together diverse perspectives from this vibrant community to share recent advances and chart future directions.


[SIGNUP]


[IMAGE-PAIR: conference-pic.jpg | rooftop-pic.jpg | The first Mechanistic  Interpretability Workshop (ICML 2024)]


## Workshop Goals

The mechanistic interpretability field benefits from a rich diversity of approaches—from rigorous mathematical analysis to large-scale empirical studies, from reverse-engineering a model via bottom-up circuit analysis, to assisting behavioral analysis via top-down analysis of model representations. But all are unified by the belief that there is meaning and structure to be found inside our models, and that this is worth studying.


This diversity reflects the field's breadth and the many valid paths toward understanding neural networks. But those in these different sub-communities often lack natural venues to meet. Our workshop aims to:


* Showcase cutting-edge research across all approaches to mechanistic interpretability

* Foster cross-pollination between different methodological traditions

* Identify convergent insights emerging from diverse research programs

* Build understanding between different perspectives, research communities, and terminologies

* Welcome newcomers by providing clear entry points into the field

We hope to explore points of active debate in the field including:


* How to prioritise between gathering evidence via rigorous qualitative analysis or performance on benchmarks/real-world tasks

* Whether to aim for complete reverse engineering, or achieving high-level understanding via top-down methods, or something else entirely

* How reliable or useful are popular methods such as [sparse](https://www.google.com/url?q=https://transformer-circuits.pub/2023/monosemantic-features/index.html&sa=D&source=editors&ust=1752111165845109&usg=AOvVaw1k9P26xMTbKzufOcRnYRnV)[autoencoders](https://www.google.com/url?q=https://adamkarvonen.github.io/machine_learning/2024/06/11/sae-intuitions.html&sa=D&source=editors&ust=1752111165845254&usg=AOvVaw0svQy_Zg2Ux3AVdpJ_kWZw), and [how much should we prioritize researching them](https://www.google.com/url?q=https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9&sa=D&source=editors&ust=1752111165845474&usg=AOvVaw1K-8XKjvTkX3qoUgkl5isw)?

* Whether to take a perspective of curiosity driven basic science vs working towards specific goals

* Whether we can predict the crucial concepts represented in models well enough to find them via supervised techniques such as probing, versus needing unsupervised techniques with the potential to surprise us, such as [transcoders](https://www.google.com/url?q=https://transformer-circuits.pub/2025/attribution-graphs/biology.html&sa=D&source=editors&ust=1752111165846008&usg=AOvVaw3Z2X0d0RNY0cVomevSdMv2).

In this workshop, we hope to bring together researchers from across these many perspectives and communities—along with skeptics, experts in adjacent fields, and those simply curious to learn more—to facilitate healthy discussion and move towards a greater mutual understanding as a field.


We invite submissions of unpublished, cutting-edge, and in-progress research. Through our call for papers, we hope to facilitate the sharing of work in this fast-moving field, across all of these axes, and especially work that helps to bridge these gaps. We welcome any submissions that seek to further our ability to use the internals of models to achieve understanding, regardless of how unconventional the approach may be.


Please see the [call for papers page](https://www.google.com/url?q=https://mechinterpworkshop.com/cfp/&sa=D&source=editors&ust=1752111165847130&usg=AOvVaw08IaCa_aN-qv4VbTEoyl0l) for further details and particular topics of interest.


[SPEAKERS]


[SCHEDULE]


## Learning More

Here are some resources you may find useful for learning more about the mechanistic interpretability field and performing research:


* We recommend starting with the review paper [Open Problems in Mechanistic Interpretability](https://www.google.com/url?q=https://arxiv.org/abs/2501.16496&sa=D&source=editors&ust=1752111165847670&usg=AOvVaw15eZM_-P7X7750KpjEMnkg) for an overview of the field

* [Ferrando et al](https://www.google.com/url?q=https://arxiv.org/abs/2405.00208&sa=D&source=editors&ust=1752111165847825&usg=AOvVaw25fWLgc3-Z_vL0-HjF-5ss) is a good primer on the key techniques of the field

* The [ARENA coding tutorials](https://www.google.com/url?q=https://arena-chapter1-transformer-interp.streamlit.app/&sa=D&source=editors&ust=1752111165848007&usg=AOvVaw1VjQOQl__nB9HAcSBgLYRS) are a great place to learn how to implement these techniques in practice

* Popular libraries include:

* [TransformerLens](https://www.google.com/url?q=https://github.com/TransformerLensOrg/TransformerLens&sa=D&source=editors&ust=1752111165848284&usg=AOvVaw0gmdzqp3R1vn3EJXIB6MvP): PyTorch, best for <=9B models

* [nnsight](https://www.google.com/url?q=https://github.com/ndif-team/nnsight&sa=D&source=editors&ust=1752111165848455&usg=AOvVaw3awgHWoGedKboyIpUU-9F1): PyTorch, good for any size models

* [Penzai](https://www.google.com/url?q=https://github.com/google-deepmind/penzai&sa=D&source=editors&ust=1752111165848621&usg=AOvVaw2EfCybmU0Y9i4HaL9Tdw1_): Jax

* The [Mechanistic Interpretability Benchmark](https://www.google.com/url?q=https://mib-bench.github.io/&sa=D&source=editors&ust=1752111165848802&usg=AOvVaw21eWPhuRAzdhbDzOaZAXau)

* The [Gemma Scope Sparse Autoencoders](https://www.google.com/url?q=https://arxiv.org/abs/2408.05147&sa=D&source=editors&ust=1752111165848965&usg=AOvVaw28wRSX1MMsBp5c9s-Lix0t) ([interactive tutorial](https://www.google.com/url?q=http://neuronpedia.org/gemma-scope&sa=D&source=editors&ust=1752111165849100&usg=AOvVaw3DSAHNzcrg_PH6A1ltnHrR))



Relevant online communities:


* [Open Source Mechanistic Interpretability Slack](https://www.google.com/url?q=http://neelnanda.io/osmi-slack-invite&sa=D&source=editors&ust=1752111165849385&usg=AOvVaw0okd3nOAwRzcveBykuRelW)

* [Mechanistic Interpretability Discord](https://www.google.com/url?q=https://discord.gg/ysVfhCfCKw&sa=D&source=editors&ust=1752111165849541&usg=AOvVaw0H8GL8Of1Skoq__XPAAguc)

* [Eleuther Discord](https://www.google.com/url?q=https://discord.gg/nHS4YxmfeM&sa=D&source=editors&ust=1752111165849708&usg=AOvVaw0TW7TsM9qzM_xwMr4HIyCu)



[ORGANIZERS]