# THE LAST SIGNAL - COM0010 Final Project

define alex = Character("Alex", color="#00cfff")
define nova = Character("Nova", color="#ff6eb4")
define kain = Character("Director Kain", color="#ff4444")
define system = Character("MERIDIAN-7", color="#27f3ff")

default trust_nova = 0
default suspicion_kain = 0
default station_minutes = 0
default access_card = False
default med_patch = False
default terminal_unlocked = False
default override_code = False
default fixed_power = False
default kain_warned = False
default quest_title = "Investigate the distress signal"
default quest_details = "A distress signal is repeating from Docking Bay 3. Confirm whether the caller is real before the station loses power."

image bg room = "bg room.jpg"
image bg controlroom = "bg controlroom.jpg"
image bg dockingbay = "bg dockingbay.jpg"
image bg engineroom = "bg engineroom.jpg"
image bg escapepod = "bg escapepod.jpg"
image bg corridor = "bg corridor.png"
image bg terminal = "bg terminal.png"

image alex neutral = "alex neutral.png"
image nova neutral = "eileen happy.png"
image nova scared = "nova scared.png"
image nova happy = "nova happy.png"
image kain neutral = "kain neutral.png"
image kain angry = "kain angry.png"

init python:
    def mission_time():
        total = 34 + station_minutes
        hour = 3 + total // 60
        minute = total % 60
        return "Day 6 - %02d:%02d station time" % (hour, minute)

    def set_objective(title, details):
        store.quest_title = title
        store.quest_details = details
        renpy.notify("Objective updated")

    def gain_item(name):
        renpy.notify("Acquired: " + name)

    if "mission_chip" not in config.overlay_screens:
        config.overlay_screens.append("mission_chip")

transform character_size:
    subpixel True
    size (400, 600)
    xalign 0.5
    yalign 1.0
    on show:
        alpha 0.0
        yoffset 24
        easeout 0.28 alpha 1.0 yoffset 0
    on replace:
        easein 0.16 alpha 1.0

transform character_left:
    subpixel True
    size (400, 600)
    xalign 0.2
    yalign 1.0
    on show:
        alpha 0.0
        xoffset -32
        easeout 0.28 alpha 1.0 xoffset 0
    on replace:
        easein 0.16 alpha 1.0

transform character_right:
    subpixel True
    size (400, 600)
    xalign 0.8
    yalign 1.0
    on show:
        alpha 0.0
        xoffset 32
        easeout 0.28 alpha 1.0 xoffset 0
    on replace:
        easein 0.16 alpha 1.0

transform character_player:
    subpixel True
    size (400, 600)
    xalign 0.16
    yalign 1.0
    on show:
        alpha 0.0
        xoffset -24
        easeout 0.28 alpha 1.0 xoffset 0
    on replace:
        easein 0.16 alpha 1.0

transform subtle_pulse:
    alpha 0.86
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.86
    repeat

transform hud_appear:
    on show:
        alpha 0.0
        yoffset -10
        easeout 0.25 alpha 1.0 yoffset 0

screen mission_chip():
    zorder 95

    if quick_menu and not main_menu and not renpy.variant("small"):
        textbutton "[mission_time()]  |  [quest_title]":
            style "mission_chip_button"
            action ShowMenu("mission_status")
            at hud_appear

style mission_chip_button is default:
    xalign 1.0
    yalign 0.0
    xoffset -24
    yoffset 18
    xmaximum 520
    background Frame("gui/mission_chip.png", Borders(22, 8, 22, 8), tile=False)
    hover_background Frame("gui/mission_chip_hover.png", Borders(22, 8, 22, 8), tile=False)
    padding (20, 8, 20, 8)

style mission_chip_button_text is gui_text:
    size 14
    color "#d8f3f8"
    hover_color "#ffffff"
    outlines [(1, "#001116", 0, 1)]

