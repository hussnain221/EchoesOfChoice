# THE LAST SIGNAL - COM0010 Final Project

define alex = Character("Alex", color="#00cfff")
define nova = Character("Nova", color="#ff6eb4")
define kain = Character("Director Kain", color="#ff4444")

default trust_nova = 0
default fixed_power = False
default kain_warned = False

image bg room = "bg room.jpg"
image bg controlroom = "bg controlroom.jpg"
image bg dockingbay = "bg dockingbay.jpg"
image bg engineroom = "bg engineroom.jpg"
image bg escapepod = "bg escapepod.jpg"

image nova neutral = "eileen happy.png"
image nova scared = "nova scared.png"
image nova happy = "nova happy.png"
image kain neutral = "kain neutral.png"
image kain angry = "kain angry.png"

transform character_size:
    size (400, 600)
    xalign 0.5
    yalign 1.0

transform character_left:
    size (400, 600)
    xalign 0.2
    yalign 1.0

transform character_right:
    size (400, 600)
    xalign 0.8
    yalign 1.0

label start:

    scene bg controlroom with fade
    play music "audio/ambient_space.mp3" fadein 2.0

    "Year 2147. Space Station Meridian-7."
    "Power is at 34 percent. Life support is stable for now."
    "You have been alone on this station for 6 days."
    "Then the distress signal came."

    alex "Another signal. Coming from Docking Bay 3."
    alex "Someone is out there."

    menu:
        "Check the signal immediately.":
            $ trust_nova += 1
            jump check_signal
        "Ignore it. Could be a trap.":
            jump ignore_signal

label ignore_signal:

    scene bg controlroom with fade

    alex "I have enough problems already."
    "Three minutes pass. The signal gets stronger."
    alex "Fine. I will check it."
    jump check_signal

label check_signal:

    scene bg dockingbay with fade

    "You walk into the Docking Bay. An escape pod is attached to airlock 3."
    "Someone is knocking from inside."
    alex "Hello? Can you hear me?"

    

    nova "Please open the door. I have been in here for two days."

    menu:
        "Open the pod now.":
            $ trust_nova += 1
            jump open_pod
        "Ask who she is first.":
            jump ask_identity

label ask_identity:

    show nova scared at character_size with dissolve

    nova "My name is Nova. I was a researcher on Sub-Level 4."
    nova "Someone locked me out of the station. I barely made it to the pod."
    alex "Sub-Level 4 was sealed three weeks ago. Kain said everyone evacuated."

    show nova neutral at character_size with dissolve

    nova "Kain lied. I was left behind on purpose."
    $ trust_nova += 1
    jump open_pod

label open_pod:

    scene bg dockingbay with fade

    show nova neutral at character_size with dissolve

    nova "Thank you. I thought I was going to die in there."
    alex "What happened to this station? Half the systems are offline."
    nova "Kain happened. He planted an override chip in the Engine Room."
    nova "If you remove it, the station stabilises."

    menu:
        "Go to the Engine Room with Nova.":
            $ trust_nova += 1
            jump engine_room_together
        "Go alone. Tell Nova to wait here.":
            jump engine_room_alone

label engine_room_together:

    scene bg engineroom with fade

    show nova neutral at character_right with dissolve

    "You and Nova move through the corridors quickly."
    "The lights flicker every few seconds."
    nova "It should be behind the main power coupling. A small black chip."
    alex "I see it."
    "You reach for the chip. Then Kain's voice cuts through the comms."

    show kain neutral at character_left with dissolve

    kain "Step away from the coupling, technician."
    alex "Director Kain."

    show kain angry at character_left with dissolve

    kain "That chip is keeping this station running on my schedule."
    kain "Walk away. Take the pod. Leave the girl."

    hide kain angry

    menu:
        "Remove the chip. Trust Nova.":
            $ trust_nova += 1
            jump good_ending
        "Listen to Kain. Step back.":
            $ kain_warned = True
            jump listen_to_kain

