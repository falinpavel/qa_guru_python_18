import allure

from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    try:
        if hasattr(browser.driver, 'get_log'):
            logs = browser.driver.get_log(log_type='browser')
            log_str = "\n".join(log['message'] for log in logs)
        else:
            log_str = "Browser logs not available (get_log not supported)"

        allure.attach(body=log_str, name='browser_logs', attachment_type=AttachmentType.TEXT, extension='.log')
    except Exception as e:
        allure.attach(body=f"Error getting logs: {str(e)}", name='log_error', attachment_type=AttachmentType.TEXT,
                      extension='.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(body=html, name='page_source', attachment_type=AttachmentType.HTML, extension='.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"

    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"

    allure.attach(body=html, name='video: ' + browser.driver.session_id, attachment_type=AttachmentType.HTML,
                  extension='.html')