# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .models import Route, Booking
# from .forms import BookingForm

# def main_page(request):
#     return render(request, 'mainpage.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('main_page')  
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'login.html')

# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
        
#         if password1 == password2:
#             try:
#                 user = User.objects.create_user(username=username, password=password1)
#                 user.save()
#                 messages.success(request, 'Registration successful! You can now log in.')
#                 return redirect('login')
#             except:
#                 messages.error(request, 'Username already exists.')
#         else:
#             messages.error(request, 'Passwords do not match.')
#     return render(request, 'register.html')

# def book_tickets(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('view_booked_tickets')
#     else:
#         form = BookingForm()
#     return render(request, 'book_tickets.html', {'form': form})

# def view_booked_tickets(request):
#     bookings = Booking.objects.all()
#     return render(request, 'view_booked_tickets.html', {'bookings': bookings})

# def available_routes(request):
#     routes = Route.objects.all()
#     return render(request, 'available_routes.html', {'routes': routes})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Route, Booking
from .forms import BookingForm

def main_page(request):
    return render(request, 'mainpage.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login')
            except:
                messages.error(request, 'Username already exists.')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')

def book_tickets(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        selected_seats = request.POST.getlist('seats')
        if form.is_valid() and selected_seats:
            booking = form.save(commit=False)
            booking.seats = ','.join(selected_seats)
            booking.save()
            messages.success(request, 'Tickets booked successfully!')
            return redirect('view_booked_tickets')
        else:
            messages.error(request, 'Please select at least one seat.')
    else:
        form = BookingForm()
    available_seats = range(1, 21)  # Example: 20 seats available
    return render(request, 'book_tickets.html', {'form': form, 'available_seats': available_seats})

def view_booked_tickets(request):
    bookings = Booking.objects.all()
    return render(request, 'view_booked_tickets.html', {'bookings': bookings})

def available_routes(request):
    routes = Route.objects.all()
    return render(request, 'available_routes.html', {'routes': routes})

