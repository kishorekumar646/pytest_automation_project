from selenium.webdriver.common.by import By


class HomePageLocators:
    movies_link = (By.PARTIAL_LINK_TEXT, 'Movies')
    tv_shows_link = (By.PARTIAL_LINK_TEXT, 'TV Shows')
    tata_ipl_link = (By.PARTIAL_LINK_TEXT, 'Sports')


class MoviesPageLocators:
    the_twilight_saga = {By.XPATH, "//h2[normalize-space()='The Twilight Saga']"}
    watch_button_from_movies = (
        By.XPATH, "//button[@class='MuiButtonBase-root MuiCardActionArea-root mui-style-88oj2h-cardActionArea']")
    watch_button_for_open_movie = (
        By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium mui-style-1dfssf2-btn']")


class TVShowsPageLocators:
    pass


class TataIplPageLocators:
    pass


class SearchPageLocators:
    search_box = (By.ID, 'searchInputBox')
    select_top_list_movie = (
        By.XPATH, '//button[@class="MuiButtonBase-root MuiCardActionArea-root mui-style-1pmk1jv-cardActionArea"]')
    select_top_list_movie_from_search = (By.TAG_NAME, 'body')
    open_selected_movie = (
        By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium mui-style-1w4bab5-btn"]')
    get_movie_title_name = (
        By.XPATH, '//h1[@class="MuiTypography-root MuiTypography-heading3Bold mui-style-18ah6rt"]')
    get_suggestions_list = (
        By.XPATH, "//div[@class='mui-style-1snl13r-dropdown']//p")


class VideoPageLocators:
    mute_button = (By.XPATH, "//button[@aria-label='Mute']")
    unmute_button = (By.XPATH, "//button[@aria-label='Unmute']")
    play_button = (
        By.XPATH, '//button[@aria-label="Play"]')
    pause_button = (
        By.XPATH, '//button[@aria-label="Pause"]'
    )
    settings_button = (
        By.XPATH, '//button[@aria-label="Resolution"]')
    resolution_standard = (By.XPATH, '//div[normalize-space()="Standard"]')
