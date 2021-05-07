"""
* Assignment: Regexp Greedy Moon Speech
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Using `re.findall()` and non-greedy qualifier split text by paragraphs
    3. In ``result: str`` catch paragraf starting with "We choose to go to the moon"
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Za pomocą `re.findall()` i non-greedy qualifier podziel tekst na paragrafy
    3. W ``result: str`` uchwyć paragraf zaczynający się od słów "We choose to go to the moon"
    X. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * In this assignments all HTML paragraphs starts with `<p>` and ends with `</p>`
    * In real life paragraphs parsing is more complex, but here it is simplified.

Test:
    >>> type(result) is str
    True
    >>> result
    'We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organize and measure the best of our energies and skills,because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win,and the others, too.'
"""


# Given
import re

DATA = ("<h1>TEXT OF PRESIDENT JOHN KENNEDY'S RICE STADIUM MOON SPEECH</h1>\n"
        "<p>President Pitzer, Mr. Vice President, Governor, "
        "CongressmanThomas, Senator Wiley, and Congressman Miller, Mr. Webb, "
        "Mr.Bell, scientists, distinguished guests, and ladies and "
        "gentlemen:</p><p>We choose to go to the moon. We choose to go to "
        "the moon in this decade and do the other things, not because they "
        "are easy, but because they are hard, because that goal will serve "
        "to organize and measure the best of our energies and skills,because "
        "that challenge is one that we are willing to accept, one we are "
        "unwilling to postpone, and one which we intend to win,and the "
        "others, too.</p><p>It is for these reasons that I regard the "
        "decision last year to shift our efforts in space from low to high "
        "gear as among the most important decisions that will be made during "
        "my incumbency in the office of the Presidency.</p><p>In the last 24 "
        "hours we have seen facilities now being created for the greatest "
        "and most complex exploration in man's history.We have felt the "
        "ground shake and the air shattered by the testing of a Saturn C-1 "
        "booster rocket, many times as powerful as the Atlas which launched "
        "John Glenn, generating power equivalent to 10,000 automobiles with "
        "their accelerators on the floor.We have seen the site where the F-1 "
        "rocket engines, each one as powerful as all eight engines of the "
        "Saturn combined, will be clustered together to make the advanced "
        "Saturn missile, assembled in a new building to be built at Cape "
        "Canaveral as tall as a48 story structure, as wide as a city block, "
        "and as long as two lengths of this field.</p>")

result = ...


# Solution
paragraphs = re.compile(r'<p>(.*?)</p>')

for p in paragraphs.findall(DATA):
    if p.startswith('We choose'):
        result = p