screen mission_status():
    tag menu

    use game_menu(_("Mission Log"), scroll="viewport"):

        vbox:
            spacing 18

            label "[quest_title]"
            text "[quest_details]"
            null height 8

            label _("Station Status")
            text "[mission_time()]"
            text "Main power: [34 if not fixed_power else 89] percent"
            text "Nova trust level: [trust_nova]"
            text "Kain suspicion level: [suspicion_kain]"

            null height 8

            label _("Inventory")

            if access_card:
                text "- Security access card"
            if med_patch:
                text "- Emergency med-patch"
            if terminal_unlocked:
                text "- Terminal route unlocked"
            if override_code:
                text "- Override chip code: 7349"
            if not access_card and not med_patch and not terminal_unlocked and not override_code:
                text "- No key items collected yet."

label start:

    $ set_objective("Investigate the distress signal", "A distress signal is repeating from Docking Bay 3. Confirm whether the caller is real before the station loses power.")

    scene bg controlroom with fade
    play music "audio/ambient_space.mp3" fadein 2.0
    play sound "audio/alarm.wav"
    show alex neutral at character_player with dissolve

    "Year 2147. Space Station Meridian-7."
    "Power is at 34 percent. Life support is stable for now."
    "You have been alone on this station for six days, repairing systems that should never have failed together."
    "Then the distress signal came."

    system "Docking Bay 3. Unauthorized pod contact. Manual confirmation required."
    alex "Another signal. Coming from Docking Bay 3."
    alex "Someone is out there, or someone wants me to think they are."

    menu:
        "Check the signal immediately.":
            $ trust_nova += 1
            $ station_minutes += 4
            jump check_signal

        "Review the station logs first.":
            $ suspicion_kain += 1
            $ station_minutes += 8
            jump review_logs

        "Ignore it. It could be a trap.":
            $ station_minutes += 10
            jump ignore_signal

label review_logs:

    scene bg controlroom with dissolve
    play sound "audio/terminal.wav"
    show alex neutral at character_player with dissolve

    "You pull up the security archive. Most of the recent footage is corrupted."
    "One clean frame remains: Director Kain standing near the Engine Room coupling three hours before the blackout."
    alex "Why would Kain be near a manual override point?"
    system "Warning. Docking Bay 3 airlock pressure falling."
    alex "Fine. Logs later. Person first."

    jump check_signal

label ignore_signal:

    scene bg controlroom with fade
    show alex neutral at character_player with dissolve

    alex "I have enough problems already."
    "Three minutes pass. The signal gets stronger."
    system "Life sign detected inside attached pod."
    alex "Life sign? That changes everything."
    jump check_signal

label check_signal:

    $ set_objective("Reach Docking Bay 3", "The pod is attached to the outer airlock. Decide whether to open it quickly or verify the survivor's identity first.")

    scene bg corridor with fade
    play sound "audio/door.wav"
    show alex neutral at character_player with dissolve

    "The corridor outside command is colder than it should be."
    "Blue status panels flicker across cracked glass. Red warning strips pulse every few seconds."
    alex "Meridian, route me to Bay 3."
    system "Shortest route compromised. Recommended path: service corridor C, terminal bay, docking ring."

    menu:
        "Take the service corridor carefully.":
            $ station_minutes += 6
            $ suspicion_kain += 1
            "You move slowly and avoid the loose power conduits dragging across the floor."

        "Run straight to the docking ring.":
            $ station_minutes += 3
            "You sprint through the corridor. Somewhere behind you, a bulkhead slams shut."

    scene bg dockingbay with fade

    "An escape pod is locked against airlock 3."
    "Someone is knocking from inside, not loudly, but with the exhausted rhythm of a person saving the last of their strength."
    alex "Hello? Can you hear me?"

    nova "Please open the door. I have been in here for two days."

    menu:
        "Open the pod now.":
            $ trust_nova += 1
            $ station_minutes += 3
            jump open_pod

        "Ask who she is first.":
            $ suspicion_kain += 1
            $ station_minutes += 4
            jump ask_identity

        "Check the pod's emergency record.":
            $ suspicion_kain += 1
            $ station_minutes += 5
            jump pod_record

