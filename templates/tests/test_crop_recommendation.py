from playwright.sync_api import Page, expect


def fill_form(
    page: Page,
    N: str,
    P: str,
    K: str,
    temperature: str,
    humidity: str,
    ph: str,
    rainfall: str,
):
    page.goto("http://127.0.0.1:5000")

    page.locator('input[name="N"]').fill(N)
    page.locator('input[name="P"]').fill(P)
    page.locator('input[name="K"]').fill(K)
    page.locator('input[name="temperature"]').fill(temperature)
    page.locator('input[name="humidity"]').fill(humidity)
    page.locator('input[name="ph"]').fill(ph)
    page.locator('input[name="rainfall"]').fill(rainfall)

    page.locator('button[type="submit"]').click()


def test_rice_recommendation(page: Page):
    fill_form(page, "120", "60", "40", "25", "80", "6.5", "150")

    expect(page.locator("#result")).to_contain_text("Rice")


def test_wheat_recommendation(page: Page):
    fill_form(page, "50", "30", "60", "30", "70", "6.5", "150")

    expect(page.locator("#result")).to_contain_text("Wheat")


def test_sugarcane_recommendation(page: Page):
    fill_form(page, "50", "30", "40", "25", "70", "6.5", "250")

    expect(page.locator("#result")).to_contain_text("Sugarcane")


def test_maize_recommendation(page: Page):
    fill_form(page, "50", "30", "40", "25", "70", "6.5", "150")

    expect(page.locator("#result")).to_contain_text("Maize")


def test_exact_boundary_does_not_trigger_rice(page: Page):
    fill_form(page, "100", "50", "40", "25", "80", "6.5", "150")

    expect(page.locator("#result")).to_contain_text("Maize")


def test_required_fields(page: Page):
    page.goto("http://127.0.0.1:5000")

    n_input = page.locator('input[name="N"]')

    expect(n_input).to_have_attribute("required", "")

    is_valid = n_input.evaluate(
        "(element) => element.validity.valid"
    )

    assert is_valid is False


def test_negative_values_are_rejected_by_browser(page: Page):
    page.goto("http://127.0.0.1:5000")

    nitrogen = page.locator('input[name="N"]')
    nitrogen.fill("-10")

    page.locator('input[name="P"]').fill("30")
    page.locator('input[name="K"]').fill("40")
    page.locator('input[name="temperature"]').fill("25")
    page.locator('input[name="humidity"]').fill("70")
    page.locator('input[name="ph"]').fill("6.5")
    page.locator('input[name="rainfall"]').fill("150")

    expect(nitrogen).to_have_attribute("min", "0")

    is_valid = nitrogen.evaluate(
        "(element) => element.checkValidity()"
    )

    assert is_valid is False


def test_prediction_history(page: Page):
    page.goto("http://127.0.0.1:5000")

    # First prediction -> Rice
    page.locator('input[name="N"]').fill("120")
    page.locator('input[name="P"]').fill("60")
    page.locator('input[name="K"]').fill("40")
    page.locator('input[name="temperature"]').fill("25")
    page.locator('input[name="humidity"]').fill("70")
    page.locator('input[name="ph"]').fill("6.5")
    page.locator('input[name="rainfall"]').fill("150")

    page.locator('button[type="submit"]').click()

    expect(page.locator("#result")).to_contain_text("Rice")
    expect(page.locator("#historyList")).to_contain_text("Rice")

    # Second prediction -> Sugarcane
    page.locator('input[name="N"]').fill("50")
    page.locator('input[name="P"]').fill("30")
    page.locator('input[name="K"]').fill("40")
    page.locator('input[name="temperature"]').fill("25")
    page.locator('input[name="humidity"]').fill("70")
    page.locator('input[name="ph"]').fill("6.5")
    page.locator('input[name="rainfall"]').fill("250")

    page.locator('button[type="submit"]').click()

    expect(page.locator("#result")).to_contain_text("Sugarcane")
    expect(page.locator("#historyList")).to_contain_text("Rice")
    expect(page.locator("#historyList")).to_contain_text("Sugarcane")