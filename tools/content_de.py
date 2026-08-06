#!/usr/bin/env python3
"""Deutsche Seiteninhalte."""
from build_site import (screen, lockscreen, sketch_widget, sketch_keep,
                        sketch_year, sketch_colours, scheme_matrix)

# Echte Einträge aus dem Katalog, gezeigt als das, was sie sind.
SENTENCES = [
    "Du hast schwere Tage schon gemeistert. Heute ist keine Ausnahme.",
    "Dein Tempo darf dein eigenes sein.",
    "Du musst dir Ruhe nicht erst verdienen.",
    "Du kannst morgen auch morgen planen.",
    "Du kannst für Menschen da sein, ohne sie zu tragen.",
    "Du musst heute nicht alles machen.",
]
# Ein Satz trägt die ganze Stile-Sektion, also muss er in allen dreien
# funktionieren: kurze Wörter, weil Bold ihn als Plakat in Versalien setzt.
# Kandidaten fürs Skizzenbild: Slate und Ultramarin aus der App, dazu vier
# neutrale Optionen. Entschieden ist davon nichts.
ACCENTS = ["#3a4a5a", "#1b2fa8", "#7a5c3e", "#2f6b4f", "#8a3d52", "#5c584e"]

THE_SENTENCE = "Du musst heute nicht alles machen."

HOME = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Ein Satz am Tag.</h1>
      <p class="lede">Eine leise Mitteilung zur Uhrzeit, die du wählst. Danach
        nichts bis morgen.</p>
      <button class="status-button" type="button" disabled>Bald im App Store</button>
    </div>
    <div>
      {lockscreen(SENTENCES[5], "Mittwoch, 5. August", "7:30", "jetzt",
                  "Ein gesperrtes iPhone um 7:30 Uhr morgens, mit einer einzelnen Mitteilung von alright: Du musst heute nicht alles machen.")}
    </div>
  </div>
</section>

<section class="statement">
  <div class="wrap">
    <blockquote>Das ist die ganze App, und genau das ist die Idee.</blockquote>
    <p class="attribution">An den meisten Tagen öffnest du sie gar nicht. Der
      Satz kommt an, du liest ihn auf dem Sperrbildschirm, das Handy wandert
      zurück in die Tasche. Öffnest du sie, steht derselbe Satz bildschirmfüllend
      da, in dem Stil, den du gewählt hast &mdash; aber nichts in alright wartet
      darauf, dass du vorbeikommst.</p>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="section-head">
      <h2>So funktioniert es</h2>
      <p>Drei Schritte, einmal. Danach will die App nichts mehr von dir.</p>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Uhrzeit wählen</h3>
        <p>Die Zeit, die wirklich zu dir passt: zum ersten Kaffee, auf dem Weg
          zur Arbeit oder als Letztes am Abend. Eine Uhrzeit, jederzeit
          änderbar.</p>
      </div>
      <div class="step">
        <h3>Ein Satz kommt an</h3>
        <p>Eine einzelne Mitteilung, einmal am Tag, zu dieser Zeit. Nie eine
          zweite, und nie eine Erinnerung an die Erinnerung.</p>
      </div>
      <div class="step">
        <h3>Lesen, Handy weglegen</h3>
        <p>Du kannst die App für die volle Setzung öffnen oder es lassen. Der
          Satz bleibt derselbe, und niemand zählt mit, ob du es getan hast.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="section-head">
      <h2>Die Sätze</h2>
      <p>Sechs von 120, unbearbeitet. Jeden gibt es auf Deutsch und Englisch,
        geschrieben statt übersetzt; die App folgt der Sprache deines Geräts.</p>
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
        <h2>Drei Setzungen für denselben Satz</h2>
        <p>Ein Katalog, drei typografische Fassungen &mdash; der Satz des Tages
          bleibt derselbe.</p>
      </div>
      <div class="style-stage" data-style-stage data-interval="4500">
        <figure class="style-shot">
          {screen("clean", THE_SENTENCE, "Mittwoch, 5. August")}
          <figcaption>Clean</figcaption>
        </figure>
        <figure class="style-shot">
          {screen("editorial", THE_SENTENCE, "Mittwoch, 5. August", initial="D")}
          <figcaption>Editorial</figcaption>
        </figure>
        <figure class="style-shot">
          {screen("bold", THE_SENTENCE, "Mittwoch, 5. August")}
          <figcaption>Bold</figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="section-head">
      <h2>Die ganze App in drei Zahlen</h2>
    </div>
    <div class="grid-features">
      <div class="feature">
        <span class="metric">120</span>
        <h3>Sätze, geschrieben statt generiert</h3>
      </div>
      <div class="feature">
        <span class="metric">1</span>
        <h3>Mitteilung am Tag</h3>
      </div>
      <div class="feature">
        <span class="metric">64</span>
        <h3>Tage im Voraus geplant</h3>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap rule-top">
    <div class="section-head">
      <h2>Was sie nicht tut</h2>
      <p>Diese Liste zählt genauso viel wie die darüber.</p>
    </div>
    <ul class="negatives">
      <li>Keine Streaks, keine Erinnerung an die Erinnerung</li>
      <li>Kein Feed, kein endloses Scrollen</li>
      <li>Kein Account, keine Anmeldung</li>
      <li>Keine Werbung, keine Hinweise auf andere Apps</li>
      <li>Keine Analyse, kein Tracking</li>
      <li>Überhaupt keine Netzwerkaufrufe</li>
    </ul>
  </div>
