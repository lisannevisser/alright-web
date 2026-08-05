#!/usr/bin/env python3
"""English page bodies."""
from build_site import (screen, lockscreen, sketch_widget, sketch_keep,
                        sketch_year, sketch_colours, scheme_matrix)

# Real entries from the catalogue, shown as themselves.
SENTENCES = [
    "You&#8217;ve handled hard days before. Today is not different.",
    "Your pace is allowed to be your own.",
    "You don&#8217;t have to earn your rest.",
    "You can plan tomorrow tomorrow.",
    "You can care about someone without carrying them.",
    "You don&#8217;t have to carry all of it today.",
]
# One sentence carries the whole styles section, so it has to work in all three
# settings: short words, because Bold sets it in capitals on a poster.
# Candidate accents for the sketch: the app's own slate and ultramarine
# alongside four neutral options. Nothing here is decided.
ACCENTS = ["#3a4a5a", "#1b2fa8", "#7a5c3e", "#2f6b4f", "#8a3d52", "#5c584e"]

THE_SENTENCE = "You don&#8217;t have to carry all of it today."

HOME = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>One affirmation a day.</h1>
      <p class="lede">One quiet notification at the hour you pick. Then nothing
        until tomorrow.</p>
      <button class="status-button" type="button" disabled>Coming to the App Store</button>
    </div>
    <div>
      {lockscreen(SENTENCES[5], "Wednesday, August 5", "7:30", "now",
                  "A locked iPhone at 7:30 in the morning, showing one notification from alright: You don&#8217;t have to carry all of it today.")}
    </div>
  </div>
</section>

<section class="statement">
  <div class="wrap">
    <blockquote>That is the whole app, and that is the point.</blockquote>
    <p class="attribution">Most days you never open it. The sentence arrives, you
      read it on the lock screen, and the phone goes back in your pocket. Open it
      and you get the same sentence full screen, set in the style you chose &mdash;
      but nothing in alright is waiting for you to come in.</p>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="section-head">
      <h2>How it works</h2>
      <p>Three steps, once. After that the app has nothing left to ask of you.</p>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Pick a time</h3>
        <p>Whatever hour actually suits you: with the first coffee, on the way
          to work, or last thing at night. One time, changeable whenever you
          like.</p>
      </div>
      <div class="step">
        <h3>One sentence arrives</h3>
        <p>A single notification, once a day, at that time. Never a second one,
          and never a reminder about the reminder.</p>
      </div>
      <div class="step">
        <h3>Read it, then put the phone down</h3>
        <p>Open the app for the full-screen setting, or don&#8217;t. The sentence
          is the same either way, and nothing counts whether you did.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="section-head">
      <h2>The sentences</h2>
      <p>Six of the 120, unedited. Every one exists in English and German,
        written rather than translated; the app follows your phone.</p>
    </div>
    <div class="sentences">
      <p>{SENTENCES[0]}</p>
      <p>{SENTENCES[1]}</p>
      <p>{SENTENCES[2]}</p>
      <p>{SENTENCES[3]}</p>
      <p>{SENTENCES[4]}</p>
      <p>{SENTENCES[5]}</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="styles-split">
      <div class="section-head">
        <h2>Three ways to set the same sentence</h2>
        <p>One catalogue, three typographic settings &mdash; the sentence of the
          day stays the same.</p>
      </div>
      <div class="style-stage" data-style-stage data-interval="4500">
        <figure class="style-shot">
          {screen("clean", THE_SENTENCE, "Wednesday, August 5")}
          <figcaption>Clean</figcaption>
        </figure>
        <figure class="style-shot">
          {screen("editorial", THE_SENTENCE, "Wednesday, August 5", initial="Y")}
          <figcaption>Editorial</figcaption>
        </figure>
        <figure class="style-shot">
          {screen("bold", THE_SENTENCE, "Wednesday, August 5")}
          <figcaption>Bold</figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="section-head">
      <h2>The whole app in three numbers</h2>
    </div>
    <div class="grid-features">
      <div class="feature">
        <span class="metric">120</span>
        <h3>Sentences, written not generated</h3>
      </div>
      <div class="feature">
        <span class="metric">1</span>
        <h3>Notification a day</h3>
      </div>
      <div class="feature">
        <span class="metric">64</span>
        <h3>Days scheduled ahead</h3>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="section-head">
      <h2>What it doesn&#8217;t do</h2>
      <p>The list matters as much as the one above it.</p>
    </div>
    <ul class="negatives">
      <li>No streaks, and no reminders about reminders</li>
      <li>No feed, no endless scrolling</li>
      <li>No account, no sign-up</li>
      <li>No ads, no promotions for other apps</li>
      <li>No analytics, no tracking</li>
      <li>No network calls at all</li>
    </ul>
  </div>