label pod_record:

    play sound "audio/terminal.wav"
    "The pod recorder sputters to life."
    system "Launch source: Sub-Level 4. Occupant: Nova Rhee. Research clearance revoked by Director Kain."
    alex "Revoked, then ejected. That is not an evacuation."
    $ trust_nova += 1
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

    $ set_objective("Stabilize Meridian-7", "Nova claims Kain planted an override chip in the Engine Room. Investigate before removing it.")

    scene bg dockingbay with fade
    play sound "audio/door.wav"

    show nova neutral at character_size with dissolve

    nova "Thank you. I thought I was going to die in there."
    alex "What happened to this station? Half the systems are offline."
    nova "Kain happened. He planted an override chip in the Engine Room."
    nova "If you remove it without the proper release code, the station might stabilize, or it might tear the grid apart."
    alex "So we need proof and the code."

    menu:
        "Believe Nova and take her with you.":
            $ trust_nova += 1
            $ station_minutes += 4
            jump investigation_hub

        "Keep Nova close, but question every detail.":
            $ suspicion_kain += 1
            $ station_minutes += 5
            jump investigation_hub

        "Tell Nova to wait in the docking bay.":
            $ trust_nova -= 1
            $ station_minutes += 3
            jump investigation_alone

label investigation_hub:

    $ set_objective("Gather evidence and tools", "Use the station map to search the terminal bay, service corridor, and emergency locker before entering the Engine Room.")

    scene bg corridor with fade
    show alex neutral at character_player
    show nova neutral at character_right with dissolve

    nova "If Kain still has cameras, he knows we opened the pod."
    alex "Then we move like we expect him to be watching."
    nova "Good. Because he always is."

    jump station_map

label investigation_alone:

    $ set_objective("Gather evidence alone", "Search the station for a release code before confronting Kain in the Engine Room.")

    scene bg corridor with fade
    show alex neutral at character_player with dissolve

    "Nova stays behind in the docking bay. The silence returns immediately."
    alex "If she is telling the truth, I just made this harder."
    jump station_map

label station_map:

    scene bg corridor with dissolve

    "The station map flickers across a cracked wall display."
    system "[mission_time()]. Emergency routing available."

    menu:
        "Search the security terminal." if not terminal_unlocked:
            jump terminal_bay

        "Inspect the emergency locker." if not med_patch:
            jump emergency_locker

        "Recover an access card from the service alcove." if not access_card:
            jump service_alcove

        "Review the mission log.":
            call screen mission_status
            jump station_map

        "Proceed to the Engine Room.":
            jump engine_room_gate

label terminal_bay:

    $ set_objective("Unlock the security terminal", "Solve the terminal code puzzle to retrieve the Engine Room release code.")
    $ station_minutes += 6

    scene bg terminal with fade
    play sound "audio/terminal.wav"
    show alex neutral at character_player with dissolve

    "The terminal bay is still alive, but only barely."
    "A holographic interface floats over the console. The screen is cracked, the input buffer cycling through damaged fragments."
    system "Security challenge active. Four digits required."

    if access_card:
        "Your recovered access card opens a maintenance hint."
        system "Hint: Kain's override key follows the order of the emergency beacons: Bay 7, Deck 3, Lab 4, Node 9."
    else:
        "Without a security card, most of the hint data is hidden."
        system "Visible fragment: Bay 7... Deck 3... Lab... Node..."

    menu:
        "Enter 7349.":
            $ terminal_unlocked = True
            $ override_code = True
            $ suspicion_kain += 1
            $ station_minutes += 2
            play sound "audio/terminal.wav"
            $ gain_item("Override chip code")
            system "Release code accepted. Engine Room safety interlock available."
            alex "That is our code."
            jump terminal_after

        "Enter 7394.":
            $ station_minutes += 4
            play sound "audio/alarm.wav"
            system "Incorrect. Security delay applied."
            alex "Wrong order. Think, Alex."
            jump terminal_bay

        "Enter 7439.":
            $ station_minutes += 4
            play sound "audio/alarm.wav"
            system "Incorrect. Security delay applied."
            alex "No. The fragments are not arranged that way."
            jump terminal_bay

