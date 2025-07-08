---
title: "Mechanistic Interpretability Workshop 2025"
---

## Why this workshop?

Larger and more capable models are having an increasing impact on the world, yet our ability to understand their internal mechanisms remains a fundamental scientific challenge. While we can observe what models do, we have limited insight into how they do it—their internal representations, learned algorithms, and how this all connects to their outward behavior remain largely opaque. This gap between performance and understanding limits our ability to predict model behavior, ensure reliability, and detect sophisticated adversarial or deceptive behavior. And many of the deepest scientific mysteries in machine learning may remain out of reach if we cannot look inside the black box.

Mechanistic interpretability addresses this challenge by developing principled methods to analyze and understand a model's internals–weights and activations–and to use this understanding to gain greater insight into its behavior, and the computation underlying it. The field has grown rapidly, with sizable communities in academia, industry and independent research, 140+ papers submitted to our ICML 2024 workshop, dedicated startups, and producing a rich ecosystem of tools and techniques. This workshop brings together diverse perspectives from this vibrant community to share recent advances and chart future directions.

<div class="embedded-signup">
  <h2>Stay Updated</h2>
  <div class="mailing-list-form">
    <form action="https://buttondown.com/api/emails/embed-subscribe/mechinterpworkshop"
          method="post" target="popupwindow"
          onsubmit="window.open('https://buttondown.com/mechinterpworkshop', 'popupwindow')"
          class="embeddable-buttondown-form">
      <input type="email" name="email" placeholder="Email" required />
      <input type="submit" value="Subscribe for updates" />
    </form>
  </div>
</div>

<div class="image-pair">
<img src="/img/conference-pic.jpg" alt="Workshop photo 1">
<img src="/img/rooftop-pic.jpg" alt="Workshop photo 2">
</div>
<p class="image-caption">The first Mechanistic Interpretability Workshop (ICML 2024)</p>

## Workshop Goals

The mechanistic interpretability field benefits from a rich diversity of approaches—from rigorous mathematical analysis to large-scale empirical studies, from reverse-engineering a model via bottom-up circuit analysis, to assisting behavioral analysis via top-down analysis of model representations. But all are unified by the belief that there is meaning and structure to be found inside our models, and that this is worth studying.

This diversity reflects the field's breadth and the many valid paths toward understanding neural networks. But those in these different sub-communities often lack natural venues to meet. Our workshop aims to:

* Showcase cutting-edge research across all approaches to mechanistic interpretability
* Foster cross-pollination between different methodological traditions
* Identify convergent insights emerging from diverse research programs
* Build understanding between different perspectives, research communities, and terminologies
* Welcome newcomers by providing clear entry points into the field

We hope to explore points of active debate in the field including:

* How to prioritise between gathering evidence via rigorous qualitative analysis or performance on benchmarks/real-world tasks
* Whether to aim for complete reverse engineering, or achieving high-level understanding via top-down methods, or something else entirely
* [How reliable or useful are popular methods such as sparse autoencoders](https://adamkarvonen.github.io/machine_learning/2024/06/11/sae-intuitions.html), and [how much should we prioritize researching them](https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9)?
* Whether to take a perspective of curiosity driven basic science vs working towards specific goals
* Whether we can predict the crucial concepts represented in models well enough to find them via supervised techniques such as probing, versus needing unsupervised techniques with the potential to surprise us, such as [transcoders](https://transformer-circuits.pub/2025/attribution-graphs/biology.html).

In this workshop, we hope to bring together researchers from across these many perspectives and communities—along with skeptics, experts in adjacent fields, and those simply curious to learn more—to facilitate healthy discussion and move towards a greater mutual understanding as a field.

We invite submissions of unpublished, cutting-edge, and in-progress research. Through our call for papers, we hope to facilitate the sharing of work in this fast-moving field, across all of these axes, and especially work that helps to bridge these gaps. We welcome any submissions that seek to further our ability to use the internals of models to achieve understanding, regardless of how unconventional the approach may be.

Please see the [call for papers page](https://mechinterpworkshop.com/cfp/) for further details and particular topics of interest.

<section class="embedded-speakers">
<h2>Keynote Speakers</h2>
<div class="speakers">
  <div class="speaker">
    <img src="/img/chrisolah.jpeg" alt="Chris Olah" />
    <div>
      <h3><a href="https://colah.github.io/about.html">Chris Olah</a></h3>
      <p>Interpretability Lead and Co-founder, Anthropic</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/beenkim.jpeg" alt="Been Kim" />
    <div>
      <h3><a href="https://beenkim.github.io/">Been Kim</a></h3>
      <p>Senior Staff Research Scientist, Google DeepMind</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/sarahschwettmann.jpeg" alt="Sarah Schwettmann" />
    <div>
      <h3><a href="https://cogconfluence.com/">Sarah Schwettmann</a></h3>
      <p>Co-founder of Transluce</p>
    </div>
  </div>
</div>
</section>

<section class="embedded-schedule">
<h2>Schedule (Provisional)</h2>
<table>
<thead>
<tr>
<th>Time</th>
<th>Activity</th>
</tr>
</thead>
<tbody>
<tr><td>09:00 - 09:30</td><td>Welcome and survey talk</td></tr>
<tr><td>09:30 - 10:00</td><td>Talk: <b>Been Kim</b></td></tr>
<tr><td>10:00 - 11:00</td><td>Contributed talks 1</td></tr>
<tr><td>11:00 - 12:00</td><td>Poster session 1, coffee</td></tr>
<tr><td>12:00 - 13:00</td><td>Lunch with organised discussions</td></tr>
<tr><td>13:00 - 13:30</td><td>Talk: <b>Sarah Schwettmann</b></td></tr>
<tr><td>13:30 - 14:30</td><td>Contributed talks 2</td></tr>
<tr><td>14:30 - 15:30</td><td>Poster session 2, coffee</td></tr>
<tr><td>15:30 - 16:00</td><td>Talk: <b>Chris Olah</b></td></tr>
<tr><td>16:00 - 16:30</td><td>Coffee & Networking break</td></tr>
<tr><td>16:30 - 17:20</td><td>Panel discussion</td></tr>
<tr><td>17:20 - 17:30</td><td>Awards & closing</td></tr>
<tr><td>19:00 - 22:00</td><td>Evening social (invite-only)</td></tr>
</tbody>
</table>
</section>

## Learning More

Here are some resources you may find useful for learning more about the mechanistic interpretability field and performing research:

* We recommend starting with the review paper [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) for an overview of the field
* [Ferrando et al](https://arxiv.org/abs/2405.00208) is a good primer on the key techniques of the field
* [The ARENA coding tutorials](https://arena-chapter1-transformer-interp.streamlit.app/) are a great place to learn how to implement these techniques in practice
* Popular libraries include:
  * [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens): PyTorch, best for <=9B models
  * [nnsight](https://github.com/ndif-team/nnsight): PyTorch, good for any size models
  * [Penzai](https://github.com/google-deepmind/penzai): Jax
* [The Mechanistic Interpretability Benchmark](https://mib-bench.github.io/)
* [The Gemma Scope Sparse Autoencoders](https://arxiv.org/abs/2408.05147) ([interactive tutorial](http://neuronpedia.org/gemma-scope))

Relevant online communities:
* [Open Source Mechanistic Interpretability Slack](http://neelnanda.io/osmi-slack-invite)
* [Mechanistic Interpretability Discord](https://discord.gg/ysVfhCfCKw)
* [Eleuther Discord](https://discord.gg/nHS4YxmfeM)

<section class="embedded-organizers">
<h2>Organizing Committee</h2>
<div class="organizers speakers">
  <div class="speaker">
    <img src="/img/neelnanda.jpeg" alt="Neel Nanda" />
    <div>
      <h3><a href="https://www.neelnanda.io/about">Neel Nanda</a></h3>
      <p>Senior Research Scientist, Google DeepMind</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/martinwattenberg.png" alt="Martin Wattenberg" />
    <div>
      <h3><a href="https://www.bewitched.com">Martin Wattenberg</a></h3>
      <p>Professor, Harvard University & Principal Research Scientist, Google DeepMind</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/sarahwiegreffe.jpeg" alt="Sarah Wiegreffe" />
    <div>
      <h3><a href="https://sarahwie.github.io/">Sarah Wiegreffe</a></h3>
      <p>Postdoc, Allen Institute for AI, incoming Assistant Professor, University of Maryland</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/atticusgeiger.jpeg" alt="Atticus Geiger" />
    <div>
      <h3><a href="https://atticusg.github.io/">Atticus Geiger</a></h3>
      <p>Lead, Pr(Ai)²R Group</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/juliusadebayo.jpeg" alt="Julius Adebayo" />
    <div>
      <h3><a href="https://juliusadebayo.com">Julius Adebayo</a></h3>
      <p>Founder and Researcher, Guide Labs</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/kayoyin.jpeg" alt="Kayo Yin" />
    <div>
      <h3><a href="https://kayoyin.github.io/">Kayo Yin</a></h3>
      <p>3rd year PhD student, UC Berkeley</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/fazlbarez.jpeg" alt="Fazl Barez" />
    <div>
      <h3><a href="https://fbarez.github.io/">Fazl Barez</a></h3>
      <p>Senior Research Fellow, Oxford Martin AI Governance Initiative</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/lawrencechan.jpeg" alt="Lawrence Chan" />
    <div>
      <h3><a href="https://chanlawrence.me/">Lawrence Chan</a></h3>
      <p>Researcher, METR</p>
    </div>
  </div>
  <div class="speaker">
    <img src="/img/matthewwearden.jpeg" alt="Matthew Wearden" />
    <div>
      <h3>Matthew Wearden</h3>
      <p>London Director, MATS</p>
    </div>
  </div>
</div>
</section>