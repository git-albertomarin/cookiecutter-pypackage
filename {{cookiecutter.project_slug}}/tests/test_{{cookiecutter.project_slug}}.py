#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""
import re

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}

{%- if cookiecutter.use_pytest == 'y' %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()

    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    assert 'Console script for {{ cookiecutter.project_name }}' in result.output

    help_result = runner.invoke(cli.cli, ["--help"])
    assert help_result.exit_code == 0
    assert re.search(r"--help\s*Show this message and exit.", help_result.output)

    run_result = runner.invoke(cli.cli, ["run"])
    assert run_result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.run_command' in run_result.output

{%- endif %}
{%- else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
{%- if cookiecutter.command_line_interface|lower == 'click' %}

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.cli)

        assert result.exit_code == 0
        assert "Console script for {{ cookiecutter.project_name }}" in result.output

        help_result = runner.invoke(cli.cli, ["--help"])
        assert help_result.exit_code == 0
        assert re.search(r"--help\s*Show this message and exit.", help_result.output)

        run_result = runner.invoke(cli.cli, ["run"])
        assert run_result.exit_code == 0
        assert '{{ cookiecutter.project_slug }}.cli.run_command' in run_result.output
{%- endif %}
{%- endif %}
