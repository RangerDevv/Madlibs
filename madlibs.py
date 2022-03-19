adj = input("Adjetive: ")
noun1 = input('Noun: ')
noun2 = input('Another Noun: ')
verb =  input('Verb: ')
letsplay = input('Do you want to play? type yes or no (NO CAPS!) ')

if letsplay == 'yes':
    print('I', adj , 'programming that I can' , noun1 , 'for it. It makes be feel' , adj , 'and helps me' , verb , 'faster. it helps me relieve my stress and makes me' , adj , 'So, weather what you think about programming... I ' , adj , 'IT!!')
    tryagain = input('Would you like to try again?')
    if tryagain == 'yes':
        adj = input("Adjetive: ")
        noun1 = input('Noun: ')
        noun2 = input('Another Noun: ')
        verb =  input('Verb: ')
        letsplay = input('Do you want to play? type yes or no (NO CAPS!) ')
        if letsplay == 'yes':
            print('I love to hangout with my friends. They are' , adj , 'and they make me' , adj , 'feel like I am ' , adj , 'My' , noun1 , 'also are the best. I can feel very ' , adj , 'around them. I get very' , verb , 'when I play' , noun2 , 'Thanks for playijng madlibs made by' , noun2, '!!!' )
    elif letsplay == 'no':
        print('OK!')
elif letsplay == 'no':
    print('please try I beg you!')