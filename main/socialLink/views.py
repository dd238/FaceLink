from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


from .models import Tweet, TwitterUser
from twitter import *
import string
import json
import csv


def searchTwitter(user):
    """
    Searches twitter for user, returns results
    ----------
    user : string
        user name query

    Returns
    -------
    users : array
        search results as twitterUser objects
    """
    twitter = Twitter(
        auth=OAuth("754771372996435968-uJ7WYrDBgd0WslQv1nzYb62xmOfW2dr",
                   "ARxSD4Wa7q8ih41aF13cvsmw1hOmjz1B8jdihhTBWdotX", "5C6fklOsuiPNBqUjcFBm2lw5Q",
                   "91gLoRw2MOEmxInmlosjyUVxdgXeWDG8fn0bhcXab7tCt6aOab"))

    results = twitter.users.search(q=user)

    users = []

    for user in results:
        users.append(TwitterUser(user["name"], user["screen_name"], user["location"]))

    return users


def removePunctuation(word):
    punct = string.punctuation
    for character in punct:
        word = word.replace(character, "")
    return word


def checkObjectionable(listOfTweets):
    """
    Rates tweets by how vulgar they are using a hardcoded list
    ----------
    listOfTweets : array

    Returns
    -------
    tweets : array
        objectionable tweets as strings
    """

    badWords = "2g1c,2 girls 1 cup,acrotomophilia,alabama hot pocket,alaskan pipeline,anal,anilingus,anus,apeshit,arsehole,ass,asshole,assmunch,auto erotic,autoerotic,babeland,baby batter,baby juice,ball gag,ball gravy,ball kicking,ball licking,ball sack,ball sucking,bangbros,bareback,barely legal,barenaked,bastard,bastardo,bastinado,bbw,bdsm,beaner,beaners,beaver cleaver,beaver lips,bestiality,big black,big breasts,big knockers,big tits,bimbos,birdlock,bitch,bitches,black cock,blonde action,blonde on blonde action,blowjob,blow job,blow your load,blue waffle,blumpkin,bollocks,bondage,boner,boob,boobs,booty call,brown showers,brunette action,bukkake,bulldyke,bullet vibe,bullshit,bung hole,bunghole,busty,butt,buttcheeks,butthole,camel toe,camgirl,camslut,camwhore,carpet muncher,carpetmuncher,chocolate rosebuds,circlejerk,cleveland steamer,clit,clitoris,clover clamps,clusterfuck,cock,cocks,coprolagnia,coprophilia,cornhole,coon,coons,creampie,cum,cumming,cunnilingus,cunt,darkie,date rape,daterape,deep throat,deepthroat,dendrophilia,dick,dildo,dingleberry,dingleberries,dirty pillows,dirty sanchez,doggie style,doggiestyle,doggy style,doggystyle,dog style,dolcett,domination,dominatrix,dommes,donkey punch,double dong,double penetration,dp action,dry hump,dvda,eat my ass,ecchi,ejaculation,erotic,erotism,escort,eunuch,faggot,fecal,felch,fellatio,feltch,female squirting,femdom,figging,fingerbang,fingering,fisting,foot fetish,footjob,frotting,fuck,fuck buttons,fuckin,fucking,fucktards,fudge packer,fudgepacker,futanari,gang bang,gay sex,genitals,giant cock,girl on,girl on top,girls gone wild,goatcx,goatse,god damn,gokkun,golden shower,goodpoop,goo girl,goregasm,grope,group sex,g-spot,guro,hand job,handjob,hard core,hardcore,hentai,homoerotic,honkey,hooker,hot carl,hot chick,how to kill,how to murder,huge fat,humping,incest,intercourse,jack off,jail bait,jailbait,jelly donut,jerk off,jigaboo,jiggaboo,jiggerboo,jizz,juggs,kike,kinbaku,kinkster,kinky,knobbing,leather restraint,leather straight jacket,lemon party,lolita,lovemaking,make me come,male squirting,masturbate,menage a trois,milf,missionary position,motherfucker,mound of venus,mr hands,muff diver,muffdiving,nambla,nawashi,negro,neonazi,nigga,nigger,nig nog,nimphomania,nipple,nipples,nsfw images,nude,nudity,nympho,nymphomania,octopussy,omorashi,one cup two girls,one guy one jar,orgasm,orgy,paedophile,paki,panties,panty,pedobear,pedophile,pegging,penis,phone sex,piece of shit,pissing,piss pig,pisspig,playboy,pleasure chest,pole smoker,ponyplay,poof,poon,poontang,punany,poop chute,poopchute,porn,porno,pornography,prince albert piercing,pthc,pubes,pussy,queaf,queef,quim,raghead,raging boner,rape,raping,rapist,rectum,reverse cowgirl,rimjob,rimming,rosy palm,rosy palm and her 5 sisters,rusty trombone,sadism,santorum,scat,schlong,scissoring,semen,sex,sexo,sexy,shaved beaver,shaved pussy,shemale,shibari,shit,shitblimp,shitty,shota,shrimping,skeet,slanteye,slut,s&m,smut,snatch,snowballing,sodomize,sodomy,spic,splooge,splooge moose,spooge,spread legs,spunk,strap on,strapon,strappado,strip club,style doggy,suck,sucks,suicide girls,sultry women,swastika,swinger,tainted love,taste my,tea bagging,threesome,throating,tied up,tight white,tit,tits,titties,titty,tongue in a,topless,tosser,towelhead,tranny,tribadism,tub girl,tubgirl,tushy,twat,twink,twinkie,two girls one cup,undressing,upskirt,urethra play,urophilia,vagina,venus mound,vibrator,violet wand,vorarephilia,voyeur,vulva,wank,wetback,wet dream,white power,wrapping men,wrinkled starfish,xx,xxx,yaoi,yellow showers,yiffy,zoophilia".split(
        ",")

    toReturn = []
    for tweet in listOfTweets:
        lowerCased = tweet.body.lower()
        splitted = lowerCased.split(" ")
        for word in splitted:
            word = removePunctuation(word)
            if word in badWords:
                tweet.rating += 1
        toReturn.append(tweet)
    # lambda is how we can sort on second element in the list
    toReturn.sort(key=(lambda x: x.rating), reverse=True)
    return toReturn


