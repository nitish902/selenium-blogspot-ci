import json

from pages.form_page import FormPage
from core.base_test import BaseTest


def load_test_data():

    with open("testdata/form_data.json") as f:

        return json.load(f)


class TestForm(BaseTest):

    def test_form(self):

        data = load_test_data()

        form = FormPage(self.driver)

        form.enter_name(data["name"])

        form.enter_email(data["email"])

        form.enter_phone(data["phone"])

        form.select_gender()

        form.select_day()

        form.select_country(data["country"])

        form.select_date(data["date"])