label terminal_after:

    if trust_nova >= 2:
        show nova happy at character_right with dissolve
        nova "You got it. Kain always used numbered systems because he thought no one else paid attention."
        alex "You did."
        nova "I had to."
    else:
        "The code sits in your log like a loaded weapon."

    jump station_map

label emergency_locker:

    $ station_minutes += 4
    scene bg corridor with dissolve
    play sound "audio/door.wav"
    show alex neutral at character_player with dissolve

    "The emergency locker is jammed half-open."
    "Inside, you find a single med-patch and a cracked oxygen gauge."
    $ med_patch = True
    $ gain_item("Emergency med-patch")

    if trust_nova >= 1:
        show nova scared at character_right with dissolve
        nova "Keep it. You are the one who has to touch the coupling."
        alex "You spent two days in a pod."
        nova "And I am still standing."
        $ trust_nova += 1
    else:
        alex "One med-patch. Hope I do not need it."

    jump station_map

label service_alcove:

    $ station_minutes += 5
    scene bg corridor with dissolve
    show alex neutral at character_player with dissolve

    "A dead maintenance drone blocks a side alcove."
    "You pry open its storage panel and find a security access card clipped inside."
    $ access_card = True
    $ gain_item("Security access card")

    if not terminal_unlocked:
        alex "This should make the terminal less hostile."

    jump station_map

label engine_room_gate:

    if not override_code:
        scene bg corridor with dissolve
        show alex neutral at character_player with dissolve
        play sound "audio/alarm.wav"
        system "Warning. Engine Room override removal without release code may cause catastrophic grid surge."

        menu:
            "Go back and find the release code.":
                jump station_map

            "Proceed anyway.":
                $ suspicion_kain += 1
                jump engine_room_alone

    if trust_nova >= 2:
        jump engine_room_together
    else:
        jump engine_room_alone

label engine_room_together:

    $ set_objective("Remove Kain's override chip", "Use the release code in the Engine Room and decide whether to trust Nova when Kain intervenes.")
    $ station_minutes += 7

    scene bg engineroom with fade
    play sound "audio/door.wav"

    show nova neutral at character_right with dissolve

    "You and Nova move through the corridors quickly."
    "The lights flicker every few seconds, but the release code keeps the safety interlock stable."
    nova "It should be behind the main power coupling. A small black chip."
    alex "I see it."
    "You enter the code. The coupling unlocks with a clean mechanical click."
    play sound "audio/terminal.wav"
    "Then Kain's voice cuts through the comms."

    show kain neutral at character_left with dissolve

    kain "Step away from the coupling, technician."
    alex "Director Kain."

    show kain angry at character_left with dissolve

    kain "That chip is keeping this station running on my schedule."
    kain "Walk away. Take the pod. Leave the girl."

    menu:
        "Remove the chip. Trust Nova.":
            $ trust_nova += 1
            jump ending_router

        "Challenge Kain with the terminal evidence.":
            $ suspicion_kain += 1
            $ trust_nova += 1
            alex "I have the pod record, your access trail, and the release code you tried to hide."
            kain "Evidence does not matter if no one survives to receive it."
            jump ending_router

        "Listen to Kain. Step back.":
            $ kain_warned = True
            jump listen_to_kain

