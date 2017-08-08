import wolframalpha

query = raw_input('Enter your math question: ')
app_id='PA237Q-XA42375UEE'


client = wolframalpha.Client(app_id)

def wolfram(query): 
    res = client.query(str(query))
    try:
        ans=next(res.results).text
    except:
        ans ='I don\'t understand, please try again'
    return ans

print wolfram(query)

q = 'yes'
while q =='yes':
    q = raw_input('Any other questions (yes/no)? ')
    if q =='no':
        q = raw_input('Are you sure you want to exit (yes/no)? ')
        if q == 'yes':
            print 'Thank you for using WolframAlpha Bot!'
            break
        else:
            query = raw_input('Enter your math question: ')
            print wolfram(query)
            q = 'yes'
    elif q =='yes':
        query = raw_input('Enter your math question: ')
        print wolfram(query)
    else:
        print 'I don\'t understand, please try again'
        q ='yes'