label engine_room_alone:

    scene bg engineroom with fade

    "You find the chip exactly where Nova described."
    "Kain's voice comes through the comms before you can touch it."

    show kain neutral at character_size with dissolve

    kain "I see you found my little addition."

    show kain angry at character_size with dissolve

    kain "That chip stays in. Walk away and I will make sure you get out alive."
    kain "The girl is not your problem."

    hide kain angry

    menu:
        "Remove the chip anyway.":
            jump neutral_ending
        "Leave the chip. Go back to Nova.":
            $ kain_warned = True
            jump warn_nova

label warn_nova:

    scene bg dockingbay with fade

    show nova neutral at character_size with dissolve

    alex "Kain is watching. He said to leave you."

    show nova scared at character_size with dissolve

    nova "So you are going to listen to him?"

    menu:
        "No. Let us find another way.":
            $ trust_nova += 1
            jump neutral_ending
        "I am sorry. I have to think about myself.":
            jump bad_ending

label listen_to_kain:

    scene bg engineroom with fade

    show nova neutral at character_size with dissolve

    "You step back. Nova stares at you."
    nova "You are really going to do what he says?"
    alex "I need to think about this."

    hide nova neutral

    show kain neutral at character_size with dissolve

    kain "Smart. There is an escape pod ready for you at Bay 1."
    kain "Leave now and you will be home by morning."

    hide kain neutral

    menu:
        "Change your mind. Go back to the chip.":
            jump neutral_ending
        "Take the offer. Leave Nova behind.":
            jump bad_ending

label good_ending:

    scene bg engineroom with fade

    hide nova scared
    hide kain angry

    "You pull the chip out. The lights stop flickering."
    "Power jumps to 89 percent."

    show nova happy at character_size with dissolve

    nova "You did it. Alex, you actually did it."

    hide nova happy

    show kain angry at character_size with dissolve

    kain "You have no idea what you have just done."

    hide kain angry

    alex "I think I do. Transmitting everything to Central Command right now."
    "Kain goes silent."

    show nova happy at character_size with dissolve

    nova "He will be arrested the moment he docks anywhere."
    nova "We make a good team."

    scene bg escapepod with fade

    show nova happy at character_size with dissolve

    "You and Nova take the main escape pod together."
    "The station holds. Rescue arrives six hours later."
    "Director Kain is arrested at Port Salis two days after that."
    alex "For someone who spent two days in a pod, you are surprisingly calm."
    nova "I had good company in the end."

    hide nova happy

    " "
    "--- GOOD ENDING ---"
    "You trusted the right person. The station survived. Justice was served."
    return

label neutral_ending:

    scene bg engineroom with fade

    "You pull the chip out alone. Power climbs back to 76 percent."
    alex "Station is stable. Kain is going to know what I did."

    scene bg dockingbay with fade

    show nova neutral at character_size with dissolve

    nova "I heard the power come back. You did it."
    nova "I am leaving. Before Kain sends someone."
    alex "Take care of yourself."
    nova "You too, Alex."

    hide nova neutral

    "Nova leaves. You stay and send a full report to Central Command."
    "Kain disappears before authorities arrive. He is never caught."
    "The station is decommissioned three months later."
    " "
    "--- NEUTRAL ENDING ---"
    "The station survived. But Kain got away."
    return

label bad_ending:

    scene bg controlroom with fade

    "You walk to Bay 1. The pod is there, just like Kain said."
    "You do not look back."

    scene bg escapepod with fade

    "From the pod window, you watch Meridian-7."
    "Twenty minutes later, the station goes dark."
    "Then the explosion."
    alex "Nova..."
    "You arrive at Port Salis alone."
    "Kain's story is already on every channel."
    "A tragic accident. A lone survivor. You."
    "You know the truth. But who would believe you now."
    " "
    "--- BAD ENDING ---"
    "You chose wrong. Some choices cannot be undone."
    return