</section>

<section class="band">
  <div class="wrap band-grid">
    <h2>Es wird nichts gesammelt, weil nichts genommen wird.</h2>
    <div>
      <p>Die Sätze stecken in der App. Deine Uhrzeit, deine Sprache und dein
        Stil bleiben im lokalen Speicher deines Geräts. Mitteilungen plant iOS
        selbst, auf dem Gerät &mdash; niemand kann sehen, ob eine zugestellt
        oder geöffnet wurde, wir eingeschlossen.</p>
      <p>Es gibt keinen Server, der deine Daten hält, und kein Konto zum
        Löschen. Die App zu entfernen entfernt alles, was alright je
        gespeichert hat.</p>
      <p><a href="%%PRIVACY%%">Zur Datenschutzerklärung</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Was als Nächstes kommt</h2>
      <p>Ideen, die nach dem Release im App Store abgewogen werden. Ohne Termin,
        und nichts davon macht die App lauter.</p>
    </div>
    <div class="cards">
      <div class="card-quiet">
        {sketch_widget("Du musst heute nicht alles machen.",
                       "Skizze: ein Homescreen-Widget mit dem Satz des Tages im Bold-Stil")}
        <h3>Ein Widget für den Homescreen</h3>
        <p>Der Satz des Tages, ohne etwas zu öffnen. Bold ist der Stil, der auf
          einem Homescreen von Weitem trägt.</p>
      </div>
      <div class="card-quiet">
        {sketch_keep(SENTENCES[1:4],
                     "Skizze: eine kurze Liste behaltener Sätze, der neueste markiert")}
        <h3>Einen Satz behalten</h3>
        <p>Ein Weg, die Sätze zu behalten, die getroffen haben, ohne die App in
          eine Sammlung zu verwandeln, die gepflegt werden will.</p>
      </div>
      <div class="card-quiet">
        {sketch_year(120, 365,
                     "Skizze: 365 Quadrate, eines pro Tag im Jahr, 120 davon gefüllt",
                     "120 von 365 Tagen geschrieben")}
        <h3>Ein Satz für jeden Tag im Jahr</h3>
        <p>Der Katalog deckt heute 120 Tage ab. Ihn auf 365 zu schreiben ist
          redaktionelle Arbeit, keine technische.</p>
      </div>
    </div>
    <p class="note">Das sind Kandidaten, keine Zusagen, und die Bilder sind
      Skizzen statt Screenshots &mdash; gebaut ist davon nichts. Zuerst
      erscheint Version eins, genau so, wie sie oben beschrieben ist.</p>
    <a class="link-more" href="%%NEXT%%">Alles, was kommt &rarr;</a>
  </div>
