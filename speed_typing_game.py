import random
#Using The  Random Module 

import time
#Using The Time Module For The Timed Function 

print("Welcome User To The \nTyping speed tests...\nToday we get our quotes from Shakespear")
username = input("\nInsert Username\n")
#Welcome the User To The Plattform 

sentance = ['To be, or not to be: that is the question',
             'Love all, trust a few, do wrong to none',
             'Good night, good night! Parting is such sweet sorrow',
             'Be not afraid of greatness. Some are born great, some achieve greatness, and some have greatness thrust upon \'em.',
             'If you prick us do we not bleed? If you tickle us do we not laugh? If you poison us do we not die? And if you wrong us, shall we not revenge?' , 'There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy.', 'If you can look into the seeds of time, and say which grain will grow and which will not, speak then to me.', 
             'Love sought is good, but given unsought is better.', 
             'If I lose mine honor, I lose myself.', 
             'It\'s not enough to speak, but to speak true.',
             'We know what we are, but know not what we may be.',
             'Modest doubt is called the beacon of the wise.',
             'How poor are they that have not patience! What wound did ever heal but by degrees?',
             'If we are true to ourselves, we can not be false to anyone.',
             'How far that little candle throws its beams! So shines a good deed in a naughty world',
             'One touch of nature makes the whole world kin.',
             'And oftentimes excusing of a fault doth make the fault the worse by the excuse.',
             'Reputation is an idle and most false imposition; oft got without merit, and lost without deserving',
             'My bounty is as boundless as the sea, my love as deep; the more I give to thee, the more I have, for both are infinite',
             'Life’s but a walking shadow, a poor player, that struts and frets his hour upon the stage, and then is heard no more; it is a tale told by an idiot, full of sound and fury, signifying nothing.',
             'And this, our life, exempt from public haunt, finds tongues in trees, books in the running brooks, sermons in stones, and good in everything.',
             'Maids want nothing but husbands, and when they have them, they want everything.',
             'God has given you one face, and you make yourself another.',]; 
#Build The Sentances That Are going to be used to test the user 

status = True 
while (status == True):
    random_sentance = random.choice(sentance)
    print("Type the following text as fast as you can: \n" +"\n" +random_sentance+"\n")
    input("Press Enter to Start...\n")

    start_seconds = time.time()
    #Recording The Time Before User Records Data 

    user_text = input("Write Here: \n").strip()    

    finish_seconds = time.time()
    #Recording The Time Before User Records Data

    session_duration = round((finish_seconds - start_seconds),2)
    print('Time Taken : ', session_duration,' seconds') 
    #Calulating The Time it took for the user to complete the session 

    
    words_in_user_sentance = user_text.count(' ') + 1 ;
    print('Number of words typed: ' + str(words_in_user_sentance) + ' words')

    words_per_minute = ((words_in_user_sentance/session_duration) * 60  )
    clean_count = round(words_per_minute,2)
    print('Typing Speed: ',clean_count,' (WPM)')
    #Calculating The WPM 



    #Calculating The Accuracy Of The Text Supplied 
    i = 0 #variable i will act as the index of calculation
    count_of_char = 0 #Variable count_of_char will act as the count of correct characters  
    while (i < len(random_sentance)) & (i < len(user_text)):
        char_random = random_sentance[i]
        char_user = user_text[i]

        if (char_random == char_user):
            count_of_char += 1
        i +=1

    if ( len(user_text) <= len(random_sentance) ):                          
        accuracy_points = round(  ( ( len(user_text)/len(random_sentance)) * (count_of_char/i)*100) ,2)
    else:
        accuracy_points = round(  ( ( ( ( len(random_sentance) - len(user_text)) + len(user_text) )/len(random_sentance)) * (count_of_char/i) * 100) ,2)
    print("Your Typing Accuracy: "+str(accuracy_points)+"%")

    user_continue = input("Do you wish to continue: Yes/No\n")
    if  ( (user_continue.lower()).strip() == "no" ):
        status = False
        print('Thank you for using this project. I hope you liked these William Shakespeare Quotes.') 
    else: 
        status = True 

#I DID IT FOR HARAMBE 