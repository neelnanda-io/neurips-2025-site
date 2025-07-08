---
title: Mechanistic Interpretability Workshop 2025
---

## Why this workshop?

Larger and more capable models are having an increasing impact on the world, yet our ability to understand them remains highly limited. Our tools for understanding and controlling their behavior are often crude, and tend to rely on studying a model’s inputs and outputs. Further, studying behaviour alone may not be enough: there are growing warnings that models may not always act in the ways we desire, and are capable of actively misleading us about this fact. And many of the deepest scientific mysteries in machine learning may remain out of reach if we cannot look inside the black box.

These trends highlight the urgent need for [**mechanistic interpretability**](https://arxiv.org/abs/2501.16496): the study of principled ways to use the internals of a model—its weights and activations—to gain insight into its behavior, and the underlying computations.

## Workshop Goals

The field of mechanistic interpretability has grown rapidly and now encompasses many different viewpoints and goals, with points of active debate including:

How to prioritise between gathering evidence via rigorous qualitative analysis or performance on benchmarks/real-world tasks

Whether to aim for complete reverse engineering, or achieving high-level understanding via top-down methods, or something else entirely

The relative merits of popular methods such as sparse autoencoders

Whether to take a perspective of curiosity driven basic science vs working towards specific goals

Whether we can predict the crucial concepts represented in models well enough to find them via supervised techniques such as probing, versus needing unsupervised techniques with the potential to surprise us, such as [transcoders](https://transformer-circuits.pub/2025/attribution-graphs/biology.html).

Researchers at different points on these spectrums often struggle to understand the perspectives of others, or communication is hindered by differing terminology. This is exacerbated by the significant communities in academia, industry, and independent research who often lack natural venues to meet, leading to duplicated work and slowed progress.

**But all are unified by the belief that there is meaning and structure to be found inside our models, and that this is worth studying**. And we believe that all have valuable insights to share.

In this workshop, we hope to bring together researchers from across these many perspectives and communities—along with skeptics, experts in adjacent fields, and those simply curious to learn more—to facilitate healthy discussion and move towards a greater mutual understanding as a field.

We invite submissions of unpublished, cutting-edge, and in-progress research. Through our call for papers, we hope to facilitate the sharing of work in this fast-moving field, across all of these axes, and especially work that helps to bridge these gaps. **We welcome any submissions that seek to further our ability to use the internals of models to achieve understanding, regardless of how unconventional the approach may be.**

Please see the [call for papers page](https://mechinterpworkshop.com/cfp/) for further details and particular topics of interest.

## Learning More

Here are some resources you may find useful for learning more about the mechanistic interpretability field and performing research:

We recommend starting with the review paper [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) for an overview of the field

[Ferrando et al](https://arxiv.org/abs/2405.00208) is a good primer on the key techniques of the field

The [ARENA coding tutorials](https://arena-chapter1-transformer-interp.streamlit.app/) are a great place to learn how to implement these techniques in practice

Popular libraries include:

[TransformerLens](https://github.com/TransformerLensOrg/TransformerLens): PyTorch, best for <=9B models

[nnsight](https://github.com/ndif-team/nnsight): PyTorch, good for any size models

[Penzai](https://github.com/google-deepmind/penzai): Jax

The [Mechanistic Interpretability Benchmark](https://mib-bench.github.io/)

The [Gemma Scope Sparse Autoencoders](https://arxiv.org/abs/2408.05147) ([interactive tutorial](http://neuronpedia.org/gemma-scope))

Relevant online communities:

[Open Source Mechanistic Interpretability Slack](http://neelnanda.io/osmi-slack-invite)

[Mechanistic Interpretability Discord](https://discord.gg/ysVfhCfCKw)

[Eleuther Discord](https://discord.gg/nHS4YxmfeM)

