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

* How reliable or useful are popular methods such as [sparse](https://www.google.com/url?q=https://transformer-circuits.pub/2023/monosemantic-features/index.html&sa=D&source=editors&ust=1752106873806513&usg=AOvVaw1pCgP78KaucbTxSdb5-weS)[autoencoders](https://www.google.com/url?q=https://adamkarvonen.github.io/machine_learning/2024/06/11/sae-intuitions.html&sa=D&source=editors&ust=1752106873806777&usg=AOvVaw2DHeDPwZTt1KvMb-0C8JEw), and [how much should we prioritize researching them](https://www.google.com/url?q=https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9&sa=D&source=editors&ust=1752106873807104&usg=AOvVaw3DPTuW9BhthaDH5gU4ftZh)?

* Whether to take a perspective of curiosity driven basic science vs working towards specific goals

* Whether we can predict the crucial concepts represented in models well enough to find them via supervised techniques such as probing, versus needing unsupervised techniques with the potential to surprise us, such as [transcoders](https://www.google.com/url?q=https://transformer-circuits.pub/2025/attribution-graphs/biology.html&sa=D&source=editors&ust=1752106873807997&usg=AOvVaw1Fke3tVCb3DRzfOPej3ZwV).

In this workshop, we hope to bring together researchers from across these many perspectives and communities—along with skeptics, experts in adjacent fields, and those simply curious to learn more—to facilitate healthy discussion and move towards a greater mutual understanding as a field.


We invite submissions of unpublished, cutting-edge, and in-progress research. Through our call for papers, we hope to facilitate the sharing of work in this fast-moving field, across all of these axes, and especially work that helps to bridge these gaps. We welcome any submissions that seek to further our ability to use the internals of models to achieve understanding, regardless of how unconventional the approach may be.


Please see the [call for papers page](https://www.google.com/url?q=https://mechinterpworkshop.com/cfp/&sa=D&source=editors&ust=1752106873809405&usg=AOvVaw16fMnFpUzYGx1r4a5P6U8i) for further details and particular topics of interest.


[SPEAKERS]


[SCHEDULE]


## Learning More

Here are some resources you may find useful for learning more about the mechanistic interpretability field and performing research:


* We recommend starting with the review paper [Open Problems in Mechanistic Interpretability](https://www.google.com/url?q=https://arxiv.org/abs/2501.16496&sa=D&source=editors&ust=1752106873810257&usg=AOvVaw1QYcu2wBretaQqueQrZdJg) for an overview of the field

* [Ferrando et al](https://www.google.com/url?q=https://arxiv.org/abs/2405.00208&sa=D&source=editors&ust=1752106873810609&usg=AOvVaw0bKROF_OC0nDmkCbz9iOEb) is a good primer on the key techniques of the field

* The [ARENA coding tutorials](https://www.google.com/url?q=https://arena-chapter1-transformer-interp.streamlit.app/&sa=D&source=editors&ust=1752106873810948&usg=AOvVaw3TTOhNOmZw7hTQC3sgBcY0) are a great place to learn how to implement these techniques in practice

* Popular libraries include:

* [TransformerLens](https://www.google.com/url?q=https://github.com/TransformerLensOrg/TransformerLens&sa=D&source=editors&ust=1752106873811351&usg=AOvVaw2GdDAA13_Ggbplky6Gkgt1): PyTorch, best for <=9B models

* [nnsight](https://www.google.com/url?q=https://github.com/ndif-team/nnsight&sa=D&source=editors&ust=1752106873811643&usg=AOvVaw31d_I4Zr0JDnpNxaasdk-H): PyTorch, good for any size models

* [Penzai](https://www.google.com/url?q=https://github.com/google-deepmind/penzai&sa=D&source=editors&ust=1752106873811840&usg=AOvVaw1njCrV_t-zO2iEX5Yhu6O1): Jax

* The [Mechanistic Interpretability Benchmark](https://www.google.com/url?q=https://mib-bench.github.io/&sa=D&source=editors&ust=1752106873812038&usg=AOvVaw35kB3VMRReUdY6SRGDC_mX)

* The [Gemma Scope Sparse Autoencoders](https://www.google.com/url?q=https://arxiv.org/abs/2408.05147&sa=D&source=editors&ust=1752106873812253&usg=AOvVaw0LNdqG82l0K8gN2lOgK6PB) ([interactive tutorial](https://www.google.com/url?q=http://neuronpedia.org/gemma-scope&sa=D&source=editors&ust=1752106873812401&usg=AOvVaw178vDNwbD3Br3W12C7Bpsg))



Relevant online communities:


* [Open Source Mechanistic Interpretability Slack](https://www.google.com/url?q=http://neelnanda.io/osmi-slack-invite&sa=D&source=editors&ust=1752106873812712&usg=AOvVaw0H2Ct54ZfnqNCd4nxiaz9b)

* [Mechanistic Interpretability Discord](https://www.google.com/url?q=https://discord.gg/ysVfhCfCKw&sa=D&source=editors&ust=1752106873812965&usg=AOvVaw1JkIfBqgi7ZkRzEEA-FuEa)

* [Eleuther Discord](https://www.google.com/url?q=https://discord.gg/nHS4YxmfeM&sa=D&source=editors&ust=1752106873813102&usg=AOvVaw3rWggf0vuYOoH4vx3NPV6M)



[ORGANIZERS]