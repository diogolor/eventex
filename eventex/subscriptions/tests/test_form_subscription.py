from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF Must only accpet digits."""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF Must have 11 digits."""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        erros = form.errors.as_data()
        errors_list = erros[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Diogo Lima', cpf='1234',
                    email='diogol.or@gmail.com', phone='21-995630304')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form