</section>"""


ABOUT = f"""<section class="page-head">
  <div class="wrap wrap-narrow">
    <p class="eyebrow">Über</p>
    <h1>Eine App für dich, gemacht von einer Person</h1>
    <p class="lede">Ich gestalte alright, baue es und schreibe die Affirmationen.
      Hier steht, wo das herkommt &mdash; und warum es so leise geworden ist.</p>
  </div>
</section>

<div class="wrap wrap-narrow">
<div class="prose">
  <section>
    <div class="about-intro">
      <!-- Hier kommt ein Porträt hin, sobald du eines hast. Datei nach assets/
           legen und auskommentieren:
      <figure class="about-portrait">
        <img src="%%ROOT%%assets/lisanne.jpg" alt="Lisanne Visser" width="640" height="800">
      </figure>
      -->
      <div>
        <p>Hi, ich bin Lisanne, Designerin, die angefangen hat zu bauen. Ich
          arbeite seit mehreren Jahren im Design und habe die ganze Zeit über
          nach Produkten gesucht, die wirklich durch ihre Oberfläche überzeugen:
          die sorgfältig damit umgehen, wie sie aussehen und wie sie sich
          verhalten, und nicht nur damit, was sie können oder womit sich am
          meisten Geld verdienen lässt.</p>
        <p>In meiner freien Zeit unterrichte ich außerdem Yoga, und Mindfulness
          ist eine Kategorie, die ich von innen kenne. Die meisten Apps &mdash;
          nicht nur in dieser Kategorie &mdash; verlangen deutlich mehr
          Aufmerksamkeit als die Praxis, die sie eigentlich stützen sollen. Ich
          wollte eine richtig gemachte: eine einzige Affirmation am Tag, in einer
          Typografie, die man gern ansieht, und die aus einer ruhigen Gewohnheit
          nie eine Pflicht macht. Irgendwann hatte Warten keinen Sinn mehr, also
          habe ich sie gebaut.</p>
        <p>Mehr von meiner Arbeit:
          <a href="https://lisannevisser.github.io/portfolio/#/">lisannevisser.github.io/portfolio</a></p>
      </div>
    </div>
  </section>

  <section>
    <h2>Warum sie so gebaut ist</h2>
    <p>Ich möchte dir die Überlegungen hinter der App zeigen. Die meisten Apps
      verhalten sich heute anders als diese. Sie zeigen viel Werbung oder drängen
      aggressiv auf ein Upgrade. Ich arbeite selbst für Produkte, die genau das
      tun &mdash; mit meiner eigenen App wollte ich es anders machen. Ich wollte
      ein ethisches Produkt bauen, das der Gesellschaft etwas zurückgibt. alright
      ist gebaut, um Menschen zu dienen, nicht meinem Geldbeutel. Hier zeige ich
      dir, warum und wie.</p>
  </section>

  <section>
    <h3>Ein Satz, vorher festgelegt</h3>
    <p>Der Satz eines Tages ergibt sich aus dem Datum selbst. Er ist für alle
      derselbe, er steht fest, bevor der Tag beginnt, und die App zweimal zu
      öffnen bringt nie einen anderen. Damit fällt genau der Reflex weg, von dem
      die Kategorie lebt: nach unten ziehen, noch einen holen, weitermachen, bis
      einer passt.</p>
    <p>Die Reihenfolge wird einmal aus einem festen Startwert gemischt. So laufen
      die 120 Sätze 120 Tage lang ohne Wiederholung durch &mdash; rund vier
      Monate, bis ein Satz wiederkommt.</p>
    <div class="aside">
      <p>Die Auswahl ist eine reine Funktion des Datums: kein Zufall zur
        Laufzeit, kein gespeicherter Zustand, nichts zu synchronisieren. Deshalb
        lässt sie sich auch ohne angeschlossenes Gerät testen.</p>
    </div>
  </section>

  <section>
    <h3>Die Mitteilung ist das Produkt</h3>
    <p>Die App besteht zum größten Teil aus einer Mitteilung am Tag. Also bekommt
      deren Planung die Sorgfalt, die sonst in eine Funktionsliste ginge. iOS
      erlaubt einer App 64 wartende Mitteilungen; alright plant alle 64 Tage im
      Voraus. Dein Satz kommt damit auch dann, wenn du die App zwei Monate lang
      nicht öffnest.</p>
    <p>Geht dieser Puffer zur Neige, sagt die letzte Mitteilung das ausdrücklich,
      statt dass die App einfach still wird. Eine App, die heimlich aufhört zu
      funktionieren, ist schlimmer als eine, die zugibt, dass sie geöffnet
      werden muss.</p>
  </section>

  <section>
    <h3>Drei Stile, ein Satz</h3>
    <p>Derselbe Text, dreimal gesetzt. Es gibt sie, weil der Satz der ganze
      Bildschirm ist: Wenn sonst nichts zu sehen ist, ist Typografie die
      komplette Oberfläche.</p>
    <h4>Clean</h4>
    <p>San Francisco auf Papierweiß, zentriert, Schrift fast schwarz. Der
      Standard, gebaut, um zu verschwinden.</p>
    <h4>Editorial</h4>
    <p>New York &mdash; Apples eigene Serife, mit echten optischen Größen &mdash;
      auf Elfenbein, mit steigendem Initial in Ultramarin. Die ersten zwei Zeilen
      laufen um das Initial herum, danach steht der Absatz wieder in voller
      Breite. Die erste Fassung dieses Stils wurde verworfen, weil sie
      &bdquo;Clean mit Serife&ldquo; war: gleiche zentrierte Komposition, gleiche
      Symmetrie, nur eine andere Schrift. Ein Stil braucht eine Idee, keinen
      Schriftwechsel.</p>
    <h4>Bold</h4>
    <p>Archivo Black in Versalien auf einer Karte: vier Pixel Kontur, zehn Pixel
      versetzter Schatten, acidgelber Grund. Die dunkle Fassung ist gestaltet,
      nicht invertiert &mdash; eine schwarze Kontur und ein schwarzer Schatten
      auf schwarzem Grund löschen genau die zwei Dinge, die den Stil ausmachen.
      Also wird Acid zur Karte und der Schatten weiß.</p>
  </section>

  <section>
    <h3>Hell und dunkel, zweimal gezeichnet</h3>
    <p>Sechs Bildschirme, nicht drei. Jeder Stil hat eine eigene dunkle Fassung
      statt einer invertierten Kopie, und die Unterschiede sind Entscheidungen,
      keine Rechnung: Aus Elfenbein wird warmes Fast-Schwarz, und das Ultramarin
      wird angehoben, damit es glüht statt zu flimmern; die Acid-Karte tauscht
      den Platz mit dem Grund, und der harte Schatten wird weiß.</p>
    {scheme_matrix(THE_SENTENCE, "D", "Mittwoch, 5. August",
                   "Hell", "Dunkel",
                   "Clean, Editorial und Bold in beiden Erscheinungsbildern. Diese Seite "
                   "folgt dem, was dein System eingestellt hat; in der App lässt sich "
                   "stattdessen auch eines davon festlegen.")}
  </section>

  <section>
    <h3>Schrift, die sich nach der Leserin richtet</h3>
    <p>Jeder Stil unterstützt Dynamic Type bis in die Barrierefreiheits-Größen.
      Der Satz ist so skaliert, dass er auch bei der größten Einstellung auf dem
      kleinsten unterstützten Gerät noch auf einen Bildschirm passt &mdash;
      niemand soll einen Satz scrollen müssen.</p>
    <p>Reduce Motion wird durchgehend respektiert. Das Zahnrad zu den
      Einstellungen ist das einzige Bedienelement auf dem Tagesbildschirm und die
      einzige Tür zu den anderen beiden Stilen. Sein Kontrast liegt deshalb über
      den 3:1, die die WCAG für ein Bedienelement verlangt &mdash; in jedem Stil,
      hell wie dunkel, geprüft von Tests statt nach Augenmaß.</p>
  </section>

  <section>
    <h3>Nichts einzurichten, nichts zu verbinden</h3>
    <p>Kein Account, keine Analyse, keine Werbung, keine Fremd-Frameworks und
      keinerlei Netzwerkaufrufe. Der Katalog liegt in der App, die Einstellungen
      im lokalen Speicher. Das ist keine nachträglich angebaute
      Datenschutzfunktion, sondern das, was herauskommt, wenn eine App von einem
      Server schlicht nichts braucht.</p>
  </section>

  <section>
    <h3>Der Name</h3>
    <p>alright wird überall kleingeschrieben, auch am Satzanfang: Der Name auf
      dem Homescreen ist klein, das Icon ist ein kleines &bdquo;a&ldquo;, und
      die App schreibt sich in ihren eigenen Texten selbst so. Die stilisierte
      Wortmarke al/right ist eine grafische Form derselben Buchstaben. Sie
      gehört auf Marken und Titel, nie in den Fließtext.</p>
  </section>
