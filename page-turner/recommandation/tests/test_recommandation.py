from django.urls.base import reverse
from django.test import TestCase


# Create your tests here.


class TestRecommandation(TestCase):

    def test_recommandation_shoud_return_books(self):

        response = self.client.post(reverse("recommandation", args=("Harry Potter",)))
        content = response.json()["stdout"].split(",")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(content) > 0)

    def test_recommandation_shoud_not_return_any_books(self):

        response = self.client.post(reverse("recommandation", args=("WrongValue1234",)))
        content = response.json()["stdout"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual("❌ COULD NOT FIND ❌", content)


""" TITLES 
hot shot
purple cow: transform your business by being remarkable
code to zero
mr. x
hidden riches
candide (candide)
wlt: a radio romance
hide & seek
power of a woman
the feast of love (vintage contemporaries (paperback))
ten things i wish i'd known before i went out into the real world
julie and romeo: a novel
born in shame
dream country
the pact: a love story
fish! a remarkable way to boost morale and improve results
object lessons
beauty
a cold heart (alex delaware novels (paperback))
i know this much is true (oprah's book club)
high tide in tucson : essays from now or never
haroun and the sea of stories
executive orders (jack ryan novels)
a tale of two cities
shampoo planet : shampoo planet
the orchid thief (ballantine reader's circle)
the piano tuner : a novel
the birth of venus
charms for easy life
dead ringer (scottoline, lisa)
summer pleasures
shadow dance
eyes of prey
the switch
the fourth perimeter
thursday's child
firestorm (johansen, iris)
heaven
nighttime is my time (clark, mary higgins)
in too deep
what the lady wants
the velveteen rabbit
lion, the witch and the wardrobe
a rage to kill and other true cases : anne rule's crime files, vol. 6 (ann rule's crime files)
a rose for her grave & other true cases (ann rule's crime files)
master and commander (aubrey-maturin (paperback))
circus of the damned (anita blake vampire hunter (paperback))
blithe images
five days in paris
warum mã?â¤nner nicht zuhã?â¶ren und frauen schlecht einparken.
the story of b
hunting badger (joe leaphorn/jim chee novels)
the weight of water : a novel tag - author of resistance and strange fits of passion
state of siege (tom clancy's op-center, 6)
void moon
before women had wings (ballantine reader's circle)
wuthering heights (signet classic)
the jury
the restraint of beasts
jane eyre
the heart is a lonely hunter (oprah's book club)
the shipping news : a novel
lightning
disobedience
atlantis found (dirk pitt adventures (hardcover))
the face of fear
cold fire
blood work
master of the game
seize the night
the pied piper
silk
the unloved
one last time: a psychic medium speaks to those we have loved and lost
coming home
dating game
hatchet
e-wally and the quest
longitude: the true story of a lone genius who solved the greatest scientific problem of his time
the vagina monologues: the v-day edition
the mother tongue
morality play
phantom
things fall apart
more than complete hitchhiker's guide
the immaculate deception
rosencrantz & guildenstern are dead
the doll's house (sandman, book 2)
lost: a novel
colony
paper doll
walking shadow
thin air
chance
hush money (spenser mysteries)
hugger mugger
having our say : the delany sisters' first 100 years
breach of promise
e
suicide blonde
tropic of cancer
anne frank's tales from the secret annex
the funny thing is...
wildlife preserves
farmer boy (little house)
bears on wheels (bright & early books)
the little prince (wordsworth collection)
nora, nora: a novel
the plague tales
soul music (discworld novels (paperback))
men at arms
spencerville
claws and effect
the killing game: only one can win...and the loser dies
24 hours
everywhere that mary went
all i need is you
secret prey
outbreak
shadow prey
silent prey
certain prey
mortal prey
crossings
remembrance
summer's end
thurston house
the house on hope street
firestarter
the green mile: the bad death of eduard delacroix (green mile series)
the green mile: night journey (green mile series)
the green mile: coffey on the mile (green mile series)
the long walk
the cat who saw red
the cat who knew a cardinal
the cat who moved a mountain
family blessings
the cat who robbed a bank (cat who... (paperback))
the cat who smelled a rat (cat who... (paperback))
the unwanted
silent partner (alex delaware novels (paperback))
in a class by itself
obsession
assassin's apprentice (the farseer trilogy, book 1)
wizard's first rule (sword of truth)
blood shot (v.i. warshawski novels (paperback))
the light of other days
the forever war
don't stand too close to a naked man
dragonwings : golden mountain chronicles: 1903 (golden mountain chronicles)
captain underpants and the invasion of the incredibly naughty cafeteria ladies from outer space
the adventures of captain underpants: an epic novel (captain underpants)
needful things
a cry in the night
robert ludlum's the hades factor
robert ludlum's the cassandra compact (a covert-one novel)
moon women
self matters : creating your life from the inside out
the arraignment
gai-jin: a novel of japan
the further observations of lady whistledown
frankenstein (changing our world)
chicks in chainmail
myst, the: book of atrus
myst: the book of ti'ana
the elvenbane (halfblood chronicles)
chobits (chobits)
bygones
q-in-law (star trek the next generation, no 18)
one hit wonderland
home for the holidays
all the queen's men
true betrayals
do what you love, the money will follow : discovering your right livelihood
inconceivable
the lost boy
where is joe merchant?
dune
the vision
capital crimes
mcnally's trial (archy mcnally novels (paperback))
secrets
zoya
the running man
i'll take manhattan
ruby (landry)
hidden jewel (landry)
flashforward
ophelia speaks : adolescent girls write about their search for self
gap creek: the story of a marriage
in harm's way: the sinking of the uss indianapolis and the extraordinary story of its survivors
their eyes were watching god
coal: a human history
blue highways a journey into america
die hã?â¤upter meiner lieben.
the bone people
day of confession
luck in the shadows (nightrunner, vol. 1)
n is for noose (kinsey millhone mysteries (hardcover))
\o\" is for outlaw"
pearl
mad cows
malice
looking back
chesapeake blue (quinn brothers (hardcover))
no greater love
tiger eyes
bad boy
private scandals
tears of the moon (irish trilogy)
midwives
the runaway jury
revenge of the middle-aged woman
small gods (discworld novels (paperback))
the genesis code
gentle rogue (malory novels (paperback))
shadowfires
carrie
storm warning
warrior's woman
mischief
the dark highlander
desire
i thee wed
catch as cat can
sweet liar
all fall down
realm of shadows
apollyon: the destroyer is unleashed (left behind #5)
assassins: assignment: jerusalem, target: antichrist (left behind #6)
practical magic
red dragon
sunset in st. tropez
the waste lands (the dark tower, book 3)
politically correct holiday stories: for an enlightened yuletide season
mexico
wuthering heights
out on a limb
the road to omaha
my gal sunday
writ of execution
cry for the strangers
complicity
the concrete blonde (a harry bosch novel)
grendel
the salaryman's wife (children of violence series)
bread alone : a novel
rosie: a novel
crooked little heart
riptide
cranberry queen
blue shoe
gianna: aborted... and lived to tell about it (living books)
sideways stories from wayside school (wayside school)
shibumi
angry housewives eating bon bons (ballantine reader's circle)
niagara falls all over again
that camden summer
the 9 steps to financial freedom
all that glitters (landry)
the cat who sniffed glue
the heiress
the heart is a lonely hunter
mary, called magdalene
autobiography of a fat bride : true tales of a pretend adulthood
nightseer
bloody bones (anita blake vampire hunter (paperback))
guilty pleasures (anita blake vampire hunter (paperback))
obsidian butterfly (anita blake vampire hunter (paperback))
the lunatic cafe (anita blake vampire hunter (paperback))
seduction of water (ballantine reader's circle)
jade peony
heart song (logan)
unfinished symphony (logan)
music in the night (logan)
time cat: the remarkable journeys of jason and gareth
the celestine prophecy
welcome to dead house (goosebumps, no 1)
disclosure
the book of three (chronicles of prydain (paperback))
the high king (chronicles of prydain (paperback))
burning chrome (ace science fiction)
downsize this!
and then there were none
emma (wordsworth classics)
the first eagle (jim chee novels)
remember me
i dreamed of africa
remember when
to green angel tower, part 1 (memory, sorrow, and thorn, book 3)
kokology : more of the game of self-discovery
death in holy orders : an adam dalgliesh mystery
anne frank: diary of a young girl
mort (discworld novels (paperback))
alive : the story of the andes survivors (avon nonfiction)
amsterdam : a novel
secret history, the
the millionaires
red leaves
fugitive pieces
der club der toten dichter. roman.
the voyage of the narwhal
payment in blood
a traitor to memory
homeport
the visitant (the anasazi mysteries, book 1)
the prize
gracie: a love story
among the hidden
the heart of a woman
deception
a certain justice (adam dalgliesh mysteries (paperback))
cloud nine
montana 1948 : montana 1948
special delivery
kaleidoscope
the unbearable lightness of being : a novel (perennial classics)
finding moon
up island: a novel
meditations for women who do too much - 10th anniversary
the new york trilogy: city of glass, ghosts, the locked room (contemporary american fiction series)
in the lake of the woods
chronicle of a death foretold
a sand county almanac (outdoor essays & reflections)
lasher: lives of the mayfair witches (lives of the mayfair witches)
cordina's crown jewel
firefly
the loop: a novel
caribbean
cause of death
singing in the comeback choir
eleventh hour: an fbi thriller
vengeance in death
loyalty in death
widow's walk
daybreak
purple cane road
presumed innocent
the source
false pretenses
beyond eden
finding the dream
second wind
more letters from a nut
wild mind: living the writer's life
beach music
special circumstances
lake wobegon: summer 1956
final jeopardy (alexandra cooper mysteries (paperback))
delusions of grandma
memnoch the devil : the vampire chronicles (vampire chronicles)
the plague (vintage international)
the letter
wherever you go, there you are : mindfulness meditation in everyday life
middle of nowhere
red light
lady of the forest
the guest list
the far side gallery 4
the indispensable calvin and hobbes
ella minnow pea: a progressively lipogrammatic epistolary fable
perfect evil (maggie o'dell novels (paperback))
split second (maggie o'dell novels (paperback))
the invitation
every living thing
the chronicles of pern: 1st fall (the dragonriders of pern)
rose daughter
prince charming
black lightning
single white vampire
one pink rose (clayborne brides)
the heiress bride (bride trilogy (paperback))
falling leaves brit edition
pride, prejudice and jasmin field : a novel
mistaken identity
cowboy
savannah blues
patron saint of liars : a novel
brave new world
why do clocks run clockwise?
waiting: the true confessions of a waitress
la cucina: a novel of rapture
dance hall of the dead (joe leaphorn novels)
orchid beach (holly barker novels (paperback))
a woman betrayed
lost boys
the fallen man (joe leaphorn novels)
legal tender
the bestseller
as the crow flies
on the banks of plum creek
dangerous angels: the weetzie bat books
the magician's nephew (rack) (narnia)
krakatoa : the day the world exploded: august 27, 1883
my family and other animals.
a portrait of the artist as a young man
dracula
ceremony (contemporary american fiction series)
the odyssey
frankenstein or the modern prometheus (penguin classics)
candide (penguin classics)
james herriot's cat stories
the phantom of manhattan
trunk music (detective harry bosch mysteries)
k-pax
the sigma protocol
tales too ticklish to tell: bloom county
city of bones
ringworld
on the beach
robots of dawn (robots of dawn)
the life and loves of a she-devil
pawn of prophecy (the belgariad, book 1)
shoeless joe
blade runner: (do androids dream of electric sheep)
guardians of the west (book 1 of the malloreon)
the horse you came in on
the power of one
a prayer for owen meany (ballantine reader's circle)
death of a stranger
the ultimate hitchhiker's guide to the galaxy
lost & found (red dress ink)
macgregor grooms (macgregors)
the macgregors: alan - grant (the macgregors)
founding brothers: the revolutionary generation
the world below
persepolis : the story of a childhood (alex awards (awards))
evening
trans-sister radio (vintage contemporaries (paperback))
the emperor of ocean park (vintage contemporaries (paperback))
don't let's go to the dogs tonight : an african childhood
aztec
the return of the indian (indian in the cupboard)
tales from watership down
savage thunder
pearl cove (donovan)
subterranean
dream a little dream
lady be good (avon romance)
this heart of mine (avon romance)
brave the wild wind
chain letter (avon camelot books (paperback))
i heard the owl call my name
the ghost
gone for good
can you keep a secret?
demolition angel
lullaby : a novel
oryx and crake
you're only old once! : a book for obsolete children
breathing lessons
the plague
are you my mother?
forgiving
the nightingale legacy
saving grace
naked came the manatee: a novel
executive orders
blue diary
hunting season
remember when (roberts, nora)
the jane austen book club
the cat who walks through walls
tom clancy's op-center: mirror image (tom clancy's op center (paperback))
acceptable risk
rapture in death
ceremony in death (eve dallas mysteries (paperback))
small vices
holiday in death
tom clancy's op-center balance of power (tom clancy's op center (paperback))
conspiracy in death
night moves (tom clancy's net force, no. 3)
fever
godplayer
stick figure: a diary of my former self
tom clancy's op-center: line of control (tom clancy's op center (paperback))
gunpowder green
cut
once in a lifetime
palomino
get shorty
lost souls
guardian angel
mixed blessings
jewels
promises
a dangerous fortune
los alamos: a novel
freedomland
holes (readers circle)
where you belong
leap of faith
taken
the magus
how to eat fried worms
the witch of blackbird pond (laurel leaf books)
the outlaws of sherwood
nothing lasts forever
mary, mary
the celestine vision: living the new spiritual awareness
street dreams
absolute power
the edge of town
up country
nightshade
the unexpected mrs. pollifax
twice shy
the ritual bath (peter decker & rina lazarus novels (paperback))
silence in hanover close
straight
seventh heaven
dave barry turns 40
small sacrifices: a true story of passion and murder
the deep end of the ocean
dead girls don't wear diamonds (blackbird sisters mysteries)
dirty work (stone barrington novels (paperback))
the stargazey: a richard jury mystery (richard jury mysteries (paperback))
the bachman books: four early novels by stephen king : rage, the long walk, roadwork, the running man
the claiming of sleeping beauty (erotic adventures of sleeping beauty)
the mammy
the quilter's apprentice
the endearment
the cat who lived high
the cat who came to breakfast
the dark room
killing floor
mad jack
eclipse bay
the music of the spheres
turbulence
eleventh hour: an fbi thriller (fbi thriller (jove paperback))
scruples two
dave barry is not making this up
chang and eng
bravo two zero
dead famous
never cry wolf
the haunted mesa
sweet revenge
genuine lies
divine evil
a suitable vengeance
\surely you're joking, mr. feynman!\": adventures of a curious character"
the right stuff
what falls away: a memoir
missing joseph
blood test (alex delaware novels (paperback))
breakfast in bed
murder, she meowed (mrs. murphy mysteries (paperback))
dark rivers of the heart
the perfect summer
lucky's lady
about a boy uk
the book of guys: stories
year of wonders: a novel of the plague
the sea hunters
high tide
empty promises
serpent : a novel from the numa files (numa files series)
the chimney sweeper's boy
hitchhik gd galaxy (hitchhiker's trilogy (paperback))
color purple
mindhunter : inside the fbi's elite serial crime unit
melody (logan)
less than zero
hollywood wives
once and always
where are the children?
perfume : perfume
disappearing acts
private parts
saint maybe
the lost world: a novel
dark rivers of the heart: a novel
pompeii: a novel
quite a year for plums
eight weeks to optimum health: a proven program for taking full advantage of your body's natural healing power (proven program for taking full advantage of your body's natural healing power)
dr. death: a novel
a natural history of the senses
sophie's choice
the man in the high castle
the tightwad gazette: promoting thrift as a viable alternative lifestyle
nobody's fool (vintage contemporaries)
in the skin of a lion: a novel
cruel and unusual
garden of eden
christmas box (christmas box trilogy)
the man who mistook his wife for a hat : and other clinical tales
the 7 habits of highly effective teens
shutter island: a novel
naked pictures of famous people
from the mixed-up files of mrs. basil e. frankweiler
the wind in the willows
the blue day book
the prize winner of defiance, ohio: how my mother raised 10 kids on 25 words or less
the partly cloudy patriot
hello, darkness
enemy within
letters for emily
my sister's keeper : a novel (picoult, jodi)
war for the oaks
bookends
wild
first person plural : my life as a multiple
parallel lies
the sexual life of catherine m.
the venetian's wife: a strangely sensual tale of a renaissance explorer, a computer, and a metamorphosis
a fire upon the deep (zones of thought)
the eye of the world : book one of 'the wheel of time' (wheel of time)
the mark: the beast rules the world (left behind no. 8)
stick a geranium in your hat and be happy!
west with the night
dragonbone chair sorrow 1 (memory, sorrow, & thorn (paperback))
way of the peaceful warrior: a book that changes lives (peaceful warrior)
my place
forbidden fruit
skyward
the soul catcher: a maggie o'dell novel
firebrand (mira historical romance)
16 lighthouse road
halfway to heaven
death qualified (barbara holloway novels (paperback))
white mountain
dark water (mira romantic suspense)
princess charming
jane eyre (wordsworth classics)
the seven spiritual laws of success: a practical guide to the fulfillment of your dreams (based on creating affluence)
venezianische scharade. commissario brunettis dritter fall.
schlafes bruder
felidae. roman.
generation x. geschichten fã?â¼r eine immer schneller werdende kultur.
gefã?â¤hrliche geliebte.
zwã?â¶lf.
neue leiden des jungen
harry potter und der stein der weisen
el hobbit
the music of chance
starship titanic
il piccolo principe prince italn
the illustrated man (grand master editions)
the magician's nephew
the long winter (little house)
prince caspian (rack) : the return to narnia (narnia)
the horse and his boy
the last battle
deenie
grace
one-hit wonder
the passion
frankenstein (wordsworth classics)
night of crash-test dummies
lasher (lives of the mayfair witches)
the book: on the taboo against knowing who you are
winnie-the-pooh
the meaning of life
the toughest indian in the world
sisters found
it's obvious you won't survive by your wits alone
do no harm
the cay
leaving cold sassy: the unfinished sequel to cold sassy
eye of the storm
blubber (yearling books (paperback))
ramona and her mother (ramona quimby (paperback))
if tomorrow comes
decked : a regan reilly mystery
blind faith
hot ice
home fires
the dead zone
swan song
whitney, my love
lammas night
oh, the places you'll go!
the ghatti's tale (finder-seekers, book one)
mind-speakers' call (the ghatti's tale, book 2)
the giving tree
snow white, blood red
tom clancy's op-center: mission of honor (tom clancy's op center (paperback))
needful things: the last castle rock story
the dilbert future: thriving on stupidity in the 21st century
no one to trust
horse and his boy
the lion, the witch and the wardrobe (rpkg) (narnia)
four past midnight
the case for christ:  a journalist's personal investigation of the evidence for jesus
legends of the fall
redemption
travels with charley: in search of america
the silence of the lambs
a house for mr. biswas
love me forever (sherring cross (paperback))
defy not the heart
man of my dreams (sherring cross (paperback))
prisoner of my desire
well favored gentleman (avon historical romance)
scandal
rendezvous
lovers
double standards
until you
la carta esferica / the nautical chart (spanish edition)
harry potter and the chamber of secrets postcard book
the mote in god's eye
vows
american indian myths and legends (pantheon fairy tale and folklore library)
plain and simple : a journey to the amish (ohio)
hotel of the saints
armageddon: the cosmic battle of the ages (left behind #11)
the miserable mill (a series of unfortunate events, book 4)
doing good
hogfather
lawless
deadly embrace
silent partner
the legacy
the macgregors: daniel-ian
fires of winter
the mask
a dry spell
daring to dream
talking to heaven: a medium's message of life after death
tarnished gold (landry)
just the way you are
magician's gambit (the belgariad, book 3)
king of the murgos (malloreon (paperback random house))
sorceress of darshiva (malloreon (paperback random house))
tai-pan
priestess of avalon
romeo and juliet
family honor
house corrino (dune: house trilogy, book 3)
midnight
captive star
behind the scenes at the museum
something wicked this way comes
hop on pop (i can read it all by myself beginner books)
desert heat
point of impact (tom clancy's net force (berkley publishing group))
sea of fire (op-center series, volume 10)
only by your touch (signet books)
skin deep
in the country of last things (contemporary american fiction)
the hobbit
the terrible hours
the ice limit
relic
mount dragon: a novel
the gate to women's country
fantasy lover
just cause
the solitaire mystery
willow (debeers)
trail of secrets
honest illusions
come the spring (clayborne brothers)
almost heaven
american star
a history of the world in 10 1/2 chapters (vintage international)
jemima j.
across the nightingale floor: tales of the otori, book one
going down
shutterbabe: adventures in love and war
witch child
deja dead
interview with the vampire : anniversary edition
the tattooed map
homicidal psycho jungle cat: a calvin and hobbes collection
the calvin & hobbes lazy sunday book
far side gallery 2
feuerkind. thriller.
what's a girl gotta do
the woman who walked into doors
all the weyrs of pern (dragonriders of pern (paperback))
no one here gets out alive
l.a. dead: a stone barrington novel (stone barrington novels (paperback))
seat of the soul
the purpose-driven life: what on earth am i here for?
the richest man in babylon
lost
death of a salesman
wither
cuba libre
replay
the mammoth hunters (earth's children (paperback))
what to expect the toddler years
ruins (the x-files)
dear exile : the true story of two friends separated (for a year) by an ocean
the love letter
voyage on the great titanic: the diary of margaret ann brady (dear america)
the cases that haunt us
solaris
deadlock (v.i. warshawski novels (paperback))
the i-5 killer (signet true crime s.)
the agony and the ecstasy: a biographical novel of michelangelo
chasing cezanne
mansfield park (penguin classics)
the magic of recluce (recluce series, book 1)
you shall know our velocity
the awakening (dover thrift editions)
watchmen
what should i do with my life?
ecotopia
the bone vault
wake up, i'm fat!
french silk
a kiss of shadows (meredith gentry novels (hardcover))
a 5th portion of chicken soup for the soul : 101 stories to open the heart and rekindle the spirit
riding in cars with boys: confessions of a bad girl who makes good
ice bound : a doctor's incredible battle for survival at the  south pole
the breaker
the pillars of creation (sword of truth, book 7)
old yeller
the silken web
a streetcar named desire
seven dials
black elk speaks: being the life story of a holy man of the oglala sioux
the illuminatus trilogy: the eye in the pyramid, the golden apple & leviathan
talisman
waiting for godot
the little friend
not without my daughter
the hottest state: a novel
where the heart is: a novel
riley in the morning
seven habits of highly effective people : powerful lessons in personal change
silent night : the story of the world war i christmas truce
the constant gardener
the runaway bunny
pandora's clock
behind the attic wall (avon camelot books (paperback))
superfudge (yearling books (paperback))
the naked face
the tall pine polka (ballantine reader's circle)
the other side and back: a psychic's guide to our world and beyond
the return
bastard out of carolina
the bell jar
love and marriage
sickened : the memoir of a munchausen by proxy childhood
the perfect lie
texas rich
shrink rap
naked prey
the other woman
first offense
heart full of lies: a true story of desire and death
eats, shoots and leaves: the zero tolerance approach to punctuation
he died with a felafel in his hand
for love of evil : book six of incarnations of immortality (incarnations of immortality (paperback))
generation golf. eine inspektion
trading spaces behind the scenes: including decorating tips and tricks
jane eyre (signet classics (paperback))
shadows
the moon is a harsh mistress
bones of the earth
dark symphony
dark legend
last orders
the wide window (a series of unfortunate events, book 3)
the ersatz elevator (a series of unfortunate events, book 6)
nice
last chapter and worse
shiloh
the devil in the white city: murder, magic, and madness at the fair that changed america
straight man
undaunted courage: meriwether lewis thomas jefferson and the opening of the american west
reunion
timequake
the piano tuner
a knight of the word (the word and the void trilogy, book 2)
dark magic
dark challenge
billy and the boingers bootleg (bloom county book)
bad girls of the bible and what we can learn from them
hostage
midnight in ruby bayou
suspicion of betrayal
balance of power
bad business
abraham : a journey to the heart of three faiths
pure drivel
a heart of stone
cosmos
old possum's book of practical cats, illustrated edition
above the law: a novel
venus envy
seventh son (tales of alvin maker, book 1)
the grapes of wrath (20th century classics)
kiss my tiara : how to rule the world as a smartmouth goddess
stone of tears (sword of truth, book 2)
there's treasure everywhere--a calvin and hobbes collection
family pictures
when we were orphans (vintage international (paperback))
bridget jones. am rande des wahnsinns.
pyramids (discworld novels (paperback))
with a southern touch
prescription for nutritional healing: a practical a-z reference to drug-free remedies using vitamins, minerals, herbs & food supplements
mother earth father sky
deadeye dick
twelve
villa incognito
irish chain (benni harper mysteries (paperback))
peace is every step: the path of mindfulness in everyday life
the sunday wife
the road to wellville
far side gallery
mother night
slaughterhouse-five
soul of the fire (sword of truth, book 5)
echo burning (jack reacher novels (paperback))
heart of darkness: with the congo diary (penguin twentieth-century classics)
one night of scandal
where the wild things are
joy luck club
fearless jones (fearless jones novels (paperback))
jazz (plume contemporary fiction)
blackbird : a childhood lost and found
the presence
the physician
flight lessons
dakota home (dakota trilogy, book 2)
drawing blood
sons and lovers
into the night
dirk gently's holistic detective agency
come to grief
beyond civilization: humanity's next great adventure
liebesleben
city of light
the fermata
thoughts while having sex
auntie mame: an irreverent escapade
clear and present danger
wielding a red sword (incarnations of immortality (paperback))
being a green mother (incarnations of immortality (paperback))
juxtaposition (apprentice adept (paperback))
indemnity only (v.i. warshawski novels (paperback))
offer from a gentleman, an
too much temptation
champions of the force (star wars: the jedi academy trilogy, vol. 3)
charming the prince
perfect
medusa's child
harry potter und die kammer des schreckens
a kingdom of dreams
tales of mystery and imagination (classics library (ntc))
10 lb. penalty
the cat who had 14 tales
no second chance
one for the money : a stephanie plum novel
high fidelity. (dt. ausgabe)
the house next door
going home: unfinished business/ island of flowers/ mind over matter
fried green tomatoes at the whistle stop cafe (ballantine reader's circle)
side effects
invisible cities (a harvest/hbj book)
satanic bible
the south beach diet: the delicious, doctor-designed, foolproof plan for fast and healthy weight loss
more than you know: a novel
the odyssey (penguin classics)
bloomability
high maintenance
captivated (silhouette single title)
from this day
ties that bind: a novel
bored of the rings: a parody of j.r.r. tolkien's the lord of the rings
the echo
a crown of swords (the wheel of time, book 7)
and the band played on: politics, people, and the aids epidemic
the lion's lady
the red hat club
nice girls finish last (viking mystery suspense)
covenant with the vampire (diaries of the family dracul)
dark prince
interest of justice
i do (but i don't)
salt: a world history
princess in love (the princess diaries, vol. 3)
web of dreams (casteel)
days are just packed : a calvin and hobbes collection (calvin and hobbes)
dracula (bantam classics)
the prince
imzadi (star trek: the next generation)
the eyes of the dragon
rilla of ingleside (anne of green gables novels (paperback))
red dwarf: infinity welcomes careful drivers
the winter of our discontent (penguin twentieth-century classics)
the onion girl (newford)
night of the mary kay commandos featuring smell o-toons
well-schooled in murder
why cats paint: a theory of feline aesthetics
wolves of the calla (the dark tower, book 5)
the house of gentle men : a novel
motion to suppress
punish the sinners
sense and sensibility (wordsworth classics)
wicked forest (debeers)
love in vein
anna karenina (penguin classics)
transformation: the breakthrough
hotel pastis : a novel of provence
bridget jones' diary (film tie-in)
the stars my destination
love in another town
judas child
fleeced : a regan reilly mystery (regan reilly mysteries (paperback))
woman: an intimate geography
mine to take (futuristic romance)
the glass menagerie
an accidental woman : a novel
year zero
the writing life
kiss and make-up
tricky business
jesus freaks: dc talk and the voice of the martyrs - stories of those who stood for jesus, the ultimate jesus freaks
the last continent (discworld novels (paperback))
bill bryson african diary
autobiography of a yogi
emma (penguin classics)
with nails the film diaries of richard e
heat
something wonderful
team rodent : how disney devours the world
uncle john's ahh-inspiring bathroom reader (bathroom reader series)
"""
