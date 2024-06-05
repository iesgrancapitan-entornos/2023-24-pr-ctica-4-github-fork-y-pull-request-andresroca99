"""
Goal:
By Fran Ogallas
Start: Last update:
"""
import re

"""
With re. search, match, findall, split and sub"""

"""
Ascii, european tlf, american tlf, safe passwords with a minimum of characters, 
ipv6, gmails, hotmails, iesgrancapitan mails, twitter accounts without repeated ats
"""

REGEX1 = {"ASCII": r"[\!-~]+", "EUROTLF": r"[0-9]{9}", "USTLF": r"\([0-9]{3}\) [0-9]{3}-[0-9]{4}",
         "PASSWORD": r"[A-Za-z0-9#\?!@$%^&\*-]{9,}",
         "IPV6": r"[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F].{1,4}",
         "GMAIL": r"\S+@gmail\.com", "HOTMAIL": r"\S+@hotmail\.com",
         "GCMAIL": r"a[0-9]{2}[a-z]{6}@iesgrancapitan\.org", "TWT": r" (@[A-Za-z0-9_-]+)"}

REGEX2 = r"\."



SAMPLE1 = ("@clarAA-2 362020002 (322) 925-1045 M3v0yd3@ki? 7340:49aa:e23b:ccc8 730:4a:3:ccc8 yokeseman@gmail.com "
           "bazingalol@hotmail.com a99bofeca@iesgrancapitan.org @@maquinador6 @6truhan__")

SAMPLE2 = ("Balder (en nórdico antiguo: Baldr), en el ámbito de la mitología nórdica y germana, es el dios de la paz,"
           " la luz y el perdón, y el segundo hijo de Odín. También es citado como Baeldaeg (num 243) en algunas"
           " fuentes protohistóricas que se refiere a un antiguo rey escandinavo del siglo iii). \nBaldur: en feroés e"
           " islandés modernos. \nBalder: en danés, noruego, sueco e inglés modernos, y en antiguo alto alemán. "
           "También es la forma que se usa en español. \nBaldr: en nórdico antiguo, el idioma original de las sagas,"
           " y, ocasionalmente, en inglés. En el siglo xii, los relatos daneses de Saxo Grammaticus y otros cronistas"
           " nórdicos registraron una versión evemerista de la historia. La Edda poética, compilada en el siglo xiii"
           " en Islandia pero basada en poemas en nórdico antiguo mucho más antiguos, y la Edda prosaica contienen"
           " numerosas referencias a la muerte de Balder, interpretada como una gran tragedia para los Æsir y una de"
           " las señales precursoras del Ragnarök. De acuerdo con la Gylfaginning, un libro de la Edda prosaica de"
           " Snorri Sturluson, la esposa de Balder se llama Nanna y su hijo es Forseti. Snorri también relata que"
           " Balder poseía la mejor nave jamás construida, llamada Hringhorni, y que no había lugar más hermoso que"
           " su salón, Breidablik.")


# TODO: BROKEN PASSWORD, TWT
# "TWT": r"[\A| ]@[A-Z|a-z|0-9|_|-]+"
# "PASSWORD":  r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#\?!@$%^&\*-]).{8,}"


def find_and_show():
    results = re.findall(REGEX1["PASSWORD"], SAMPLE1)
    print(results)
    for result in results:
        print(result)


def fragment_text():
    results = re.split(REGEX2, SAMPLE2, 6)
    for result in results:
        print(result)


def substitute():
    changed_str = re.sub(r"Balder", r"El caído", SAMPLE2, 1)
    results = re.split(REGEX2, changed_str)
    for result in results:
        print(result)


def main():
    substitute()


if __name__ == "__main__":
    main()
