# from django.shortcuts import render, get_object_or_404
# from .models import Profile
# from .forms import registerForm
# # Create your views here.

# def register(request):
# 	if request.method == 'POST':
# 		user_form = UserRegistrationForm(request.POST)
# 		if user_form.is_valid():
# 			# Create a new user object but avoid saving it 
# 			new_user = user_form.save(commit=False)
# 			# Set the chosen password
# 			new_user.set_password(user_form.cleaned_data['password'])
# 			# Save the User object
# 			new_user.save()
		
# 			# Create the user profile
# 			Profile.objects.create(user=new_user)
# 			return render(request, 'authe/register_done.html', {'new_user': new_user})
# 	else:
# 		user_form = UserRegistrationForm()
# 	return render(request, 'authe/register.html', {'user_form': user_form})

