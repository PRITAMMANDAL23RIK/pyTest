
import pytest
from selenium import webdriver


driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup1(request):
    global driver
    br_nm = request.config.getoption("browser")
    if br_nm == "chrome" :
       driver = webdriver.Chrome()
    elif br_nm == "firefox" :
       driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)