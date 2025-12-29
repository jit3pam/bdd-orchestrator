from pytest_bdd import scenarios, given, when, then
from bdd_orchestrator import run_step

scenarios("features/login.feature")


@given("user opens login page")
def open_page():
    run_step("open page", lambda: print("opened"))


@when("user enters credentials")
def enter_creds():
    state = {"fixed": False}

    def flaky():
        if not state["fixed"]:
            state["fixed"] = True
            raise Exception("First attempt failed")
        # success on retry

    run_step("enter creds", flaky)


@then("user should be logged in")
def verify():
    run_step("verify", lambda: True)
