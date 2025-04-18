import pytest

@pytest.mark.parametrize("name", [
    "경영대학",
    "공과대학",
    "농업생명과학대학",
    "사범대학",
    "생활과학대학",
    "수의과대학",
    "약학대학",
    "예술대학",
    "인문대학",
    "자연과학대학",
    "AI융합대학",
    "공학대학",
    "문화사회과학대학",
    "수산해양대학",
])
@pytest.mark.parametrize("setting_page", ["단과대 알림"], indirect=True)
def test_단과대_알림을_설정한다(setting_page, name):
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_on(name)
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_off(name)