label engine_room_alone:

    $ set_objective("Confront the override chip", "You are entering the Engine Room without full trust or full preparation. Your previous choices will decide how stable the outcome is.")
    $ station_minutes += 8

    scene bg engineroom with fade
    show alex neutral at character_player with dissolve

    "You find the chip exactly where Nova described."

    if override_code:
        "The release code keeps the coupling from sparking when you open the panel."
    else:
        "Without the release code, the coupling spits white sparks into the air."
        play sound "audio/alarm.wav"

    "Kain's voice comes through the comms before you can touch it."

    show kain neutral at character_size with dissolve

    kain "I see you found my little addition."

    show kain angry at character_size with dissolve

    kain "That chip stays in. Walk away and I will make sure you get out alive."
    kain "The girl is not your problem."

    menu:
        "Remove the chip anyway.":
            jump ending_router

        "Call Nova and admit you need her help.":
            $ trust_nova += 1
            jump warn_nova

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
        "No. I need your help to finish this.":
            $ trust_nova += 1
            if override_code:
                jump engine_room_together
            else:
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
            $ trust_nova += 1
            jump ending_router

        "Take the offer. Leave Nova behind.":
            jump bad_ending

label ending_router:

    if override_code and trust_nova >= 4 and station_minutes <= 55:
        jump good_ending

    if override_code and trust_nova >= 2:
        jump neutral_ending

    if med_patch and trust_nova >= 2:
        jump neutral_ending

    jump bad_ending

label good_ending:

    $ fixed_power = True
    $ set_objective("Good ending achieved", "You trusted Nova, solved the terminal puzzle, used the release code, and exposed Kain before Meridian-7 failed.")

    scene bg engineroom with fade

    hide nova scared
    hide kain angry

    "You pull the chip out. The safety interlock catches the surge."
    play sound "audio/power_restore.wav"
    "The lights stop flickering."
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
    "You trusted the right person, solved the override puzzle, and saved Meridian-7."
    return

label neutral_ending:

    $ fixed_power = True
    $ set_objective("Neutral ending achieved", "The station survived, but the evidence chain was incomplete and Kain escaped.")

    scene bg engineroom with fade
    show alex neutral at character_player with dissolve

    "You pull the chip out."

    if override_code:
        play sound "audio/power_restore.wav"
        "The release code absorbs most of the surge. Power climbs back to 76 percent."
    else:
        play sound "audio/alarm.wav"
        "The coupling screams before the emergency systems clamp down. Power crawls back to 61 percent."

    alex "Station is stable. Kain is going to know what I did."

    scene bg dockingbay with fade

    show nova neutral at character_size with dissolve

    nova "I heard the power come back. You did it."

    if trust_nova >= 3:
        nova "Maybe next time, we start by trusting each other."
    else:
        nova "I am leaving before Kain sends someone else."

    alex "Take care of yourself."
    nova "You too, Alex."

    hide nova neutral

    "Nova leaves. You stay and send a full report to Central Command."
    "Kain disappears before authorities arrive. He is never caught."
    "The station is decommissioned three months later."
    " "
    "--- NEUTRAL ENDING ---"
    "The station survived, but Kain got away."
    return

label bad_ending:

    $ set_objective("Bad ending achieved", "The choices made on Meridian-7 left the station unstable and Nova without enough support.")

    scene bg controlroom with fade
    play sound "audio/alarm.wav"
    show alex neutral at character_player with dissolve

    "You walk to Bay 1. The pod is there, just like Kain said."
    "You do not look back."

    scene bg escapepod with fade

    "From the pod window, you watch Meridian-7."
    "Twenty minutes later, the station goes dark."
    play sound "audio/explosion.wav"
    "Then the explosion."
    alex "Nova..."
    "You arrive at Port Salis alone."
    "Kain's story is already on every channel."
    "A tragic accident. A lone survivor. You."
    "You know the truth. But who would believe you now?"
    " "
    "--- BAD ENDING ---"
    "You chose wrong. Some choices cannot be undone."
    return