</section>

<section class="band">
  <div class="wrap band-grid">
    <h2>Nothing is collected, because nothing is taken.</h2>
    <div>
      <p>The sentences ship with the app. Your time, your language and your
        style stay in local storage on your device. Notifications are scheduled
        by iOS, on the device, so no one &mdash; including us &mdash; can see
        whether one was delivered or opened.</p>
      <p>There is no server to hold your data and no account to delete. Removing
        the app removes everything alright ever stored.</p>
      <p><a href="%%PRIVACY%%">Read the privacy policy</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>What&#8217;s next</h2>
      <p>Ideas being weighed after the App Store release. No dates, and nothing
        here will make the app louder.</p>
    </div>
    <div class="cards">
      <div class="card-quiet">
        {sketch_widget("You don&#8217;t have to carry all of it today.",
                       "Sketch: a home screen widget showing the day&#8217;s sentence in the Bold style")}
        <h3>A home screen widget</h3>
        <p>The sentence of the day without opening anything. The Bold style is
          the one that would carry across a home screen.</p>
      </div>
      <div class="card-quiet">
        {sketch_keep(SENTENCES[1:4],
                     "Sketch: a short list of kept sentences, the newest one marked")}
        <h3>Keeping a sentence</h3>
        <p>A way to hold on to the ones that landed, without turning the app
          into a collection to maintain.</p>
      </div>
      <div class="card-quiet">
        {sketch_year(120, 365,
                     "Sketch: 365 squares, one per day of the year, 120 of them filled",
                     "120 of 365 days written")}
        <h3>A sentence for every day of the year</h3>
        <p>The catalogue currently covers 120 days. Writing it out to 365 is
          editorial work, not engineering.</p>
      </div>
    </div>
    <p class="note">These are candidates, not commitments, and the images are
      sketches rather than screenshots &mdash; none of it is built. What ships
      first is version one, exactly as described above.</p>
    <a class="link-more" href="%%NEXT%%">All of what&#8217;s next &rarr;</a>
  </div>
</section>"""


ABOUT = f"""<section class="page-head">
  <div class="wrap wrap-narrow">
    <p class="eyebrow">About</p>
    <h1>An app for you, made by one person</h1>
    <p class="lede">I design alright, build it and write the affirmations. Here
      is where it comes from, and why it turned out this quiet.</p>
  </div>
</section>

