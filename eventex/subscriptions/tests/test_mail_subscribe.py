from django.core import mail
from django.test import TestCase


class SubscribedPostValid(TestCase):
    def setUp(self):
        data = dict(name='Diogo Lima', cpf='12345678901', email='diogol.or@gmail.com', phone='21-995630304')
        self.resp = self.client.post('/inscricao/', data)
        self.mail = mail.outbox[0]

    def test_subscription_email_subject(self):

        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.mail.subject)

    def test_subscription_email_from(self):

        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.mail.from_email)

    def test_subscription_email_to(self):

        expect = ['contato@eventex.com.br', 'diogol.or@gmail.com']
        self.assertEqual(expect, self.mail.to)

    def test_subscription_email_body(self):
        contents = [
            'Diogo Lima',
            '12345678901',
            'diogol.or@gmail.com',
            '21-995630304'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.mail.body)