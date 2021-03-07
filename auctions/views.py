from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, activelistings, categories, comments, bids

def all(request):
    return render(request, "auctions/all.html", {
        "activelistings": activelistings.objects.all()
    })

def index(request):
    return render(request, "auctions/index.html", {
        "activelistings": activelistings.objects.all()
    })

def listingpage(request, listingid):
    return render(request, "auctions/listingpage.html",{
        "activelistings": activelistings.objects.get(pk=listingid),
        "comments": comments.objects.all(),
        "bids": bids.objects.all(),
        })

@login_required(login_url='/login')
def bid(request):
    userid = request.POST["biddinguserid"]
    user = User.objects.get(pk=userid)
    listingid = request.POST["listingid"]
    listing = activelistings.objects.get(pk=listingid)
    newbidprice = int(request.POST["bidprice"])
    startingbid = int(request.POST["startingbid"])
    try:
        oldbid = bids.objects.get(listing=listing)
        oldbidprice = oldbid.bidprice
        if newbidprice > oldbidprice:
            oldbid.delete()
            data = bids(bidprice=newbidprice, biddinguser=user , listing=listing)
            data.save()
            return render(request, "auctions/listingpage.html",{
            "activelistings": activelistings.objects.get(pk=listingid),
            "comments": comments.objects.all(),
            "bids": bids.objects.all()
            })
        else:
            return render(request, "auctions/listingpage.html", {
                "message": "Error: You bid amount is lower than current bid amount. Please increase your bid amount.",
                "activelistings": activelistings.objects.get(pk=listingid),
                "comments": comments.objects.all(),
                "bids": bids.objects.all()
            })
    
    except: 
        oldbidprice = startingbid
        if newbidprice > oldbidprice:
            data = bids(bidprice=newbidprice, biddinguser=user , listing=listing)
            data.save()
            return render(request, "auctions/listingpage.html",{
            "activelistings": activelistings.objects.get(pk=listingid),
            "comments": comments.objects.all(),
            "bids": bids.objects.all()
            })
        else:
            return render(request, "auctions/listingpage.html", {
                "message": "Error: You bid amount is lower than current bid amount. Please increase your bid amount.",
                "activelistings": activelistings.objects.get(pk=listingid),
                "comments": comments.objects.all(),
                "bids": bids.objects.all()
            })
@login_required(login_url='/login')
def watchlist(request, userid):
        if request.method == "POST":
            user = User.objects.get(pk=userid)
            listingid = request.POST['listingid']
            listing = activelistings.objects.get(pk=listingid)
            user.savedlistings.add(listing)
            return HttpResponseRedirect(reverse("listingpage", args=(listingid,)))
        else:
            user = User.objects.get(pk=userid)
            return render(request, "auctions/watchlist.html", {
                "activelistings": user.savedlistings.all()
            })

def unsave(request):
        userid = request.POST['userid']
        user = User.objects.get(pk=userid)
        listingid = request.POST['listingid']
        listing = activelistings.objects.get(pk=listingid)
        user.savedlistings.remove(listing)
        return HttpResponseRedirect(reverse("listingpage", args=(listingid,)))

@login_required(login_url='/login')
def comment(request):
        comment = request.POST["comment"]
        userid = request.POST["userid"]
        user = User.objects.get(pk=userid)
        listingid = request.POST["listingid"]
        listing = activelistings.objects.get(pk=listingid)
        data = comments(comment=comment, listing=listing, author=user)
        data.save()
        return render(request, "auctions/listingpage.html",{
        "activelistings": activelistings.objects.get(pk=listingid),
        "comments": comments.objects.all(),
        })

def categoryindex(request):
    return render(request, "auctions/categoryindex.html", {
        "categories": categories.objects.all()
    })

def categorypage(request, categoryid):
    category = categories.objects.get(pk=categoryid)
    return render(request, "auctions/categorypage.html", {
        "category": category,
        "activelistings": activelistings.objects.all(),
        "categories": categories.objects.get(pk=categoryid)
    })

@login_required(login_url='/login')
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageurl = request.POST["imageurl"]
        if imageurl=='':
            imageurl = request.POST["altimageurl"]
        startingBid = request.POST["startingbid"]
        categoryid = request.POST["categoryid"]
        category = categories.objects.get(pk=categoryid)
        userid = request.POST["userid"]
        user = User.objects.get(pk=userid)
        data = activelistings(title=title, description=description, category=category, imageurl=imageurl, startingBid=startingBid, creator=user)
        data.save()
        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", {
        "categories": categories.objects.all()
    })

def inactive(request):
    listingid=request.POST["listingid"]
    listing = activelistings.objects.get(pk=listingid)
    listing.status = "inactive"
    listing.save()
    #return HttpResponse("Listing closed")
    return HttpResponseRedirect(reverse("listingpage", args=(listingid,)))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
