def madlibs():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter a adjective: ")
    place = input("Enter a place: ")

    story = f"One day a {adjective} {noun} decided to {verb} at {place}. It was an unforgettable adventure!" 

    print("/n here is your mad libs story: ")
    print(story)

madlibs()

