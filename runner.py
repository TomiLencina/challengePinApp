from behave.__main__ import main as behave_main


if __name__ == "__main__":
    behave_main('features --tags=@TC_Footer_001 -f allure_behave.formatter:AllureFormatter -o report/')
