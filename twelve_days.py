#marked with comment(#) is the original value

#def recite(start_verse, end_verse):
#    pass

def recite(start_verse, end_verse):
    ordinal = ['first','second', 'third', 'fourth',
               'fifth', 'sixth', 'seventh', 'eighth',
               'ninth', 'tenth', 'eleventh', 'twelfth']


    things = ['a Partridge in a Pear Tree.', 'two Turtle Doves',
              'three French Hens', 'four Calling Birds',
              'five Gold Rings', 'six Geese-a-Laying',
              'seven Swans-a-Swimming', 'eight Maids-a-Milking',
              'nine Ladies Dancing', 'ten Lords-a-Leaping',
              'eleven Pipers Piping', 'twelve Drummers Drumming']

    #1 = ..1.. + a
    #2 = ..2.. + b + and + a
    #3 = ..3.. + c + b + and + a
    #...

    song = []
    for day in range (start_verse-1, end_verse):
        lyrics = 'On the ' + ordinal[day] + ' day of Christmas my true love gave to me: '
        if day == 0:
            lyrics = lyrics + things[0]
        else:
            gifts = [things[i] for i in range (day, 0, -1)]
            gifts = ', '.join(gifts)
            gifts = gifts + ', and ' + things[0]
            lyrics = lyrics + gifts
                
        song.append(lyrics)

    return song