<div class="wrap wrap-narrow">
<div class="prose">
  <section>
    <div class="about-intro">
      <!-- A portrait goes here whenever you have one. Drop the file into
           assets/ and uncomment:
      <figure class="about-portrait">
        <img src="%%ROOT%%assets/lisanne.jpg" alt="Lisanne Visser" width="640" height="800">
      </figure>
      -->
      <div>
        <p>Hi, I&#8217;m Lisanne, a designer who started building. I have worked
          in design for several years, and the whole time I&#8217;ve been
          searching for products that genuinely win you over through their
          interface: things that are careful about how they look and how they
          behave, not only about what they can do or how to make the most
          money.</p>
        <p>In my free time, I also teach yoga, and mindfulness is a category I
          know from the inside. Most apps &mdash; not just in this category
          &mdash; ask for far more attention than the practice they are supposed
          to support. I wanted a properly made one: a single affirmation a day,
          set in typography worth looking at, that never turns a quiet habit
          into an obligation. At some point waiting for one stopped making
          sense, so I built it.</p>
        <p>More of my work:
          <a href="https://lisannevisser.github.io/portfolio/#/">lisannevisser.github.io/portfolio</a></p>
      </div>
    </div>
  </section>

  <section>
    <h2>Why it is built like this</h2>
    <p>I want to give you the reasoning behind the app. Most apps today behave
      differently from this one. They show lots of ads or aggressively prompt you
      to upgrade. Although I work for products that do the same, with my own app
      I wanted to do something else. I wanted to build an ethical product that
      gives back to society. alright is built to serve people, not my wallet.
      Let me show you more about why and how I did it.</p>
  </section>

  <section>
    <h3>One sentence, fixed in advance</h3>
    <p>The sentence for a given day is worked out from the date itself. It is the
      same sentence for everyone, it is settled before the day starts, and
      opening the app twice will never produce a different one. That rules out
      the reflex the category runs on: pull down, get another, keep going until
      one feels right.</p>
    <p>The order is shuffled once from a fixed seed, so the 120 sentences run
      through 120 days without repeating &mdash; roughly four months before a
      sentence comes back.</p>
    <div class="aside">
      <p>The engine is a pure function of the date: no randomness at runtime, no
        stored state, nothing to sync. Which is also why it can be tested
        without a phone attached.</p>
    </div>
  </section>

  <section>
    <h3>The notification is the product</h3>
    <p>Most of the app is one notification a day, so the scheduling gets the care
      that a feature list would otherwise get. iOS allows an app 64 pending
      notifications; alright schedules the full 64 days ahead, which means your
      sentence keeps arriving even if you don&#8217;t open the app for two
      months.</p>
    <p>When that buffer is close to running out, the last notification says so
      plainly instead of the app simply going silent. An app that quietly stops
      working is worse than one that admits it needs opening.</p>
  </section>

  <section>
    <h3>Three styles, one sentence</h3>
    <p>The same text, set three ways. They exist because the sentence is the
      whole screen: with nothing else to look at, typography is the entire
      interface.</p>
    <h4>Clean</h4>
    <p>San Francisco on paper white, centred, near-black ink. The default,
      designed to disappear.</p>
    <h4>Editorial</h4>
    <p>New York &mdash; Apple&#8217;s own serif, with real optical sizes &mdash;
      on ivory, with a raised initial in ultramarine. The first two lines set
      around the initial, then the paragraph returns to its full measure. The
      first version of this style was rejected for being &ldquo;Clean with a
      serif&rdquo;: same centred composition, same symmetry, only a different
      typeface. A style needs an idea, not a font swap.</p>
    <h4>Bold</h4>
    <p>Archivo Black in capitals on a slab: a four-pixel border, a ten-pixel
      offset shadow, acid yellow ground. Its dark version is drawn rather than
      inverted, because a black border and a black shadow on a black ground
      erase the two things that make the style what it is. So acid becomes the
      slab and the shadow turns white.</p>
  </section>

  <section>
    <h3>Light and dark, drawn twice</h3>
    <p>Six screens, not three. Every style has a dark version of its own rather
      than an inverted copy, and the differences are decisions rather than
      arithmetic: ivory becomes warm near-black and the ultramarine lifts so it
      glows instead of vibrating; the acid slab swaps places with the ground and
      the hard shadow turns white.</p>
    {scheme_matrix(THE_SENTENCE, "Y", "Wednesday, August 5",
                   "Light", "Dark",
                   "Clean, Editorial and Bold, in both appearances. This site follows "
                   "whichever one your system is set to; the app can also be pinned to "
                   "one of them instead.")}
  </section>

  <section>
    <h3>Type that answers to the reader</h3>
    <p>Every style supports Dynamic Type, including the accessibility sizes. The
      sentence is scaled so it still fits on a single screen at the largest
      setting on the smallest supported phone &mdash; the app never asks anyone
      to scroll a sentence.</p>
    <p>Reduced Motion is respected throughout. The gear that opens settings is
      the only control on the daily screen and the only door to the other two
      styles, so its contrast is held above the 3:1 that WCAG asks of a control
      &mdash; in every style, in both light and dark, checked by tests rather
      than by eye.</p>
  </section>

  <section>
    <h3>Nothing to configure, nothing to connect</h3>
    <p>No account, no analytics, no advertising, no third-party frameworks, and
      no network calls of any kind. The catalogue ships inside the app; the
      settings live in local storage. This is not a privacy feature bolted on
      afterwards &mdash; it is what happens when an app has nothing it needs
      from a server.</p>
  </section>

  <section>
    <h3>The name</h3>
    <p>alright is written lowercase everywhere, including at the start of a
      sentence: the home screen name is lowercase, the icon is a lowercase
      &ldquo;a&rdquo;, and the app writes itself that way in its own text. The
      stylised al/right wordmark is a graphic form of the same letters. It
      belongs on marks and covers, never in running text.</p>
  </section>
</div>
</div>"""


NEXT = f"""<section class="page-head">
  <div class="wrap wrap-narrow">
    <p class="eyebrow">What&#8217;s next</p>
    <h1>What&#8217;s next</h1>
    <p class="lede">An honest list: what comes first, what is being weighed, and
      what will never be built. Nothing here has a date.</p>
  </div>
</section>

