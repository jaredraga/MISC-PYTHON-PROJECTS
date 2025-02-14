import androidhelper, random, time

droid = androidhelper.Android()

allDuckTranslations = 'eend pato itik'.split()

while True:

    duckTranslation = random.choice(allDuckTranslations)

    droid.notify(duckTranslation, 'Duck Translation of the Day')
    
    time.sleep(86400)