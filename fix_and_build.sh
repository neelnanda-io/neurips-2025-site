#!/bin/bash
# Fix and rebuild the site

echo "=== Fixing content ==="

# First, check if the content is truncated
if tail -1 content/_index.md | grep -q "^\[$"; then
    echo "Content is truncated, fixing..."
    
    # Remove the trailing [
    sed -i.bak 's/\[$//g' content/_index.md
    
    # Add the organizers section
    cat >> content/_index.md << 'EOF'

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
EOF
fi

echo "=== Cleaning up Google URLs ==="
# Fix Google redirect URLs in all content files
find content -name "*.md" -exec sed -i.bak 's|https://www\.google\.com/url?q=\([^&]*\)&[^)]*|\1|g' {} \;

echo "=== Building site ==="
hugo --minify

echo "=== Done! ==="
echo "Check public/index.html to see if the content is complete"