from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_Number = forms.IntegerField()
    Reg_Number =forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class TeacherRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_Number = forms.IntegerField()
    Reg_Number =forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)



class EmployeeForm(forms.Form):

    full_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'Farhan-full_name',
                'placeholder': 'Full Name'
            }
        )
    )

    department = forms.CharField(
        max_length=100,
        required=True,
        initial="Engineering",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'Farhan-department',
                'placeholder': 'Department'
            }
        )
    )

    salary = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'Farhan-salary',
                'placeholder': 'Salary'
            }
        )
    )

    status = forms.CharField(
        required=True,
        initial="Active",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'Farhan-status',
                'placeholder': 'Status'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Change label suffix
        self.label_suffix = " >>"

        # Field order
        self.order_fields([
            "full_name",
            "department",
            "salary",
            "status"
        ])

    class Name(forms.Form):
        field = forms.CharField(
            max_length=50,
            required=True,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter value'
                }
            ),
            error_messages={
                'required': 'This field is required',
                'invalid': 'Invalid value'
            }
        )
    
        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data
