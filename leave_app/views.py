from django.shortcuts import render, redirect
from .models import LeaveRequest
from .forms import LeaveRequestForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# 👇 This view handles the leave request form submission
@login_required
def submit_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_requests')  # Redirect after successful submission
    else:
        form = LeaveRequestForm()  # Show empty form on GET

    return render(request, 'leave_app/submit_leave.html', {'form': form})


# 👇 This view displays all submitted leave requests
@login_required
def view_leave_requests(request):
    leaves = LeaveRequest.objects.all()
    return render(request, 'leave_app/view_requests.html', {'leaves': leaves})
@login_required
def approve_leave(request, leave_id):
    leave = get_object_or_404(LeaveRequest, id=leave_id)
    leave.status = 'Approved'
    leave.save()
    return redirect('view_requests')

@login_required
def reject_leave(request, leave_id):
    leave = get_object_or_404(LeaveRequest, id=leave_id)
    leave.status = 'Rejected'
    leave.save()
    return redirect('view_requests')