<div class="wrap wrap-narrow">
<div class="prose">
  <section>
    <h2>First: the App Store</h2>
    <p>Version one is finished and in testing. It does what the homepage says it
      does, and nothing on this page is needed for it to be worth using. If
      nothing below ever shipped, alright would still be complete.</p>
  </section>

  <section>
    <h2>Being weighed</h2>
    <p>Candidates, in no particular order. Each has to pass the same test: does
      it make the app quieter or louder? The pictures are sketches of the idea,
      not screenshots: none of this is built.</p>
    <h3>A home screen widget</h3>
    {sketch_widget("You don&#8217;t have to carry all of it today.",
                   "Sketch: a home screen widget showing the day&#8217;s sentence in the Bold style")}
    <p>The sentence of the day without opening anything &mdash; arguably the
      most natural home for it. The Bold style is the one that reads across a
      home screen from arm&#8217;s length.</p>
    <h3>Keeping a sentence</h3>
    {sketch_keep(SENTENCES[1:4],
                 "Sketch: a short list of kept sentences, the newest one marked")}
    <p>Some sentences land harder than others, and today there is no way to hold
      on to one. The open question is how to allow that without turning the app
      into a collection that wants tending.</p>
    <h3>A sentence for every day of the year</h3>
    {sketch_year(120, 365,
                 "Sketch: 365 squares, one per day of the year, 120 of them filled",
                 "120 of 365 days written")}
    <p>120 sentences means a sentence returns after about four months. Writing
      the catalogue out to 365 is editorial work rather than engineering, and it
      is the change that would most improve the product.</p>
    <h3>Choosing the accent colour</h3>
    {sketch_colours("Sketch: a row of accent colours with one of them picked",
                    ACCENTS)}
    <p>The styles set the temperature; a colour would make it yours. Every
      colour needs a checked light and dark version, otherwise the sentence
      becomes unreadable in exactly one of them.</p>
    <h3>Switching language inside the app</h3>
    <p>Today alright follows the language of the phone. People who read in two
      languages don&#8217;t always want their affirmations in the one their
      phone is set to.</p>
  </section>

  <section>
    <h2>Deliberately not planned</h2>
    <p>None of these are oversights, and none of them are waiting for a spare
      afternoon. Each one was considered and turned down, and here is the
      reasoning in each case.</p>

    <h3>Accounts and sign-ups</h3>
    <p>There is nothing to log in to. The sentence for a day is worked out from
      the date, which every phone can do on its own, and your settings are three
      values in local storage. An account would create data where none exists
      today &mdash; an address, a password, a server to keep them on &mdash; and
      not one of those things would make the app better at its single job.</p>

    <h3>Streaks, scores, anything that can be broken</h3>
    <p>A streak turns a day you missed into a failure, and the people this app is
      written for do not need one more thing they have let down. There is a
      second reason, and it is the harder one: counting means watching. alright
      never learns whether a notification was delivered or opened, so it could
      not keep score without starting to observe you first. No number is worth
      that trade.</p>

    <h3>A feed, a community, sentences from other people</h3>
    <p>The sentence is the same for everyone on a given day and settled before the
      day starts. A feed would bring back precisely the reflex the day engine
      exists to remove: pull down, get another, keep going until one feels right.
      And sentences written by strangers, in a place people open on bad days,
      would need moderating &mdash; every day, indefinitely. That is a duty a
      one-person project should not promise, and an unmoderated version of it is
      worse than none.</p>

    <h3>Advertising, cross-promotion, notifications that sell something</h3>
    <p>alright asks for one moment of attention a day, and that moment is the
      entire product. Spending it on a second notification with something to sell
      would trade the only thing the app has for whatever such a placement pays.
      The rule stays simple enough to check: one notification a day, and it
      contains a sentence.</p>

    <h3>Analytics and tracking of any kind</h3>
    <p>The app makes no network calls at all, which is why its privacy policy can
      be short, and why the privacy labels on the App Store page will say that
      no data is collected. The cost is
      real and accepted: nobody here knows how many people read their sentence,
      how long they keep the app, or which sentences land hardest. That feedback
      would genuinely help. It is not worth it in an app whose one promise is that
      nothing leaves your phone &mdash; so the feedback comes by email instead,
      from people who choose to write.</p>

    <p>These aren&#8217;t missing features. They are the reason the app is worth
      building at all.</p>
  </section>

  <section>
    <h2>Something you&#8217;re missing?</h2>
    <p>Write to <a href="mailto:alrightapp@icloud.com">alrightapp@icloud.com</a>.
      Every message is read by the person who builds the app, and this list is
      the kind of thing that changes because of them.</p>
  </section>
</div>
</div>"""