</div>
</div>"""


NEXT = f"""<section class="page-head">
  <div class="wrap wrap-narrow">
    <p class="eyebrow">Was kommt</p>
    <h1>Was als Nächstes kommt</h1>
    <p class="lede">Eine ehrliche Liste: was zuerst kommt, was abgewogen wird und
      was nie gebaut wird. Nichts davon hat einen Termin.</p>
  </div>
</section>

<div class="wrap wrap-narrow">
<div class="prose">
  <section>
    <h2>Zuerst: der App Store</h2>
    <p>Version eins ist fertig und im Test. Sie kann das, was auf der Startseite
      steht, und nichts auf dieser Seite wird gebraucht, damit sie sich lohnt.
      Käme von unten nie etwas, wäre alright trotzdem vollständig.</p>
  </section>

  <section>
    <h2>In Prüfung</h2>
    <p>Kandidaten, ohne Reihenfolge. Jeder muss dieselbe Frage bestehen: Macht
      er die App leiser oder lauter? Die Bilder sind Skizzen der Idee, keine
      Screenshots: gebaut ist davon nichts.</p>
    <h3>Ein Widget für den Homescreen</h3>
    {sketch_widget("Du musst heute nicht alles machen.",
                   "Skizze: ein Homescreen-Widget mit dem Satz des Tages im Bold-Stil")}
    <p>Der Satz des Tages, ohne etwas zu öffnen &mdash; wahrscheinlich sein
      natürlichster Ort. Bold ist der Stil, der auf einem Homescreen aus
      Armlänge noch trägt.</p>
    <h3>Einen Satz behalten</h3>
    {sketch_keep(SENTENCES[1:4],
                 "Skizze: eine kurze Liste behaltener Sätze, der neueste markiert")}
    <p>Manche Sätze treffen stärker als andere, und heute gibt es keinen Weg,
      einen davon zu behalten. Offen ist, wie das geht, ohne dass die App zu
      einer Sammlung wird, die gepflegt werden will.</p>
    <h3>Ein Satz für jeden Tag im Jahr</h3>
    {sketch_year(120, 365,
                 "Skizze: 365 Quadrate, eines pro Tag im Jahr, 120 davon gefüllt",
                 "120 von 365 Tagen geschrieben")}
    <p>120 Sätze heißt: Nach etwa vier Monaten kommt ein Satz wieder. Den Katalog
      auf 365 zu schreiben ist redaktionelle Arbeit statt technischer &mdash;
      und die Änderung, die das Produkt am meisten verbessern würde.</p>
    <h3>Die Akzentfarbe wählen</h3>
    {sketch_colours("Skizze: eine Reihe Akzentfarben, eine davon ausgewählt", ACCENTS)}
    <p>Die Stile setzen die Temperatur; eine Farbe würde sie zu deiner machen.
      Jede Farbe braucht eine geprüfte helle und dunkle Fassung, sonst wird der
      Satz in genau einem der beiden Modi unlesbar.</p>
    <h3>Die Sprache in der App umstellen</h3>
    <p>Heute folgt alright der Sprache des Geräts. Wer in zwei Sprachen liest,
      will seine Affirmationen nicht immer in der, auf die das Handy eingestellt
      ist.</p>
  </section>

  <section>
    <h2>Bewusst nicht geplant</h2>
    <p>Nichts davon ist vergessen worden, und nichts davon wartet auf einen
      freien Nachmittag. Jeder Punkt wurde erwogen und abgelehnt &mdash; hier
      steht jeweils, warum.</p>

    <h3>Konten und Anmeldungen</h3>
    <p>Es gibt nichts, wo man sich anmelden könnte. Der Satz eines Tages ergibt
      sich aus dem Datum, und das kann jedes Telefon allein ausrechnen; deine
      Einstellungen sind drei Werte im lokalen Speicher. Ein Konto würde Daten
      erzeugen, wo heute keine sind &mdash; eine Adresse, ein Passwort, ein
      Server, auf dem beides liegt &mdash; und keines davon würde die App in
      ihrer einen Aufgabe besser machen.</p>

    <h3>Streaks, Punkte, alles, was reißen kann</h3>
    <p>Eine Streak macht aus einem ausgelassenen Tag ein Versagen, und die
      Menschen, für die diese App geschrieben ist, brauchen nicht noch etwas,
      das sie enttäuscht haben. Dazu kommt der schwerere Grund: Zählen heißt
      Beobachten. alright erfährt nie, ob eine Mitteilung zugestellt oder
      geöffnet wurde, könnte also gar nicht mitzählen, ohne dich vorher zu
      beobachten. Dafür ist keine Zahl gut genug.</p>

    <h3>Ein Feed, eine Community, Sätze von anderen Leuten</h3>
    <p>Der Satz ist am selben Tag für alle derselbe und steht fest, bevor der
      Tag beginnt. Ein Feed brächte genau den Reflex zurück, gegen den es die
      Datumslogik überhaupt gibt: nach unten ziehen, noch einen holen,
      weitermachen, bis einer passt. Und Sätze von Fremden, an einem Ort, den
      Leute an schlechten Tagen öffnen, müssten moderiert werden &mdash; jeden
      Tag, auf unbestimmte Zeit. Das ist eine Pflicht, die ein
      Ein-Personen-Projekt nicht versprechen sollte, und unmoderiert wäre es
      schlimmer als gar nicht.</p>

    <h3>Werbung, Cross-Promotion, Mitteilungen, die etwas verkaufen</h3>
    <p>alright bittet einmal am Tag um einen Moment Aufmerksamkeit, und dieser
      Moment ist das ganze Produkt. Ihn für eine zweite Mitteilung auszugeben,
      die etwas verkauft, hieße, das Einzige herzugeben, was die App hat &mdash;
      für das, was so eine Platzierung eben zahlt. Die Regel bleibt einfach
      genug zum Nachprüfen: eine Mitteilung am Tag, und darin steht ein Satz.</p>

    <h3>Analyse und Tracking in jeder Form</h3>
    <p>Die App macht überhaupt keine Netzwerkaufrufe. Deshalb kann ihre
      Datenschutzerklärung kurz sein, und deshalb wird auf der App-Store-Seite
      stehen, dass keine Daten erhoben werden. Der Preis dafür ist echt und in Kauf
      genommen: Hier weiß niemand, wie viele Leute ihren Satz lesen, wie lange
      sie die App behalten oder welche Sätze am stärksten treffen. Diese
      Rückmeldung würde wirklich helfen. In einer App, deren einziges Versprechen
      lautet, dass nichts das Gerät verlässt, ist sie es nicht wert &mdash; also
      kommt die Rückmeldung per Mail, von Leuten, die sich entscheiden zu
      schreiben.</p>

    <p>Das sind keine fehlenden Funktionen. Das ist der Grund, warum es die App
      überhaupt gibt.</p>
  </section>

  <section>
    <h2>Fehlt dir etwas?</h2>
    <p>Schreib an <a href="mailto:alrightapp@icloud.com">alrightapp@icloud.com</a>.
      Jede Nachricht liest die Person, die die App baut &mdash; und genau daran
      ändert sich diese Liste.</p>
  </section>
</div>
</div>"""