def getObjectionableTweets(user):
    """
    Searches user's tweets, returns thems in order of objectionability
    ----------
    user : string
        user name

    Returns
    -------
    tweets : array
        objectionable tweets as strings
    """
    twitter = Twitter(
        auth=OAuth("754771372996435968-uJ7WYrDBgd0WslQv1nzYb62xmOfW2dr",
                   "ARxSD4Wa7q8ih41aF13cvsmw1hOmjz1B8jdihhTBWdotX", "5C6fklOsuiPNBqUjcFBm2lw5Q",
                   "91gLoRw2MOEmxInmlosjyUVxdgXeWDG8fn0bhcXab7tCt6aOab"))

    results = twitter.statuses.user_timeline(screen_name=user)
    tweets = []

    for status in results:
        tweets.append(Tweet(status["text"].encode("ascii", "ignore"), status["created_at"].encode("ascii", "ignore")[:10]))

    return checkObjectionable(tweets)


# Create your views here.

def index(request):
    # json.dumps(request)
    # print request.body
	tweets = []
	linkedInUrl = ''
    # hmmprint "REQUEST META: " + str(QueryDict(request.META["QUERY_STRING"]))


	queryDict = QueryDict(request.META["QUERY_STRING"])
	if 'linked' in queryDict.keys():
		linkedInUrl = queryDict['linked']
		name = " ".join(linkedInUrl[linkedInUrl.find("/in/") + 4:].split("-")[:2]) # grabs name from URL
		screen_name = searchTwitter(name)[0].username
		tweets = getObjectionableTweets(screen_name)

	print "Linkedin: " + linkedInUrl



	template = loader.get_template("socialLink/index.html")
	context = {
	    'tweets': tweets,
	    'linkedInUrl': linkedInUrl
	}
	return HttpResponse(template.render(context, request))
